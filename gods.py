def readGodsFile():
    arq = open("gods.dat")

    godsList = []
    godsHash = dict({})

    for line in arq:

        if( line != '\n'):
            line = line.strip("\n").split("|")
            godsList.append( line )
            godsHash[line[0]] = line[1:]

    return godsHash



if( __name__ == "__main__"):
    godsHash = readGodsFile()

    for god in godsHash:
        print( "God: " + god + "\n\n" )
        for quote in godsHash[god]:
            print(quote + "\n")
        print("\n")