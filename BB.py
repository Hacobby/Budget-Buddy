import os.path
import pickle

default = {
    "firstTAlert" : True,
    "meta" : 0,
    "progress" : 0,
    "mDate" : 0,
    "rDate" : 0,
    "operator" : 0
}

print("Looking for data...")
if not os.path.exists("Data.data"):
    print("No data found, creating new data...")
    with open("Data.data", "wb") as dataFile:
        pickle.dump(default, dataFile)
    print("Data created")

else:
    print("Data found, loading...")
    with open("Data.data", "rb") as dataFile:
        data = pickle.load(dataFile)
    print("Data loaded")

with open("Data.data", "rb") as dataFile:
    data = pickle.load(dataFile)

gate = True
firstTAlert = data["firstTAlert"]
meta = data["meta"]
progress = data["progress"]
mDate = data["mDate"] # Días configurados de la meta
rDate = data["rDate"] # Días registrados, lo uso para calcular el faltante a la fecha configurada
operator = data["operator"]

while gate:

    rDate = mDate - rDate

    if firstTAlert:
        print("""---Budget Buddy Helper--
Puedes escribir config meta o conf m para configurar una meta,
escribe input / in para registrar un ingreso u output / out para registrar una salida.
  
Puedes desactivar esta alerta usando firstTimeAlert configurarlo a False\n""")

    print(f"Tu meta actual es ${meta}\nTe faltan ${meta - progress} para alcanzarla!\nNecesitas ${operator} al dia para alcanzarla\n{rDate} dias restantes para alcanzarla")
    cmd = input("N: ")

    if cmd == "firstTimeAlert":
        cmd = input("Nuevo valor: ")
        if cmd == "True":
            firstTAlert = True
        if cmd == "False":
            firstTAlert = False

    if cmd == "input" or cmd == "in":
        if meta <= 0:
            print("Configura una meta primero!")
            continue
        cmd = int(input("Valor de ingreso: "))
        progress += cmd

    if cmd == "output" or cmd == "out":
        if meta <= 0:
            print("Configura una meta primero!")
            continue
        if progress <= 0:
            print("No puedes sacar mas del dinero total que has ingresado")
            continue
        cmd = int(input("Valor de salida: "))
        progress -= cmd

    if cmd == "config meta" or cmd == "conf m":
        meta = int(input("A que monto quiere llegar?: "))
        mDate = int(input("En cuantos dias?: "))
        operator = int(meta / mDate)

    if cmd == "exit":
        print("Saliendo...")

        currentData = {
            "firstTAlert" : firstTAlert,
            "meta" : meta,
            "progress" : progress,
            "mDate" : mDate,
            "rDate" : rDate,
            "operator" : operator
        }
        with open("Data.data", "wb") as dataFile:
            pickle.dump(currentData, dataFile)

        gate = False
        print("Goodbye")