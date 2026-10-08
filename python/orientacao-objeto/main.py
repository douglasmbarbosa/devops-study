from conta_corrente import ContaCorrente, CartaoCredito
from agencia import AgenciaVirtual, AgenciaPremium, AgenciaComum

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