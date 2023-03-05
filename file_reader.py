from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
import docx

def read_pdf(file):
    output_string = StringIO()
    with file:
        extract_text_to_fp(file, output_string, laparams=LAParams())
        text = output_string.getvalue()
    return text

def convert_docx_to_text(doc_file):
    document = docx.Document(doc_file)
    text = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])
    return text