# -*- coding: unicode -*-
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
                botSpeak("modo geral")
        elif( mode == 1):
                botSpeak("modo especifico")
                print( ">>>>>>>>>>>> " + q.upper() + " <<<<<<<<<<<<")

                for quote in godsHash[q]:
                        print( quote )
                        botSpeak("Deseja saber mais sobre?")
                        zin = input(" -??? ")
                        if( zin == "nao" or zin == "n"):
                                break
                        

def worlds( q , mode):
        print( "worlds")
    

def welcomeMessage():
    print(" ->>> Bem-Vindo, diga-nos sobre o que você quer saber?")

def botSpeak( message ):
        print(" ->>> " + message)

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
                        botSpeak("Desculpe, não entendi.")

                
                
                

    