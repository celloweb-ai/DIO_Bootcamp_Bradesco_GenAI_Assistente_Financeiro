"""Módulo de gerenciamento de banco de dados.

Este módulo fornece funcionalidades para persistência de dados,
incluindo histórico de conversas e preferências do usuário.
"""

from .db_manager import DatabaseManager
from .conversation_store import ConversationStore

__all__ = ['DatabaseManager', 'ConversationStore']
