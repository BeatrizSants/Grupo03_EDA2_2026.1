import json
import spacy


class SimilarityGraph:
    DOMAIN_TERMS = {
        # restrições alimentares
        "vegetariano", "vegetariana",
        "vegano", "vegana",
        "lactose", "gluten", "glúten",
        "celiaco", "celíaco",
        "alergia",

        # alergias
        "leite", "ovo", "peixe", "camarao", "camarão",
        "frutos", "mar",

        # categorias
        "doce", "doces",
        "sobremesa", "sobremesas",
        "confeitaria",
        "bolo", "bolos",
        "salgado", "salgados",
        "saudavel", "saudável",

        # ingredientes
        "tofu", "soja", "aveia",
        "grao", "grão",
        "bico",
        "coco"
    }
    def __init__(self):
        self.__pln = spacy.load("pt_core_news_md")
        self.__users = {}
        self.__users_spacy = {}

    def _process(self, descricao):
        doc = self.__pln(descricao.lower())
 
        tokens_relevantes = [
            token.text
            for token in doc
            if not token.is_stop
            and not token.is_punct
            and token.lemma_ in self.DOMAIN_TERMS
        ]
 
        if not tokens_relevantes:
            return doc
        texto_filtrado = " ".join(tokens_relevantes)
        return self.__pln(texto_filtrado)

    def load_users(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            users = json.load(f)

        for u_id, data in users.items():
            node_user = f"U_{u_id}"
            self.__users[node_user] = data

            descricao = data.get("descricao", "")
            self.__users_spacy[node_user] = self._process(descricao)


    def add_temp_user(self, temp_id, user_data):
        self.__users[temp_id] = user_data

        descricao = user_data.get("descricao", "")
        self.__users_spacy[temp_id] = self._process(descricao)

       
    def find_similar_users(self, target_id, top_n=3):

        target_spacy = self.__users_spacy[target_id]
        similarities = []

        for u_id, description in self.__users_spacy.items():
            if u_id != target_id:
                if description.vector_norm and target_spacy.vector_norm:
                    score = target_spacy.similarity(description)
                else:
                    score = 0.0
                
                similarities.append((u_id, score))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_n]