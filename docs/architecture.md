# Arquitetura do Sistema

## Visão Geral

O Assistente Financeiro Inteligente segue uma arquitetura modular baseada em microserviços, permitindo escalabilidade e manutenibilidade.

## Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────┐
│                  Interface Streamlit                     │
│                      (app.py)                           │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
   ┌────▼─────┐            ┌─────▼──────┐
   │ Chatbot  │            │ Analytics  │
   │  Module  │            │   Module   │
   └────┬─────┘            └─────┬──────┘
        │                        │
   ┌────▼──────────────────┬─────▼──────┐
   │  LLM Integration      │  Data      │
   │  (OpenAI/Gemini)      │  Analysis  │
   └───────────────────────┴────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
   ┌────▼─────┐            ┌─────▼──────┐
   │  FAQs    │            │ Context    │
   │  Module  │            │  Manager   │
   └────┬─────┘            └─────┬──────┘
        │                        │
   ┌────▼────────────────────────▼──────┐
   │      Database Layer (SQLite)       │
   └────────────────────────────────────┘
```

## Componentes Principais

### 1. Interface (Streamlit)
- **Responsabilidade**: Renderização da UI e gerenciamento de sessão
- **Tecnologia**: Streamlit 1.28+
- **Comunicação**: Chamadas síncronas aos módulos

### 2. Chatbot Module
- **Responsabilidade**: Processamento de linguagem natural
- **Componentes**:
  - `ChatbotEngine`: Orquestração de conversas
  - `IntentClassifier`: Classificação de intenções
  - `ResponseGenerator`: Geração de respostas
- **Tecnologia**: LangChain, OpenAI API

### 3. Calculators Module
- **Responsabilidade**: Cálculos financeiros
- **Funções**:
  - Financiamentos (SAC, PRICE)
  - Investimentos
  - Juros compostos
  - Simulações

### 4. Knowledge Base (FAQs)
- **Responsabilidade**: Gerenciamento de perguntas frequentes
- **Recursos**:
  - Busca semântica
  - Embeddings vetoriais
  - Cache de respostas

### 5. Data Analysis
- **Responsabilidade**: Análise e visualização de dados
- **Bibliotecas**: Pandas, Plotly, NumPy
- **Outputs**: Gráficos interativos, insights

### 6. Context Manager
- **Responsabilidade**: Persistência de conversações
- **Armazenamento**: SQLite com backup JSON
- **Features**: Histórico, sessões, preferências

### 7. Database Layer
- **Responsabilidade**: Persistência de dados
- **Tecnologia**: SQLite3
- **Tabelas**:
  - `conversations`: Histórico de conversas
  - `user_preferences`: Preferências do usuário
  - `faqs_cache`: Cache de FAQs

## Fluxo de Dados

### Fluxo de Conversa Típica

```
Usuário → Streamlit → ChatbotEngine
                          ↓
                   IntentClassifier
                          ↓
            ┌─────────────┴─────────────┐
            │                           │
       FAQ Module              Calculator Module
            │                           │
            └─────────────┬─────────────┘
                          ↓
                  ResponseGenerator
                          ↓
                   ContextManager
                          ↓
                      Database
                          ↓
                    Streamlit UI
```

## Segurança

### Camadas de Segurança

1. **Autenticação**: Tokens de sessão
2. **Criptografia**: AES-256 para dados sensíveis
3. **Validação**: Input sanitization
4. **Rate Limiting**: Proteção contra abuso
5. **Logs**: Auditoria de acessos

### Conformidade LGPD

- Consentimento explícito
- Direito ao esquecimento
- Portabilidade de dados
- Anonimização quando aplicável

## Escalabilidade

### Vertical
- Otimização de queries SQL
- Cache em memória (Redis futuro)
- Compressão de dados

### Horizontal
- Preparado para containerização (Docker)
- Stateless quando possível
- Microserviços independentes

## Monitoramento

- **Logs**: Estruturados em JSON
- **Métricas**: Tempo de resposta, taxa de erro
- **Alertas**: Thresholds configuráveis

## Tecnologias

| Componente | Tecnologia | Versão |
|------------|------------|--------|
| Backend | Python | 3.9+ |
| UI | Streamlit | 1.28+ |
| LLM | OpenAI/Gemini | Latest |
| Database | SQLite | 3.x |
| Orquestração | LangChain | 0.1+ |
| Análise | Pandas | 2.x |
| Visualização | Plotly | 5.x |

## Deployment

### Ambientes

1. **Desenvolvimento**: Local com SQLite
2. **Staging**: Streamlit Cloud
3. **Produção**: Cloud (AWS/Azure/GCP)

### CI/CD

- GitHub Actions para testes
- Deploy automático via Git push
- Rollback automático em falhas

## Próximos Passos

- [ ] Migração para PostgreSQL
- [ ] Implementação de cache Redis
- [ ] API REST para integrações
- [ ] Containerização com Docker
- [ ] Kubernetes para orquestração
