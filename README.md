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
📂 src/
├── 📂 data/             # Camada de Persistência
│   ├── user.json
│   └── receita.json
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
└── main.py
```

### Funcionamento dos Grafos e Algoritmos:
1. **Grafo Bipartido (Usuário-Receita):** Conecta `Vértices(Usuário)` a `Vértices(Receita)`. As arestas possuem pesos baseados no tipo de interação.
2. **Projeção / Grafo de Similaridade:** O módulo de PLN analisa as descrições de restrições e conecta usuários similares.
3. **Recomendação com BFS (Busca em Largura):** A partir de um usuário alvo, o algoritmo explora a vizinhança no grafo para encontrar usuários com restrições idênticas e, em seguida, utiliza uma fila comum para o rastreamento e uma **Fila de Prioridade (Heap de Máximo)** para ordenar e extrair as receitas mais próximas e de maior peso consumidas por esse grupo.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Banco de Dados:** Arquivos estruturados em formato `JSON`
* **Biblioteca de PLN:** `Spacy`

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