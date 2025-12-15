# 🔍 Autômatos: Da Teoria à Prática (Meu Grep)

> Uma implementação prática de um motor de busca de padrões textuais baseado em Autômatos Finitos.

Este projeto foi desenvolvido como parte da disciplina de **Linguagens Formais e Autômatos** no **Instituto Federal Catarinense (Campus Blumenau)**. O objetivo principal é desmistificar conceitos abstratos (como Teorema de Kleene e Algoritmo de Thompson) criando uma ferramenta funcional inspirada no utilitário UNIX `grep`.

---

## 🚀 Sobre o Projeto

Muitas vezes, a teoria dos autômatos é vista apenas como diagramas matemáticos. Este software prova o contrário: ele traduz definições algébricas (Expressões Regulares) em máquinas de estados eficientes capazes de processar arquivos de texto reais.

**Destaque:** Este projeto é puramente educacional e **não utiliza bibliotecas de regex prontas** (como `re` do Python) para a lógica central de compilação. Toda a engine foi construída do zero.

## ⚙️ O Pipeline de Processamento

O sistema funciona como um compilador dividido em 4 etapas cruciais:

1.  **Pré-processamento:** Tradução de "açúcar sintático" (como classes de caracteres `[a-z]`) para operações primitivas.
2.  **Parser:** Conversão da Regex para notação **Pós-fixa** (Polonesa Reversa) para facilitar a leitura pela máquina.
3.  **Compilação (Thompson):** Geração de um Autômato Finito Não Determinístico (AFN).
4.  **Otimização (Subconjuntos):** Determinização para um Autômato Finito Determinístico (AFD), garantindo busca com complexidade linear **O(n)**.

## 🛠️ Funcionalidades e Operadores

O motor de busca suporta os operadores clássicos da teoria de Linguagens Regulares e algumas facilidades modernas.

### Tabela de Operadores

| Operador | Símbolo | Exemplo | Descrição |
| :--- | :---: | :--- | :--- |
| **Concatenação** | `.` (implícito) | `ab` | Encontra 'a' seguido imediatamente de 'b'. |
| **União (Ou)** | `\|` | `a\|b` | Encontra 'a' **ou** 'b'. |
| **Fecho de Kleene** | `*` | `a*` | Encontra zero ou mais repetições de 'a'. |
| **Agrupamento** | `( )` | `(ab)*` | Define prioridade e escopo para os operadores. |
| **Curinga** | `.` | `a.c` | O ponto representa qualquer caractere válido. |
| **Classes** | `[ ]` | `[0-9]` | Atalho para união de intervalos (ex: `0\|1\|...\|9`). |

*Funcionalidade Extra:* O sistema possui opção de exportar os resultados da análise.

## 📂 Estrutura do Projeto

O código foi arquitetado de forma modular para facilitar o entendimento de cada etapa teórica:

* `main.py`: Ponto de entrada (Menu interativo).
* `meu_grep.py`: Interface de busca e leitura de arquivos.
* `pre_processador.py`: Expande classes de caracteres (ex: `[a-c]` → `(a|b|c)`).
* `construtor_thompson.py`: Implementa o algoritmo de Thompson (Regex → AFN).
* `AFD_para_AFN.py`: Implementa a Construção de Subconjuntos (AFN → AFD).
* `automato.py`: Definição das classes e estrutura de dados dos autômatos (Estados, Transições).

## ⚡ Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Passo a Passo

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/seu-usuario/seu-repo.git](https://github.com/seu-usuario/seu-repo.git)
    cd seu-repo
    ```

2.  Execute o arquivo principal:
    ```bash
    python main.py
    ```

3.  No menu interativo, escolha a **Opção 1** para iniciar o buscador.

## 🧪 Exemplos de Uso (Inputs)

Crie um arquivo de texto simples (ex: `texto.txt`) para servir de alvo e teste os seguintes padrões:

### 1. Busca Simples
*Procura uma palavra exata.*
* **Regex:** `computador`
* **Resultado:** Encontra todas as linhas contendo "computador".

### 2. Alternância (União)
*Procura por uma coisa ou outra.*
* **Regex:** `carro|moto`
* **Resultado:** Encontra linhas que tenham "carro" ou "moto".

### 3. Repetição (Kleene Star)
*Procura padrões repetitivos.*
* **Regex:** `a*b`
* **Resultado:** Encontra 'b', 'ab', 'aab', 'aaaaab'...

### 4. Classes de Caracteres
*Procura números ou letras específicas.*
* **Regex:** `[a-z][0-9]`
* **O que acontece:** O sistema traduz internamente para `(a|b|...|z).(0|1|...|9)`.
* **Match:** "a1", "b9", "z0".

### 5. Expressões Complexas
*Combinando operadores.*
* **Regex:** `(a|b)*c[0-9]`
* **Explicação:** Uma sequência de 'a's e 'b's, seguida de um 'c', seguido de um número.
* **Match:** `abac1`, `bbc9`, `c0`.

## 📚 Fundamentação Teórica

Este projeto serve como prova empírica do **Teorema de Kleene**, demonstrando a equivalência computacional entre a definição algébrica (Expressão Regular) e a máquina de estados (Autômato Finito).

O desempenho da busca no texto é **Linear O(n)**, onde *n* é o tamanho do texto. Isso significa que, independentemente da complexidade da Regex inicial, o autômato determinístico processa o texto na velocidade máxima de leitura, sem retrocesso (*backtracking*).

## 👥 Autores

* **Gabriel Rodrigues Gonçalves** - *Desenvolvimento e Implementação*
* **Eder Augusto Penharbel** - *Orientação e Revisão*

---
*Projeto acadêmico - IFC Campus Blumenau*
