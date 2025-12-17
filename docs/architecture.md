# Arquitetura do Sistema

## Visão Geral

O Assistente Financeiro Inteligente é construído com uma arquitetura modular em camadas, permitindo escalabilidade, manutenibilidade e fácil integração de novos componentes.

## Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                    Interface do Usuário                 │
│                   (Streamlit Web App)                   │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  Camada de Aplicação                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ Chatbot  │  │  FAQs    │  │Calculator│             │
│  │ Engine   │  │  System  │  │  Engine  │             │
│  └──────────┘  └──────────┘  └──────────┘             │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  Camada de Serviços                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │   LLM    │  │ Context  │  │   Data   │             │
│  │ Service  │  │ Manager  │  │ Analysis │             │
│  └──────────┘  └──────────┘  └──────────┘             │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  Camada de Dados                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │  SQLite  │  │Knowledge │  │ External │             │
│  │    DB    │  │   Base   │  │   APIs   │             │
│  └──────────┘  └──────────┘  └──────────┘             │
└─────────────────────────────────────────────────────────┘
```

## Componentes Principais

### 1. Interface do Usuário (UI Layer)

**Tecnologia**: Streamlit

**Responsabilidades**:
- Renderização da interface web
- Captura de entrada do usuário
- Exibição de respostas e visualizações
- Gerenciamento de estado da sessão

### 2. Camada de Aplicação

#### 2.1 Chatbot Engine
- Processamento de linguagem natural
- Interpretação de intenções do usuário
- Geração de respostas contextualizadas
- Integração com LLM (OpenAI GPT/Google Gemini)

#### 2.2 FAQ System
- Busca semântica em base de conhecimento
- Matching de perguntas e respostas
- Ranking de relevância
- Aprendizado contínuo

#### 2.3 Calculator Engine
- Cálculos financeiros (SAC, Price, Juros Compostos)
- Simulações de investimento
- Projeções de aposentadoria
- Validação de entrada

### 3. Camada de Serviços

#### 3.1 LLM Service
- Abstração de provedores de IA (OpenAI, Gemini)
- Gerenciamento de prompts
- Controle de tokens e custos
- Fallback entre modelos

#### 3.2 Context Manager
- Persistência do histórico de conversas
- Gerenciamento de memória da sessão
- Recuperação de contexto relevante
- Limpeza de contexto antigo

#### 3.3 Data Analysis Service
- Análise de transações
- Geração de insights
- Visualizações com Plotly
- Detecção de padrões

### 4. Camada de Dados

#### 4.1 SQLite Database
- Armazenamento de conversas
- Cache de respostas
- Configurações do usuário
- Logs de auditoria

#### 4.2 Knowledge Base
- FAQs estruturadas
- Documentação de produtos
- Políticas e regulamentações
- Embeddings para busca semântica

#### 4.3 External APIs
- APIs bancárias (Open Banking)
- Cotações de mercado
- Dados econômicos
- Serviços de terceiros

## Fluxo de Dados

### Fluxo de Conversação

```
Usuário → Streamlit → Chatbot Engine → LLM Service → Resposta
                ↓                           ↑
         Context Manager ←───────────────────┘
                ↓
            SQLite DB
```

### Fluxo de Cálculo

```
Usuário → Streamlit → Calculator Engine → Validação → Cálculo → Resultado
                                              ↓
                                        Data Analysis
                                              ↓
                                        Visualização
```

## Padrões de Design

### 1. **Singleton Pattern**
- Usado para gerenciadores de conexão de banco de dados
- Garante única instância de serviços críticos

### 2. **Factory Pattern**
- Criação de instâncias de LLM baseado em configuração
- Permite fácil troca entre provedores

### 3. **Strategy Pattern**
- Diferentes estratégias de cálculo financeiro
- Algoritmos de busca em FAQs

### 4. **Observer Pattern**
- Notificações de eventos da aplicação
- Logging e monitoramento

## Segurança

### Camadas de Segurança

1. **Autenticação** (planejado)
   - OAuth 2.0
   - JWT tokens
   - Multi-fator authentication

2. **Autorização**
   - RBAC (Role-Based Access Control)
   - Políticas de acesso granular

3. **Criptografia**
   - Dados em repouso (AES-256)
   - Dados em trânsito (TLS 1.3)
   - Variáveis de ambiente para secrets

4. **Conformidade**
   - LGPD (Lei Geral de Proteção de Dados)
   - Auditoria de acessos
   - Anonimização de dados

## Escalabilidade

### Estratégias de Escala

1. **Horizontal Scaling**
   - Containerização com Docker
   - Orquestração com Kubernetes (futuro)
   - Load balancing

2. **Caching**
   - Cache de respostas frequentes
   - Redis para sessões (planejado)
   - CDN para assets estáticos

3. **Otimização de Banco de Dados**
   - Índices adequados
   - Particionamento de tabelas
   - Migração para PostgreSQL (futuro)

## Monitoramento e Observabilidade

### Métricas
- Tempo de resposta
- Taxa de erro
- Uso de tokens LLM
- Conversões/interações bem-sucedidas

### Logging
- Logs estruturados (JSON)
- Níveis: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Agregação com ELK Stack (planejado)

### Alertas
- Threshold de erros
- Latência elevada
- Consumo excessivo de API

## Tecnologias e Ferramentas

| Camada | Tecnologia | Versão |
|--------|-----------|--------|
| Frontend | Streamlit | 1.28+ |
| Backend | Python | 3.9+ |
| LLM | OpenAI GPT | 4.0 |
| LLM Alt | Google Gemini | Pro |
| Database | SQLite | 3.0 |
| Analytics | Pandas | 2.0+ |
| Viz | Plotly | 5.0+ |
| Testing | Pytest | 7.0+ |
| CI/CD | GitHub Actions | - |

## Roadmap Técnico

### Curto Prazo (3 meses)
- [ ] Integração com Open Banking
- [ ] Sistema de autenticação
- [ ] Testes de integração completos
- [ ] Dockerização

### Médio Prazo (6 meses)
- [ ] Migração para PostgreSQL
- [ ] API REST completa
- [ ] Cache com Redis
- [ ] Monitoramento com Prometheus

### Longo Prazo (12 meses)
- [ ] App mobile (React Native)
- [ ] Kubernetes deployment
- [ ] Machine Learning personalizado
- [ ] Multi-tenancy

## Referências

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [LangChain Documentation](https://python.langchain.com/)
- [Python Best Practices](https://docs.python-guide.org/)
