inventario = []

while True:
    escolha = input(
        "\n[1] - Adicionar item\n"
        "[2] - Remover item\n"
        "[3] - Ver inventário\n"
        "[4] - Buscar item\n"
        "[5] - Sair\n"
        "Escolha: "
    )

    if escolha == "1":
        item = input("Digite o nome do item: ").lower().strip()

        while item == "":
            print("Nome inválido!")
            item = input("Digite o nome do item: ").lower().strip()

        inventario.append(item)
        print("Item cadastrado com sucesso!")

    elif escolha == "2":
        remover = input("Digite o nome do item: ").lower().strip()

        while remover == "":
            print("Nome inválido!")
            remover = input("Digite o nome do item: ").lower().strip()

        if remover in inventario:
            inventario.remove(remover)
            print("Item removido com sucesso!")
        else:
            print("Item não encontrado!")

    elif escolha == "3":
        if not inventario:
            print("Inventário vazio!")
        else:
            print("\n=== INVENTÁRIO ===")

            for item in inventario:
                print(f"- {item}")

    elif escolha == "4":
        busca = input("Buscar qual item: ").lower().strip()

        while busca == "":
            print("Nome inválido!")
            busca = input("Buscar qual item: ").lower().strip()

        if busca in inventario:
            print("Item encontrado no inventário!")
        else:
            print("Item não encontrado!")

    elif escolha == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")
