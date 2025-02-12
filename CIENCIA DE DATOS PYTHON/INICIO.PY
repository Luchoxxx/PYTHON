
# Ciencia de datos python
# Inicio 3 pm del 14/11/2023

usuarios = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Didcionario vacio 
# Inicializamos la lista de amigos para cada usuario en vacia
friendship = {usuario["id"] :[] for usuario in usuarios}

for i, j in friendship_pairs:
    friendship[i].append(j)             
    friendship[j].append(i)

def number_of_friends(usuario):
    usuario_ID = usuario["id"]
    amigos_IDS = friendship_pairs[usuario_ID]
    return len(amigos_IDS)
    # Total de conecciones
total_conecciones = sum(number_of_friends(usuario) for usuario in usuarios)

num_usuarios = len(usuarios)  # Longitud de la lista de usuarios
avg_conecciones = total_conecciones/num_usuarios
# Otra forma de encontra los usuarios mas conectados
# Creamos una lista usuario_id , nombre_de_amigos
nombre_de_amigos_id =[(usuario["id"],number_of_friends(usuario)) for usuario in usuarios]
nombre_de_amigos_id.sort(key=lambda id_and_friends: id_and_friends[1],
                         reverse=True)


