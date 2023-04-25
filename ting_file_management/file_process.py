import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):

    for index in instance._data:
        if index["nome_do_arquivo"] == path_file:
            return None

    archive = txt_importer(path_file)
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(archive),
        "linhas_do_arquivo": archive
    }

    instance.enqueue(output)
    print(output, file=sys.stdout)


def remove(instance):
    if len(instance) != 0:
        archive = instance._data[0]["nome_do_arquivo"]
        instance.dequeue()
        print(
            f"Arquivo {archive} removido com sucesso",
            file=sys.stdout
        )
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
