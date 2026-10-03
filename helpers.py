import os
import unicodedata

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def normalizar_texto(texto):
    texto = texto.upper()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto