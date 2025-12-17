"""Funções auxiliares gerais."""

import uuid
import hashlib
import re
from typing import Optional
from datetime import datetime


def generate_session_id() -> str:
    """Gera um ID único de sessão.
    
    Returns:
        String com UUID
        
    Example:
        >>> session_id = generate_session_id()
        >>> len(session_id)
        36
    """
    return str(uuid.uuid4())


def hash_password(password: str) -> str:
    """Gera hash de senha.
    
    Args:
        password: Senha a ser hasheada
        
    Returns:
        Hash SHA-256 da senha
    """
    return hashlib.sha256(password.encode()).hexdigest()


def sanitize_input(text: str) -> str:
    """Remove caracteres potencialmente perigosos.
    
    Args:
        text: Texto a sanitizar
        
    Returns:
        Texto sanitizado
        
    Example:
        >>> sanitize_input('<script>alert("xss")</script>')
        'scriptalert("xss")/script'
    """
    # Remove tags HTML
    text = re.sub(r'<[^>]+>', '', text)
    # Remove caracteres de controle
    text = ''.join(char for char in text if ord(char) >= 32 or char == '\n')
    return text.strip()


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Trunca texto para comprimento máximo.
    
    Args:
        text: Texto a truncar
        max_length: Comprimento máximo
        suffix: Sufixo a adicionar
        
    Returns:
        Texto truncado
        
    Example:
        >>> truncate_text('Este é um texto muito longo', 10)
        'Este é um...'
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def calculate_age(birth_date: datetime) -> int:
    """Calcula idade a partir da data de nascimento.
    
    Args:
        birth_date: Data de nascimento
        
    Returns:
        Idade em anos
        
    Example:
        >>> calculate_age(datetime(2000, 1, 1))
        24  # assumindo ano atual 2024
    """
    today = datetime.now()
    age = today.year - birth_date.year
    
    # Ajusta se ainda não fez aniversário este ano
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age


def extract_numbers(text: str) -> list:
    """Extrai todos os números de um texto.
    
    Args:
        text: Texto a processar
        
    Returns:
        Lista de números encontrados
        
    Example:
        >>> extract_numbers('Tenho R$ 1.500,00 e preciso de mais 500')
        [1500.0, 500.0]
    """
    # Remove símbolos de moeda
    text = text.replace('R$', '')
    # Encontra padrões de números
    pattern = r'\d+[.,]?\d*'
    matches = re.findall(pattern, text)
    
    numbers = []
    for match in matches:
        # Converte formato brasileiro para float
        num = match.replace('.', '').replace(',', '.')
        try:
            numbers.append(float(num))
        except ValueError:
            continue
    
    return numbers
