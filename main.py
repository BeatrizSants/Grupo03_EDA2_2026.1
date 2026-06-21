from src.service.recommender import recommend
from plot_graph import plot_bipartite_graph

def exibir_menu():
    print("\n" + "=" * 50)
    print("       Sistema de Recomendação de Receitas")
    print("=" * 50)
    print("1. Buscar Recomendações Personalizadas")
    print("2. Visualizar Grafo da Base de Dados")
    print("3. Sair do Sistema")
    print("=" * 50)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            print("\n=== Novo Usuário ===")
            nome = input("Nome: ")
            descricao = input("Descrição das restrições alimentares: ")
            input("\nPressione Enter para gerar recomendações...")

            recomendacoes = recommend(user_name=nome, user_description=descricao, top_n=5)

            print("\n=== Top 5 Recomendações ===\n")

            if not recomendacoes:
                print("Nenhuma recomendação encontrada para o perfil informado.")
            else:
                for receita in recomendacoes:
                    print(f"ID: {receita['id']}")
                    print(f"Título: {receita['titulo']}")

                    print("\nIngredientes:")
                    lista_ingredientes = [ing.strip() for ing in receita["ingredientes"].split(";") if ing.strip()]
                    for ingrediente in lista_ingredientes:
                        print(f"- {ingrediente}")

                    print("\nModo de preparo:")
                    print(receita["modo_preparo"])

                    print("\n" + "-" * 50)
                    
        elif opcao == "2":
            print("\nGerando visualização do Grafo Bipartido...")
            # Executa a sua plotagem adicionada
            plot_bipartite_graph()
            
        elif opcao == "3":
            print("\nSaindo do sistema...")
            break
            
        else:
            print("\nOpção inválida! Por favor, escolha entre 1, 2 ou 3.")

if __name__ == "__main__":
    main()