estudantes = []

while True:
    print("\nBem-vindo ao Gerenciador de Estudantes!\n")
    print("Opções")
    print("1 - Adicionar estudante")
    print("2 - Remover estudante")
    print("3 - Listar estudantes")
    print("4 - Buscar estudante por nome")
    print("5 - Buscar estudante por idade")
    print("6 - Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do estudante: ")
        idade = int(input("Digite a idade do estudante: "))
        nota = float(input("Digite a nota do estudante: "))
        estudante = {'nome': nome, 'idade': idade, 'nota': nota}
        estudantes.append(estudante)
        print(f'Estudante "{nome}" adicionado com sucesso!')

    elif opcao == 2:
        for i, estudante in enumerate(estudantes):
            print(f"{i+1} - Nome: {estudante['nome']}, Idade: {estudante['idade']}, Nota: {estudante['nota']}")
        indice = int(input("Digite o número do estudante a ser removido: ")) - 1
        if 0 <= indice < len(estudantes):
            nome = estudantes[indice]['nome']
            estudantes.pop(indice)
            print(f'Estudante "{nome}" removido com sucesso!')
        else:
            print("Índice inválido")

    elif opcao == 3:
        for estudante in estudantes:
            print(f"Nome: {estudante['nome']}, Idade: {estudante['idade']}, Nota: {estudante['nota']}")

    elif opcao == 4:
        nome_busca = input("Digite o nome do estudante a ser buscado: ")
        encontrados = [estudante for estudante in estudantes if estudante['nome'] == nome_busca]
        if encontrados:
            print("Estudante(s) encontrado(s)")
            for estudante in encontrados:
                print(f"Nome: {estudante['nome']}, Idade: {estudante['idade']}, Nota: {estudante['nota']}")
        else:
            print(f"Nenhum estudante com o nome '{nome_busca}' encontrado!")

    elif opcao == 5:
        idade_busca = int(input("Digite a idade do estudante a ser buscado: "))
        encontrados = [estudante for estudante in estudantes if estudante['idade'] == idade_busca]
        if encontrados:
            print("Estudante(s) encontrado(s)")
            for estudante in encontrados:
                print(f"Nome: {estudante['nome']}, Idade: {estudante['idade']}, Nota: {estudante['nota']}")
        else:
            print(f"Nenhum estudante com a idade '{idade_busca}' encontrado.")

    elif opcao == 6:
        print("Obrigado por usar o Gerenciador de Estudantes")
        break

    else:
        print("Opção inválida. Digite outro valor.")
