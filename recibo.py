def texto_do_recibo(emprestimo):
    return emprestimo.descricao() + ": " + str(emprestimo.prazo()) + " dias"