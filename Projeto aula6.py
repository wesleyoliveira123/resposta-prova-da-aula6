lista_de_tarefas = [{
        "Nome": "Lavar a louça",
        "Descrição": "Lavar e secar a louça de ontem",
        "Prioridade": 2,
        "Categoria": "Doméstica",
        "Concluído": False
    },
    {
        "Nome": "Ir para academia",
        "Descrição": "Malhar peito e tríceps",
        "Prioridade": 1,
        "Categoria": "Saúde",
        "Concluído": False
    },
    {
        "Nome": "Estudar Python",
        "Descrição": "Revisar funções e dicionários",
        "Prioridade": 3,
        "Categoria": "Educação",
        "Concluído": True
    }
]

def adicionarTarefa():
    nome_tarefa = str(input("Digite o nome da tarefa: "))
    descricao_tarefa = str(input("Digite a descrição da tarefa: "))
    prioridade_tarefa = int(input("Digite a prioridade da tarefa: [1 - Baixa | 2 - Médio | 3 - Alta] "))
    categoria_tarefa = str(input("Digite a categoria da tarefa: "))

    dicionario = {
        "Nome": nome_tarefa,
        "Descrição": descricao_tarefa,
        "Prioridade": prioridade_tarefa,
        "Categoria": categoria_tarefa,
        "Concluído": False
    }

    lista_de_tarefas.append(dicionario)
    return "Tarefa adicionada com sucesso."

def ver_todos():
    for dicionario in lista_de_tarefas:
        status = 'concluído' if dicionario['Concluído'] else 'não concluído'
        print(f"Tarefa: {dicionario['Nome']}, Descrição: {dicionario['Descrição']}, Prioridade: {dicionario['Prioridade']}, Status: {status}")

def marcar_concluido():
    nome_tarefa = str(input("Digite o nome da tarefa que deseja marcar como concluída: "))
    for dicionario in lista_de_tarefas:
        if dicionario['Nome'] == nome_tarefa:
            dicionario['Concluído'] = True
            return 'Tarefa marcada como concluída.'
    return 'Tarefa não encontrada.'

def exibir_por_Prioridade():
    ordenada = sorted(lista_de_tarefas, key=lambda k: k['Prioridade'], reverse=False)
    resultado = ""
    for dicionario in ordenada:
        status = 'concluído' if dicionario['Concluído'] else 'não concluído'
        resultado += f"Tarefa: {dicionario['Nome']}, Descrição: {dicionario['Descrição']}, Prioridade: {dicionario['Prioridade']}, Status: {status}\n"
    return resultado

def exibir_por_categoria():
    ordenada = sorted(lista_de_tarefas, key=lambda k: k['Categoria'])
    resultado = ""
    for dicionario in ordenada:
        status = 'concluído' if dicionario['Concluído'] else 'não concluído'
        resultado += f"Categoria: {dicionario['Categoria']}, Tarefa: {dicionario['Nome']}, Descrição: {dicionario['Descrição']}, Prioridade: {dicionario['Prioridade']}, Status: {status}\n"
    return resultado



while True:
    menu = int(input("""
1 - Adicionar
2 - Ver todos
3 - Marcar como Concluído
4 - Exibir por Prioridades
5 - Exibir por Categorias
0 - Sair 
Escolha uma opção: """))

    match menu:
        case 1:
            print(adicionarTarefa())
        case 2:
            ver_todos()
        case 3:
            print(marcar_concluido())
        case 4:
            print(exibir_por_Prioridade())
        case 5:
            print(exibir_por_categoria())
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção inválida")