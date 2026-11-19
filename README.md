# Python e TDD — Validação de Regras de Negócio (ByteBank)

Repositório de estudos focado em **Test-Driven Development (TDD)** e testes unitários em **Python** utilizando `pytest`, simulando regras de negócio da classe `Funcionario` em um contexto bancário fictício (*ByteBank*).

## 🎯 Objetivo do Projeto

Praticar a escrita e organização de testes automatizados para validar comportamentos, cenários de fronteira e exceções esperadas em Python, mantendo a suíte de testes separada do código principal.

## 📁 Estrutura do Repositório

```text
.
├── codigo/
│   └── bytebank.py          # Implementação da classe Funcionario e regras de negócio
├── tests/
│   └── tests_bytebank.py    # Suíte de testes unitários parametrizados com pytest
├── .gitignore
└── requirements.txt
```

## 🧠 Regras e Cenários Cobertos

Em `codigo/bytebank.py`, a classe `Funcionario` modela dados básicos (`nome`, `data_nascimento`, `salario`) e regras testadas em `tests/tests_bytebank.py`:

* **Cálculo de idade (`idade`)**: valida o cálculo considerando se o funcionário já fez ou ainda não fez aniversário no ano corrente com base em dia e mês.
* **Extração de sobrenome (`sobrenome`)**: valida a obtenção do sobrenome a partir de nomes completos (incluindo casos com espaços extras nas extremidades).
* **Decréscimo salarial para diretoria/sócios (`decrescimo_salario` / `_eh_socio`)**: aplica redução de 10% apenas quando o salário é `>= 100.000` e o sobrenome consta na lista de sócios/diretoria, testando cenários ativos e de fronteira.
* **Cálculo de bônus (`calcular_bonus`)**: calcula 10% do salário até o teto de `1.000` (salários até `10.000`) e lança `ValueError` caso o bônus ultrapasse esse limite (salários acima de `10.000`).

## 🛠️ Tecnologias e Ferramentas

* **Python**
* **pytest** (testes parametrizados com `@pytest.mark.parametrize` e validação de exceções com `pytest.raises`)
* **pytest-cov** / **coverage**
* **Git e GitHub**

## ▶️ Como Executar Localmente

1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone https://github.com/schurtverreschi/2622-python-tdd.git
   cd 2622-python-tdd
   ```

2. Crie e ative um ambiente virtual (opcional, recomendado):
   ```bash
   python -m venv .venv
   # Linux/macOS:
   source .venv/bin/activate
   # Windows:
   .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute os testes com `pytest`:
   ```bash
   pytest
   ```
   *(Opcional)* Para rodar com saída detalhada ou relatório de cobertura:
   ```bash
   pytest -v
   pytest --cov=codigo
   ```
