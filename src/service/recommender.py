import os
from graphs.graph import BipartiteGraph
from graphs.search import BFSSearcher
from nlp.similarity import SimilarityGraph
from utils.max_heap import MaxHeap

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
USER_PATH = os.path.join(BASE_DIR, "data", "user.json")
RECEITAS_PATH = os.path.join(BASE_DIR, "data", "receitas.json")

def recommend(user_name, user_description, top_n=5):

    graph = BipartiteGraph()
    graph.load_from_json(USER_PATH, RECEITAS_PATH)

    similarity_graph = SimilarityGraph()
    similarity_graph.load_users(USER_PATH)

    temp_id = "U_TEMP"

    similarity_graph.add_temp_user(temp_id, {"nome": user_name, "descricao": user_description})
    similar_users = similarity_graph.find_similar_users(temp_id, top_n=3)

    bfs = BFSSearcher(graph)

    global_heap = MaxHeap()
    
    recipe_scores = {}

    for user_id, similarity_score in similar_users:

        user_number = user_id.replace("U_", "")

        recommendations = bfs.recommend_for_user(
            user_number,
            top_n
        )

        for score, recipe_id, recipe_data in recommendations:

            weighted_score = score * similarity_score

            if recipe_id not in recipe_scores:
                recipe_scores[recipe_id] = {
                    "score": 0,
                    "data": recipe_data
                }

            recipe_scores[recipe_id]["score"] += weighted_score

    for recipe_id, info in recipe_scores.items():

        global_heap.push(
            info["score"],
            recipe_id,
            info["data"]
        )
    final_recipes = []

    while len(final_recipes) < top_n:

        item = global_heap.pop()

        if item is None:
            break

        score, recipe_id, recipe_data = item

        final_recipes.append({
            "id": recipe_id.replace("R_", ""),
            "titulo": recipe_data["titulo"],
            "ingredientes": recipe_data["ingredientes"],
            "modo_preparo": recipe_data["modo_preparo"]
        })

    return final_recipes
    