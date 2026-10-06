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
    pass


class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass


agencia_1 = Agencia(22223333, 12345678910, 1212)
agencia_vitual_1 = Agencia(22223334, 12345678910, 1212)
agencia_1.caixa = 1000000

agencia_1.verificar_caixa()
agencia_1.fazer_emprestimo(12500, 125634658, 0.02)
print(agencia_1.emprestimos)

agencia_1.adicionar_cliente("Douglas", 1234567800, 125205)
print(agencia_1.clientes)
