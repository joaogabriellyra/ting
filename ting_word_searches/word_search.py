def exists_word(word, instance, search_for_word=False):
    output = []

    for archive in instance._data:
        occurrences = []
        for index, file in enumerate(archive["linhas_do_arquivo"], start=1):
            if word.lower() in file.lower():
                occurrences.append(
                    {"linha": index, "conteudo": file}
                    if search_for_word
                    else {"linha": index}
                )
    if len(occurrences) != 0:
        output.append(
            {
                "arquivo": archive["nome_do_arquivo"],
                "palavra": word,
                "ocorrencias": occurrences,
            }
        )
    return output


def search_by_word(word, instance):
    return exists_word(word, instance, True)
