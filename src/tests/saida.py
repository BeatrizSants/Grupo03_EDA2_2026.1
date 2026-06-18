#Teste de saída para verificar a relação usuário-receita.
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

USER_PATH = os.path.join(BASE_DIR, "data", "user.json")
RECEITAS_PATH = os.path.join(BASE_DIR, "data", "receitas.json")


def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as file:
        return json.load(file)

def buscar_receitas_todos_usuarios():
    usuarios = carregar_json(USER_PATH)
    receitas = carregar_json(RECEITAS_PATH)

    print("\n=== BUSCA DE RECEITAS POR INTERAÇÃO ===")

    #Percorre todos os usuários
    for usuario_id, usuario in usuarios.items():

        print("\n======================================")
        print(f"Usuário ID: {usuario_id}")
        print(f"Nome: {usuario['nome']}")
        print(f"Descrição: {usuario['descricao']}")
        interacoes = usuario.get("interacoes", {})
        if not interacoes:
            print("Sem interações.")
            continue
        print("\nReceitas relacionadas:")

        for receita_id in interacoes:
            receita = receitas.get(str(receita_id))
            if receita:
                print("\n---------------------------")
                print(f"ID Receita: {receita_id}")
                print(f"Título: {receita.get('titulo')}")

                if "ingredientes" in receita:
                    print("\nIngredientes:")
                    ingredientes = receita["ingredientes"].split(";")
                    for ingrediente in ingredientes:
                        print(f" - {ingrediente.strip()}")

                if "modo_preparo" in receita:
                    print("\nModo de preparo:")
                    print(receita["modo_preparo"])

            else:
                print(f"Receita {receita_id} não encontrada.")


if __name__ == "__main__":
    buscar_receitas_todos_usuarios()