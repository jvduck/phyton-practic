class Cajero():
    #atributos de clase
    def __init__(self,usuario: str,password:int,saldo: int=0) -> None:
        self.__saldo = saldo
        self.usuario = usuario
        self.password = password
    #identificacion del objeto
    def __str__(self) -> str:
        return f'Cuenta Activa: {self.usuario}'
    
    #metodos de clase
    def validarUser(self):
        while True:
            usuario = int(input("Ingrese su clave de Seguridad: "))
            if usuario == self.password:
                print(f"Bienvenido nuevamente {self.usuario}")
                break
            else:
                print("Clave invalida. Intente Nuevamente.")
                
    def getSaldo(self):
        print(f"Su saldo actual es de {self.__saldo}")
    
    def setExtraccion(self,monto):
        while True:
            if monto > self.__saldo:
                print(f"Fondo insuficiente, su saldo es de {self.__saldo}. Ingrese otro importe")
                monto = int(input("Ingrese un monto a extraer: "))
                continue
            self.__saldo -= monto
            print(f"Se ha retirado {monto} de su cuenta ")
            break
    
    def setSaldo(self,monto):
        self.__saldo += monto
        print(f"Se han depositado {monto} satisfactoriamente a su cuenta")

class User(Cajero):
    def __init__(self, usuario: str, password: int, saldo: int = 0) -> None:
        super().__init__(usuario, password, saldo)