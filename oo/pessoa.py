class Pessoa:
    def __init__(self, *filhos, nome=None, idade=65, sobrenome='Nogueira', cor='Pardo', sexo='Masculino', cor_olhos='castanho'):
        self.cor_olhos = cor_olhos
        self.sexo = sexo
        self.cor = cor
        self.sobrenome = sobrenome
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    guilherme = Pessoa(nome='Guilherme', idade=43, sexo='Masculino', cor='Pardo', cor_olhos='Castanho')
    luiz = Pessoa(guilherme, nome='Lula')
    print(Pessoa.cumprimentar(luiz))
    print(id(luiz))
    print(luiz.cumprimentar())
    print(luiz.nome)
    print(luiz.nome, luiz.sobrenome, luiz.cor, luiz.sexo, luiz.idade)
    luiz.cidade_nascimento = 'Tinguá'
    for filho in luiz.filhos:
        print(filho.nome, filho.sobrenome, filho.cor, filho.sexo, filho.idade)
    print(luiz.__dict__)
    del luiz.filhos
    print(luiz.__dict__)