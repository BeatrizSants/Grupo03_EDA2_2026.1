from src.service.recommender import recommend

def main():

    print("=" * 50)
    print(" Sistema de Recomendação de Receitas")
    print("=" * 50)
    print("\n=== Usuário ===")
    nome = input("Nome: ")
    descricao = input("Descrição das restrições alimentares: ")
    input("\nPressione Enter para gerar recomendações...")

    recomendacoes = recommend(user_name=nome, user_description=descricao, top_n=5)

    print("\n=== Top 5 Recomendações ===\n")

    for receita in recomendacoes:
        print(f"ID: {receita['id']}")
        print(f"Título: {receita['titulo']}")

        print("\nIngredientes:")
        for ingrediente in receita["ingredientes"]:
            print(f"- {ingrediente}")

        print("\nModo de preparo:")
        for passo in receita["modo_preparo"]:
            print(passo)

        print("\n" + "-" * 50)

if __name__ == "__main__":
    main()