# Diretório de Dados

Este diretório contém datasets e arquivos de dados utilizados pelo assistente financeiro.

## Estrutura

```
data/
├── raw/              # Dados brutos não processados
├── processed/        # Dados processados e limpos
├── samples/          # Dados de exemplo para testes
└── exports/          # Dados exportados das análises
```

## Datasets Disponíveis

### Samples (Demonstração)
- `sample_transactions.csv` - Transações financeiras de exemplo
- `sample_investments.csv` - Portfólio de investimentos
- `sample_faqs.json` - Base de conhecimento inicial

## Uso

Os dados são carregados automaticamente pela aplicação. Para adicionar novos datasets:

1. Coloque arquivos brutos em `raw/`
2. Processe usando scripts em `notebooks/`
3. Salve versões processadas em `processed/`

## Privacidade

⚠️ **IMPORTANTE**: Nunca commite dados sensíveis ou pessoais. Use dados anonimizados ou fictícios.
