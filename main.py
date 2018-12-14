from gods import *
from worlds import *

deusesCommands = ["deus" , "deuses"]
mundosCommands = ["mundos" , "mundo"]

godsHash = readGodsFile()
worldsHash = readWorldsFile()

listOfGods = list(godsHash.keys())
listOfWorlds = list(worldsHash.keys())


def gods( q , mode):
        if( mode == 0):
                botSpeak("A Mitologia Nórdica possui muitos deuses interessantes e você pode conferir detalhes sobre alguns deles aqui.")
                print("São eles: " , end="\n")
                for god in listOfGods:
                        print("\t" + god + " ")
        elif( mode == 1):
                print("\n\n")
                botSpeak( "\t>>>>>>>>>>>> " + q.upper() + " <<<<<<<<<<<<\n")

                for quote in godsHash[q]:
                        botSpeak( quote )
                        botSpeak("Deseja saber mais sobre?")
                        zin = input(" -??? ")
                        if( zin == "nao" or zin == "n"):
                                botSpeak("okay")
                                break
                        

def worlds( q , mode):
        print( "worlds")
    

def welcomeMessage():
    print(" ->>> Bem-Vindo, diga-nos sobre o que você quer saber?")

def botSpeak( message ):
        print(" ->>> " + message + "\n")

if( __name__ == "__main__"):
        welcomeMessage()
        while( True ):
                botSpeak("Diga algo que você queira saber")
                question = input(" -??? ")
                parsedQ = question.split(" ")

                if( question in deusesCommands ):
                        gods( question , 0)
                elif( question in listOfGods):
                        gods( question , 1)
                elif( question in mundosCommands):
                        worlds( question , 0)
                elif( question in listOfWorlds):
                        worlds( question , 1)
                elif( question == "sair"):
                        break
                else:
                        print("")
                        botSpeak("Desculpe, não entendi, mas se estiver afim de saber mais sobre deuses, mundos ou lendas da mitologia nórdica fique a vontade.")

                
                
                

    