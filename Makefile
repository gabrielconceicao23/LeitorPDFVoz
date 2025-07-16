.PHONY: install run clean help

install:
	if [ ! -d "venv" ]; then python3 -m venv venv; fi
	source venv/bin/activate && pip install -r requirements.txt

run:
	source venv/bin/activate && python leitor_pdf_voz.py Biblioteca

clean:
	rm -rf venv

help:
	@echo "Comandos disponíveis:"
	@echo "  make install  - cria venv e instala dependências"
	@echo "  make run      - executa o programa (lê PDFs na pasta Biblioteca)"
	@echo "  make clean    - remove o ambiente virtual"
