# Política de Segurança

## Versões Suportadas

Atualmente, oferecemos suporte de segurança para as seguintes versões:

| Versão | Suportada          |
| ------ | ------------------ |
| 1.0.x  | :white_check_mark: |

## Relatando uma Vulnerabilidade

A segurança é levada a sério neste projeto. Se você descobrir uma vulnerabilidade de segurança, por favor, siga as diretrizes abaixo:

### Como Reportar

**NÃO** crie uma issue pública no GitHub para vulnerabilidades de segurança.

Em vez disso:

1. **Envie um e-mail** para marcus@vasconcellos.net.br com:
   - Descrição detalhada da vulnerabilidade
   - Passos para reproduzir o problema
   - Possível impacto
   - Sugestões de correção (se houver)

2. **Use o título**: "[SEGURANÇA] Descrição breve da vulnerabilidade"

3. **Aguarde resposta**: Você receberá uma confirmação em até 48 horas

### O que Esperar

Após reportar uma vulnerabilidade:

- **Confirmação**: Confirmaremos o recebimento em 48 horas
- **Avaliação**: Avaliaremos a vulnerabilidade e sua gravidade
- **Atualização**: Forneceremos atualizações regulares sobre o progresso
- **Correção**: Trabalharemos em uma correção e a lançaremos o mais rápido possível
- **Divulgação**: Coordenaremos a divulgação pública após a correção

### Política de Divulgação

- Manteremos você informado sobre o progresso da correção
- Daremos crédito apropriado pela descoberta (se desejar)
- Divulgaremos a vulnerabilidade apenas após a correção estar disponível
- Pedimos que você não divulgue a vulnerabilidade publicamente antes da correção

## Boas Práticas de Segurança

### Para Usuários

1. **Chaves de API**
   - Nunca compartilhe suas chaves de API
   - Use variáveis de ambiente (arquivo `.env`)
   - Nunca faça commit do arquivo `.env`
   - Rotacione chaves regularmente

2. **Dados Sensíveis**
   - Não armazene informações financeiras reais
   - Use dados fictícios para testes
   - Implemente criptografia para dados sensíveis

3. **Atualizações**
   - Mantenha as dependências atualizadas
   - Execute `pip install -r requirements.txt --upgrade` regularmente
   - Monitore avisos de segurança

### Para Desenvolvedores

1. **Validação de Entrada**
   - Sempre valide dados de entrada do usuário
   - Use sanitização apropriada
   - Implemente rate limiting quando aplicável

2. **Autenticação**
   - Use HTTPS em produção
   - Implemente autenticação robusta
   - Não armazene credenciais em código

3. **Dependências**
   - Audite dependências regularmente: `pip audit`
   - Mantenha requirements.txt atualizado
   - Remova dependências não utilizadas

4. **Logging**
   - Não registre dados sensíveis em logs
   - Implemente logging apropriado para auditoria
   - Proteja arquivos de log

## Vulnerabilidades Conhecidas

Atualmente, não há vulnerabilidades conhecidas não corrigidas.

## Agradecimentos

Agradecemos aos seguintes pesquisadores de segurança por suas contribuições:

- (Lista será atualizada conforme contribuições forem recebidas)

## Recursos Adicionais

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [OpenAI Security Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)

---

**Última atualização**: Dezembro 2025