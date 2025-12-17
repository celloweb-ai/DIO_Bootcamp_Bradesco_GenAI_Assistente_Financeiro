# Diretório de Dados

Este diretório contém datasets e arquivos de dados utilizados pelo assistente financeiro.

## Estrutura

```
data/
├── raw/              # Dados brutos não processados
├── processed/        # Dados processados e limpos
├── external/         # Dados de fontes externas
├── samples/          # Amostras de dados para testes
└── exports/          # Dados exportados e relatórios
```

## Tipos de Dados

### Dados de Mercado
- Cotações de ações
- Índices econômicos
- Taxas de juros
- Inflação (IPCA, IGP-M)

### Dados de Produtos
- Informações de produtos bancários
- Taxas e tarifas
- Características de investimentos

### Dados de Usuário (anonimizados)
- Perfis de investidor
- Histórico de interações
- Preferências e configurações

## Segurança e Privacidade

⚠️ **IMPORTANTE**: 
- Nunca commite dados sensíveis ou pessoais identificáveis
- Use dados anonimizados ou sintéticos para testes
- Dados reais devem estar listados no `.gitignore`
- Siga as diretrizes da LGPD

## Fontes de Dados

- **B3**: Dados de mercado de capitais
- **Banco Central**: Taxas e indicadores econômicos
- **IBGE**: Índices de inflação e dados demográficos
- **CVM**: Informações sobre fundos de investimento
