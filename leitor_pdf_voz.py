import pyttsx3
import fitz  # PyMuPDF
import sys
import os

def ler_pdf_em_voz_alta(caminho_pdf):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    try:
        documento = fitz.open(caminho_pdf)
        for pagina in documento:
            texto = pagina.get_text()
            if texto.strip():
                engine.say(texto)
                engine.runAndWait()
        documento.close()
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pasta = sys.argv[1]
        if os.path.isdir(pasta):
            arquivos = [f for f in os.listdir(pasta) if f.lower().endswith('.pdf')]
            if not arquivos:
                print(f"Nenhum PDF encontrado na pasta {pasta}")
            for arquivo in arquivos:
                print(f"Lendo {arquivo}...")
                ler_pdf_em_voz_alta(os.path.join(pasta, arquivo))
        else:
            print(f"A pasta {pasta} não existe.")
    else:
        caminho_pdf = input("Digite o caminho do arquivo PDF: ").strip()
        ler_pdf_em_voz_alta(caminho_pdf)
