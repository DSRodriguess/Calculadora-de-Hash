
# 🔐 Calculadora de Hash

Este projeto é uma calculadora de hash desenvolvida em Python, que permite aos usuários inserir um texto ou selecionar um arquivo `.txt` como entrada.
A aplicação aplica funções hash e retorna uma string alfanumérica de valor fixo único, representando a entrada fornecida.
A ferramenta suporta algoritmos recomendados pelo NIST (National Institute of Standards and Technology) das famílias SHA-2 e SHA-3.

## ⚙️ Funcionalidades

- **Entrada de Dados**:
  - Inserção direta de texto pela interface.
  - Seleção de arquivos `.txt` para cálculo do hash.

- **Algoritmos de Hash Suportados**:
  - SHA-2: `SHA-224`, `SHA-256`, `SHA-384`, `SHA-512`
  - SHA-3: `SHA3-224`, `SHA3-256`, `SHA3-384`, `SHA3-512`

- **Saída**:
  - Exibição da string hash resultante correspondente à entrada fornecida.

## 🧱 Estrutura do Projeto

O projeto possui a seguinte estrutura:

```
Calculadora-de-Hash/
├── Calculadora_de_Hash.py   # Script principal da aplicação
└── README.md                # Documentação do projeto
```

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- Módulo `hashlib` para cálculos de hash
- Interface gráfica (se aplicável, por exemplo, `Tkinter`)

## 🚀 Como Executar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/DSRodriguess/Calculadora-de-Hash.git
   cd Calculadora-de-Hash
   ```

2. **Execute o script**:

   ```bash
   python Calculadora_de_Hash.py
   ```

   Certifique-se de ter o Python 3 instalado em seu sistema.

## 📄 Licença

Este projeto é de uso acadêmico e não possui uma licença específica definida.

## 👨‍💻 Autor

- [DSRodriguess](https://github.com/DSRodriguess)
