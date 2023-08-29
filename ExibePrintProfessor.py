class Professor:
    def __init__(self, nome, drt, contratacao, status, disciplina, carga_maxima):
        self.nome = nome
        self.drt  = drt
        self.contratacao = contratacao
        self.status = status
        self.disciplina = disciplina
        self.carga_maxima = carga_maxima

    def exibe(self):
        print(30 * '-')
        print(f'Nome:.........: {self.nome}')
        print(f'DRT:..........: {self.drt}')
        print(f'Contratação...: {self.contratacao}')
        print(f'Status........: {self.status}')
        print(f'Disciplina....: {self.disciplina}')
        print(f'numero Carga Maxima..: {self.carga_maxima}')
        print(30 * '-')
        print()

nome = input('Nome? ')
drt = int(input('numero da drr? '))
contratacao = input('contratacao? ')
status = input ('Status? ')
disciplina = input ('Disciplina? ')
carga_maxima = int(input('carga maxima? '))

p1 = Professor(nome, drt, contratacao, status, disciplina, carga_maxima)

p1.exibe()
