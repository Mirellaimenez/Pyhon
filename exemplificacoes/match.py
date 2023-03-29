print("Escolha sua bebida do café da manhã")
bebida = (input())

match bebida:
    case "café":
        print("Cafeina em excesso não faz bem")
    case "leite":
        print("Ficaria bom com um achocolatado")
    case "capuccino":
        print("Uau! Um ótimo jeito de começar o dia")
    case "chá":
        print("Uma boa escolha para se tranquilizar")
    case "suco de laranja":
        print("Sucos de frutas são refrescantes")
    case other:
        print("Essa não me parece uma boa opção para o café da manhã, mas tudo bem!")
print("Fim de programa") #fora da estrutura match case
