from watchdog.events import FileSystemEventHandler
from pdf_reader import PdfReaderCustom
import os
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith('.pdf'):
            old_path = event.src_path
            directory = os.path.dirname(old_path)
            old_filename = os.path.basename(old_path)
            print(f"PDF file created: {old_filename}")

            if os.path.exists(old_path):
                try:
                    pdf_reader = PdfReaderCustom(old_path)
                    character_count = pdf_reader.read_pdf()
                    name, ext = os.path.splitext(old_filename)
                    new_filename = f"{name}_{character_count}{ext}"
                    new_path = os.path.join(directory, new_filename)

                    time.sleep(0.5)

                    os.rename(old_path, new_path)

                    print(f" Renamed: {old_filename} -> {new_filename}")

                    if character_count > 0:
                        print(f" Total characters (excluding spaces): {character_count}")
                    else:
                        print("Failed to process the file.")

                except Exception as e:
                        print(f" Error: {e}")


