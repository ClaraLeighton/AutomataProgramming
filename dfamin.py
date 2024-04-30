def dfa(archivo):
    input = open(archivo,"r")

    dfa = {"Estados": [], "Alfabeto": [], "Transiciones": []}

    e = False
    a = False
    t = False

    for line in input:
        if line.split()[0] == "Estados":
            e = True
            continue
        
        if line.split()[0] == "Alfabeto":
            e = False
            a = True
            continue

        if line.split()[0] == "Transiciones":
            e = False
            a = False
            t = True
            continue

        if e:
            dfa["Estados"].append(line.split()[0])
        
        if a: 
            dfa["Alfabeto"].append(line.split()[0])
        
        if t:
            dfa["Transiciones"].append(f"{line.split()[0]}{line.split()[1]}{line.split()[3]}")

    input.close()
    
    print(f"Estados: {dfa["Estados"]}")
    print(f"Alfabeto: {dfa["Alfabeto"]}")
    print(f"Transiciones: {dfa["Transiciones"]}")

    return dfa

def crear_matriz(dfa):
    estados = [] #lista con todos los estados
    pares = [] #lista con 
    for i in range(len(dfa["Estados"])):
        estados.append(dfa["Estados"][i][-1])
    
    for i in range(len(estados)):
        for j in range(i+1, len(estados)):
            pares.append(estados[i] + estados[j])

    alf = []
    for i in range(len(dfa["Alfabeto"])):
        alf.append(0)

    matriz_minimizacion = {}
    for par in pares:
        matriz_minimizacion[par] = [alf.copy(),0]

    return matriz_minimizacion

dfa = dfa("dfa_input.txt")
matriz = crear_matriz(dfa)
print(matriz)