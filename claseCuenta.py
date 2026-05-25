class CuentBancaria:
    def __init__(self,numeroCuenta,titular,saldo):
        self.numeroCuenta=numeroCuenta
        self.titular=titular
        self.saldo=saldo
    def depositar(self,monto):
        print("Se deposito ",monto,"Bs")
        self.saldo=self.saldo+monto
        print("Saldo actual ",self.saldo)
    def retirar(self,monto):
        if monto<=self.saldo:
            print("Retirando ",monto,"Bs")
            self.saldo=self.saldo-monto
            print("Salto actual ",monto,"Bs")
        else:
            print("Error saldo insuficiente")

class CuentaAhorro(CuentBancaria):
    def __init__(self,numeroCuenta,titular,saldo,tasaInteres,limiteRetiro):
        super().__init__(numeroCuenta,titular,saldo)
        self.tasaInteres=tasaInteres
        self.limiteRetiro=limiteRetiro
    def validarLimite(self,monto):
        limite=3000
        if monto>limite:
            print("Limite de retiro vuelva a intentarlo mañana...")

persona1=CuentaAhorro(7455121247,"Kevin Arroyo",8000,10,3000)
limite=persona1.validarLimite(3200)
if limite:
    print("Error...")
else:
    print("Retirando...")

persona1.Depositar(3500)
