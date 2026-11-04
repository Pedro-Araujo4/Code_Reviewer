"""Interface web local em Gradio para o agente revisor."""

from __future__ import annotations

import sys
from pathlib import Path

# Garante que o diretório src/ esteja no sys.path para importar main
# independentemente de onde o script é invocado.
_SRC_DIR = Path(__file__).resolve().parent
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

import gradio as gr  # noqa: E402

from main import PROJECT_ROOT, REPORTS_DIR, ReviewError, review_file  # noqa: E402


def review_upload(uploaded_file: str | None, progress: gr.Progress = gr.Progress()) -> tuple[str, str | None]:
    """Envia o arquivo carregado ao fluxo de revisão compartilhado."""
    if not uploaded_file:
        return "Selecione um arquivo `.py` para iniciar a revisão.", None

    file_path = Path(uploaded_file)
    file_name = file_path.name

    progress(0.1, desc=f"Lendo {file_name}…")

    try:
        progress(0.3, desc="Enviando para análise com Gemini…")
        result = review_file(file_path)
    except ReviewError as exc:
        return f"### ❌ Revisão não concluída\n\n{exc}", None
    except Exception:
        return (
            "### ❌ Revisão não concluída\n\nOcorreu um erro inesperado. "
            "Verifique a configuração (.env, chave de API, modelo) e tente novamente.",
            None,
        )

    progress(0.9, desc="Gerando relatório…")

    status_parts = [f"\n\n---\n\n✅ Relatório salvo em `{result.report_path.name}`."]
    if result.rejected_count:
        status_parts.append(
            f"⚠️ {result.rejected_count} achado(s) descartados por falha de validação."
        )

    progress(1.0, desc="Concluído!")
    return result.markdown + " ".join(status_parts), str(result.report_path)


# ---------------------------------------------------------------------------
# Interface Gradio
# ---------------------------------------------------------------------------

_CUSTOM_CSS = """
.main-header { text-align: center; margin-bottom: 0.5em; }
.privacy-note { font-size: 0.9em; color: #666; }
"""

with gr.Blocks(title="Code Reviewer") as demo:

    gr.Markdown(
        "# 🔍 Code Reviewer\n"
        "Envie um arquivo Python para receber uma revisão baseada nas regras do projeto.",
        elem_classes="main-header",
    )

    gr.Markdown(
        "**Privacidade:** o conteúdo do arquivo é enviado à API Gemini para análise. "
        "O código **não** é executado. Envie apenas arquivos que você pode compartilhar "
        "com esse serviço.",
        elem_classes="privacy-note",
    )

    with gr.Row():
        with gr.Column(scale=1):
            uploaded_file = gr.File(
                label="Arquivo Python (.py)",
                file_types=[".py"],
                file_count="single",
                type="filepath",
            )
            review_button = gr.Button(
                "🚀 Revisar arquivo",
                variant="primary",
                size="lg",
            )

    report_output = gr.Markdown(
        label="Relatório",
        value="*Nenhuma revisão realizada ainda. Envie um arquivo para começar.*",
    )

    download_output = gr.File(
        label="📥 Baixar relatório Markdown",
        file_count="single",
        interactive=False,
    )

    review_button.click(
        fn=review_upload,
        inputs=uploaded_file,
        outputs=[report_output, download_output],
        concurrency_limit=1,
    )


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=False,
        allowed_paths=[str(REPORTS_DIR)],
        theme=gr.themes.Soft(),
        css=_CUSTOM_CSS,
    )
