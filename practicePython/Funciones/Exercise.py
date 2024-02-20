def es_palindromo(texto):
    texto = elim_spaces(texto)
    new_text = reverse(texto)
    return texto.lower() == new_text.lower()


def reverse(texto):
    text_reverse = ""
    for chars in texto:
        text_reverse = chars + text_reverse
    return text_reverse


def elim_spaces(texto):
    new_text = ""
    for chars in texto:
        if chars != " ":
            new_text += chars
    return new_text


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("hola mundo"))
