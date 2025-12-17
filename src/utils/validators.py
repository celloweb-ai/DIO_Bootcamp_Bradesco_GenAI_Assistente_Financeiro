"""Validadores de dados."""

import re
from typing import Optional


def validate_email(email: str) -> bool:
    """Valida endereço de email.
    
    Args:
        email: Email a validar
        
    Returns:
        True se válido, False caso contrário
        
    Example:
        >>> validate_email('user@example.com')
        True
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_cpf(cpf: str) -> bool:
    """Valida CPF.
    
    Args:
        cpf: CPF a validar
        
    Returns:
        True se válido, False caso contrário
        
    Example:
        >>> validate_cpf('123.456.789-01')
        True ou False dependendo da validação
    """
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula primeiro dígito verificador
    sum_digits = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digit1 = (sum_digits * 10 % 11) % 10
    
    if digit1 != int(cpf[9]):
        return False
    
    # Calcula segundo dígito verificador
    sum_digits = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digit2 = (sum_digits * 10 % 11) % 10
    
    return digit2 == int(cpf[10])


def validate_phone(phone: str) -> bool:
    """Valida telefone brasileiro.
    
    Args:
        phone: Telefone a validar
        
    Returns:
        True se válido, False caso contrário
        
    Example:
        >>> validate_phone('(11) 98765-4321')
        True
    """
    # Remove caracteres não numéricos
    phone = ''.join(filter(str.isdigit, phone))
    
    # Verifica se tem 10 ou 11 dígitos (celular com 9)
    if len(phone) not in [10, 11]:
        return False
    
    # Verifica DDD válido (11 a 99)
    ddd = int(phone[:2])
    if ddd < 11 or ddd > 99:
        return False
    
    return True


def validate_amount(amount: str) -> Optional[float]:
    """Valida e converte valor monetário.
    
    Args:
        amount: Valor a validar
        
    Returns:
        Float com o valor ou None se inválido
        
    Example:
        >>> validate_amount('R$ 1.234,56')
        1234.56
    """
    try:
        # Remove símbolos e espaços
        amount = amount.replace('R$', '').replace(' ', '')
        # Substitui separadores brasileiros
        amount = amount.replace('.', '').replace(',', '.')
        value = float(amount)
        return value if value >= 0 else None
    except ValueError:
        return None
