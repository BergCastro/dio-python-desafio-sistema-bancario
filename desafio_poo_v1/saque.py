from transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor: float = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)