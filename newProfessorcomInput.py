class Professor:
    def __init__(self, nome, drt, contratacao, status, disciplina, carga_maxima):
        self.nome = nome
        self.drt  = drt
        self.contratacao = contratacao
        self.status = status
        self.disciplina = disciplina
        self.carga_maxima = carga_maxima


nome = input('Nome? ')
drt = int(input('numero da drr? '))
contratacao = input('contratacao? ')
status = input ('Status? ')
disciplina = input ('Disciplina? ')
carga_maxima = int(input('carga maxima? '))

p1 = Professor(nome, drt, contratacao, status, disciplina, carga_maxima)

p1 = Professor()
print(p1.nome)
print(p1.drt)
print(p1.contratacao)
print(p1.status)
print(p1.disciplina)
print(p1.carga_maxima)
