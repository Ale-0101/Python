def qualOTipo (var):
    print(type(var))

list = [0,True,"",0.0,[],{0,0},{0:0},()]

for x in list:
    qualOTipo(x)