import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

while True:
    try:
        pokemon = input("\n>>> Escribe el nombre de un pokemon (o end para terminar): ")
    
        respuesta = requests.get(URL + pokemon)
        datos = respuesta.json()

        def operation_pokemon(require):

            if require == 1 or require == "move":
                print(mov_pokemon(pokemon))
            elif require == 2 or require == "type":
                print(type_pokemon(pokemon))
            elif require == 3 or require == "stats":
                print(stats_pokemon(pokemon))
            elif require == 4 or require == "all":
                print(mov_pokemon(pokemon))
                print(type_pokemon(pokemon))
                print(stats_pokemon(pokemon))
            else:
                print("Enter a valid option")

# funcion que muestra los/el moc¿vimiento/s del pokemon solicitado
        def mov_pokemon(pokemon):
            print(f"\n----------- The moves of '{pokemon}' -----------")
            for move in datos["moves"]:
                print(move["move"]["name"])

# funcion que muestra el tipo/s del pokemon solicitado
        def type_pokemon(pokemon):
            print(f"\n----------- The type/s of '{pokemon}' -----------")
            for types in datos["types"]:
                print(types["type"]["name"])

# funcion que muestra las estadisticas del pokemon solicitado
        def stats_pokemon(pokemon):
            print(f"\n----------- The stats of '{pokemon}' -----------")
            for stats in datos["stats"]:
                print(stats["stat"]["name"], stats["base_stat"])

# Imprimir la informacion
#print(mov_pokemon(pokemon))
#print(type_pokemon(pokemon))
#print(stats_pokemon(pokemon))



# ejecution
        while True:

            if pokemon == "end":
                break

            require = input("\n>>> Enter an opction to call (move, type, stats, or all) or end to finish the code: ")
            if require == "end":
                break
            else:
                operation_pokemon(require)
    except:
        print(f"¡{pokemon} don't found!, please enter a valid pokemon")
