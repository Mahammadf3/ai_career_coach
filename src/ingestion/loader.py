import tempfile
from pathlib import Path
import docx2txt
from pypdf import PdfReader

def read_uploaded_file(uploaded_file) -> str:
    """
    Extract text from TXT, PDF, or DOCX files.
    """
    file_name = uploaded_file.name
    suffix= Path(file_name).suffix.lower()

    if suffix == ".txt":
        return uploaded_file.getvalue().decode(
            "utf-8",
            errors="ignore"
        )
    if suffix not in [".pdf", ".docx"]:
        raise ValueError(
            "Unsupported file type. "
            "Use PDF, DOCX, or TXT."
        )
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as tmp:

        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    try:

        if suffix == ".pdf":

            reader = PdfReader(tmp_path)

            return "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        return docx2txt.process(tmp_path)

    finally:

        Path(tmp_path).unlink(
            missing_ok=True
        )