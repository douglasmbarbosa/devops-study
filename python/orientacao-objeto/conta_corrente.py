from datetime import datetime
import pytz


class ContaCorrente():

    """
    Cria um objeto da classe ContaCorrente para
    gerenciar as contas dos clientes do banco

    Atributos:
        nome: nome do cliente
        cpf: cpf do cliente
        saldo: saldo da conta do cliente
        limite: limite da conta do cliente
        agencia: agencia da conta do cliente
        numero_conta: numero da conta do cliente
        transacoes: histórico de transações do cliente
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR).strftime('%d/%m/%Y %H:%M:%S') 
        return horario_BR

    def __init__(self, nome, cpf, agencia, numero_conta):
        self._nome = nome 
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._transacoes = []

    def consultar_saldo(self):
        print(f"Saldo disponível R${self._saldo:,.2f}")

    def depositar(self, valor):
        self._saldo += valor
        self.consultar_saldo()
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _verificar_limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        if ((self._saldo - valor) < self._verificar_limite_conta()):
            print(f"Não é possível sacar {valor}")
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            self.consultar_saldo()

    def mostrar_extrato(self):
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))


# Programa


conta_corrente_1 = ContaCorrente("Douglas", "123.456.789-00", 1234, 45690)
conta_corrente_2 = ContaCorrente("Jose", "123.456.789-01", 1234, 45691)


conta_corrente_1.consultar_saldo()
conta_corrente_1.depositar(10000)
conta_corrente_1.sacar(200)
conta_corrente_1.sacar(100)

print("-" * 30)

conta_corrente_1.mostrar_extrato()

conta_corrente_1.transferir(1000, conta_corrente_2)
conta_corrente_1.consultar_saldo()
conta_corrente_2.consultar_saldo()
