from DataHelper import DataHelper
from BlazeLib import Utils

blazeLib = Utils()
dataHelper = DataHelper()
dataHelper.dataLoader()
data = dataHelper.getData()

gate = True
firstTAlert = data["firstTAlert"]
meta = data["meta"]
progress = data["progress"]
mDate = data["mDate"] # Días configurados de la meta
rDate = data["rDate"] # Días registrados, lo uso para calcular el faltante a la fecha configurada
operator = data["operator"]
currentDate = data["currentDate"] # Aún no hace nada

bbMsg = """---Budget Buddy Helper--
Puedes escribir config meta o conf m para configurar una meta,
escribe input / in para registrar un ingreso u output / out para registrar una salida.
  
Puedes desactivar esta alerta usando firstTimeAlert configurarlo a False\n"""

while gate:
    dateProgress = mDate - rDate

    if firstTAlert:
        print(bbMsg)
        cmd = input("Enter para continuar")
        blazeLib.clear()

    print(f"Tu meta actual es ${meta}\nTe faltan ${meta - progress} para alcanzarla!\nNecesitas ${operator} al dia para alcanzarla\n{dateProgress} dias restantes para alcanzarla")
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
            "operator" : operator,
            "currentDate" : currentDate,
        }
        dataHelper.setData(currentData)
        dataHelper = dataHelper.dataSaver()
        gate = False
        print("Goodbye")