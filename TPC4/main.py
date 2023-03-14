import re, ply.lex as lex
import Alunos, Alunos2, Alunos3, Alunos4, Alunos5

print('Indique o pathfile do ficheiro a ver')
pathfile = input()

in_file = open(pathfile, 'r')
first_line = in_file.readline()

if re.match(r'[A-Za-zÀ-Üà-ü]+(,[A-Za-zÀ-Üà-ü]+)*\{\d+\},+', first_line):
    Alunos2.alunos2(pathfile)
elif re.match(r'[A-Za-zÀ-Üà-ü]+(,[A-Za-zÀ-Üà-ü]+)*\{\d+,\d+\},+', first_line):
    Alunos3.alunos3(pathfile)
elif re.match(r'[A-Za-zÀ-Üà-ü]+(,[A-Za-zÀ-Üà-ü]+)*\{\d+,\d+\}\:\:[a-z]+,+', first_line):
    func = re.sub(r',', r'', first_line[30:35])
    if func == 'sum':
        Alunos4.alunos4(pathfile)
    elif func == 'media':
        Alunos5.alunos5(pathfile)
else:
    Alunos.alunos(pathfile)

in_file.close()
