import json
import os
import networkx as nx
import matplotlib.pyplot as plt

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
    
    # Seleciona uma amostra de 5 usuários para que os números dos pesos fiquem legíveis
    usuarios_amostra = list(users_data.keys())[:5]
    
    for u_id in usuarios_amostra:
        u_node = f"U_{u_id}"
        # Guarda o nome do usuário como label
        G.add_node(u_node, bipartite=0, label=users_data[u_id]["nome"].split()[0])
        
        interacoes = users_data[u_id].get("interacoes", {})
        for r_id, info in interacoes.items():
            r_node = f"R_{r_id}"
            
            if r_id in receitas_data:
                # Guarda o título simplificado da receita como label
                nome_receita = receitas_data[r_id].get("titulo") or receitas_data[r_id].get("nome") or f"Rec {r_id}"
                G.add_node(r_node, bipartite=1, label=nome_receita[:12] + "...")
                
                # Obtém o peso numérico da interação
                peso = info.get("peso_interacao", 1)
                G.add_edge(u_node, r_node, weight=peso)

    # 3. Organiza o Layout Bipartido (Duas Colunas)
    top_nodes = [n for n, d in G.nodes(data=True) if d.get('bipartite') == 0]
    pos = nx.bipartite_layout(G, top_nodes)
    
    # Mapeia as espessuras com base nos pesos
    edges = G.edges(data=True)
    widths = [edge[2]['weight'] * 1.0 for edge in edges]
    
    # Cria os dicionários de labels para os nós e para os pesos das arestas
    node_labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # 4. Configura a Janela Gráfica (OPÇÃO 1: AMOSTRA CONTROLADA COM PESOS)
    plt.figure(figsize=(12, 8))
    plt.title("Amostra do Grafo Bipartido com Pesos Numéricos das Arestas", fontsize=14, fontweight='bold')
    
    # Desenha os nós dos Usuários (Azul)
    nx.draw_networkx_nodes(G, pos, nodelist=top_nodes, node_color="skyblue", node_size=700, edgecolors="black")
    
    # Desenha os nós das Receitas (Laranja)
    bottom_nodes = [n for n in G.nodes() if n not in top_nodes]
    nx.draw_networkx_nodes(G, pos, nodelist=bottom_nodes, node_color="orange", node_size=600, edgecolors="black")
    
    # Desenha as linhas com espessura proporcional ao peso
    nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color="gray", width=widths)
    
    # Desenha os nomes nos nós
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9, font_weight="bold")
    
    # Desenha os números dos pesos nas linhas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color="darkred", font_weight="bold")

    
    # =========================================================================
    # 🚨 GRAFO COMPLETO (100 usuários e 300+ receitas)
    # Para testar, DESCOMENTE o bloco abaixo (remova as #) e COMENTE o bloco da Opção 1 acima (Linha 55 até 73).
    # =========================================================================
    """
    # 1. Recarrega a base sem limites para o grafo completo
    G_completo = nx.Graph()
    for u_id, info_u in users_data.items():
        u_node = f"U_{u_id}"
        G_completo.add_node(u_node, bipartite=0)
        for r_id, info_r in info_u.get("interacoes", {}).items():
            if r_id in receitas_data:
                r_node = f"R_{r_id}"
                G_completo.add_node(r_node, bipartite=1)
                G_completo.add_edge(u_node, r_node, weight=info_r.get("peso_interacao", 1))
                
    top_nodes_c = [n for n, d in G_completo.nodes(data=True) if d.get('bipartite') == 0]
    pos_c = nx.bipartite_layout(G_completo, top_nodes_c)
    widths_c = [edge[2]['weight'] * 0.3 for edge in G_completo.edges(data=True)]
    
    plt.figure(figsize=(16, 10))
    plt.title("Grafo Bipartido COMPLETO (Base de Dados Total)\nEspessura representa o Peso da Interação", fontsize=14, fontweight='bold')
    
    nx.draw_networkx_nodes(G_completo, pos_c, nodelist=top_nodes_c, node_color="skyblue", node_size=60, alpha=0.7)
    bottom_nodes_c = [n for n in G_completo.nodes() if n not in top_nodes_c]
    nx.draw_networkx_nodes(G_completo, pos_c, nodelist=bottom_nodes_c, node_color="orange", node_size=50, alpha=0.7)
    nx.draw_networkx_edges(G_completo, pos_c, alpha=0.2, edge_color="gray", width=widths_c)
    # Omitimos os textos aqui para o gráfico não virar um borrão preto ilegível
    
    # =========================================================================
    """
    plt.axis("off")
    plt.tight_layout()
    
    print("A renderizar o gráfico do sistema... Aguarde a janela se abrir!")
    plt.show()

if __name__ == "__main__":
    plot_bipartite_graph()