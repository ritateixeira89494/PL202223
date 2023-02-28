import sys
import re

# Nesta solução não é possível ter diferentes tipos na mesma linha, ou seja, 'On 21 =' irá dar erro

def main():
    soma = 0
    for line in sys.stdin:
        if re.match(r'[oO][nN]', line):
            soma = on(soma)
        elif re.match(r'[oO][fF]{2}', line):
            continue
        elif re.match(r'(=)', line):
            print(soma)


def on(res):
    for line in sys.stdin:
        if re.match(r'(\d+)', line):
            res += sum(int(i) for i in re.findall(r'\d', line))
        elif re.match(r'(=)', line):
            print(res)
        elif re.match(r'[oO][fF]{2}', line):
            return res


if __name__ == '__main__':
    main()
