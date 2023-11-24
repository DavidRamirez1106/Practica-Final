import random


class Pregunta:
    def __init__(self, pregunta, opciones, respuesta_correcta, premio):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.premio = premio
        self.comodin_usado = False

    def mostrar_pregunta(self):
        print(self.pregunta)
        for i, opcion in enumerate(self.opciones, start=1):
            print(f"{i}. {opcion}")
    
    def verificar_respuesta(self, respuesta_usuario):
        return respuesta_usuario == self.respuesta_correcta

    def comodin_50_50(self):
        if not self.comodin_usado:
            opciones_mostradas = [self.respuesta_correcta]
            opciones_incorrectas = [i + 1 for i in range(len(self.opciones)) if i + 1 != self.respuesta_correcta]
            opciones_mostradas.append(random.choice(opciones_incorrectas))
            opciones_mostradas.sort()
            self.comodin_usado = True
            return opciones_mostradas
        else:
            print("El comodín '50/50' ya ha sido utilizado. ¡Elige otra opción!")
            return None


def juego_quien_quiere_ser_millonario(usuario):
    # Definir preguntas y respuestas con premios en dinero
    preguntas = [
        Pregunta("¿Cuál es la capital de Japón?", ["Pekín", "Seúl", "Tokio", "Bangkok"], 3, 1000),
        Pregunta("¿Cuál es el río más largo del mundo?", ["Amazonas", "Nilo", "Yangtsé", "Misisipi"], 1, 2000),
        Pregunta("¿Quién escribió 'Cien años de soledad'?", ["Mario Vargas Llosa", "Julio Cortázar", "Gabriel García Márquez", "Isabel Allende"], 3, 3000),
        Pregunta("¿En qué año se fundó Microsoft?", ["1975", "1985", "1995", "2005"], 1, 2000),
        Pregunta("¿Cuál es el planeta más grande del sistema solar?", ["Tierra", "Marte", "Júpiter", "Saturno"], 3, 4000),
        Pregunta("¿Cuál es la montaña más alta del mundo?", ["Monte Everest", "K2", "Annapurna", "Matterhorn"], 1, 1000),
        Pregunta("¿Quién pintó 'La última cena'?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], 1, 1000),
        Pregunta("¿Cuál es el océano más grande?", ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Antártico"], 3, 1000),
        Pregunta("¿En qué año se llevó a cabo la Revolución Rusa?", ["1917", "1927", "1937", "1947"], 1, 1000),
        Pregunta("¿Cuál es la capital de Australia?", ["Sídney", "Melbourne", "Canberra", "Brisbane"], 3, 1500),
        Pregunta("¿Cuál es el río que atraviesa París?", ["Sena", "Támesis", "Danubio", "Ródano"], 1, 1200),
        Pregunta("¿Quién escribió 'Don Quijote de la Mancha'?", ["Miguel de Cervantes", "Federico García Lorca", "Gabriel García Márquez", "Jorge Luis Borges"], 1, 2000),
        Pregunta("¿En qué año se declaró la independencia de México?", ["1808", "1810", "1821", "1830"], 3, 1800),
        Pregunta("¿Cuál es el país más grande de África?", ["Sudáfrica", "Nigeria", "Argelia", "Egipto"], 3, 2500),
        Pregunta("¿Quién fue el primer hombre en caminar sobre la Luna?", ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"], 1, 3000),
        Pregunta("¿Cuál es el metal más pesado?", ["Plomo", "Oro", "Uranio", "Mercurio"], 3, 2000),
        Pregunta("¿En qué continente se encuentra la Gran Barrera de Coral?", ["Asia", "África", "Oceanía", "América"], 3, 1800),
        Pregunta("¿En qué año comenzó la Segunda Guerra Mundial?", ["1935", "1939", "1942", "1945"], 2, 2500),
        Pregunta("¿Cuál es el desierto más seco del mundo?", ["Desierto del Sahara", "Desierto de Atacama", "Desierto de Gobi", "Desierto de Kalahari"], 2, 2200),
        Pregunta("¿Quién fue el primer presidente de Estados Unidos?", ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"], 2, 3000),
        Pregunta("¿Cuál es la moneda oficial de Japón?", ["Yuan", "Won", "Yen", "Ringgit"], 3, 1200),
        Pregunta("¿En qué año se proclamó la independencia de Brasil?", ["1808", "1822", "1850", "1889"], 2, 1500),
        Pregunta("¿Cuál es el componente principal del aire que respiramos?", ["Oxígeno", "Nitrógeno", "Dióxido de carbono", "Hidrógeno"], 2, 2000),
        Pregunta("¿Cuál es la película más taquillera de la historia?", ["Titanic", "Avatar", "Avengers: Endgame", "El Rey León (2019)"], 3, 3000),
        Pregunta("¿En qué año se inauguró el Canal de Panamá?", ["1904", "1914", "1924", "1934"], 2, 1800),
        Pregunta("¿Cuál es el país más poblado del mundo?", ["India", "China", "Estados Unidos", "Brasil"], 2, 2500),
        Pregunta("¿Cuál es el instrumento musical nacional de Japón?", ["Taiko", "Shamisen", "Koto", "Shakuhachi"], 3, 1200),
        Pregunta("¿En qué año se llevó a cabo la Revolución Cubana?", ["1952", "1961", "1970", "1980"], 2, 2200),
        Pregunta("¿Cuál es el mamífero más grande del mundo?", ["Elefante", "Ballena azul", "Jirafa", "Tigre"], 2, 3000),
    ]

    # Mezclar las preguntas para que aparezcan en un orden aleatorio
    random.shuffle(preguntas)

    # Iniciar el juego
    premio_acumulado = 0
    preguntas_realizadas = 0

    for pregunta_actual in preguntas:
        pregunta_actual.mostrar_pregunta()

        # Comodín 50/50
        usar_comodin = input("¿Deseas usar un comodín 50/50? (s/n): ")
        if usar_comodin.lower() == 's':
            opciones_mostradas = pregunta_actual.comodin_50_50()
            if opciones_mostradas is None:
                continue  # Preguntar de nuevo si el comodín ya ha sido utilizado
            print(f"Opciones restantes: {opciones_mostradas}")

        respuesta_usuario = input("Ingresa el número de tu respuesta: ")

        if usar_comodin.lower() == 's':
            if int(respuesta_usuario) in opciones_mostradas:
                print(f"¡Respuesta correcta! {usuario} ganaste ${pregunta_actual.premio}\n")
                premio_acumulado += pregunta_actual.premio
            else:
                print(f"Respuesta incorrecta. La respuesta correcta era la opción {pregunta_actual.respuesta_correcta}: {pregunta_actual.opciones[pregunta_actual.respuesta_correcta - 1]}\n")
                break
        else:
            if pregunta_actual.verificar_respuesta(int(respuesta_usuario)):
                print(f"¡Respuesta correcta! {usuario} ganaste ${pregunta_actual.premio}\n")
                premio_acumulado += pregunta_actual.premio
            else:
                print(f"Respuesta incorrecta. La respuesta correcta era la opción {pregunta_actual.respuesta_correcta}: {pregunta_actual.opciones[pregunta_actual.respuesta_correcta - 1]}\n")
                break  # Terminar el juego si la respuesta es incorrecta

        preguntas_realizadas += 1

        if preguntas_realizadas % 5 == 0:
            respuesta_retiro = input(f"Has respondido {preguntas_realizadas} preguntas. ¿Deseas retirarte con ${premio_acumulado} acumulado, {usuario}? (s/n): ")
            if respuesta_retiro.lower() == 's':
                print(f"¡Felicidades! {usuario} has decidido retirarte con ${premio_acumulado}")
                return premio_acumulado

    # Mostrar el resultado final
    print(f"Fin del juego. {usuario}, tu premio acumulado es: ${premio_acumulado}")
    return premio_acumulado


if __name__ == "__main__":
    # Primer jugador
    nombre_jugador_1 = input("Ingresa tu nombre, jugador 1: ")
    premios_jugador_1 = juego_quien_quiere_ser_millonario(nombre_jugador_1)

    # Segundo jugador
    nombre_jugador_2 = input("Ingresa tu nombre, jugador 2: ")
    premios_jugador_2 = juego_quien_quiere_ser_millonario(nombre_jugador_2)

    # Mostrar los premios acumulados de ambos jugadores
    print(f"\nResumen final:")
    print(f"{nombre_jugador_1}, tu premio acumulado es: ${premios_jugador_1}")
    print(f"{nombre_jugador_2}, tu premio acumulado es: ${premios_jugador_2}")
