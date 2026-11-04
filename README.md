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
- Localização: arquivo e linha, quando a evidência puder ser vinculada ao código. Se a linha exata não for confirmada, o achado é exibido mesmo assim, como geral.
- Evidência e impacto, em poucas palavras.
- Sugestão de correção.

Em seguida, o relatório inclui uma seção **Possíveis melhorias**, com sugestões opcionais como refatoração, legibilidade, manutenção, desempenho ou testes. Essas melhorias não são tratadas como defeitos.

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

## Como usar

### Instalação

O projeto requer **Python 3.10** ou superior.

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com a chave da API Gemini:

```
GEMINI_API_KEY=sua_chave_aqui
```

### Interface web (Gradio)

```bash
python src/ui.py
```

Acesse `http://127.0.0.1:7860` no navegador. Na interface, faça upload de um arquivo `.py`, clique em **Revisar arquivo** e acompanhe a análise. Ao final, o relatório é exibido na página e pode ser baixado em Markdown.

### Linha de comando (CLI)

```bash
# Revisão do único .py em input/
python src/main.py

# Revisão de um arquivo específico
python src/main.py caminho/para/arquivo.py

# Especificar o destino do relatório
python src/main.py arquivo.py --output relatorio.md
```

## Configuração

| Variável | Descrição | Padrão |
|---|---|---|
| `GEMINI_API_KEY` ou `API_KEY` | Chave da API Gemini (obrigatória) | — |
| `GEMINI_MODEL` | Modelo a usar na análise | `gemini-3.5-flash-lite` |
| `MAX_FILE_SIZE_MB` | Tamanho máximo do arquivo em MB | `1` |
| `GEMINI_MAX_ATTEMPTS` | Tentativas da API, incluindo a primeira | `4` |
| `GEMINI_RETRY_INITIAL_DELAY_S` | Espera inicial em segundos após uma falha temporária | `1` |
| `GEMINI_RETRY_MAX_DELAY_S` | Espera máxima entre tentativas, em segundos | `30` |

- O código submetido é enviado à API Gemini e **não** é executado. Não envie arquivos que não possam ser compartilhados com esse serviço.
- A chave é lida do `.env`. Não compartilhe nem versione esse arquivo.
- Falhas temporárias da API (por exemplo 408, 429, 500, 502, 503 e 504) são repetidas até `GEMINI_MAX_ATTEMPTS`, com espera que dobra a cada tentativa até `GEMINI_RETRY_MAX_DELAY_S`. Erros permanentes, como chave inválida, não são repetidos.
- O relatório é salvo em Markdown na pasta `reports/`, com achados (severidade, linha, evidência, impacto e correção) e uma seção de possíveis melhorias, como refatoração.

## Próximas melhorias

- Criar testes automatizados para leitura das regras, validação de linhas e evidências e geração do relatório. Usar respostas simuladas nos testes; deixar chamadas reais à API para verificações manuais opcionais.
- Avaliar revisão em lote de vários arquivos.
- Avaliar suporte a relatório JSON além do Markdown.
- Considerar ferramentas estáticas como complemento à análise da IA.
