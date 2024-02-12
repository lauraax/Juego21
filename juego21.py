import random
simbolos=["\U00002663",  "\U00002666", "\U00002665", "\U00002660"]
valores=["A", "J","Q","K"]+[str(i)for i in range (2,11)]
mazo=[(U,P)for U in valores for P in simbolos]

random.shuffle(mazo)

def valorCarta(carta):
    valor = carta[0]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)

def valorMano(mano):
    valor = sum(valorCarta(carta) for carta in mano)
    return valor
    

print("Bienvenido a Blackjack!")
manoJugador = [mazo.pop(), mazo.pop()]
print("Tu mano: ", manoJugador)

manoBanca = [mazo.pop(), mazo.pop()]
print("Mano de la casa: ",[manoBanca[0],"\U00002753"])

while valorMano(manoJugador) < 21:
    opcion = input("Digite 1 para PEDIR CARTA ó 2 para PLANTARSE:  ")
    if opcion == "1":
        manoJugador.append(mazo.pop())
        print("Tu mano:", manoJugador)
    else:
        break

if valorMano(manoJugador) > 21:
    print("Tu mano superó los 21 puntos, perdiste","\U0001F61E")
else:
    while valorMano(manoBanca)<17:
        manoBanca.append(mazo.pop())

    print("Tu mano: ", manoJugador)
    print("Mano de la banca: ",manoBanca)

    valorManoJugador=valorMano(manoJugador)
    valorManoBanca=valorMano(manoBanca)

    if valorManoJugador>valorManoBanca or valorManoBanca>21:
        print("FELICIDADES, LE GANASTE A LA BANCA")
    elif valorManoJugador<valorManoBanca:
        print("Tu mano superó los 21 puntos, perdiste","\U0001F61E")
    else:
        print("EMPATE")


   
    

