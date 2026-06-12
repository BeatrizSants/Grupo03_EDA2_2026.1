# Sistema de Recomendação de Receitas para Restrições Alimentares

## 📋 Propósito
Este projeto foi desenvolvido como requisito prático para a disciplina de **Estrutura de Dados 2**. O sistema consiste em uma ferramenta de recomendação de textos (receitas) baseada em **Grafos Bipartidos** e algoritmos de busca e ordenação em grafos. A aplicação conecta usuários com necessidades dietéticas semelhantes e sugere opções seguras e relevantes com base no histórico de interações da comunidade.

## 🎯 Objetivo e Problema Solucionado
* **Problema:** Pessoas com restrições alimentares (alergias, intolerâncias, dietas específicas) enfrentam dificuldades para filtrar e encontrar receitas seguras, saborosas e personalizadas em bases de dados genéricas.
* **Solução:** O sistema resolve esse problema mapeando o comportamento de usuários com perfis dietéticos similares. Através do processamento de linguagem natural (PLN) das descrições das restrições e da análise de um grafo de interações (usuário-receita), a aplicação identifica quais receitas performaram melhor entre pessoas com a mesma condição e as recomenda prioritariamente.

## 🏗️ Arquitetura de Software Sugerida
Para garantir que o projeto seja simples de rodar no terminal, mas mantenha uma estrutura organizada, escalável e de fácil manutenção, adota-se uma **Arquitetura em Camadas (Layered Architecture)**. Esta abordagem separa claramente a persistência de dados, o processamento de texto, as estruturas de dados e a interface com o usuário.

### Estrutura de Diretórios
```text
📂 src/
├── 📂 data/             # Camada de Persistência (Banco de Dados JSON)
│   ├── usuarios.json    # Dados fictícios de perfis e descrições de restrições
│   └── receitas.json    # Dados reais de receitas cadastradas (textos)
│
├── 📂 nlp/              # Processamento de Linguagem Natural
│   └── similarity.py    # Análise de similaridade textual das restrições
│
├── 📂 graphs/           # Estrutura de Dados e Algoritmos (Core do projeto)
│   ├── graph.py         # Modelagem do Grafo Bipartido e Projeções
│   └── search.py        # Implementação do BFS customizado para caminhos e pesos
│
├── 📂 service/          # Camada de Negócio / Motor de Recomendação
│   └── recommender.py   # Orquestrador que gera e filtra as sugestões por usuário
│
└── main.py              # Ponto de entrada da aplicação (Interface CLI no Terminal)
```
### Funcionamento dos Grafos e Algoritmos:
1. **Grafo Bipartido (Usuário-Receita):** Conecta `Vértices(Usuário)` a `Vértices(Receita)`. As arestas possuem pesos baseados no tipo de interação (ex: leitura = 1, salvou = 2, avaliou positivamente = 3).
2. **Projeção / Grafo de Similaridade:** O módulo de PLN analisa as descrições de restrições e conecta usuários similares.
3. **Recomendação com BFS (Busca em Largura):** A partir de um usuário alvo, o algoritmo explora a vizinhança no grafo para encontrar usuários com restrições idênticas e, em seguida, utiliza uma fila (`queue`) para rastrear e ordenar as receitas mais próximas e de maior peso consumidas por esse grupo.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Banco de Dados:** Arquivos estruturados em formato `JSON`
* **Biblioteca de PLN (Sugestão):** `Spacy` ou `Scikit-learn` (TF-IDF / Cosine Similarity) para análise das restrições textuais.
* **Interface:** Prompt de Comando / Terminal (CLI)

## 👥 Equipe
* **Beatriz Figueiredo dos Santos** - *Desenvolvedora Principal*