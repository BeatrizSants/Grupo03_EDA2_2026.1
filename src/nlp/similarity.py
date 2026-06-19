import json
import spacy


class SimilarityGraph:
    def __init__(self):
        self.pln = spacy.load("pt_core_news_md")
        self.users = {}
        self.users_spacy = {}


    def load_users(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            users = json.load(f)

        for u_id, data in users.items():
            node_user = f"U_{u_id}"
            self.users[node_user] = data

            descricao = data.get("descricao", "")
            self.users_spacy[node_user] = self.pln(descricao.lower())


    def add_temp_user(self, temp_id, user_data):
        self.users[temp_id] = user_data

        descricao = user_data.get("descricao", "")
        self.users_spacy[temp_id] = self.pln(descricao.lower()) 