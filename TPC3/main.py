import json
import re

dicts_ficheiro = []


def definir_dicionarios():
    with open("processos.txt", "r") as ficheiro:
        for linha in ficheiro:
            dicionario = {}
            items = linha.split("::")
            if len(items) < 6:
                continue
            dicionario["Processo"] = items[0]
            ano_mes_dia = items[1].split("-")
            dicionario["Ano"] = ano_mes_dia[0]
            dicionario["Mes"] = ano_mes_dia[1]
            dicionario["Dia"] = ano_mes_dia[2]
            dicionario["Nome"] = items[2]
            dicionario["Pai"] = items[3]
            dicionario["Mae"] = items[4]
            dicionario["Observacoes"] = items[5]
            dicts_ficheiro.append(dicionario)


def frequencia_processos_ano():
    result = {}
    for entry in dicts_ficheiro:
        ano = entry["Ano"]
        result[ano] = result.setdefault(ano, 0) + 1
    return print(result)


def freq_relacao():
    result = {}
    for entry in dicts_ficheiro:
        relacionamentos = re.findall(r',((\w+)( \w+)*)\.', entry["Observacoes"])
        for relacionamento in relacionamentos:
            result[relacionamento[0]] = result.setdefault(relacionamento[0], 0) + 1
    return print(result)


def primeiros_20():
    with open("result.json", "w") as result:
        for i in range(0, 19):
            result.write(json.dumps(dicts_ficheiro[i], indent=4))


if __name__ == '__main__':
    definir_dicionarios()
    freq_relacao()
