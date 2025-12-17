"""Sistema de FAQs inteligentes com contexto financeiro.

Implementa busca semântica e respostas contextualizadas para
perguntas frequentes sobre produtos e serviços financeiros.
"""

from typing import List, Dict, Tuple
import json
from difflib import SequenceMatcher


class IntelligentFAQ:
    """Sistema de FAQs com busca semântica e respostas contextualizadas."""
    
    def __init__(self):
        """Inicializa o sistema de FAQs com base de conhecimento."""
        self.faq_database = self._load_faq_database()
        
    def _load_faq_database(self) -> List[Dict[str, str]]:
        """Carrega base de dados de FAQs."""
        return [
            {
                "category": "Conta Corrente",
                "question": "Como abrir uma conta corrente?",
                "answer": """Para abrir uma conta corrente no Bradesco, você precisa:
1. Ter mais de 18 anos (ou ser emancipado)
2. Apresentar documento oficial com foto (RG ou CNH)
3. Apresentar CPF
4. Comprovante de residência

Você pode abrir pelo app, internet banking ou em uma agência.""",
                "keywords": ["abrir conta", "nova conta", "criar conta", "conta corrente"]
            },
            {
                "category": "Investimentos",
                "question": "Quais são os tipos de investimentos disponíveis?",
                "answer": """O Bradesco oferece diversos tipos de investimentos:

**Renda Fixa:**
- CDB (Certificado de Depósito Bancário)
- LCI/LCA (Letras de Crédito)
- Tesouro Direto

**Renda Variável:**
- Ações
- Fundos de Investimento
- Fundos Imobiliários (FIIs)

**Previdência:**
- PGBL
- VGBL

Cada investimento tem perfil de risco e rentabilidade diferentes.""",
                "keywords": ["investimento", "aplicação", "investir", "CDB", "ações", "fundo"]
            },
            {
                "category": "Cartão de Crédito",
                "question": "Como solicitar um cartão de crédito?",
                "answer": """Para solicitar um cartão de crédito Bradesco:

1. Acesse o app Bradesco ou Internet Banking
2. Vá em 'Cartões' > 'Solicitar novo cartão'
3. Escolha o cartão que atende suas necessidades
4. Preencha os dados solicitados
5. Aguarde a análise de crédito

A análise geralmente leva de 24 a 72 horas.""",
                "keywords": ["cartão", "crédito", "solicitar cartão", "novo cartão"]
            },
            {
                "category": "Empréstimos",
                "question": "Quais as taxas de juros dos empréstimos?",
                "answer": """As taxas de juros variam conforme:

- Tipo de empréstimo (pessoal, consignado, imobiliário)
- Seu relacionamento com o banco
- Score de crédito
- Prazo de pagamento

**Taxas médias:**
- Empréstimo Consignado: a partir de 1,4% ao mês
- Empréstimo Pessoal: a partir de 2,5% ao mês
- Crédito Imobiliário: a partir de 9,5% ao ano + TR

Consulte as taxas personalizadas no app ou com seu gerente.""",
                "keywords": ["empréstimo", "financiamento", "juros", "taxa", "crédito"]
            },
            {
                "category": "Poupança",
                "question": "Como funciona a poupança?",
                "answer": """A poupança é o investimento mais tradicional e seguro:

**Rendimento:**
- Se Selic > 8,5%: 0,5% ao mês + TR
- Se Selic ≤ 8,5%: 70% da Selic + TR

**Características:**
- Isenta de Imposto de Renda
- Garantida pelo FGC até R$ 250.000
- Liquidez diária (após aniversário)
- Sem taxas de manutenção

O rendimento é creditado mensalmente no dia de aniversário.""",
                "keywords": ["poupança", "rendimento poupança", "quanto rende"]
            },
            {
                "category": "Segurança",
                "question": "Como proteger minha conta de fraudes?",
                "answer": """Dicas essenciais de segurança:

1. **Nunca compartilhe:**
   - Senha do app/internet banking
   - Códigos SMS de verificação
   - Dados do cartão completos

2. **Sempre desconfie:**
   - E-mails e SMS pedindo dados
   - Ligações solicitando senhas
   - Links suspeitos

3. **Use recursos de segurança:**
   - Autenticação em dois fatores
   - Biometria
   - Notificações de transações

4. **Em caso de suspeita:**
   - Bloqueie o cartão imediatamente pelo app
   - Altere suas senhas
   - Entre em contato: 4004-0022 (capitais) ou 0800-570-0022""",
                "keywords": ["segurança", "fraude", "golpe", "proteção", "senha"]
            },
            {
                "category": "Pix",
                "question": "Como funciona o Pix?",
                "answer": """O Pix é o sistema de pagamentos instantâneos:

**Vantagens:**
- Transferências em até 10 segundos
- Disponível 24/7, inclusive finais de semana
- Sem tarifas para pessoas físicas
- Seguro e rastreável

**Como usar:**
1. Cadastre suas chaves Pix (CPF, e-mail, celular ou aleatória)
2. Para enviar: informe a chave ou use QR Code
3. Para receber: compartilhe sua chave ou QR Code

**Limites:**
- Diurno (6h às 20h): definido por você
- Noturno (20h às 6h): limitado para segurança""",
                "keywords": ["pix", "transferência", "chave pix", "pagamento instantâneo"]
            }
        ]
    
    def search_faq(self, query: str, threshold: float = 0.4) -> List[Dict[str, any]]:
        """Busca FAQs relevantes baseado na query do usuário.
        
        Args:
            query: Pergunta do usuário
            threshold: Limiar mínimo de similaridade (0-1)
            
        Returns:
            Lista de FAQs relevantes ordenados por relevância
        """
        query_lower = query.lower()
        results = []
        
        for faq in self.faq_database:
            # Calcula similaridade com a pergunta
            question_similarity = self._calculate_similarity(
                query_lower, faq['question'].lower()
            )
            
            # Calcula similaridade com keywords
            keyword_similarity = max([
                self._calculate_similarity(query_lower, kw.lower())
                for kw in faq['keywords']
            ] + [0])
            
            # Usa a maior similaridade
            max_similarity = max(question_similarity, keyword_similarity)
            
            if max_similarity >= threshold:
                results.append({
                    'faq': faq,
                    'relevance': max_similarity
                })
        
        # Ordena por relevância
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calcula similaridade entre dois textos usando SequenceMatcher.
        
        Args:
            text1: Primeiro texto
            text2: Segundo texto
            
        Returns:
            Score de similaridade entre 0 e 1
        """
        return SequenceMatcher(None, text1, text2).ratio()
    
    def get_answer(self, query: str) -> Dict[str, any]:
        """Obtém resposta para uma pergunta.
        
        Args:
            query: Pergunta do usuário
            
        Returns:
            Dicionário com resposta e informações adicionais
        """
        results = self.search_faq(query)
        
        if not results:
            return {
                'found': False,
                'message': 'Desculpe, não encontrei uma resposta específica para sua pergunta. '
                          'Você pode reformular ou falar com nosso atendimento.',
                'suggestions': self._get_popular_questions()
            }
        
        best_match = results[0]
        return {
            'found': True,
            'category': best_match['faq']['category'],
            'question': best_match['faq']['question'],
            'answer': best_match['faq']['answer'],
            'relevance': best_match['relevance'],
            'related': [r['faq']['question'] for r in results[1:3]]  # Até 2 relacionadas
        }
    
    def _get_popular_questions(self) -> List[str]:
        """Retorna perguntas populares por categoria."""
        return [faq['question'] for faq in self.faq_database[:3]]
    
    def list_categories(self) -> List[str]:
        """Lista todas as categorias disponíveis."""
        return list(set(faq['category'] for faq in self.faq_database))
    
    def get_faqs_by_category(self, category: str) -> List[Dict[str, str]]:
        """Retorna todas as FAQs de uma categoria.
        
        Args:
            category: Nome da categoria
            
        Returns:
            Lista de FAQs da categoria
        """
        return [faq for faq in self.faq_database if faq['category'] == category]
