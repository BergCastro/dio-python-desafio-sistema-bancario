from conta import Conta
from saque import Saque

class ContaCorrente(Conta):
    def __init__(self, numero: str, cliente, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self.limite: float = limite
        self.limite_saques: int = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = len([
            transacao
            for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__
        ])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self) -> str:
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """