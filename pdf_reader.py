from PyPDF2 import PdfReader


class PdfReaderCustom:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file

    def read_pdf(self):
        try:
            reader = PdfReader(self.pdf_file)
            character_count = 0
            for page_number, page in enumerate(reader.pages, 1):
                text = page.extract_text()

                if text:
                    characters_on_page = sum(1 for char in text if not char.isspace())
                    character_count += characters_on_page
            return character_count

        except FileNotFoundError:
            print(f"Error: File '{self.pdf_file}' not found!")
            return 0
        except Exception as e:
            print(f"Error while processing PDF: {e}")
            return 0


