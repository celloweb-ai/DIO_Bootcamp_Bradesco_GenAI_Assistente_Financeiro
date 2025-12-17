# Arquitetura do Sistema

## Visão Geral

O Assistente Financeiro Inteligente utiliza uma arquitetura modular baseada em microsserviços e IA generativa.

## Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                    Interface do Usuário                      │
│                     (Streamlit Web App)                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Camada de Aplicação                        │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Chatbot    │  │ Calculadoras │  │     FAQs     │      │
│  │    Engine    │  │  Financeiras │  │   Dinâmicas  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  Camada de Serviços                          │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  LLM Service │  │   Context    │  │    Data      │      │
│  │ (GPT/Gemini) │  │   Manager    │  │   Analysis   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Camada de Dados                            │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   SQLite DB  │  │  Knowledge   │  │   Vector DB  │      │
│  │  (Histórico) │  │     Base     │  │  (Embeddings)│      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## Componentes Principais

### 1. Interface do Usuário (UI)
- **Framework**: Streamlit
- **Responsabilidades**:
  - Renderização da interface web
  - Captura de inputs do usuário
  - Exibição de respostas e visualizações
  - Gerenciamento de sessões

### 2. Chatbot Engine
- **Tecnologias**: LangChain, OpenAI/Gemini
- **Funcionalidades**:
  - Processamento de linguagem natural
  - Geração de respostas contextualizadas
  - Integração com base de conhecimento
  - Chamada de ferramentas (calculadoras, APIs)

### 3. Calculadoras Financeiras
- **Módulos**:
  - Financiamento (SAC, Price, Amortização Constante)
  - Investimentos (Renda Fixa, Tesouro, Ações)
  - Aposentadoria
  - Juros Compostos
- **Saídas**: JSON, DataFrames, Visualizações

### 4. Sistema de FAQs
- **Busca Semântica**: Embeddings + Vector DB
- **Ranking**: Similaridade de cosseno
- **Personalização**: Baseada em perfil do usuário

### 5. Context Manager
- **Persistência**: SQLite
- **Funcionalidades**:
  - Histórico de conversas
  - Preferências do usuário
  - Estado da sessão
  - Memória de longo prazo

### 6. Data Analysis
- **Bibliotecas**: Pandas, NumPy, Plotly
- **Análises**:
  - Padrões de gastos
  - Projeções financeiras
  - Recomendações personalizadas

## Fluxo de Dados

### 1. Interação do Usuário
```
Usuário → Input → Streamlit → Chatbot Engine
```

### 2. Processamento
```
Chatbot Engine → LLM → Context Manager → Knowledge Base
                  ↓
              Calculadoras/APIs
```

### 3. Resposta
```
Resposta Gerada → Formatação → UI → Usuário
                      ↓
                  Persistência
```

## Segurança

### Camadas de Proteção
1. **Autenticação**: JWT tokens
2. **Criptografia**: Dados sensíveis em repouso
3. **Sanitização**: Inputs do usuário
4. **Rate Limiting**: Prevenção de abuso
5. **LGPD Compliance**: Anonimização de dados

### Boas Práticas
- Variáveis de ambiente para secrets
- Validação de inputs
- Logs auditáveis
- Backup regular de dados

## Escalabilidade

### Estratégias
1. **Cache**: Redis para respostas frequentes
2. **Queue**: Celery para tarefas assíncronas
3. **Load Balancing**: Nginx
4. **Containerização**: Docker
5. **Orquestração**: Kubernetes (produção)

## Monitoramento

### Métricas
- Tempo de resposta
- Taxa de erro
- Uso de recursos
- Satisfação do usuário

### Ferramentas
- Prometheus
- Grafana
- Sentry (erros)
- Application Insights

## Tecnologias

| Componente | Tecnologia | Versão |
|------------|------------|--------|
| Backend | Python | 3.9+ |
| Framework Web | Streamlit | 1.28+ |
| LLM | OpenAI/Gemini | - |
| Orquestração LLM | LangChain | 0.1+ |
| Banco de Dados | SQLite | 3 |
| Análise de Dados | Pandas | 2.0+ |
| Visualização | Plotly | 5.0+ |
| Testes | Pytest | 7.0+ |

## Ambientes

### Desenvolvimento
- SQLite local
- Mock de APIs externas
- Debug mode ativado

### Staging
- Banco PostgreSQL
- APIs reais (sandbox)
- Logs detalhados

### Produção
- PostgreSQL gerenciado
- APIs produção
- Otimizações ativadas
- Monitoramento completo

## Roadmap Técnico

- [ ] Migração para PostgreSQL
- [ ] Implementação de cache Redis
- [ ] API REST para integrações
- [ ] App mobile (React Native)
- [ ] Microserviços independentes
- [ ] CI/CD com GitHub Actions
- [ ] Deploy em cloud (AWS/Azure/GCP)
