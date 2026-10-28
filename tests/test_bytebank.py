import pytest

from codigo.bytebank import Funcionario


class TestFuncionario:
    def test_metodo_idade_recebe_13_10_2000_retorna_26(self):
        funcionario_test = Funcionario("Pessoa Teste", "13/10/2000", 1612)
        resultado = funcionario_test.idade()
        esperado = 26
        assert resultado == esperado

    @pytest.mark.parametrize(
        "nome, esperado",
        [
            ("Fulano da Silva", "da Silva"),
            (" Pessoa Teste ", "Teste"),
        ],
    )
    def test_metodo_sobrenome_recebe_nome_retorna_sobrenome(self, nome, esperado):
        funcionario_test = Funcionario(nome, "13/10/2000", 1612)
        resultado = funcionario_test.sobrenome()
        assert resultado == esperado

    @pytest.mark.parametrize(
        "nome, salario,esperado, motivo",
        [
            # Cenário de Sucesso (Regra ativa)
            (
                "Jorge Ptolomeu",
                100000,
                90000,
                "Diretor com 100k ou mais deve receber decréscimo",
            ),
            # Cenários de Fronteira (Regra inativa)
            (
                "Gustavo Khan",
                90000,
                90000,
                "Diretor abaixo de 100k não deve receber decréscimo",
            ),
            (
                "João Pessoa",
                150000,
                150000,
                "Outros cargos acima de 100k não devem receber decréscimo",
            ),
        ],
        ids=["diretor_100k", "diretor_90k", "gerente_150k"],
    )
    def test_metodo_decrescimo_salario_deve_reduzir_apenas_da_diretoria_se_mais_de_cem_mil(
        self, nome, salario, esperado, motivo
    ):
        funcionario_test = Funcionario(nome, "13/10/1900", salario)
        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario

        assert resultado == esperado, f"Falhou no cenário: {motivo}"
