# Dados do Projeto

Este diretório contém os dados utilizados pelo Assistente Financeiro.

## Estrutura

```
data/
├── raw/              # Dados brutos (não processados)
├── processed/        # Dados processados e limpos
├── external/         # Dados de fontes externas
├── samples/          # Amostras para testes e demonstração
└── README.md         # Este arquivo
```

## Tipos de Dados

### 1. Dados de Usuários (Anonimizados)
- Preferências de produtos
- Histórico de interações
- Perfil de risco

### 2. Dados Financeiros
- Taxas de juros históricas
- Índices econômicos (CDI, IPCA, Selic)
- Cotações de ativos

### 3. Base de Conhecimento
- FAQs e respostas
- Descrições de produtos
- Termos financeiros

## Segurança e Privacidade

⚠️ **IMPORTANTE**: 
- Nunca commitar dados sensíveis ou identificáveis
- Todos os dados de usuários devem ser anonimizados
- Utilizar `.gitignore` para arquivos de dados grandes
- Conformidade com LGPD

## Fontes de Dados

- Banco Central do Brasil (BCB)
- IBGE
- B3 (Bolsa de Valores)
- Dados sintéticos para demonstração
