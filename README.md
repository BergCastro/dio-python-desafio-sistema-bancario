# 🏦 Desafios do Sistema Bancário em Python (Trilha DIO)

<p align="center">
  <img src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png" alt="DIO Logo" width="200">
</p>

## ✨ Sobre os Desafios

Este projeto representa a conclusão de uma série de desafios propostos na Trilha de Python da Digital Innovation One (DIO). O objetivo principal é desenvolver um sistema bancário simplificado, simulando operações essenciais. Cada desafio visa consolidar os conhecimentos adquiridos sobre a linguagem Python, com diferentes níveis de complexidade e abordagens.

Os desafios exploram:

*   **Estruturas de Dados:** Listas, dicionários e tuplas.
*   **Controle de Fluxo:** Condicionais (`if`, `else`, `elif`) e loops (`for`, `while`).
*   **Funções:** Definição e utilização para modularização do código.
*   **Orientação a Objetos (POO):** Implementação de classes para representar entidades bancárias (desafio específico).
*   **Tratamento de Exceções:** Utilização de `try-except` para lidar com entradas inválidas.
*   **Boas Práticas de Programação:** Legibilidade, indentação e comentários.

## 🎯 Desafios Implementados

Este repositório contém as seguintes versões do desafio do sistema bancário:

1.  **Desafio 1: Implementação Simples:**  Uma implementação básica do sistema bancário utilizando funções e estruturas de dados simples. (Arquivo: `desafio.py`)

2.  **Desafio 2: Implementações de Funções:** Uma versão mais estruturada, com foco na modularização do código através de funções bem definidas. (Arquivo: `desafio_v2.py`)

3.  **Desafio 3: Modelagem POO:** Uma implementação completa utilizando os princípios da Programação Orientada a Objetos, com classes representando contas, clientes, transações, etc. (Pasta: `desafio_poo_v1/`)

## 🚀 Funcionalidades (Comum a Todos os Desafios)

Embora a implementação varie entre os desafios, as funcionalidades principais do sistema bancário são:

*   **Depósito:** Permite depositar valores positivos na conta.
*   **Saque:** Permite realizar saques, respeitando limites diários, valores máximos e saldo disponível.
*   **Extrato:** Exibe o histórico de operações (depósitos e saques) e o saldo atual.

## ⚙️ Como Executar os Sistemas

1.  **Pré-requisitos:**
    *   Python 3.6 ou superior instalado em seu sistema.
2.  **Download:**
    *   Clone este repositório para sua máquina local:
        ```bash
        git clone https://github.com/BergCastro/dio-python-desafio-sistema-bancario.git
        ```
3.  **Execução:**

    *   **Desafio 1 (Implementação Simples):**
        ```bash
        python desafio.py
        ```

    *   **Desafio 2 (Implementações de Funções):**
        ```bash
        python desafio_v2.py
        ```

    *   **Desafio 3 (Modelagem POO):**
        ```bash
        cd desafio_poo_v1
        ```

    *   **Desafio 4 (Iteradores e Geradores):**
        ```bash
        cd desafio_iteradores_geradores
        ```
        

4.  **Utilização:**
    *   Siga as instruções exibidas no menu interativo de cada versão para realizar as operações desejadas.

## 🏛️ Arquitetura do Projeto

*   `desafio.py`: Script principal do Desafio 1.
*   `desafio_v2.py`: Script principal do Desafio 2.
*   `desafio_poo_v1/`:
    *   `conta.py`: Classe base para contas bancárias.
    *   `conta_corrente.py`: Classe para contas correntes (herda de `conta.py`).
    *   `cliente.py`: Classe para clientes.
    *   `pessoa_fisica.py`: Classe para pessoas físicas (herda de `cliente.py`).
    *   `transacao.py`: Classe base para transações.
    *   `saque.py`: Classe para saques (herda de `transacao.py`).
    *   `deposito.py`: Classe para depósitos (herda de `transacao.py`).
    *   `historico.py`: Classe para o histórico de transações.
    *   ... (outros arquivos relevantes para a implementação POO)
    `desafio_iteradores_geradores/`:
    *   `desafio.py`: cript principal do Desafio 4.
*   `README.md`: Documentação do projeto (este arquivo).

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Outras Bibliotecas:**
    *   `datetime`: Utilizada para registrar a data e hora das transações (pode ser utilizada em todos os desafios, mas mais relevante no Desafio 1 e 2).

## ✒️ Contribuições

Contribuições são sempre bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - consulte o arquivo `LICENSE` para obter detalhes.

---

© 2025 Lindemberg Nunes de Castro