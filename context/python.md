# Regras de revisão para código Python

Estas regras formam uma base geral para revisar código Python. Convenções explícitas do projeto e a versão de Python adotada pelo projeto têm prioridade. Ao apontar uma regra, explique o impacto no código em análise; não transforme preferências de estilo em defeitos sem consequência prática.

## Legibilidade e estilo

- Siga as convenções da [PEP 8](https://peps.python.org/pep-0008/) para nomes, organização e formatação, respeitando o formatador e o estilo já adotados pelo projeto.
- Use nomes descritivos e consistentes. Classes normalmente usam `PascalCase`; funções, métodos e variáveis usam `snake_case`; constantes usam letras maiúsculas com sublinhados quando essa convenção fizer sentido.
- Mantenha funções e métodos focados em uma responsabilidade compreensível. Sugira divisão quando o tamanho ou a complexidade dificultar entender, testar ou alterar o comportamento.
- Use docstrings para documentar propósito, parâmetros, retornos e exceções quando isso não estiver claro pelo código ou pela interface. Siga a convenção de docstrings adotada pelo projeto; na ausência dela, consulte a [PEP 257](https://peps.python.org/pep-0257/).
- Evite comentários que apenas repetem o código. Prefira explicar decisões, restrições ou comportamentos que não sejam óbvios.
- Organize imports de forma clara, remova imports comprovadamente não usados e evite imports com efeitos colaterais inesperados.

## Correção e interfaces

- Verifique os caminhos de sucesso e de falha, inclusive entradas vazias, limites, valores `None` e tipos inesperados quando puderem ocorrer.
- Use `==` para comparar valores e `is` principalmente para comparar com singletons como `None`.
- Não use objetos mutáveis como valores padrão de parâmetros. Use `None` ou outro marcador apropriado e crie o valor dentro da função.
- Preserve os contratos das funções: entradas aceitas, tipo e significado do retorno, efeitos colaterais e exceções esperadas.
- Use anotações de tipo para tornar interfaces e estruturas importantes mais claras, especialmente em APIs públicas ou código que já adota tipagem. Não presuma que anotações validam valores em tempo de execução.
- Evite estados globais mutáveis quando tornam o comportamento dependente da ordem de execução ou dificultam testes e manutenção.
- Ao modificar coleções durante uma iteração, confirme que o comportamento é intencional e correto; quando necessário, itere sobre uma cópia ou construa uma nova coleção.

## Exceções e recursos

- Capture apenas as exceções que o código sabe tratar. Evite `except:` e `except Exception` sem uma razão clara e sem tratamento que preserve a informação necessária.
- Não silencie falhas com `pass` ou retornos que pareçam sucesso. Se a falha for intencionalmente ignorada, o motivo deve estar claro e o comportamento deve ser seguro.
- Use gerenciadores de contexto (`with`) para recursos que precisem de encerramento garantido, como arquivos, locks e conexões compatíveis com esse protocolo.
- Não exponha detalhes internos, caminhos sensíveis, credenciais ou dados pessoais em mensagens de erro e logs.
- Preserve a causa de uma exceção ao traduzi-la para outro tipo quando isso ajudar a depuração, usando encadeamento apropriado.

## Segurança e dados

- Trate entradas externas como não confiáveis. Valide formato, tipo, tamanho e limites de acordo com o uso antes de processá-las.
- Use APIs parametrizadas para consultas e argumentos estruturados para comandos; não monte SQL ou comandos de shell concatenando dados não confiáveis.
- Não use `eval`, `exec`, `pickle` ou mecanismos equivalentes com dados não confiáveis. Prefira formatos e parsers seguros para o caso de uso.
- Evite caminhos de arquivo controlados diretamente por usuários sem validação e restrição ao diretório esperado.
- Não inclua segredos no código-fonte, logs, mensagens de erro ou respostas. Use mecanismos de configuração e segredo adequados ao ambiente do projeto.
- Verifique autenticação e autorização junto à operação protegida; não confie apenas em verificações feitas por um chamador ou interface.
- Em Python, nomes com sublinhado inicial, como `_atributo`, indicam uma convenção de uso interno; não impedem acesso. Avalie se há uma exposição real de dados ou operações através de uma fronteira de confiança antes de apontar um problema de acesso.

## Desempenho, concorrência e dependências

- Priorize clareza. Aponte problemas de desempenho quando houver custo relevante e explicável no contexto, como trabalho repetido, crescimento sem limite ou algoritmo inadequado para o volume esperado.
- Em código assíncrono, verifique se operações bloqueantes impedem o event loop e se tarefas e exceções são tratadas corretamente.
- Em código concorrente, examine o acesso compartilhado a estado mutável e a ordem das operações quando isso puder causar condições de corrida.
- Evite dependências ou abstrações desnecessárias. Não declare uma dependência vulnerável sem evidência suficiente, como versão aplicável e vulnerabilidade pertinente.
- Não recomende sintaxe ou recursos sem considerar a versão mínima de Python informada pelo projeto. Se ela não estiver disponível, sinalize a dependência de versão em vez de presumir compatibilidade.

## Como registrar achados

- Priorize problemas de correção, segurança, confiabilidade e manutenção com impacto concreto.
- Para cada achado, indique localização, evidência, consequência e uma sugestão específica de melhoria. Informe severidade de acordo com o impacto e a possibilidade de ocorrência.
- Separe fatos confirmados de riscos que dependem de contexto ausente. Não invente comportamento, requisitos, versão do Python ou convenções do projeto.
- Não reporte apenas uma preferência de formatação ou nomenclatura. Aponte-a somente quando contrariar uma regra explícita do projeto ou causar confusão ou defeito observável.
- Se não houver problemas relevantes, diga isso e resuma brevemente o escopo revisado.
