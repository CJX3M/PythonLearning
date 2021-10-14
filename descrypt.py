def lassoLetter(char, shift):
    # Obtenemos el número ascii de la primera letra
    aCharAscii = ord('a')
    # Establecemos el tamaño del alfabeto para revisar el offset
    alphabetSize = 26
    # Obtenemos el código ascii del caracter a cambiar
    charCode = ord(char.lower())
    # Calculamos el nuevo caracter. tomando en cuenta la posibilidad de un bucle en el alfabeto
    newCharCode = aCharAscii + (((charCode - aCharAscii) + shift) % alphabetSize)
    # Obtenemos el nuevo caracter
    newChar = chr(newCharCode)
    return newChar

def lassoWord(word, shift):
    newWord = ''
    for letter in word:
        newWord += lassoLetter(letter, shift)
    return newWord

print(lassoLetter('p', -2))

print( "Shifting Ncevy by 13 gives: \n" + lassoWord( "Ncevy", 13 ) )
print( "Shifting gpvsui by 25 gives: \n" + lassoWord( "gpvsui", 25 ) )
print( "Shifting ugflgkg by -18 gives: \n" + lassoWord( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lassoWord( "wjmmf", -1 ) )