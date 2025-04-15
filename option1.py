#OPCION 1

class CifradoCesar:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento
        self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def cifrar(self, texto):
        texto = texto.upper()
        resultado = ''

        for letra in texto:
            if letra in self.alfabeto:
                indice_original = self.alfabeto.index(letra)
                nuevo_indice = (indice_original + self.desplazamiento) % 26
                resultado += self.alfabeto[nuevo_indice]
            else:
                resultado += letra  # mantener caracteres que no están en el alfabeto

        return resultado

# Interacción con el usuario
texto_usuario = input("Ingresa el texto que deseas cifrar (solo letras): ")
desplazamiento_usuario = int(input("Ingresa el número de desplazamiento: "))

cifrado = CifradoCesar(desplazamiento_usuario)
texto_cifrado = cifrado.cifrar(texto_usuario)

print(f"\nTexto original: {texto_usuario.upper()}")
print(f"Texto cifrado: {texto_cifrado}")



#OPCION 2

class BubbleSort:
    def __init__(self, lista):
        self.lista = lista

    def ordenar(self):
        n = len(self.lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    # Intercambiar si el actual es mayor que el siguiente
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]

    def obtener_lista_ordenada(self):
        return self.lista

# Interacción con el usuario
entrada = input("Ingresa una lista de números separados por comas: ")
numeros = [int(n) for n in entrada.split(",")]

# Crear una instancia de la clase y ordenar
ordenador = BubbleSort(numeros)
ordenador.ordenar()

# Mostrar el resultado
print(f"Lista ordenada: {ordenador.obtener_lista_ordenada()}")
