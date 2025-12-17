# Guia de Contribuição

## Como Contribuir

Obrigado por considerar contribuir para o Assistente Financeiro Inteligente! Este documento fornece diretrizes para contribuições.

## Processo de Contribuição

1. **Fork o Repositório**
   - Crie um fork do projeto para sua conta GitHub

2. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/dio-bootcamp-bradesco-genai-assistente-financeiro.git
   cd dio-bootcamp-bradesco-genai-assistente-financeiro
   ```

3. **Crie uma Branch**
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
   
   Use prefixos descritivos:
   - `feature/` - Nova funcionalidade
   - `fix/` - Correção de bug
   - `docs/` - Documentação
   - `refactor/` - Refatoração de código
   - `test/` - Adição ou modificação de testes

4. **Instale as Dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o Ambiente**
   - Copie `.env.example` para `.env`
   - Configure suas chaves de API

6. **Faça suas Alterações**
   - Escreva código limpo e bem documentado
   - Siga as convenções de código Python (PEP 8)
   - Adicione docstrings para funções e classes

7. **Escreva Testes**
   - Adicione testes para novas funcionalidades
   - Garanta que todos os testes passem:
   ```bash
   pytest tests/
   ```

8. **Commit suas Alterações**
   ```bash
   git add .
   git commit -m "tipo: descrição clara das alterações"
   ```
   
   Exemplos de mensagens de commit:
   - `feat: adicionar calculadora de investimentos`
   - `fix: corrigir bug no cálculo de juros compostos`
   - `docs: atualizar documentação da API`

9. **Push para o GitHub**
   ```bash
   git push origin feature/nova-funcionalidade
   ```

10. **Abra um Pull Request**
    - Vá para o repositório original no GitHub
    - Clique em "New Pull Request"
    - Descreva suas alterações detalhadamente
    - Referencie issues relacionadas

## Padrões de Código

### Python
- Siga o PEP 8
- Use type hints quando possível
- Máximo de 88 caracteres por linha (Black formatter)
- Use nomes descritivos para variáveis e funções

### Documentação
- Use docstrings no formato Google ou NumPy
- Documente todos os parâmetros e retornos
- Inclua exemplos quando apropriado

### Testes
- Mantenha cobertura de testes acima de 80%
- Use nomes descritivos para funções de teste
- Teste casos de sucesso e falha
- Use fixtures do pytest quando apropriado

## Diretrizes de UX

- Mensagens devem ser claras e em português
- Feedback ao usuário deve ser imediato
- Erros devem ser informativos e sugerir soluções
- Interface deve ser intuitiva e acessível

## Segurança

- Nunca faça commit de chaves de API ou senhas
- Use variáveis de ambiente para informações sensíveis
- Valide todas as entradas do usuário
- Reporte vulnerabilidades de forma privada

## Dúvidas?

Se tiver dúvidas, abra uma issue com a tag "question" ou entre em contato com os mantenedores do projeto.

## Código de Conduta

Este projeto segue o [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar, você concorda em seguir suas diretrizes.