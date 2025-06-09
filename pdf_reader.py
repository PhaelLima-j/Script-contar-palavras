from PyPDF2 import PdfReader

class PdfReaderCustom:
    def __init__(self, pdf):
        self.pdf = pdf

    def leitura_pdf(self):
        try:
            reader = PdfReader(self.pdf)
            total_caracteres_geral = 0
            for numero_pagina, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                
                if text:
                    caracteres_pagina = sum(1 for letra in text if not letra.isspace())
                    total_caracteres_geral += caracteres_pagina
                               
            return total_caracteres_geral
        
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.pdf}' não encontrado!")
            return 0
        except Exception as e:
            print(f"Erro ao processar PDF: {e}")
            return 0