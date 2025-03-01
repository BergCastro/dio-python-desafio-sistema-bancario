# 🏦 Desafio do Sistema Bancário em Python (Trilha DIO)

<p align="center">
  <img src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png" alt="DIO Logo" width="200">
</p>

## ✨ Sobre o Desafio

Este projeto representa a conclusão de um dos desafios propostos na Trilha de Python da Digital Innovation One (DIO). O objetivo principal é desenvolver um sistema bancário simplificado, simulando operações essenciais como depósitos, saques e a emissão de extratos. Este desafio visa consolidar os conhecimentos adquiridos sobre a linguagem Python, incluindo:

*   **Estruturas de Dados:** Listas, dicionários e tuplas.
*   **Controle de Fluxo:** Condicionais (`if`, `else`, `elif`) e loops (`for`, `while`).
*   **Funções:** Definição e utilização para modularização do código.
*   **Orientação a Objetos (Opcional):** Implementação de classes para representar entidades bancárias.
*   **Tratamento de Exceções:** Utilização de `try-except` para lidar com entradas inválidas.
*   **Boas Práticas de Programação:** Legibilidade, indentação e comentários.

## 🚀 Funcionalidades Implementadas

O sistema bancário oferece as seguintes funcionalidades:

*   **Depósito:**
    *   Permite que o usuário deposite valores positivos em sua conta.
    *   Registra a data e hora do depósito no extrato.
    *   Valor mínimo para depósito: R$ 1.00
*   **Saque:**
    *   Permite que o usuário realize saques, respeitando as seguintes restrições:
        *   Limite de saques diários (configurável).
        *   Valor máximo por saque (configurável).
        *   Saldo disponível na conta.
    *   Registra a data e hora do saque no extrato.
*   **Extrato:**
    *   Exibe um histórico completo de todas as operações realizadas na conta, incluindo depósitos e saques.
    *   Mostra o saldo atual da conta.
    *   Caso não haja movimentações, exibe uma mensagem informativa.

## ⚙️ Como Executar o Sistema

1.  **Pré-requisitos:**
    *   Python 3.6 ou superior instalado em seu sistema.
2.  **Download:**
    *   Clone este repositório para sua máquina local:
        ```bash
        git clone https://github.com/BergCastro/dio-python-desafio-sistema-bancario.git
        ```
3.  **Execução:**
    *   Execute o script desafio v1:
        ```bash
        python desafio.py
        ```
    *   Execute o script desafio v2
        ```bash
        python desafio_v2.py
        ```
4.  **Utilização:**
    *   Siga as instruções exibidas no menu interativo para realizar as operações desejadas.

## 🏛️ Arquitetura do Projeto

O projeto está estruturado da seguinte forma:

desafio.py # Script principal com a lógica do sistema README.md # Documentação do projeto (este arquivo)


O script `desafio.py` contém as seguintes funções principais:

*   `exibir_menu()`: Exibe as opções do menu para o usuário.
*   `depositar(saldo, extrato)`: Realiza a operação de depósito.
*   `sacar(saldo, extrato, numero_saques)`: Realiza a operação de saque.
*   `exibir_extrato(saldo, extrato)`: Exibe o extrato da conta.
*   `main()`: Função principal que controla o fluxo do programa.

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Outras Bibliotecas:**
    *   `datetime`: Utilizada para registrar a data e hora das transações.

## ✒️ Contribuições

Contribuições são sempre bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - consulte o arquivo `LICENSE` para obter detalhes.

---

© 2025 Lindemberg Nunes de Castro