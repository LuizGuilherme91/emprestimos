class ComRenovacao:
    def __init__(self, emprestimo):
        self.emprestimo = emprestimo

    def prazo(self):
        return self.emprestimo.prazo() + 7

    def descricao(self):
        return self.emprestimo.descricao() + " com renovação"


class ComProfessor:
    def __init__(self, emprestimo):
        self.emprestimo = emprestimo

    def prazo(self):
        return self.emprestimo.prazo() + 14

    def descricao(self):
        return self.emprestimo.descricao() + " para professor"