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

## Decisões pendentes antes da implementação

- Forma de uso: linha de comando, interface web ou API.
- Método de análise: modelo de IA, ferramentas estáticas ou combinação dos dois.
- Formatos de entrada e saída do relatório, como Markdown ou JSON.
- Versões de Python e tamanho máximo de arquivo suportados.
- Uso de serviços externos e política para envio, retenção e proteção dos arquivos.
- Dependências, configuração e forma de instalação do projeto.
