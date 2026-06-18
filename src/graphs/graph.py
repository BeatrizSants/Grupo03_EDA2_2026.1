import json
import os

class BipartiteGraph:
    def __init__(self):
        self.adj = {}
        self.users = {}
        self.recipes = {}

    def add_node(self, node_id, data=None):
        if node_id not in self.adj:
            self.adj[node_id] = {}
        
        if node_id.startswith("U_"):
            self.users[node_id] = data or {}
        elif node_id.startswith("R_"):
            self.recipes[node_id] = data or {}

    def add_edge(self, u_id, r_id, weight):
        if u_id not in self.adj:
            self.add_node(u_id)
        if r_id not in self.adj:
            self.add_node(r_id)
            
        self.adj[u_id][r_id] = weight
        self.adj[r_id][u_id] = weight

    def get_neighbors(self, node_id):
        return self.adj.get(node_id, {})

    def load_from_json(self, users_filepath, recipes_filepath):
        with open(recipes_filepath, 'r', encoding='utf-8') as f:
            receitas_data = json.load(f)
            
        for r_id, data in receitas_data.items():
            node_r = f"R_{r_id}"
            self.add_node(node_r, data)
            
        with open(users_filepath, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
            
        for u_id, data in users_data.items():
            node_u = f"U_{u_id}"
            
            interacoes = data.pop("interacoes", {})
            self.add_node(node_u, data)
            
            for r_id, int_data in interacoes.items():
                node_r = f"R_{r_id}"
                peso = int_data.get("peso_interacao", 1)
                self.add_edge(node_u, node_r, peso)

    def print_stats(self):
        print("=== Estatísticas do Grafo Bipartido ===")
        print(f"Total de Usuários: {len(self.users)}")
        print(f"Total de Receitas: {len(self.recipes)}")
        
        num_edges = sum(len(neighbors) for neighbors in self.adj.values()) // 2
        print(f"Total de Interações (Arestas): {num_edges}")
        print("=======================================")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    USER_PATH = os.path.join(BASE_DIR, "data", "user.json")
    RECEITAS_PATH = os.path.join(BASE_DIR, "data", "receitas.json")
    
    graph = BipartiteGraph()
    graph.load_from_json(USER_PATH, RECEITAS_PATH)
    graph.print_stats()