# Leitor PDF em Voz Alta

Aplicação simples em Python que lê arquivos PDF em voz alta. Focado em acessibilidade para pessoas com deficiência visual.

## Funcionalidades

- Leitura de arquivos PDF usando síntese de voz.
- Funciona offline.
- Interface simples via terminal.
- Possibilidade de ler todos PDFs em uma pasta.

## Como usar

1. Instale as dependências:

   ```bash
   make install

    Para rodar o programa lendo todos os PDFs da pasta Biblioteca:

make run

Ou execute manualmente:

source venv/bin/activate
python leitor_pdf_voz.py Biblioteca

Para rodar lendo um PDF específico:

    python3 leitor_pdf_voz.py caminho/para/arquivo.pdf

Tecnologias usadas

    Python 3.x

    PyMuPDF

    pyttsx3

Autor: Gabriel da Costa Conceição


---
