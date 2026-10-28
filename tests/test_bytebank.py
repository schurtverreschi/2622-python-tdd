from codigo.bytebank import Funcionario


class TestFuncionario:
    def test_metodo_idade_recebe_13_10_2000_retorna_26(self):
        funcionario_test = Funcionario("Pessoa Teste", "13/10/2000", 1612)
        resultado = funcionario_test.idade()
        assert resultado == 26
