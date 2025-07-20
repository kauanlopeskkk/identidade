#import getpass
#SENHA_CORRETA = "Allany"
#Nome = "Kauan"
#while True:
    #try:
        #senha = input("Digite a senha: ")

        #if senha == SENHA_CORRETA and senha.isalpha():
           # print(f"{senha}: essa senha está correta (Somente Letras)")
           # print(f"Ola {Nome}: seja bem vindo ao overwatch ")
           # break  

       # elif not senha.isalpha():
           # raise ValueError("Senha Incorreta: não use números e símbolos")

        #elif senha !=SENHA_CORRETA:
            #print(f"{senha}: essa senha está incorreta (Letras estão corretas, mas a senha não confere)")

    ##except ValueError as erro:
        #print(f"Erro: {erro}")



class HeroisdoOverwatch:
        def __init__(self,nome,funcao,hp,altura,peso,habilidade,pais): 
            self.nome = nome
            self.funcao = funcao
            self.hp = hp
            self.altura = altura
            self.peso = peso
            self.habilidade = habilidade
            self.pais = pais

        def mostrar_heroi(self):
            print(f"Nome: {self.nome}")
            print(f"Função: {self.funcao}")
            print(f"HP: {self.hp}") 
            print(f"Altura: {self.altura} cm")
            print(f"Peso: {self.peso} kg")     
            print(f"Habilidade: {self.habilidade}")
            print(f"País: {self.pais}")
            
Ashe = HeroisdoOverwatch("Ashe", "Dano", 200, 185, 70, "Rifle de precisão, lança dinamite, invoca B.O.B", "EUA") 
Cassidy = HeroisdoOverwatch("Cassidy", "Dano", 200, 180, 80, "Revólver, granada de concussão, rolagem de evasão", "EUA")
Widowmaker = HeroisdoOverwatch("Widowmaker", "Dano" , 200 , 170 , 60, "Rifle de precisão, mina de viúva, gancho", "França")
Genji = HeroisdoOverwatch("Genji", "Dano", 200, 175, 70, "Shuriken, espada, salto duplo", "Japão")
Freja = HeroisdoOverwatch("Freja", "Dano", 200, 180, 75, "Lança-chamas, lança de gelo, escudo de gelo", "Islândia")

#while True:
   #try:
        #print("Escoha o seu heroi(Dano meus personagens favorito)")
        #print("1 - Freja")
        #print("2 - Cassidy")
        #print("3 - Genji")
        #print("4 - Ashe")
        #print("5 - Widowmaker")
        #print("6 - Outras")
        #print("7 - Sair")
    
        
        #escolha = int(input("Escolha o seu boneco (ou outras)[1,7]:"))
        
        #if escolha == 1:
             #Freja.mostrar_heroi()

        #elif escolha == 2:
             #Cassidy.mostrar_heroi()
        #elif escolha == 3:
             #Genji.mostrar_heroi()  
        #elif escolha == 4:
             #Ashe.mostrar_heroi()  
        #elif escolha == 5:
             #Widowmaker.mostrar_heroi() 
        #elif escolha == 6:
             #print("Ok. Voce que Jogar outros herois ") 
       # #elif escolha == 7:
           # print("Sair do jogo")
            # break  
       # else#:
             #print("Opçao Invalida.Porfavor escolha o opçao que esta exibido")
    #except ValueError:
        # print("Nao digitar a letra (So numeros)")         
