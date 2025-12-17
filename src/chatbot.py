"""Módulo principal do chatbot com IA generativa.

Implementa conversação com processamento de linguagem natural
utilizando OpenAI GPT para interações financeiras personalizadas.
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI
from datetime import datetime


class FinancialChatbot:
    """Chatbot financeiro com IA generativa e contexto persistente."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Inicializa o chatbot com API OpenAI.
        
        Args:
            api_key: Chave da API OpenAI (usa variável de ambiente se None)
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("API key da OpenAI não configurada")
            
        self.client = OpenAI(api_key=self.api_key)
        self.conversation_history: List[Dict[str, str]] = []
        self.system_prompt = self._build_system_prompt()
        
    def _build_system_prompt(self) -> str:
        """Constrói o prompt de sistema para o assistente financeiro."""
        return """Você é um assistente financeiro inteligente e amigável do Bradesco.
        
Suas responsabilidades:
- Fornecer orientações financeiras claras e precisas
- Explicar produtos bancários e investimentos
- Realizar cálculos financeiros quando solicitado
- Responder dúvidas sobre educação financeira
- Manter um tom profissional, mas acessível
- Priorizar a segurança e privacidade do usuário

Diretrizes:
- Nunca solicite informações sensíveis (senhas, cartões)
- Sempre recomende falar com um gerente para operações financeiras
- Use linguagem clara, evitando jargões desnecessários
- Seja conciso mas completo nas respostas
- Quando não souber, admita e sugira alternativas
"""
    
    def chat(self, user_message: str, use_context: bool = True) -> str:
        """Processa mensagem do usuário e retorna resposta da IA.
        
        Args:
            user_message: Mensagem do usuário
            use_context: Se True, mantém contexto da conversa
            
        Returns:
            Resposta gerada pela IA
        """
        # Adiciona mensagem do usuário ao histórico
        self.conversation_history.append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Prepara mensagens para a API
        messages = [{'role': 'system', 'content': self.system_prompt}]
        
        if use_context:
            # Inclui histórico (últimas 10 mensagens)
            context_messages = self.conversation_history[-10:]
            for msg in context_messages:
                messages.append({
                    'role': msg['role'],
                    'content': msg['content']
                })
        else:
            messages.append({'role': 'user', 'content': user_message})
        
        try:
            # Chama a API OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            assistant_message = response.choices[0].message.content
            
            # Adiciona resposta ao histórico
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message,
                "timestamp": datetime.now().isoformat()
            })
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"Erro ao processar mensagem: {str(e)}"
            return error_msg
    
    def clear_context(self):
        """Limpa o histórico de conversação."""
        self.conversation_history = []
    
    def get_context(self) -> List[Dict[str, str]]:
        """Retorna o histórico de conversação."""
        return self.conversation_history.copy()
    
    def save_conversation(self, filepath: str):
        """Salva a conversação em arquivo JSON.
        
        Args:
            filepath: Caminho do arquivo para salvar
        """
        import json
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
