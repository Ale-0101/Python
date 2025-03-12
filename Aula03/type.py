import hashlib

senha = "senha123"

print(hashlib.sha256(senha.encode()).hexdigest())