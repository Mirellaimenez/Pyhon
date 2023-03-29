idade=25
frase="Sou Mirella e tenho {} anos"
print(frase.format(idade))

#exemplo moeda 
dolar=5.25
euro=5.79
libra=4.79
frase= "Moeda $ {}, @ {}, e £ {}"
print(frase.format(dolar,euro,libra))

#exemplo ditado
p1="ri" #0
p2="último" #1
p3="melhor" #2
frase="Quem {0} por {1}, {0} {2}" #controle pelo indice
print(frase.format(p1,p2,p1,p3))

#Exemplo frases decimais em exibição
dolar=5.2
libra=5.25766
frase="Moeda ${:.2f} e £ {:.2f}"
print(frase.format(dolar,libra))

#Simplificação:abreviação
nome="Mirella"
altura=1.5
print(f"Olá {nome} você tem {altura} metros")