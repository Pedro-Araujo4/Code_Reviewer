# Code Reviewer

Agente para revisar arquivos Python, apontar problemas comprováveis e sugerir melhorias. Destina-se a pessoas desenvolvedoras e equipes que queiram uma revisão inicial consistente com as regras do projeto.

## Fluxo de revisão

1. O usuário fornece um arquivo Python.
2. O agente consulta as regras e orientações pertinentes do projeto.
3. Analisa o código e identifica problemas com evidências.
4. Gera um relatório breve com sugestões.

## Relatório

O relatório deve ser simples e direto. Para cada achado, informa:

- Severidade: crítica, alta, média ou baixa.
- Localização: arquivo e linha, quando disponíveis.
- Evidência e impacto, em poucas palavras.
- Sugestão de melhoria.

Se não houver achados relevantes, o agente informa isso e resume brevemente o escopo revisado.

## Limites

- O agente não executa o arquivo Python submetido.
- A revisão não substitui testes, auditoria especializada nem validação por uma pessoa desenvolvedora.
- O agente não altera o código analisado, salvo solicitação explícita do usuário.

## Regras e instruções do agente

O agente consulta as referências aplicáveis durante a análise. As regras detalhadas permanecem nos arquivos próprios e não são repetidas aqui:

- [Instruções do agente revisor](agents/reviewer.md)
- [Regras de revisão Python](context/python.md)
- [Diretrizes de segurança](context/security.md)
- [Diretrizes de arquitetura e IA](context/architecture.md)
- [Skill de análise geral](skills/analyze-code/SKILL.md)
- [Skill de análise de segurança](skills/detect-security-issues/SKILL.md)

## Configuração atual

- Interface de linha de comando; uma revisão analisa um arquivo `.py` por vez. Se nenhum caminho for informado, o programa usa o único arquivo Python em `input/`.
- A análise usa a API Gemini, com `gemini-3.8-flash` como modelo padrão. O modelo pode ser configurado pela variável `GEMINI_MODEL`.
- O código submetido é enviado à API Gemini e não é executado. Não envie arquivos que não possam ser compartilhados com esse serviço.
- A chave é lida de `GEMINI_API_KEY` ou `API_KEY` no `.env`. Não compartilhe nem versione esse arquivo.
- O tamanho máximo padrão é 1 MB e pode ser alterado por `MAX_FILE_SIZE_MB`.
- O relatório é salvo em Markdown na pasta `reports/`, com severidade, linha, evidência, impacto e sugestão.
- O projeto requer Python 3.10 ou superior. As dependências estão em [requirements.txt](requirements.txt).

## Próximas melhorias

- Definir tentativas limitadas e espera progressiva para falhas temporárias da API, como respostas 503.
- Criar testes automatizados para leitura das regras, validação de linhas e evidências e geração do relatório. Usar respostas simuladas nos testes; deixar chamadas reais à API para verificações manuais opcionais.
- Avaliar revisão em lote de vários arquivos.
- Avaliar suporte a relatório JSON além do Markdown.
- Considerar ferramentas estáticas como complemento à análise da IA.
