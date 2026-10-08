from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if (self.caixa < 1000000):
            print(f"Caixa abaixo do recomendado. Caixa atual: R${self.caixa:,.2f}")
        else:
            print(f"O valor do caixa está OK. Caixa atual: R${self.caixa:,.2f}")

    def fazer_emprestimo(self, valor, cpf, juros):
        if (self.caixa > valor):
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Empréstimo não disponível. Valor não disponível em caixa")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

# Todas as subclasses herdam os atributos e métodos da Classe Superior


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal += valor


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if (patrimonio > 1000000):
            super.adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("O cliente não tem patrimômio suficiente para entrar na Agência Premium")


if __name__ == __main__:

    agencia_1 = Agencia(22223333, 12345678910, 1212)
    agencia_vitual_1 = AgenciaVirtual("agenciavirtual.com.br",22223334, 12345678910)
    agencia_comum_1 = AgenciaComum(22223335, 12345678910)
    agencia_premium_1 = AgenciaPremium(22223336, 12345678910)

    print(agencia_vitual_1.__dict__)
    print(agencia_comum_1.__dict__)
    agencia_vitual_1.verificar_caixa()
    agencia_comum_1.verificar_caixa()
    agencia_vitual_1.depositar_paypal(10000)
    print(agencia_vitual_1.caixa)
    print(agencia_vitual_1.caixa_paypal)

    # agencia_1.caixa = 1000000

    # agencia_1.verificar_caixa()
    # agencia_1.fazer_emprestimo(12500, 125634658, 0.02)
    # print(agencia_1.emprestimos)

    # agencia_1.adicionar_cliente("Douglas", 1234567800, 125205)
    # print(agencia_1.clientes)
