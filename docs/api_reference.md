# API Reference

## Visão Geral

Documentação completa das APIs e módulos do Assistente Financeiro.

## Módulos

### 1. Chatbot Module

#### `ChatbotEngine`

```python
from src.chatbot import ChatbotEngine

engine = ChatbotEngine(api_key="your_key", model="gpt-4")
response = engine.chat(message="Como investir em CDB?", context={})
```

**Métodos:**

##### `chat(message: str, context: dict) -> dict`

Processa uma mensagem do usuário e retorna resposta.

**Parâmetros:**
- `message` (str): Mensagem do usuário
- `context` (dict): Contexto da conversa

**Retorna:**
```python
{
    "response": str,      # Resposta gerada
    "intent": str,        # Intenção identificada
    "confidence": float,  # Confiança (0-1)
    "suggestions": list   # Sugestões de follow-up
}
```

##### `reset_context() -> None`

Reseta o contexto da conversa.

---

### 2. Calculators Module

#### `FinancingCalculator`

```python
from src.calculators import FinancingCalculator

calc = FinancingCalculator()
result = calc.calculate_sac(
    principal=100000,
    annual_rate=10.5,
    months=24
)
```

**Métodos:**

##### `calculate_sac(principal: float, annual_rate: float, months: int) -> dict`

Calcula financiamento pelo Sistema SAC.

**Parâmetros:**
- `principal` (float): Valor financiado
- `annual_rate` (float): Taxa anual (%)
- `months` (int): Prazo em meses

**Retorna:**
```python
{
    "installments": [          # Lista de parcelas
        {
            "number": int,
            "payment": float,
            "principal": float,
            "interest": float,
            "balance": float
        }
    ],
    "total_paid": float,       # Total pago
    "total_interest": float    # Juros totais
}
```

##### `calculate_price(principal: float, annual_rate: float, months: int) -> dict`

Calcula financiamento pelo Sistema PRICE.

**Parâmetros:** Mesmos do SAC

**Retorna:** Mesma estrutura do SAC

##### `calculate_investment(initial: float, monthly: float, rate: float, months: int) -> dict`

Calcula rendimento de investimento.

**Parâmetros:**
- `initial` (float): Valor inicial
- `monthly` (float): Aporte mensal
- `rate` (float): Taxa mensal (%)
- `months` (int): Período em meses

**Retorna:**
```python
{
    "invested": float,         # Total investido
    "final_value": float,      # Valor final
    "earnings": float,         # Rendimento
    "monthly_data": [          # Evolução mensal
        {
            "month": int,
            "balance": float,
            "interest": float
        }
    ]
}
```

---

### 3. FAQs Module

#### `FAQManager`

```python
from src.faqs import FAQManager

faq = FAQManager()
results = faq.search("como abrir conta")
```

**Métodos:**

##### `search(query: str, limit: int = 5) -> list`

Busca FAQs relevantes.

**Parâmetros:**
- `query` (str): Pergunta do usuário
- `limit` (int): Máximo de resultados

**Retorna:**
```python
[
    {
        "id": int,
        "question": str,
        "answer": str,
        "category": str,
        "similarity": float  # Score de similaridade
    }
]
```

##### `add_faq(question: str, answer: str, category: str) -> int`

Adiciona nova FAQ.

**Retorna:** ID da FAQ criada

##### `get_categories() -> list`

Retorna todas as categorias disponíveis.

---

### 4. Data Analysis Module

#### `FinancialAnalyzer`

```python
from src.data_analysis import FinancialAnalyzer
import pandas as pd

df = pd.read_csv('transactions.csv')
analyzer = FinancialAnalyzer(df)
insights = analyzer.generate_insights()
```

**Métodos:**

##### `generate_insights() -> dict`

Gera insights dos dados financeiros.

**Retorna:**
```python
{
    "summary": {
        "total_income": float,
        "total_expenses": float,
        "balance": float,
        "avg_monthly_expense": float
    },
    "by_category": dict,       # Gastos por categoria
    "trends": dict,            # Tendências temporais
    "recommendations": list    # Recomendações
}
```

##### `plot_expenses(by: str = 'category') -> plotly.graph_objs.Figure`

Gera gráfico de despesas.

**Parâmetros:**
- `by` (str): Agrupamento ('category', 'month', 'type')

**Retorna:** Objeto Figure do Plotly

##### `predict_next_month() -> dict`

Prevê gastos do próximo mês.

**Retorna:**
```python
{
    "predicted_expenses": float,
    "confidence_interval": (float, float),
    "by_category": dict
}
```

---

### 5. Context Manager

#### `ContextManager`

```python
from src.context_manager import ContextManager

ctx = ContextManager()
ctx.add_message("user", "Olá")
ctx.add_message("assistant", "Como posso ajudar?")
history = ctx.get_history()
```

**Métodos:**

##### `add_message(role: str, content: str) -> None`

Adiciona mensagem ao contexto.

**Parâmetros:**
- `role` (str): 'user' ou 'assistant'
- `content` (str): Conteúdo da mensagem

##### `get_history(limit: int = 10) -> list`

Retorna histórico de mensagens.

**Parâmetros:**
- `limit` (int): Número máximo de mensagens

**Retorna:**
```python
[
    {
        "role": str,
        "content": str,
        "timestamp": str
    }
]
```

##### `save_session() -> str`

Salva sessão no banco de dados.

**Retorna:** ID da sessão

##### `load_session(session_id: str) -> bool`

Carrega sessão salva.

**Retorna:** True se sucesso

---

### 6. Database Module

#### `DatabaseManager`

```python
from src.database import DatabaseManager

db = DatabaseManager()
db.execute("INSERT INTO ...", params)
results = db.query("SELECT * FROM ...")
```

**Métodos:**

##### `execute(query: str, params: tuple = None) -> int`

Executa query de modificação.

**Retorna:** Número de linhas afetadas

##### `query(sql: str, params: tuple = None) -> list`

Executa query de consulta.

**Retorna:** Lista de resultados

##### `create_tables() -> None`

Cria estrutura do banco de dados.

---

## Utilities

### `src.utils.validators`

```python
from src.utils.validators import validate_cpf, validate_email

if validate_cpf("123.456.789-00"):
    print("CPF válido")
```

**Funções:**

- `validate_cpf(cpf: str) -> bool`
- `validate_email(email: str) -> bool`
- `validate_phone(phone: str) -> bool`
- `sanitize_input(text: str) -> str`

### `src.utils.formatters`

```python
from src.utils.formatters import format_currency, format_percentage

print(format_currency(1250.50))  # "R$ 1.250,50"
print(format_percentage(0.125))   # "12,5%"
```

**Funções:**

- `format_currency(value: float) -> str`
- `format_percentage(value: float) -> str`
- `format_date(date: datetime) -> str`

---

## Códigos de Erro

| Código | Descrição |
|--------|----------|
| 1001 | Erro de validação de entrada |
| 1002 | Parâmetro obrigatório ausente |
| 2001 | Erro de conexão com LLM |
| 2002 | Rate limit excedido |
| 3001 | Erro de banco de dados |
| 3002 | Sessão não encontrada |
| 4001 | Erro de cálculo |
| 5001 | FAQ não encontrada |

---

## Exemplos de Uso Completos

### Exemplo 1: Conversa Completa

```python
from src.chatbot import ChatbotEngine
from src.context_manager import ContextManager

engine = ChatbotEngine()
context = ContextManager()

# Primeira mensagem
response = engine.chat("Quero investir R$ 10.000", {})
context.add_message("user", "Quero investir R$ 10.000")
context.add_message("assistant", response["response"])

# Segunda mensagem com contexto
ctx_dict = context.get_context()
response = engine.chat("Qual rende mais?", ctx_dict)
```

### Exemplo 2: Análise Financeira Completa

```python
import pandas as pd
from src.data_analysis import FinancialAnalyzer

df = pd.read_csv('data/samples/sample_transactions.csv')
analyzer = FinancialAnalyzer(df)

# Gerar insights
insights = analyzer.generate_insights()

# Criar visualização
fig = analyzer.plot_expenses(by='category')
fig.show()

# Previsão
prediction = analyzer.predict_next_month()
print(f"Previsão: R$ {prediction['predicted_expenses']:.2f}")
```

### Exemplo 3: Calculadora de Investimento

```python
from src.calculators import FinancingCalculator
import pandas as pd

calc = FinancingCalculator()

result = calc.calculate_investment(
    initial=10000,
    monthly=500,
    rate=0.8,  # 0.8% ao mês
    months=24
)

df = pd.DataFrame(result['monthly_data'])
print(f"Total investido: R$ {result['invested']:.2f}")
print(f"Valor final: R$ {result['final_value']:.2f}")
print(f"Rendimento: R$ {result['earnings']:.2f}")
```
