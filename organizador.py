import os
import shutil

pasta = os.path.expanduser("~/Downloads")
arquivos = os.listdir(pasta)
print(arquivos)

categorias = {
    ".pdf": "PDFs",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".odt": "Documentos",
    ".xlsx": "Documentos",
    ".pptx": "Documentos",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".mp3": "Áudio",
    ".wav": "Áudio",
    ".flac": "Áudio",
    ".mp4": "Vídeo",
    ".avi": "Vídeo",
    ".mkv": "Vídeo",
    ".mov": "Vídeo",
    ".exe": "Instaladores",
    ".msi": "Instaladores",
    ".dmg": "Instaladores",
}

for arquivo in arquivos:
    if os.path.isdir(os.path.join(pasta, arquivo)):
        continue # Se haver pasta não irá ser movida

    nome,extensao = os.path.splitext(arquivo)
    categoria = categorias.get(extensao.lower(), "Outros")

    destino = os.path.join(pasta, categoria)
    os.makedirs(destino, exist_ok=True)
    os.rename(os.path.join(pasta, arquivo), os.path.join(destino, arquivo))

print("Arquivos organizados com sucesso!")

