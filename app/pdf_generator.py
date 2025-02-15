import pdfkit

def gerar_pdf(html_content, output_path="plano_aula.pdf"):
    pdfkit.from_string(html_content, output_path)
    return output_path
