from adicionais import ComProfessor, ComRenovacao
from emprestimo import Emprestimo
from recibo import texto_do_recibo

print(texto_do_recibo(Emprestimo()))
print(texto_do_recibo(ComRenovacao(Emprestimo())))
print(texto_do_recibo(ComProfessor(ComRenovacao(Emprestimo()))))