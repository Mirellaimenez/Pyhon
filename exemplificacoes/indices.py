#       0123456789    : o indice começa do 0, cada caracter está em uma posição do indice
frase= "Hakuna Matata"
print(frase[7 : 11]) #--para mostrar somente as letras desejadas, basta colocar o indice necessário.
#-- No exemplo, queremos mostrar somente o "MATA" que é do indice 7:10, porém é necessário colocar 7:11

print(frase[0:6])

#Valores negativos: começa no -1 e a leitura é da direita para a esquerda
print(frase[-11: -4]) #o maior valor a esquerda e o menor valor a direira
print(frase[-1])
print(frase[-10:-3])

#valores negativos 2
# -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  H   A   K    U  N  A     M  A  T  A  T  A
print(frase[-13: -7])