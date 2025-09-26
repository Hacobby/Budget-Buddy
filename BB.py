import threading

from DataHelper import DataHelper
from BlazeLib import Utils

class BB:
    def __init__(self):
        self.dataHelper = DataHelper(self)
        self.blazeLib = Utils()
        self.dataHelper.dataLoader()

        self.gate = True

        self.firstTAlert = self.dataHelper.data["firstTAlert"]
        self.meta = self.dataHelper.data["meta"]
        self.progress = self.dataHelper.data["progress"]
        self.mDate = self.dataHelper.data["mDate"] # Días configurados de la meta
        self.rDate = self.dataHelper.data["rDate"] # Días registrados, lo uso para calcular el faltante a la fecha configurada
        self.operator = self.dataHelper.data["operator"]
        self.currentDate = self.dataHelper.data["currentDate"] # Aún no hace nada

        self.dateProgress = 0

        self.firstStart = True

        self.bbMsg = """---Budget Buddy Helper--
Puedes escribir config meta o conf m para configurar una meta,
escribe input / in para registrar un ingreso u output / out para registrar una salida.
  
Puedes desactivar esta alerta usando firstTimeAlert configurarlo a False\n"""

    #Main loop
    def main(self):

        autosave = threading.Thread(target=self.dataHelper.autosave, daemon=True)
        autosave.start()

        while self.gate:
            self.dateProgress = self.mDate - self.rDate

            if self.firstTAlert and self.firstStart:
                print(self.bbMsg)
                cmd = input("Enter para continuar")
                self.firstStart = False
                self.blazeLib.clear()

            print(f"Tu meta actual es ${self.meta}\nTe faltan ${self.meta - self.progress} para alcanzarla!\nNecesitas ${self.operator} al dia para alcanzarla\n{self.dateProgress} dias restantes para alcanzarla")
            cmd = input("N: ")

            if cmd == "firstTimeAlert":
                cmd = input("Nuevo valor: ")
                if cmd == "True":
                    self.firstTAlert = True
                if cmd == "False":
                    self.firstTAlert = False

            if cmd == "input" or cmd == "in":
                if self.meta <= 0:
                    print("Configura una meta primero!")
                    continue
                cmd = int(input("Valor de ingreso: "))
                self.progress += cmd

            if cmd == "output" or cmd == "out":
                if self.meta <= 0:
                    print("Configura una meta primero!")
                    continue
                if self.progress <= 0:
                    print("No puedes sacar mas del dinero total que has ingresado")
                    continue
                cmd = int(input("Valor de salida: "))
                self.progress -= cmd

            if cmd == "config meta" or cmd == "conf m":
                self.meta = int(input("A que monto quiere llegar?: "))
                self.mDate = int(input("En cuantos dias?: "))
                self.operator = int(self.meta / self.mDate)

            self.blazeLib.clear()

            if cmd == "exit":
                print("Saliendo...")
                self.dataHelper.dataSaver()
                self.gate = False
                print("Goodbye")
                self.blazeLib.wait(1)

if __name__ == "__main__":
    BB().main()