# Guia de UX/UI - Assistente Financeiro

## Princípios de Design

### 1. Simplicidade
- Interface limpa e intuitiva
- Foco na tarefa principal
- Mínimo de distrações visuais

### 2. Acessibilidade
- Contraste adequado (WCAG 2.1 AA)
- Suporte a leitores de tela
- Navegação por teclado
- Textos claros e objetivos

### 3. Consistência
- Padrões visuais uniformes
- Terminologia consistente
- Comportamentos previsíveis

### 4. Feedback
- Respostas imediatas às ações
- Indicadores de carregamento
- Confirmações de sucesso/erro
- Mensagens claras

## Paleta de Cores

### Cores Principais
```
Primária:   #C8102E (Vermelho Bradesco)
Secundária: #003366 (Azul Escuro)
Acento:     #FFD700 (Dourado)
```

### Cores de Status
```
Sucesso:    #28A745
Aviso:      #FFC107
Erro:       #DC3545
Info:       #17A2B8
```

### Neutros
```
Texto:      #212529
Texto Sec:  #6C757D
Fundo:      #F8F9FA
Bordas:     #DEE2E6
```

## Tipografia

### Fontes
- **Primária**: Inter, -apple-system, sans-serif
- **Código**: 'Fira Code', monospace

### Hierarquia
```
H1: 2.5rem / 40px - Bold
H2: 2rem / 32px - Semibold
H3: 1.5rem / 24px - Semibold
Body: 1rem / 16px - Regular
Small: 0.875rem / 14px - Regular
```

## Componentes UI

### 1. Chat Interface

#### Mensagens do Usuário
- Alinhamento: Direita
- Cor de fundo: #E3F2FD
- Bordas arredondadas: 12px
- Padding: 12px 16px

#### Mensagens do Assistente
- Alinhamento: Esquerda
- Cor de fundo: #FFFFFF
- Borda: 1px solid #DEE2E6
- Bordas arredondadas: 12px
- Padding: 12px 16px
- Ícone: 🤖

### 2. Botões

#### Primário
```css
Background: #C8102E
Color: #FFFFFF
Padding: 10px 20px
Border-radius: 6px
Font-weight: 600

Hover: #A00D25
Active: #8A0B20
```

#### Secundário
```css
Background: Transparent
Color: #C8102E
Border: 2px solid #C8102E
Padding: 10px 20px
Border-radius: 6px

Hover: Background #FFF5F5
```

### 3. Inputs

#### Campo de Texto
```css
Border: 1px solid #DEE2E6
Border-radius: 6px
Padding: 10px 12px
Font-size: 1rem

Focus: Border-color #C8102E, Box-shadow 0 0 0 3px rgba(200, 16, 46, 0.1)
```

### 4. Cards

#### Calculadora/FAQ
```css
Background: #FFFFFF
Border: 1px solid #DEE2E6
Border-radius: 8px
Padding: 20px
Box-shadow: 0 2px 4px rgba(0,0,0,0.05)

Hover: Box-shadow 0 4px 8px rgba(0,0,0,0.1)
```

## Layout

### Estrutura da Página

```
┌────────────────────────────────────────┐
│            Header/Logo                 │
├────────────────────────────────────────┤
│  Sidebar  │      Main Content          │
│           │                            │
│  Menu     │   Chat Area                │
│  Items    │                            │
│           │   ┌──────────────────┐     │
│           │   │   Message        │     │
│           │   │   Message        │     │
│           │   │   Message        │     │
│           │   └──────────────────┘     │
│           │                            │
│           │   [Input Field]  [Send]    │
└───────────┴────────────────────────────┘
```

### Responsividade

#### Desktop (>1024px)
- Sidebar: 280px
- Main: Flex
- Layout: 2 colunas

#### Tablet (768px - 1024px)
- Sidebar: 240px
- Main: Flex
- Layout: 2 colunas colapsáveis

#### Mobile (<768px)
- Sidebar: Menu hamburger
- Main: 100%
- Layout: 1 coluna

## Microinterações

### 1. Botão de Envio
```
Idle → Hover (escala 1.05) → Click (pulso) → Loading (spinner)
```

### 2. Mensagens
```
Aparecem com fade-in + slide-up (300ms)
```

### 3. Calculadoras
```
Resultados aparecem com fade-in (200ms)
```

### 4. Tooltips
```
Hover delay: 500ms
Fade-in: 200ms
```

## Estados de Loading

### Chat
- Mensagem temporária: "Assistente está pensando..."
- Animação: 3 pontos pulsantes
- Cor: #6C757D

### Calculadoras
- Skeleton screen para resultados
- Spinner centralizado

### Dados
- Progress bar para carregamentos longos
- Mensagem descritiva

## Mensagens de Erro

### Estrutura
```
┌─────────────────────────────────────┐
│  ⚠️  Título do Erro                 │
│                                     │
│  Descrição clara do problema        │
│                                     │
│  [Ação Sugerida]                    │
└─────────────────────────────────────┘
```

### Exemplos
- **Erro de Conexão**: "Não foi possível conectar. Verifique sua internet."
- **Erro de API**: "Serviço temporariamente indisponível. Tente novamente em instantes."
- **Validação**: "Por favor, preencha todos os campos obrigatórios."

## Acessibilidade (WCAG 2.1)

### Checklist
- [ ] Contraste mínimo 4.5:1 para texto
- [ ] Todos os elementos interativos acessíveis por teclado
- [ ] Labels descritivos para inputs
- [ ] Alt text para imagens
- [ ] Aria-labels para ícones
- [ ] Foco visível em elementos interativos
- [ ] Suporte a zoom até 200%
- [ ] Sem dependência apenas de cor

## Tom de Voz

### Características
- **Amigável**: Como um consultor pessoal
- **Profissional**: Confiável e competente
- **Claro**: Sem jargões desnecessários
- **Prestativo**: Sempre disposto a ajudar

### Exemplos

❌ **Evitar**: "Erro 500: Internal Server Error"
✅ **Preferir**: "Ops! Algo deu errado. Nossa equipe já foi notificada."

❌ **Evitar**: "Input inválido"
✅ **Preferir**: "Por favor, insira um valor entre R$ 1.000 e R$ 1.000.000"

## Animações

### Timing
- Rápida: 150-200ms (hover, tooltips)
- Média: 300-400ms (transições, modals)
- Lenta: 500-600ms (page transitions)

### Easing
- **Entrada**: ease-out
- **Saída**: ease-in
- **Bidirecionais**: ease-in-out

## Performance UX

### Tempos Alvo
- Resposta de chat: < 2s
- Cálculo financeiro: < 500ms
- Carregamento de página: < 1s
- Busca em FAQs: < 300ms

### Estratégias
- Skeleton screens
- Optimistic UI updates
- Lazy loading de componentes
- Debounce em buscas (300ms)

## Testes de Usabilidade

### Métricas
1. **Task Success Rate**: > 90%
2. **Time on Task**: < 2 min (para tarefas comuns)
3. **Error Rate**: < 5%
4. **Satisfaction (SUS)**: > 80

### Cenários de Teste
1. Simular um financiamento
2. Buscar informação sobre produto
3. Fazer uma pergunta complexa
4. Navegar entre funcionalidades
5. Usar em dispositivo móvel
