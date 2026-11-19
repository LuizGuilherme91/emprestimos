from adicionais import ComProfessor, ComRenovacao
from emprestimo import Emprestimo
from recibo import texto_do_recibo


def test_emprestimo_puro():
    assert texto_do_recibo(Emprestimo()) == "Empréstimo: 7 dias"


def test_com_renovacao():
    assert texto_do_recibo(ComRenovacao(Emprestimo())) == "Empréstimo com renovação: 14 dias"


def test_com_renovacao_para_professor():
    emprestimo = ComProfessor(ComRenovacao(Emprestimo()))
    assert emprestimo.prazo() == 28
    assert emprestimo.descricao() == "Empréstimo com renovação para professor"


def test_renovacao_em_dobro():
    assert ComRenovacao(ComRenovacao(Emprestimo())).prazo() == 21