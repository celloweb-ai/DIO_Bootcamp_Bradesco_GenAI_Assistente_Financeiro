# Casos de Uso

## Visão Geral

Documentação dos principais casos de uso do Assistente Financeiro Inteligente.

---

## 1. Consulta de Produtos Bancários

### Descrição
Usuário busca informações sobre produtos e serviços bancários.

### Atores
- Usuário (Cliente ou Prospect)
- Assistente IA
- Base de Conhecimento

### Pré-condições
- Aplicação em execução
- Base de FAQs carregada

### Fluxo Principal

1. Usuário acessa a aplicação
2. Usuário digita pergunta sobre produto (ex: "O que é CDB?")
3. Sistema identifica intenção usando NLP
4. Sistema busca na base de FAQs
5. Sistema gera resposta personalizada com IA
6. Sistema exibe resposta com links relacionados
7. Sistema sugere perguntas relacionadas

### Fluxo Alternativo 1: FAQ não encontrada

4a. Sistema não encontra FAQ específica
4b. Sistema gera resposta usando conhecimento geral do LLM
4c. Sistema registra gap para futura adição

### Pós-condições
- Conversa registrada no histórico
- Contexto atualizado para próximas interações

### Exemplo

```
Usuário: "Quanto rende a poupança?"

Assistente: "A poupança atualmente rende 70% da taxa Selic 
quando esta estiver acima de 8,5% ao ano, mais TR (Taxa 
Referencial). Com a Selic em 13,75% (dez/2024), o 
rendimento fica em aproximadamente 9,62% ao ano ou 
0,77% ao mês.

Deseja simular quanto você pode ganhar investindo na 
poupança?

📊 Calcular Rendimento | 💡 Alternativas à Poupança"
```

---

## 2. Simulação de Financiamento

### Descrição
Usuário deseja simular financiamento (imóvel, veículo, etc.).

### Atores
- Usuário
- Calculadora de Financiamento
- Módulo de Visualização

### Pré-condições
- Usuário informou intenção de simular

### Fluxo Principal

1. Usuário solicita simulação de financiamento
2. Sistema apresenta formulário interativo
3. Usuário informa:
   - Valor do bem
   - Valor de entrada
   - Prazo desejado
   - Sistema de amortização (SAC/PRICE)
4. Sistema valida dados
5. Sistema calcula parcelas
6. Sistema gera visualização comparativa
7. Sistema exibe resultados detalhados
8. Sistema oferece salvar simulação

### Fluxo Alternativo 1: Dados inválidos

4a. Sistema detecta valor inválido
4b. Sistema exibe mensagem de erro específica
4c. Sistema mantém outros campos preenchidos
4d. Retorna ao passo 3

### Fluxo Alternativo 2: Comparação de sistemas

6a. Usuário solicita comparar SAC vs PRICE
6b. Sistema calcula ambos os sistemas
6c. Sistema exibe tabela comparativa lado a lado
6d. Sistema destaca diferenças principais

### Pós-condições
- Simulação salva (opcional)
- Usuário tem todas informações necessárias

### Exemplo de Interação

```
Usuário: "Quero financiar um carro de R$ 50.000"

Assistente: "Vou te ajudar a simular! Preciso de algumas 
informações:"

[Formulário exibido]
Valor do veículo: R$ 50.000
Entrada: R$ 10.000
Prazo: 48 meses
Sistema: SAC ▼

[Calcular]

Resultados:
┌─────────────────────────────────┐
│ Sistema SAC - 48 meses         │
│ Taxa: 1,5% a.m. (19,56% a.a.) │
├─────────────────────────────────┤
│ Primeira parcela: R$ 1.433,33  │
│ Última parcela: R$ 842,08      │
│ Total de juros: R$ 14.800,00   │
│ Total a pagar: R$ 54.800,00    │
└─────────────────────────────────┘

[Ver tabela completa] [Comparar com PRICE] [Salvar]
```

---

## 3. Análise de Gastos Pessoais

### Descrição
Usuário carrega dados bancários para análise e insights.

### Atores
- Usuário
- Módulo de Análise de Dados
- IA Generativa (para insights)

### Pré-condições
- Usuário tem arquivo CSV/Excel com transações
- Arquivo segue formato esperado

### Fluxo Principal

1. Usuário acessa seção "Análise de Dados"
2. Usuário faz upload do arquivo
3. Sistema valida formato e dados
4. Sistema processa transações
5. Sistema categoriza automaticamente
6. Sistema gera visualizações:
   - Gastos por categoria
   - Evolução temporal
   - Comparativo mensal
7. IA gera insights personalizados
8. Sistema exibe recomendações
9. Usuário pode fazer perguntas sobre dados

### Fluxo Alternativo 1: Arquivo inválido

3a. Sistema detecta formato incorreto
3b. Sistema exibe exemplo de formato correto
3c. Sistema permite baixar template
3d. Retorna ao passo 2

### Fluxo Alternativo 2: Categorização manual

5a. Sistema não reconhece categoria
5b. Sistema solicita confirmação do usuário
5c. Sistema aprende com a escolha
5d. Continua no passo 6

### Pós-condições
- Dados analisados e salvos
- Insights gerados e disponíveis
- Modelo melhorado com feedback

### Exemplo de Insights

```
📊 Análise - Novembro 2024

💰 Resumo Financeiro
Receitas: R$ 8.500,00
Despesas: R$ 6.750,00
Saldo: +R$ 1.750,00 (20,6%)

📈 Principais Insights:

1. 🍔 Alimentação em alta
   Você gastou 35% a mais com alimentação este mês 
   (R$ 1.850 vs R$ 1.370 média).
   
   Sugestão: Considere meal prep para reduzir gastos 
   com delivery.

2. 💡 Economia em energia
   Parabéns! Sua conta de luz reduziu 15%.
   Economia de R$ 45,00.

3. 🎯 Meta de investimento
   Você investiu R$ 1.000 este mês.
   Faltam R$ 500 para sua meta de 15% da renda.

[Ver detalhes] [Exportar relatório] [Definir metas]
```

---

## 4. Planejamento de Aposentadoria

### Descrição
Usuário quer planejar aposentadoria e descobrir quanto precisa poupar.

### Atores
- Usuário
- Calculadora de Investimentos
- IA para recomendações

### Pré-condições
- Nenhuma

### Fluxo Principal

1. Usuário expressa interesse em aposentadoria
2. Sistema inicia questionário guiado:
   - Idade atual
   - Idade desejada para aposentadoria
   - Renda mensal desejada
   - Quanto já tem poupado
   - Quanto pode poupar mensalmente
3. Sistema calcula valor necessário
4. Sistema simula diferentes cenários:
   - Conservador (Renda fixa)
   - Moderado (Misto)
   - Arrojado (Renda variável)
5. Sistema mostra evolução do patrimônio
6. Sistema gera plano de ação personalizado
7. Usuário pode ajustar parâmetros

### Fluxo Alternativo 1: Meta inatingível

3a. Sistema detecta que meta é irreal
3b. Sistema sugere ajustes:
   - Aumentar idade de aposentadoria
   - Reduzir renda desejada
   - Aumentar aportes mensais
3c. Usuário ajusta parâmetros
3d. Retorna ao passo 3

### Pós-condições
- Plano de aposentadoria gerado
- Usuário tem clareza sobre próximos passos

### Exemplo

```
Usuário: "Quero me aposentar aos 60 anos"

Assistente: "Ótimo! Vou te ajudar a planejar. 
Qual sua idade hoje?"

Usuário: "35 anos"

Assistente: "Perfeito! Você tem 25 anos para construir 
seu patrimônio. Qual renda mensal deseja na aposentadoria?"

Usuário: "R$ 10.000 por mês"

Assistente: "Entendi. Para garantir R$ 10.000/mês 
até os 85 anos, você precisará de aproximadamente 
R$ 3.000.000.

Considerando investimentos com rentabilidade média 
de 8% a.a., você precisaria investir:

💰 Sem patrimônio atual: R$ 3.200/mês
💰 Com R$ 100.000 hoje: R$ 2.400/mês

Você já tem algum valor investido?"
```

---

## 5. Educação Financeira Interativa

### Descrição
Usuário quer aprender sobre finanças de forma interativa.

### Atores
- Usuário
- IA Educadora
- Base de Conhecimento

### Pré-condições
- Nenhuma

### Fluxo Principal

1. Usuário acessa seção "Aprender"
2. Sistema apresenta trilhas de aprendizado:
   - Básico (Controle financeiro)
   - Intermediário (Investimentos)
   - Avançado (Estratégias complexas)
3. Usuário escolhe trilha ou tópico específico
4. Sistema apresenta conteúdo de forma conversacional
5. Sistema intercala com perguntas práticas
6. Sistema usa exemplos personalizados
7. Sistema avalia compreensão
8. Sistema recomenda próximos tópicos

### Fluxo Alternativo 1: Dúvida durante aprendizado

4a. Usuário faz pergunta
4b. Sistema responde contextualizadamente
4c. Sistema oferece aprofundar tópico
4d. Retorna ao conteúdo ou aprofunda

### Pós-condições
- Progresso salvo
- Certificado virtual (ao completar trilha)

### Exemplo

```
📚 Trilha: Investimentos para Iniciantes
Módulo 1: Entendendo Renda Fixa
Progresso: ████░░░░░░ 40%

Assistente: "Vamos falar sobre CDB!

CDB é como emprestar dinheiro ao banco. Em troca, 
o banco te paga juros. É garantido pelo FGC até 
R$ 250.000.

Por exemplo: você investe R$ 10.000 em um CDB que 
paga 120% do CDI por 2 anos.

Sabendo que o CDI hoje está em ~13,65% ao ano, 
quanto você acha que terá no final?

a) R$ 10.500
b) R$ 12.900
c) R$ 13.100
d) R$ 15.000"

Usuário: "b"

Assistente: "🎉 Correto! Muito bem!

Com 120% do CDI, você teria aproximadamente 
R$ 12.928.

Agora uma pergunta: se você precisar do dinheiro 
antes dos 2 anos, o que acontece?"
```

---

## 6. Atendimento Multicanal

### Descrição
Usuário inicia conversa em um canal e continua em outro.

### Atores
- Usuário
- Sistema de Sessões
- Múltiplos canais (Web, Mobile)

### Pré-condições
- Usuário autenticado
- Sistema de sessões configurado

### Fluxo Principal

1. Usuário inicia conversa no navegador
2. Sistema cria sessão com ID único
3. Usuário faz perguntas e recebe respostas
4. Usuário fecha navegador
5. Mais tarde, abre app mobile
6. Sistema recupera sessão ativa
7. Sistema exibe histórico
8. Usuário continua de onde parou

### Fluxo Alternativo 1: Nova sessão

6a. Usuário prefere começar nova conversa
6b. Sistema arquiva sessão anterior
6c. Sistema cria nova sessão
6d. Histórico anterior acessível em "Conversas Antigas"

### Pós-condições
- Contexto preservado entre sessões
- Experiência contínua

---

## 7. Alertas Inteligentes

### Descrição
Sistema proativamente alerta usuário sobre oportunidades ou riscos.

### Atores
- Sistema de Monitoramento
- Usuário
- Módulo de Notificações

### Pré-condições
- Usuário configurou preferências de alerta
- Sistema tem dados do usuário

### Fluxo Principal

1. Sistema monitora continuamente:
   - Taxas de juros
   - Gastos anormais
   - Oportunidades de investimento
   - Vencimentos
2. Sistema detecta evento relevante
3. Sistema avalia relevância para usuário
4. Sistema gera alerta personalizado
5. Sistema envia notificação
6. Usuário visualiza e pode agir

### Exemplos de Alertas

```
⚠️ Gasto Incomum Detectado
Você gastou R$ 850 em "Alimentação" esta semana.
Isso é 120% acima da sua média.

[Ver detalhes] [Está tudo OK]

---

💡 Oportunidade de Investimento
A taxa do Tesouro Selic aumentou para 14,25%.
Com esse valor, seus R$ 10.000 renderiam R$ 118/mês.

[Simular] [Investir agora] [Lembrar depois]

---

📅 Lembrete
Fatura do cartão vence em 3 dias: R$ 2.450,00
Saldo disponível: R$ 3.100,00 ✓

[Pagar agora] [Já paguei]
```

---

## Métricas de Sucesso

Para cada caso de uso, medimos:

- **Taxa de Conclusão**: % que completam o fluxo
- **Tempo Médio**: Duração da interação
- **Satisfação**: Rating do usuário (1-5)
- **Taxa de Erro**: % de falhas
- **Retenção**: Usuários que retornam

---

## Roadmap de Casos de Uso

### Em Desenvolvimento
- [ ] Integração com Open Banking
- [ ] Recomendação de cartão de crédito
- [ ] Comparador de investimentos

### Planejado
- [ ] Negociação de dívidas
- [ ] Análise de crédito imobiliário
- [ ] Planejamento de viagens
- [ ] Gestão de benefícios corporativos
