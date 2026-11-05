# main.py

# Importando o nosso arquivo de chatbot como um módulo
import PitonBot as py

def iniciar_chat():
    print("🤖 Olá! Eu sou o assistente virtual da nossa Biblioteca. Como posso ajudar?")
    
    while True:
        # Chama a função de menu que está no outro arquivo
        py.exibir_menu()
        escolha = input("\nEscolha uma opção (1 a 4): ").strip()
        
        if escolha == "1":
            # Exibe a listagem de livros
            print(py.listar_livros())
            
        elif escolha == "2":
            termo = input("Digite o título ou palavra-chave do livro que deseja buscar: ")
            print(py.buscar_livro(termo))
            
        elif escolha == "3":
            termo = input("Digite o título exato do livro que deseja pegar emprestado: ")
            print(py.emprestar_livro(termo))
            
        elif escolha == "4":
            print("\n🤖 Chatbot: Obrigado por usar a Biblioteca Digital! Até logo! 👋")
            break
            
        else:
            print("⚠️ Opção inválida! Por favor, escolha um número entre 1 e 4.")

if __name__ == "__main__":
    iniciar_chat()