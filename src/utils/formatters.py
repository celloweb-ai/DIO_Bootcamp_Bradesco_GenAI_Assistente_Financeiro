"""Formatadores de dados."""

from datetime import datetime
from typing import Optional


def format_currency(value: float, symbol: str = "R$") -> str:
    """Formata valor monetário.
    
    Args:
        value: Valor a formatar
        symbol: Símbolo da moeda
        
    Returns:
        String formatada
        
    Example:
        >>> format_currency(1234.56)
        'R$ 1.234,56'
    """
    formatted = f"{value:,.2f}"
    formatted = formatted.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{symbol} {formatted}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """Formata percentual.
    
    Args:
        value: Valor a formatar
        decimals: Número de casas decimais
        
    Returns:
        String formatada
        
    Example:
        >>> format_percentage(15.5678)
        '15,57%'
    """
    formatted = f"{value:.{decimals}f}".replace(".", ",")
    return f"{formatted}%"


def format_date(date: datetime, format_str: str = "%d/%m/%Y") -> str:
    """Formata data.
    
    Args:
        date: Data a formatar
        format_str: Formato de saída
        
    Returns:
        String formatada
        
    Example:
        >>> format_date(datetime(2024, 12, 25))
        '25/12/2024'
    """
    return date.strftime(format_str)


def format_phone(phone: str) -> str:
    """Formata número de telefone.
    
    Args:
        phone: Telefone a formatar (apenas dígitos)
        
    Returns:
        String formatada
        
    Example:
        >>> format_phone('11987654321')
        '(11) 98765-4321'
    """
    phone = ''.join(filter(str.isdigit, phone))
    
    if len(phone) == 11:
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
    elif len(phone) == 10:
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"
    
    return phone


def format_cpf(cpf: str) -> str:
    """Formata CPF.
    
    Args:
        cpf: CPF a formatar (apenas dígitos)
        
    Returns:
        String formatada
        
    Example:
        >>> format_cpf('12345678901')
        '123.456.789-01'
    """
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    return cpf
