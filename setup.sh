#!/bin/bash

# Criar ambiente virtual
python3 -m venv venv

# Ativar e instalar dependências
source venv/bin/activate
pip install -r requirements.txt

echo "Tudo pronto. Para rodar:"
echo "source venv/bin/activate && python leitor_pdf_voz.py"
