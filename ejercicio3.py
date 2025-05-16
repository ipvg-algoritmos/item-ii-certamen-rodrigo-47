# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código

def es_palindromo(texto):
    texto = texto. lower()
    texto_sin_espacios ="".join (texto.split())
    return texto_sin_espacios == texto_sin_espacios[::-1]
entrada = input("ingrese una palabra o frase:")
if es_palindromo(entrada):
    print(f"'{entrada}'es un palindromo.")
else:
    print(f"'{entrada}'no es un palindromo.")