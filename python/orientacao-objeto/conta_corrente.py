from datetime import datetime
import pytz
from random import randint


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
        self.cartoes_credito = []

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


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f"{CartaoCredito._data_hora().month} / {CartaoCredito._data_hora().year + 4}"
        self.codigo_segurança = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes_credito.append(self)


# Programa

# Funcionamento Classe ContaCorrente


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

# Funcionamento Classe CartaoCredito

cartao_credito_1 = CartaoCredito('Douglas', conta_corrente_1)

print(cartao_credito_1.codigo_segurança)