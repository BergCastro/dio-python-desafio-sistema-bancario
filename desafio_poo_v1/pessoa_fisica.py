from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str) -> None:
        super().__init__(endereco)
        self.nome: str = nome
        self.data_nascimento: str = data_nascimento
        self.cpf: str = cpf