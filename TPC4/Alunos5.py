import re, ply.lex as lex


def alunos5(pathfile):
    tokens = ('NUMERO', 'NOME', 'CURSO', 'NOTAS')
    states = (
    ('TAB', 'exclusive'), ('NUM', 'exclusive'), ('NAME', 'exclusive'), ('CURS', 'exclusive'), ('NOTES', 'exclusive'))

    t_ANY_ignore = '\t'
    t_NAME_ignore = ','
    t_CURS_ignore = ','

    def t_newline(t):
        r'(.+)\n'
        t.lexer.func = re.sub(r',', r'', t.value[30:35])
        t.value = t.value[:23]
        t.lexer.keys = t.value.replace('\n', '').split(',')

        for i in range(len(t.lexer.keys)):
            t.lexer.dictionary[t.lexer.keys[i]] = []
        t.lexer.begin('NUM')

    def t_TAB_newline(t):
        r'\n'
        t.lexer.begin('NUM')

    def t_NUM_NUMERO(t):
        r'\d+'
        t.lexer.dictionary[t.lexer.keys[0]].append(int(t.value))
        t.lexer.begin('NAME')

    def t_NAME_NOME(t):
        r'[A-Za-zÀ-Üà-ü]+[ ][A-Za-zÀ-Üà-ü]+'
        t.lexer.dictionary[t.lexer.keys[1]].append(t.value)
        t.lexer.begin('CURS')

    def t_CURS_CURSO(t):
        r'[A-Za-zÀ-Üà-ü]+([ ][A-Za-zÀ-Üà-ü]+)*'
        t.lexer.dictionary[t.lexer.keys[2]].append(t.value)
        t.lexer.begin('NOTES')

    def t_NOTES_NOTAS(t):
        r'((20|1\d),)+(20|1\d)'
        lexer.notas = [int(x) for x in t.value.split(',')]
        t.lexer.dictionary[t.lexer.keys[3]].append(t.lexer.notas)
        t.lexer.begin('TAB')

    def t_ANY_error(t):
        print('token não reconhecido', t.value)
        t.lexer.skip(1)

    lexer = lex.lex()
    lexer.notas = []
    lexer.keys = []
    lexer.dictionary = {}
    lexer.func = ""

    in_file = open(pathfile, 'r')
    for line in in_file:
        lexer.input(line)
        for tok in lexer:
            pass
    in_file.close()
    with open('Ficheiros_Output/alunos5.json', 'w') as out_file:
        s = '['
        i = j = 0
        for i in range(len(lexer.dictionary) - 1):
            s += '\n\t{'
            for j in range(len(lexer.dictionary.keys())):
                k = list(lexer.dictionary.keys())[j]
                v = list(lexer.dictionary.values())[j][i]
                if (j == len(lexer.dictionary.keys()) - 1):
                    s += '\n\t\t"' + str(k) + '_' + str(lexer.func) + '": ' + str(sum(v) / len(v))
                else:
                    s += '\n\t\t"' + str(k) + '": ' + '"' + str(v) + '",'
            if (i == len(lexer.dictionary) - 2):
                s += '\n\t}'
            else:
                s += '\n\t},'
        s += '\n]'
        out_file.write(s)
        out_file.close()
        print(f"Conteudo do ficheiro alunos5.json:\n{s}")