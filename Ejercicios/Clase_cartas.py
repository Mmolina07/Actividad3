class carta:
    
    PINTAS = ('corazones', 'picas','diamantes','treboles')

def __init__(self,valor,pinta):
    self.valor = valor
    self.pinta = pinta


mi_carta = carta(10,'picas')

print("Valor de la carta:", mi_carta.valor)
print("Pinta de la carta:", mi_carta.pinta)