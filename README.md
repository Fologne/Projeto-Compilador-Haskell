# 🚀 Projeto Compilador Haskell

Este projeto consiste na implementação de um **compilador simples** inspirado na linguagem **Haskell**, desenvolvido como parte de estudos de **compiladores e linguagens formais**.  
O objetivo é criar um compilador que reconheça e traduza programas escritos em uma linguagem simplificada, contendo **tipos primitivos, estruturas de controle, entrada/saída e expressões**.

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
 do{
      // bloco executado ao menos uma vez
 } while(condição)