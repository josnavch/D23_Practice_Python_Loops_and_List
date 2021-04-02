def lyrics_generator (cancion):
    letra = ""
    estribillo = 0
    for item in cancion:
        if item == 0:
            letra += "Boom "
            estribillo = 0
        elif item == 1:
            letra += "Drop the base "
            estribillo += 1
            if estribillo == 3:
                letra += "!!!Break the base!!! "
    return letra        


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))