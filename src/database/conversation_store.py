"""Armazenamento de conversas e histórico."""

from typing import List, Dict, Optional
from datetime import datetime
from .db_manager import DatabaseManager


class ConversationStore:
    """Gerencia armazenamento de conversas."""
    
    def __init__(self, db_manager: Optional[DatabaseManager] = None):
        """Inicializa o armazenamento de conversas.
        
        Args:
            db_manager: Instância do gerenciador de banco
        """
        self.db = db_manager or DatabaseManager()
    
    def create_conversation(self, user_id: Optional[int], session_id: str) -> int:
        """Cria uma nova conversa.
        
        Args:
            user_id: ID do usuário (opcional)
            session_id: ID da sessão
            
        Returns:
            ID da conversa criada
        """
        query = "INSERT INTO conversations (user_id, session_id) VALUES (?, ?)"
        self.db.execute_update(query, (user_id, session_id))
        return self.db.get_last_insert_id()
    
    def add_message(self, conversation_id: int, role: str, content: str) -> int:
        """Adiciona uma mensagem à conversa.
        
        Args:
            conversation_id: ID da conversa
            role: Papel (user ou assistant)
            content: Conteúdo da mensagem
            
        Returns:
            ID da mensagem criada
        """
        query = "INSERT INTO messages (conversation_id, role, content) VALUES (?, ?, ?)"
        self.db.execute_update(query, (conversation_id, role, content))
        return self.db.get_last_insert_id()
    
    def get_conversation_history(self, conversation_id: int) -> List[Dict]:
        """Obtém histórico de uma conversa.
        
        Args:
            conversation_id: ID da conversa
            
        Returns:
            Lista de mensagens
        """
        query = """
            SELECT role, content, timestamp
            FROM messages
            WHERE conversation_id = ?
            ORDER BY timestamp ASC
        """
        return self.db.execute_query(query, (conversation_id,))
    
    def get_user_conversations(self, user_id: int, limit: int = 10) -> List[Dict]:
        """Obtém conversas de um usuário.
        
        Args:
            user_id: ID do usuário
            limit: Número máximo de conversas
            
        Returns:
            Lista de conversas
        """
        query = """
            SELECT id, session_id, started_at, ended_at
            FROM conversations
            WHERE user_id = ?
            ORDER BY started_at DESC
            LIMIT ?
        """
        return self.db.execute_query(query, (user_id, limit))
    
    def end_conversation(self, conversation_id: int):
        """Marca uma conversa como finalizada.
        
        Args:
            conversation_id: ID da conversa
        """
        query = "UPDATE conversations SET ended_at = CURRENT_TIMESTAMP WHERE id = ?"
        self.db.execute_update(query, (conversation_id,))
    
    def delete_conversation(self, conversation_id: int):
        """Deleta uma conversa e suas mensagens.
        
        Args:
            conversation_id: ID da conversa
        """
        # Deleta mensagens
        self.db.execute_update(
            "DELETE FROM messages WHERE conversation_id = ?",
            (conversation_id,)
        )
        # Deleta conversa
        self.db.execute_update(
            "DELETE FROM conversations WHERE id = ?",
            (conversation_id,)
        )
