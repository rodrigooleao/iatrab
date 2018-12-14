def readWorldsFile():
    arq = open("mundos.dat", encoding="utf8")

    worldsList = []
    worldsHash = dict({})

    for line in arq:
        if( line != '\n'):
            line = line.strip("\n").split("|")
            worldsList.append( line )
            worldsHash[line[0]] = line[1:]

    return worldsHash



if( __name__ == "__main__"):
    worldsHash = readWorldsFile()

    for god in worldsHash:
        print( "World: " + god + "\n" )
        for quote in worldsHash[god]:
            print(quote + "\n")
        print("\n")