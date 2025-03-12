def converter_para_int(n):
    try:
        return f'o numero convertido é {int(n)}'
        
    except Exception as e:
        return f'none. ERROR MESSAGE: "{e}"'

numero = input("Digite um numero para ser analisado\n")

int = converter_para_int(numero)

print(int)
  