




livros_disponiveis = [
    {"Titulo": "O caçador de pipas", "autor": "Khaled Hosseini", "quantidade": 6},
    {"Titulo": "As crônicas de Narnia", "autor": "C.S.Lewis", "quantidade": 2},
    {"Titulo": "A menina que roubava livros", "autor": "Markus Zusak", "quantidade": 3},
    {"Titulo": "Assassinato No Expresso do Oriente", "autor": "Khaled Hosseini" , "quantidade": 15}
]

def exibir_menu():
    """Exibir as opções disponiveis no chatbot da biblioteca"""
    print("\n --- Bem Vindo a Biblioteca Digite ---")
    print("1. Listar todos os livros disponiveis")
    print("2. Buscar os livros pelo titulo")
    print("3. Emprestar um livro")
    print("4. Sair")

def listar_livros():
    """Retornar uma string com os livros e suas quantidades"""
    resultado = "\n **Acervo da Biblioteca:**\n"
    for livro in livros_disponiveis:
        resultado += f" - {livro['titulo']} (autor: {livro['autor']}) | Disponíveis: {livro['quantidade']}\n"
    return resultado

def buscar_livro(titulo_busca: str):
    """Busca um livro por sua categoria"""
    titulo_busca = titulo_busca().strip()
    encontrados = [ l for l in livros_disponiveis if titulo_busca in l["titulo"]. lower()]

    if not encontrados:
        return f" Nenhum livro foi encontrado com o termo '{titulo_busca}'."

    resposta = f"\n ... **Resultados da busca para '{titulo_busca}':**\n"
    for livro in encontrados:
        resposta = f"- {livro['titulo']} por {livro['autor']} (Disponíveis: {livro['quantidade']})\n"
    return resposta

def emprestar_livro(titulo_buscar:str):
    """Vai simular o empretismo de um livro, para um usuario"""
    titulo_busca = titulo_busca.lower().strip()
    for livro in livros_disponiveis:
        if titulo_busca in livro["titulo"].lower():
            if livro["quantidade"] > 0:
                livro["quantidade"] -= 1
                return f" Empréstimo realizado! O livro '{livro['título']}' foi emprestado com sucesso. Restam {livro['quantidade']} unidades."
            else:
                return f" Desculpa, o livro '{livro['titulo']}' está esgotado no momento!"
    return f" Livro '{titulo_busca}' não foi encontrado no acervo."
