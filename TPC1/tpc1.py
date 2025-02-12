import sys
import re

#Início da soma dos dígitos
soma = 0
enable = True

for line in sys.stdin:
    # Divide o texto em palavras "on", "off", dígitos e '='
    palavras = re.findall(r'on|off|\d+|=', line.lower())
    for palavra in palavras:
        if palavra == 'off':
            enable = False
        elif palavra == 'on':
            enable = True
        elif palavra == '=':
            print(soma)
            soma = 0
        elif enable and palavra.isdigit():
            soma += int(palavra)

