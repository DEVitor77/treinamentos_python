class Professor:
    def __init__(self,a,b,c,d,e,f):
        self.nome = a
        self.drt  = b
        self.contratacao = c
        self.status = d
        self.disciplina = e
        self.cargaMaxima = f
        
p1 = Professor('Megan', 123, '28/08/2023', 'Pleno',
               'Programacão',20)
print(p1.nome)
print(p1.drt)
print(p1.contratacao)
print(p1.status)
print(p1.disciplina)
print(p1.cargaMaxima)
