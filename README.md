# 🚀 Projeto Compilador Haskell

Este projeto consiste na implementação de um **compilador simples** inspirado na linguagem **Haskell**, desenvolvido como parte de estudos de **compiladores e linguagens formais**.  
O objetivo é criar um compilador que reconheça e traduza programas escritos em uma linguagem simplificada, contendo **tipos primitivos, estruturas de controle, entrada/saída e expressões**.
O projeto possui "licenças poéticas", como o while que não é nativo em **Haskell**, reforçando que é um **projeto para faculdade** e que isto foi autorizado pelo professor da matéria.
Foi implementado a analise semantica de tipos de variáveis e se a variável foi declarada ou não, para registrar tipos e tipagem correta de operadores.
Foi utilizado para geração de código, C ao invés de Assembly, para fins práticos e por causa do tempo curto para implementação.


---

## 📌 Funcionalidades da Linguagem

### 🔹 Tipos de dados
- **int** → números inteiros  
- **double** → números reais 

---

### 🔹 Entrada e saída
- `scan()` → comando para leitura de dados do usuário  
- `print()` → comando para impressão na saída padrão  

---

### 🔹 Controle de fluxo
- **Condicional**  
  ```haskell
  if(condição){
      // bloco verdadeiro
  } else{
      // bloco falso
  }
- **Repetição**
```haskell
 while(condição){
       // bloco executado enquanto a condição for verdadeira
 }
```
## Configuração do Ambiente
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```
## Instalação das Dependências
```bash
# Instalar runtime do ANTLR para Python
pip install antlr4-python3-runtime

```
## Execução do Compilador
```bash
# Gerar arquivos semanticos baseados em nossa pseudolinguagem
java -jar ./antlr-4.13.1-complete.jar -Dlanguage=Python3 Haskell.g4

# Executar o compilador
python.exe main.py .\Exercicio1e2.hs

# Para executar o arquivo C
gcc *.c -o main.exe
./main.exe
```
## 👥 Desenvolvimento

- **Disciplina**: Compiladores
- **Instituição**: IFMT - Campus Octayde Jorge - 2025/2
- **Desenvolvedores**:
  - [Gabriel Foloni](https://github.com/Fologne)
  - [Danilo Vinicius](https://github.com/danilovinicius51)
