import sys


def txt_importer(path_file):
    if not path_file.endswith("txt"):
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file, "r") as file:
            lines = file.readlines()
        output = [line.rstrip("\n") for line in lines]
        return output
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
