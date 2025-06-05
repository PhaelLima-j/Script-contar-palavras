from PyPDF2 import PdfReader
import sys
import os

class PdfReaderCustom:

    def __init__(self, pdf):
        self.pdf = pdf

    def leitura_pdf(self):
        reader = PdfReader(self.pdf)
        page = reader.pages[0]

        text = page.extract_text()
        total_letras = []

        if text:
            for letra in text:
                if not letra.isspace():
                    total_letras.append(letra)

        return len(total_letras)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: arraste um arquivo PDF ou passe o caminho como argumento.")
        input("Pressione Enter para sair...")
        sys.exit(1)

    caminho_pdf = sys.argv[1]

    if not os.path.exists(caminho_pdf):
        print(f"Arquivo não encontrado: {caminho_pdf}")
        input("Pressione Enter para sair...")
        sys.exit(1)

    leitor = PdfReaderCustom(caminho_pdf)
    total = leitor.leitura_pdf()

    print(f"O PDF contém {total} letras (desconsiderando espaços).")
    input("Pressione Enter para sair...")
