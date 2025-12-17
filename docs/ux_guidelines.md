# Guia de UX/UI - Assistente Financeiro Inteligente

## Princípios de Design

### 1. Clareza e Simplicidade
- **Linguagem clara**: Evitar jargões financeiros complexos sem explicação
- **Interface limpa**: Minimizar elementos visuais desnecessários
- **Hierarquia visual**: Destacar informações mais importantes

### 2. Confiança e Segurança
- **Transparência**: Explicar como os dados são usados
- **Indicadores de segurança**: Mostrar status de conexão segura
- **Avisos claros**: Alertas sobre operações críticas

### 3. Acessibilidade
- **Contraste adequado**: WCAG 2.1 AA ou superior
- **Tamanho de fonte**: Mínimo 14px para texto corrido
- **Navegação por teclado**: Suporte completo

### 4. Responsividade
- **Mobile-first**: Design otimizado para dispositivos móveis
- **Breakpoints**: 320px, 768px, 1024px, 1440px
- **Touch targets**: Mínimo 44x44px

## Paleta de Cores

### Cores Primárias
```css
--primary: #CC092F;        /* Vermelho Bradesco */
--primary-dark: #A00725;
--primary-light: #E63950;
```

### Cores Secundárias
```css
--secondary: #0066CC;      /* Azul confiança */
--success: #28A745;        /* Verde sucesso */
--warning: #FFC107;        /* Amarelo alerta */
--danger: #DC3545;         /* Vermelho erro */
--info: #17A2B8;          /* Azul informação */
```

### Cores Neutras
```css
--gray-50: #F8F9FA;
--gray-100: #E9ECEF;
--gray-200: #DEE2E6;
--gray-300: #CED4DA;
--gray-400: #ADB5BD;
--gray-500: #6C757D;
--gray-600: #495057;
--gray-700: #343A40;
--gray-800: #212529;
--gray-900: #0D0E10;
```

## Tipografia

### Fontes
```css
--font-primary: 'Inter', 'Segoe UI', sans-serif;
--font-monospace: 'Roboto Mono', 'Courier New', monospace;
```

### Escala Tipográfica
```css
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
```

## Componentes

### Chat Interface

#### Mensagem do Usuário
```
┌─────────────────────────────────────┐
│ Qual é a melhor opção de            │
│ investimento para meu perfil?   👤  │
└─────────────────────────────────────┘
```
- Alinhamento: Direita
- Background: `--gray-100`
- Borda: Arredondada (12px)
- Padding: 12px 16px

#### Mensagem do Assistente
```
┌─────────────────────────────────────┐
│ 🤖  Baseado no seu perfil           │
│     moderado, sugiro...             │
└─────────────────────────────────────┘
```
- Alinhamento: Esquerda
- Background: Branco
- Borda: Arredondada (12px) + sombra leve
- Padding: 12px 16px

### Botões

#### Primário
```css
background: var(--primary);
color: white;
border-radius: 8px;
padding: 12px 24px;
font-weight: 600;
transition: all 0.2s ease;

&:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(204, 9, 47, 0.3);
}
```

#### Secundário
```css
background: transparent;
color: var(--primary);
border: 2px solid var(--primary);
border-radius: 8px;
padding: 12px 24px;

&:hover {
  background: var(--primary);
  color: white;
}
```

### Cards

#### Card de Produto Financeiro
```
┌────────────────────────────────────┐
│ 💰 CDB Bradesco                    │
│                                    │
│ Rentabilidade: 110% CDI            │
│ Liquidez: D+0                      │
│ Investimento mínimo: R$ 500        │
│                                    │
│ [Saiba mais] [Simular]             │
└────────────────────────────────────┘
```
- Background: Branco
- Borda: 1px `--gray-200`
- Border-radius: 12px
- Box-shadow: `0 2px 8px rgba(0,0,0,0.05)`
- Padding: 20px

### Formulários

#### Input Field
```css
border: 1px solid var(--gray-300);
border-radius: 8px;
padding: 12px 16px;
font-size: var(--text-base);

&:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(204, 9, 47, 0.1);
  outline: none;
}

&:error {
  border-color: var(--danger);
}
```

#### Labels
```css
font-weight: 600;
margin-bottom: 8px;
color: var(--gray-700);
```

## Ícones

### Sistema de Ícones
- **Biblioteca**: Material Icons / Font Awesome
- **Tamanho padrão**: 24px
- **Cor**: Herdar do contexto ou `--gray-600`

### Ícones por Contexto
```
💬 Chat / Conversação
📊 Análise / Gráficos
💰 Dinheiro / Valores
📈 Investimentos / Crescimento
🔒 Segurança / Privacidade
⚙️ Configurações
❓ Ajuda / FAQ
✅ Sucesso / Confirmação
⚠️ Alerta / Atenção
❌ Erro / Cancelar
```

## Layouts

### Layout Principal (Desktop)
```
┌─────────────────────────────────────────────┐
│ 🏦 Bradesco Assistente IA    👤 ⚙️        │
├──────────┬──────────────────────────────────┤
│          │                                  │
│ Sidebar  │      Área Principal             │
│          │                                  │
│ - Chat   │  ┌────────────────────────┐     │
│ - FAQs   │  │                        │     │
│ - Calc   │  │   Conteúdo Dinâmico    │     │
│ - Dados  │  │                        │     │
│          │  └────────────────────────┘     │
│          │                                  │
│          │  [Input de Chat]                │
└──────────┴──────────────────────────────────┘
```

### Layout Mobile
```
┌─────────────────────┐
│ ☰  Bradesco IA  👤 │
├─────────────────────┤
│                     │
│   Área Principal    │
│                     │
│  ┌───────────────┐  │
│  │  Conteúdo     │  │
│  └───────────────┘  │
│                     │
│  [Input de Chat]    │
│                     │
│ [──────────────]    │ <- Bottom Nav
└─────────────────────┘
```

## Interações

### Estados de Loading
```
⏳ Processando sua solicitação...
🔄 Analisando dados...
💭 Pensando na melhor resposta...
```

### Feedback Visual
- **Sucesso**: Toast verde com ícone ✅ (3s)
- **Erro**: Toast vermelho com ícone ❌ (5s)
- **Alerta**: Toast amarelo com ícone ⚠️ (4s)
- **Info**: Toast azul com ícone ℹ️ (3s)

### Animações
```css
/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Slide up */
@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

/* Duração recomendada: 200-300ms */
/* Easing: ease-out ou cubic-bezier(0.4, 0, 0.2, 1) */
```

## Microinterações

### Hover em Cards
```css
transition: transform 0.2s, box-shadow 0.2s;

&:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}
```

### Click Feedback
```css
&:active {
  transform: scale(0.98);
}
```

## Mensagens de Erro

### Formato
```
❌ Ops! Algo deu errado

Não foi possível processar sua solicitação.

O que você pode fazer:
• Verificar sua conexão com a internet
• Tentar novamente em alguns instantes
• Entrar em contato com o suporte

[Tentar Novamente] [Falar com Suporte]
```

### Tom de Voz
- **Empático**: "Entendemos sua frustração..."
- **Claro**: Explicar o que aconteceu
- **Acionável**: Oferecer próximos passos
- **Positivo**: Manter tom otimista

## Acessibilidade (A11Y)

### Checklist
- [ ] Contraste mínimo 4.5:1 para texto normal
- [ ] Contraste mínimo 3:1 para texto grande
- [ ] Todos os elementos interativos acessíveis via teclado
- [ ] Focus indicators visíveis
- [ ] Alt text para todas as imagens
- [ ] ARIA labels para elementos dinâmicos
- [ ] Suporte a leitores de tela
- [ ] Opção de aumentar fonte
- [ ] Modo de alto contraste

### Navegação por Teclado
```
Tab       → Próximo elemento
Shift+Tab → Elemento anterior
Enter     → Ativar/Selecionar
Esc       → Fechar modal/dropdown
Arrows    → Navegar em listas
```

## Performance UX

### Tempos de Resposta
- **Instantâneo**: < 100ms (feedback visual)
- **Imediato**: < 1s (operações simples)
- **Aceitável**: < 3s (cálculos complexos)
- **Crítico**: > 10s (mostrar progresso detalhado)

### Otimizações
- Lazy loading de imagens
- Paginação de listas longas
- Debounce em buscas (300ms)
- Cache de resultados frequentes
- Skeleton screens durante loading

## Boas Práticas

### Do's ✅
- Usar linguagem positiva e encorajadora
- Fornecer feedback imediato
- Manter consistência visual
- Oferecer ajuda contextual
- Permitir desfazer ações importantes

### Don'ts ❌
- Usar jargão sem explicação
- Bloquear a UI sem feedback
- Forçar ações sem confirmação
- Esconder informações críticas
- Ignorar estados de erro

## Testes de Usabilidade

### Métricas
- **Task Success Rate**: % de tarefas completadas
- **Time on Task**: Tempo médio para completar
- **Error Rate**: Frequência de erros
- **Satisfaction**: NPS/CSAT scores

### Ferramentas
- Hotjar (heatmaps)
- Google Analytics (eventos)
- UserTesting (testes remotos)
- A/B Testing (Optimizely)

## Referências

- [Material Design Guidelines](https://material.io/design)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/)
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [Nielsen Norman Group](https://www.nngroup.com/)
