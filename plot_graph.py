import json
import os
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def plot_bipartite_graph():
    # Caminhos dos arquivos JSON oficiais do grupo
    user_path = os.path.join("src", "data", "user.json")
    receita_path = os.path.join("src", "data", "receitas.json")
    
    # Inicializa o grafo do NetworkX
    G = nx.Graph()
    
    # 1. Carrega os Usuários
    with open(user_path, "r", encoding="utf-8") as f:
        users_data = json.load(f)
        
    # 2. Carrega as Receitas
    with open(receita_path, "r", encoding="utf-8") as f:
        receitas_data = json.load(f)
    
    # Seleciona a amostra de 5 usuários
    usuarios_amostra = list(users_data.keys())[:5]
    
    for u_id in usuarios_amostra:
        u_node = f"U_{u_id}"
        # Salva o ID curto (ex: 1) e o nome do usuário
        G.add_node(u_node, bipartite=0, id_curto=u_id, label=users_data[u_id]["nome"].split()[0])
        
        interacoes = users_data[u_id].get("interacoes", {})
        for r_id, info in interacoes.items():
            r_node = f"R_{r_id}"
            
            if r_id in receitas_data:
                nome_receita = receitas_data[r_id].get("titulo") or receitas_data[r_id].get("nome") or f"Rec {r_id}"
                # Salva o ID curto da receita (ex: 14) e o título completo
                G.add_node(r_node, bipartite=1, id_curto=r_id, label=nome_receita)
                
                peso = info.get("peso_interacao", 1)
                G.add_edge(u_node, r_node, weight=peso)

   # 3. Organiza o Layout Bipartido (Duas Colunas)
    top_nodes = [n for n, d in G.nodes(data=True) if d.get('bipartite') == 0]
    pos_original = nx.bipartite_layout(G, top_nodes)
    
    # AJUSTE CUSTOMIZADO DE DISTÂNCIA (Estilo o layout do Brunno)
    pos = {}
    for node, (x, y) in pos_original.items():
        if node in top_nodes:
            # Coluna dos Usuários: 
            # Empurramos o x um pouco para a direita (aproximando das receitas)
            # E multiplicamos o y por 0.6 para espremer verticalmente e deixá-los mais próximos
            pos[node] = (-0.6, y * 0.6)
        else:
            # Coluna das Receitas:
            # Empurramos o x um pouco para a esquerda (aproximando dos usuários)
            # O y das receitas deixamos normal (1.0) para que elas continuem bem distribuídas na vertical
            pos[node] = (0.3, y * 1.0)
            
    # Mapeamento de cores das arestas
    cor_por_peso = {1: "#2b5c8f", 3: "#32cd32", 5: "#ffa114"}
    edges = G.edges(data=True)
    edge_colors = [cor_por_peso.get(edge[2]['weight'], "gray") for edge in edges]
    
    # 4. Configura a Janela Gráfica
    plt.figure(figsize=(14, 8))
    plt.title("Amostra do Grafo Bipartido com Pesos das Arestas e IDs dos Vértices", fontsize=16, fontweight='bold', pad=20)
    
    # Desenha os nós dos Usuários
    nx.draw_networkx_nodes(G, pos, nodelist=top_nodes, node_color="orchid", node_size=900, edgecolors="gray", linewidths=1.5)
    
    # Desenha os nós das Receitas
    bottom_nodes = [n for n in G.nodes() if n not in top_nodes]
    nx.draw_networkx_nodes(G, pos, nodelist=bottom_nodes, node_color="gold", node_size=700, edgecolors="gray", linewidths=1.5)
    
    # Desenha as linhas coloridas
    nx.draw_networkx_edges(G, pos, alpha=0.9, edge_color=edge_colors, width=2.0)
    
    # --- MÁGICA DOS IDS DENTRO DOS VÉRTICES ---
    # Pega o ID curto de cada nó e desenha exatamente no centro (pos) da bolinha
    labels_internos = nx.get_node_attributes(G, 'id_curto')
    nx.draw_networkx_labels(G, pos, labels=labels_internos, font_size=9, font_weight="bold", font_color="black")
    
    # --- AJUSTE DOS NOMES DO LADO FORA ---
    # Duplica as posições para empurrar o texto descritivo para as laterais externas
    pos_labels_externos = {}
    for node, (x, y) in pos.items():
        if node in top_nodes:
            pos_labels_externos[node] = (x - 0.04, y) # Afasta o nome para a esquerda
        else:
            pos_labels_externos[node] = (x + 0.03, y) # Afasta o título para a direita
            
    labels_usuarios = {n: G.nodes[n]['label'] for n in top_nodes}
    labels_receitas = {n: G.nodes[n]['label'] for n in bottom_nodes}
    
    # Desenha os nomes por fora das bolinhas
    nx.draw_networkx_labels(G, pos_labels_externos, labels=labels_usuarios, font_size=10, font_weight="bold", horizontalalignment='right')
    nx.draw_networkx_labels(G, pos_labels_externos, labels=labels_receitas, font_size=9, font_weight="bold", horizontalalignment='left')
    
    # 5. Legenda inferior
    legenda_peso1 = mlines.Line2D([], [], color='#2b5c8f', marker='s', linestyle='', markersize=10, label='Peso 1 — Visualizou')
    legenda_peso3 = mlines.Line2D([], [], color='#32cd32', marker='s', linestyle='', markersize=10, label='Peso 3 — Curtiu/Salvou')
    legenda_peso5 = mlines.Line2D([], [], color="#ffa114", marker='s', linestyle='', markersize=10, label='Peso 5 — Avaliou positivamente')
    
    plt.legend(handles=[legenda_peso1, legenda_peso3, legenda_peso5], loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=3, frameon=True, fontsize=10)
    
    plt.xlim(-1.2, 1.5)

    plt.axis("off")
    plt.tight_layout()
    
    print("Gerando o grafo com IDs internos... Verifique a janela gráfica!")
    plt.show()

if __name__ == "__main__":
    plot_bipartite_graph()