import pytest

from codigo.bytebank import Funcionario


class TestFuncionario:
    def test_metodo_idade_recebe_13_10_2000_retorna_26(self):
        funcionario_test = Funcionario("Pessoa Teste", "13/10/2000", 1612)
        resultado = funcionario_test.idade()
        assert resultado == 26

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
