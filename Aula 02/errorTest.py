def calcular(dividendo,divisor):
    try:
        return f'O resultado é {int(dividendo)/int(divisor)}'
    except (TypeError, ZeroDivisionError) as e:
        print(f'!ERRO! : "{e}"')
        raise
     

dividendo = input("Digite um numero para ser o dividendo:")
divisor = input("Digite um numero para ser o divisor:")

resultado = calcular(dividendo, divisor)

print(resultado)