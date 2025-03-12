def analise_positivo(numero):
    if numero>-1:
        return "positivo"
    else:
        return "negativo"
    
def par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"


numero = int(input("Digite um numero para ser analisado"))

positivo_ou_negativo = analise_positivo(numero)
positivo_ou_negativo = par_impar(numero)

print(f"o numero é {str(positivo_ou_negativo)} e é {positivo_ou_negativo}")
  