# Sistema de Recomendação de Receitas para Restrições Alimentares

## 📋 Propósito
Este projeto foi desenvolvido como requisito prático para a disciplina de **Estrutura de Dados 2**. O sistema consiste em uma ferramenta de recomendação de textos (receitas) baseada em **Grafos Bipartidos** e algoritmos de busca e ordenação em grafos. A aplicação conecta usuários com restrições alimentares semelhantes e sugere opções seguras e relevantes com base no histórico de interações da comunidade.

## 🎯 Objetivo e Problema Solucionado
* **Problema:** Pessoas com restrições alimentares (alergias, intolerâncias, dietas específicas) enfrentam dificuldades para filtrar e encontrar receitas seguras, saborosas e personalizadas em bases de dados genéricas.
* **Solução:** O sistema resolve esse problema mapeando o comportamento de usuários com perfis dietéticos similares. Através do processamento de linguagem natural (PLN) das descrições das restrições e da análise de um grafo de interações (usuário-receita), a aplicação identifica quais receitas performaram melhor entre pessoas com a mesma condição e as recomenda prioritariamente.

## 🏗️ Arquitetura de Software
**Padrão:** Arquitetura em Camadas
### Estrutura de Diretórios
```text
📂 Grupo03_EDA2_2026.1/
├── main.py                  # Ponto de entrada do sistema (terminal)
├── plot_graph.py            # Visualização do grafo bipartido
├── requirements.txt
│
└── 📂 src/
    ├── 📂 data/             # Camada de Persistência
    │   ├── user.json
    │   └── receitas.json
    │
    ├── 📂 nlp/              # Processamento de Linguagem Natural
    │   └── similarity.py
    │
    ├── 📂 graphs/           # Estrutura de Dados e Algoritmos
    │   ├── graph.py
    │   └── search.py
    │
    ├── 📂 utils/            # Estrutura de Dados Auxiliar
    │   └── max_heap.py
    │
    ├── 📂 service/          # Camada de Negócio / Motor de Recomendação
    │   └── recommender.py
    │
    └── 📂 tests/            # Scripts de validação dos dados
        └── saida.py
```

### Funcionamento dos Grafos e Algoritmos:
1. **Grafo Bipartido (Usuário-Receita):** Conecta `Vértices(Usuário)` a `Vértices(Receita)`. As arestas possuem pesos baseados no tipo de interação.
2. **Projeção / Grafo de Similaridade:** O módulo de PLN analisa as descrições de restrições e conecta usuários similares.
3. **Recomendação com BFS (Busca em Largura):** A partir de um usuário alvo, o algoritmo explora a vizinhança no grafo para encontrar usuários com restrições idênticas e, em seguida, utiliza uma fila comum para o rastreamento e uma **Fila de Prioridade (Heap de Máximo)** para ordenar e extrair as receitas mais próximas e de maior peso consumidas por esse grupo.

## 🗄️ Modelagem dos Dados

### Usuários (`src/data/user.json`)
Cada usuário possui um ID numérico único e os campos abaixo. O campo `interacoes` mapeia os IDs das receitas com que ele interagiu e o respectivo peso dessa interação:

```json
"1": {
  "nome": "Ana Clara",
  "descricao": "Vegetariana há 2 anos, gosta de receitas saudáveis...",
  "interacoes": {
    "103": { "peso_interacao": 5 },
    "120": { "peso_interacao": 3 }
  }
}
```

**Escala de pesos de interação:**
| Peso | Significado |
|------|-------------|
| `1`  | Visualizou / Abriu a receita |
| `3`  | Curtiu / Salvou a receita |
| `5`  | Testou e avaliou positivamente |

### Receitas (`src/data/receitas.json`)
Cada receita possui um ID numérico único e os campos abaixo. Os IDs são organizados em faixas por restrição alimentar:

```json
"103": {
  "titulo": "Patê vegano: homus",
  "ingredientes": "2 xícaras de grão-de-bico cozido; ...",
  "modo_preparo": "Bata todos os ingredientes no liquidificador..."
}
```

**Faixas de IDs por restrição alimentar:**
| Faixa de IDs | Restrição |
|---|---|
| `101 – 150` | Vegano / Vegetariano |
| `200 – 234` | Sem Glúten |
| `300 – 329` | Sem Lactose |
| `400 – 449` | Alergia a Ovo |
| `500 – 539` | Alergia a Frutos do Mar |

## 🚀 Como Usar o Sistema

### 1. Pré-requisitos
* Python 3.10 ou superior

### 2. Instalar dependências
Na raiz do projeto, execute:
```bash
pip install -r requirements.txt
```

### 3. Executar o sistema
```bash
python main.py
```

### 4. Exemplo de uso no terminal
```
==================================================
 Sistema de Recomendação de Receitas
==================================================
1. Buscar Recomendações Personalizadas
2. Visualizar Grafo da Base de Dados
3. Sair do Sistema
==================================================
Escolha uma opção (1-3): 1

=== Novo Usuário ===
Nome: João Silva
Descrição das restrições alimentares: Sou intolerante a lactose e prefiro pratos doces

Pressione Enter para gerar recomendações...

=== Top 5 Recomendações ===

ID: 321
Título: Molho Branco Sem Lactose

Ingredientes:
- 2 colheres de azeite
- 2 colheres de farinha de arroz
- 500ml de leite de castanhas
- sal e noz-moscada

Modo de preparo:
Doure a farinha no azeite, adicione o leite de castanhas aos poucos mexendo sempre até engrossar.

--------------------------------------------------
...
```

> **Nota:** Se a descrição for deixada em branco, o sistema sugere automaticamente as receitas com maior engajamento geral da comunidade. A opção **2** abre uma janela gráfica com o grafo bipartido visualizado.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Banco de Dados:** Arquivos estruturados em formato `JSON`
* **Biblioteca de PLN:** `spaCy` com modelo `pt_core_news_md`
* **Visualização do Grafo:** `networkx` e `matplotlib` (exclusivamente para plotagem — a lógica de recomendação é implementação própria)

## 👥 Equipe
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/BeatrizSants">
        <img src="https://github.com/BeatrizSants.png" width="100px;" alt="Foto Beatriz Figueiredo"/><br />
        <sub><b>Beatriz Figueiredo</b></sub>
      </a><br />
    </td>
    <td align="center">
      <a href="https://github.com/brunnoff">
        <img src="https://github.com/brunnoff.png" width="100px;" alt="Foto Integrante 2"/><br />
        <sub><b>Brunno Fernandes</b></sub>
      </a><br />
    </td>
    <td align="center">
      <a href="https://github.com/JosefWojtyla">
        <img src="https://github.com/JosefWojtyla.png" width="100px;" alt="Foto Integrante 3"/><br />
        <sub><b>Josef Wojtyla</b></sub>
      </a><br />
    </td>
    <td align="center">
      <a href="https://github.com/nbg-cordeiro">
        <img src="https://github.com/nbg-cordeiro.png" width="100px;" alt="Foto Integrante 4"/><br />
        <sub><b>João N.S. Cordeiro</b></sub>
      </a><br />
    </td>
    <td align="center">
      <a href="https://github.com/radamesGuerra">
        <img src="https://github.com/radamesGuerra.png" width="100px;" alt="Foto Integrante 5"/><br />
        <sub><b>Rafaela Guerra</b></sub>
      </a><br />
    </td>
  </tr>
</table>