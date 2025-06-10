# Lauds Counter

**Lauds Counter** é um script desenvolvido em Python que monitora continuamente um diretório específico e, sempre que um novo arquivo `.pdf` é adicionado, realiza as seguintes ações automaticamente:

- Lê o conteúdo do arquivo PDF.
- Conta a quantidade total de caracteres presentes no texto.
- Renomeia o arquivo adicionando essa contagem ao nome do arquivo.

O script utiliza as bibliotecas [PyPDF2](https://pypi.org/project/PyPDF2/) para a leitura dos arquivos PDF e [Watchdog](https://pypi.org/project/watchdog/) para monitoramento em tempo real do diretório.

## Requisitos

- Python 3.7 ou superior
- PyPDF2
- Watchdog

## Instalação

```bash
pip install PyPDF2 watchdog
