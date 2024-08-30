import random




class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'o que você pode fazer?': ['Eu posso responder a perguntas simples.', 'Eu posso ajudar a resolver problemas.'],
            'olá': ['Olá!', 'Oi!', 'Olá, como posso ajudar?'],
            'como você está?': ['Estou bem, obrigado!', 'Tudo certo, e você?'],
            'você fala qual lingua?': ['inglês intermediario, espanhol basico, português fluente'],
            'qual é a sua idade?': ['17 anos', '50 anos ',' eu sou um robô seu burro'],
            'qual time você torce?': ['real madrid ',' barcelona',' milan ', 'jeddah'],
            'qual é o seu nome?': ['Eu sou um chatbot sem nome.', 'Você pode me chamar de Chatbot.'],
            'tchau': ['Tchau!', 'Até logo!', 'Adeus!'],
            'explique o que é git pull': ['comando para puxar do repositorio remoto para o local.'],
            'passa a resposta da lição': ['qual é a lição?'],
            'lição de ia': ['qual semana e aula?'],
            's15- aula- 3': ['a resposta é criar perguntas para o chat bot interagir com você']
        }
   
    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return 'Desculpe, não entendi sua pergunta.'




def main():
    bot = SimpleChatbot()
    print("Bem-vindo a sua assistente virtual PaimonBot! (Digite 'tchau' para sair)")
   
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'tchau':
            print("PaimonBot: Tchau!")
            break
        response = bot.get_response(user_input)
        print(f"PaimonBot: {response}")




if __name__ == "__main__":
    main()

