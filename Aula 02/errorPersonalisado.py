class SenhaInsegura(Exception):
    pass

def validarSenha(key):
    if len(key) < 8:
        raise SenhaInsegura("A senha é muito curta(menos de 8 caracteres).")
    if len(key) > 20:
        raise SenhaInsegura("A senha é muito longa(mais de 20 caracteres).")
    if not any (c.isdigit() for c in key):
        raise SenhaInsegura("A senha deve conter numeros.")
    return True

senha = input("Digite sua senha\n")

try:
    validarSenha(senha)
except SenhaInsegura as e:
    print(f'!ERROR: "{e}"')
  
