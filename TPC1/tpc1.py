import sys
import re

#Início da soma dos dígitos
soma = 0
enable = True


#Linha de input é lida
for line in sys.stdin:
    # Divide o texto em palavras "on", "off", dígitos e '='
    palavras = re.findall(r'on|off|\d+|=', line.lower())
    for palavra in palavras:
        #Quando encontra a sequencia off desliga o comportamento de somar as sequências de digitos
        if palavra == 'off':
            enable = False
        #E liga o comportamento quando encontra a sequencia on
        elif palavra == 'on':
            enable = True
        #Quando encontra o carater '='  imprime o resultado da soma até então e reinicia a soma a 0
        elif palavra == '=':
            print(soma)
        #Assim que a sequencia de digitos é encontrada é somada a sequência de digitos ao resultado da soma até então
        elif enable and palavra.isdigit():
            soma += int(palavra)

#No final imprime o resultado da soma
print(soma)
