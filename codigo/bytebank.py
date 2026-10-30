from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome  # pragma: no cover

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split("/")
        dia_nasc = int(data_nascimento_quebrada[0])
        mes_nasc = int(data_nascimento_quebrada[1])
        ano_nasc = int(data_nascimento_quebrada[2])

        hoje = date.today()

        idade_calculada = hoje.year - ano_nasc

        if (hoje.month, hoje.day) < (mes_nasc, dia_nasc):
            idade_calculada -= 1

        return idade_calculada

    def sobrenome(self):
        nome_quebrado = self._nome.strip().split(" ", 1)
        sobrenome = nome_quebrado[1]
        return sobrenome

    def _eh_socio(self):
        sobrenomes = [
            "Bragança",
            "Windsor",
            "Bourbon",
            "Yamato",
            "Al Saud",
            "Khan",
            "Tudor",
            "Ptolomeu",
        ]
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._eh_socio():
            self._salario *= 0.9

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise ValueError("Salário não se enquadra no critério do bônus")
        return valor

    def __str__(self):
        return f"Funcionário({self._nome}, {self._data_nascimento}, {self._salario})"
