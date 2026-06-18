from collections import deque
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.max_heap import MaxHeap

class BFSSearcher:
    def __init__(self, graph):
        self.graph = graph

    def recommend_for_user(self, target_user_id, top_n=5):
        node_u = f"U_{target_user_id}"
        if node_u not in self.graph.adj:
            return []

        interacted_recipes = set(self.graph.get_neighbors(node_u).keys())
        
        queue = deque()
        heap = MaxHeap()
        visited = set()
        visited.add(node_u)
        
        recipe_scores = {}

        for r_id, weight in self.graph.get_neighbors(node_u).items():
            queue.append((r_id, weight, 1))
            visited.add(r_id)
            
        while queue:
            current_node, current_weight, depth = queue.popleft()
            
            if depth > 2:
                continue
                
            neighbors = self.graph.get_neighbors(current_node)
            for neighbor_node, edge_weight in neighbors.items():
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append((neighbor_node, edge_weight, depth + 1))
                    
                    if neighbor_node.startswith("R_") and neighbor_node not in interacted_recipes:
                        if neighbor_node not in recipe_scores:
                            recipe_scores[neighbor_node] = 0
                        recipe_scores[neighbor_node] += edge_weight

        for r_id, score in recipe_scores.items():
            recipe_data = self.graph.recipes.get(r_id, {})
            heap.push(score, r_id, recipe_data)

        recommendations = []
        for _ in range(top_n):
            item = heap.pop()
            if item:
                recommendations.append(item)
            else:
                break
                
        return recommendations