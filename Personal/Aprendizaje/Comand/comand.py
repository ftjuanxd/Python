from abc import ABC, abstractmethod

#interfaz command 
class Command(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

#Comando Concreto 1
class RetirarDinero(Command):
    def __init__(self, cajero, monto):
        self.cajero = cajero
        self.monto = monto

    def ejecutar(self):
        self.cajero.retirar_dinero(self.monto)

#Comando Concreto 2
class ConsultarSaldo(Command):
    def __init__(self, cajero):
        self.cajero = cajero

    def ejecutar(self):
        self.cajero.consultar_saldo()

#Comando Concreto 3
class DepositaDinero(Command):
    def __init__(self, cajero, monto):
        self.cajero = cajero
        self.monto = monto

    def ejecutar(self):
        self.cajero.deposita_dinero(self.monto)

#Invoker
class TerminalCajero:
    def set_comando(self, comando):
        self.comando = comando

    def ejecutar_comando(self):
        self.comando.ejecutar()

#receptor
class CajeroAutomatico:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar_dinero(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Se ha retirado $", monto)
            self.consultar_saldo()
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        print("El saldo actual es: $", self.saldo)

    def deposita_dinero(self, monto):
        self.saldo += monto
        print("Se ha depositado $", monto)
        self.consultar_saldo()
        
#Main
if __name__ == "__main__":
    cajero = CajeroAutomatico(10000)
    terminal = TerminalCajero()

    while True:
        print("Por favor, elige una opción:\n")
        print("1. Retirar dinero")
        print("2. Consultar saldo")
        print("3. Depositar dinero")
        print("4. Salir")
        opcion = input("Digite la Opción: ")

        try:
            opcion = int(opcion)
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")
            continue

        if opcion == 1:
            monto_retiro = float(input("Ingresa el monto a retirar: "))
            terminal.set_comando(RetirarDinero(cajero, monto_retiro))
            terminal.ejecutar_comando()
        elif opcion == 2:
            terminal.set_comando(ConsultarSaldo(cajero))
            terminal.ejecutar_comando()
        elif opcion == 3:
            monto_deposito = float(input("Ingresa el monto a depositar: "))
            terminal.set_comando(DepositaDinero(cajero, monto_deposito))
            terminal.ejecutar_comando()
        elif opcion == 4:
            print("Gracias por usar nuestro cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


