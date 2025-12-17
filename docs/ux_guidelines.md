# Guia de UX/UI - Assistente Financeiro

## Princípios de Design

### 1. Simplicidade
- Interface limpa e intuitiva
- Fluxos diretos sem passos desnecessários
- Linguagem clara e acessível

### 2. Confiabilidade
- Design profissional que transmite segurança
- Feedback claro em todas as ações
- Transparência nos processos

### 3. Acessibilidade
- Contraste adequado (WCAG AA)
- Suporte a leitores de tela
- Navegação por teclado
- Textos legíveis (mín. 14px)

## Paleta de Cores

### Cores Principais
```
Primária (Azul Bradesco): #CC092F / #E30613
Secundária (Azul): #003A70
Sucesso: #28A745
Alerta: #FFC107
Erro: #DC3545
Neutro: #6C757D
```

### Aplicação
- **Primária**: CTAs principais, destaques
- **Secundária**: Links, elementos secundários
- **Sucesso**: Confirmações, resultados positivos
- **Alerta**: Avisos, atenção necessária
- **Erro**: Erros, validações falhas

## Tipografia

### Hierarquia
```
H1: 32px - Títulos principais
H2: 24px - Seções
H3: 20px - Subseções
Body: 16px - Texto principal
Caption: 14px - Legendas
Small: 12px - Notas
```

### Fontes
- **Principal**: Inter, -apple-system, sans-serif
- **Monospace**: 'Courier New' (valores financeiros)

## Componentes

### Chatbot

#### Mensagens do Usuário
- Alinhamento: Direita
- Background: #E3F2FD (azul claro)
- Borda: Arredondada (12px)
- Padding: 12px 16px

#### Mensagens do Assistente
- Alinhamento: Esquerda
- Background: #F5F5F5 (cinza claro)
- Ícone: Robot emoji 🤖
- Markdown: Suporte completo

### Botões

#### Primário
```css
Background: #CC092F
Color: #FFFFFF
Padding: 12px 24px
Border-radius: 8px
Hover: #A00725
```

#### Secundário
```css
Background: transparent
Border: 2px solid #003A70
Color: #003A70
Hover: Background #E3F2FD
```

### Cards
```css
Background: #FFFFFF
Border: 1px solid #E0E0E0
Border-radius: 12px
Padding: 20px
Shadow: 0 2px 8px rgba(0,0,0,0.08)
```

### Inputs
```css
Border: 1px solid #CED4DA
Border-radius: 8px
Padding: 10px 14px
Focus: Border #003A70, Shadow
Error: Border #DC3545
```

## Fluxos de Interação

### Conversa com Chatbot

1. **Abertura**
   - Mensagem de boas-vindas
   - Sugestões de tópicos
   - Input sempre visível

2. **Durante a Conversa**
   - Indicador de digitação
   - Scroll automático para novas mensagens
   - Timestamps opcionais

3. **Ações Rápidas**
   - Botões de sugestão
   - Atalhos para calculadoras
   - Link para FAQs

### Calculadoras

1. **Entrada de Dados**
   - Labels claros
   - Placeholders com exemplos
   - Validação em tempo real
   - Máscaras para valores (R$)

2. **Resultados**
   - Destaque visual
   - Gráficos quando relevante
   - Opção de salvar/exportar
   - Comparações lado a lado

### Visualizações

#### Gráficos
- **Cores**: Paleta consistente
- **Tooltips**: Informativos
- **Responsividade**: Mobile-friendly
- **Interatividade**: Zoom, filtros

#### Tabelas
- **Cabeçalhos**: Fixos ao scroll
- **Zebra striping**: Linhas alternadas
- **Ordenação**: Clicável
- **Paginação**: 10-20 itens/página

## Estados de Interface

### Loading
- Spinner com mensagem contextual
- Skeleton screens para conteúdo
- Progress bar para processos longos

### Empty States
- Ilustração amigável
- Texto explicativo
- CTA para primeira ação

### Erro
- Mensagem clara do problema
- Sugestão de solução
- Opção de tentar novamente
- Contato para suporte

### Sucesso
- Confirmação visual (✓)
- Mensagem positiva
- Próximos passos sugeridos

## Responsividade

### Breakpoints
```
Mobile: < 768px
Tablet: 768px - 1024px
Desktop: > 1024px
```

### Mobile First
- Design primário para mobile
- Progressive enhancement
- Touch targets mín. 44x44px
- Gestos intuitivos

## Microinterações

### Animações
- **Duração**: 200-300ms
- **Easing**: ease-in-out
- **Uso**: Transições suaves, não distrações

### Feedback Tátil
- Hover states claros
- Active states visíveis
- Focus rings para acessibilidade

## Mensagens e Copywriting

### Tom de Voz
- Profissional mas amigável
- Claro e direto
- Evitar jargões técnicos
- Use "você" (informal)

### Exemplos

✅ **Bom**: "Vamos calcular seu financiamento?"
❌ **Ruim**: "Iniciar processo de cálculo de amortização"

✅ **Bom**: "Algo deu errado. Tente novamente."
❌ **Ruim**: "Erro 500: Internal Server Error"

## Acessibilidade (WCAG 2.1)

### Nível AA Compliance

- [ ] Contraste mínimo 4.5:1
- [ ] Texto redimensionável até 200%
- [ ] Navegação por teclado
- [ ] Alt text em imagens
- [ ] Labels em formulários
- [ ] ARIA labels quando necessário
- [ ] Foco visível
- [ ] Estrutura semântica HTML

### Testes
- Lighthouse Audit
- axe DevTools
- Leitores de tela (NVDA, JAWS)
- Navegação por teclado

## Performance

### Otimizações
- Lazy loading de imagens
- Code splitting
- Minificação de assets
- Cache de dados
- Debounce em inputs

### Métricas Alvo
- First Contentful Paint: < 1.8s
- Time to Interactive: < 3.9s
- Largest Contentful Paint: < 2.5s

## Checklist de Qualidade

Antes de cada release:

- [ ] Teste em diferentes navegadores
- [ ] Teste em dispositivos mobile
- [ ] Validação de acessibilidade
- [ ] Performance audit
- [ ] Spell check
- [ ] Teste de usabilidade
- [ ] Revisão de copywriting
