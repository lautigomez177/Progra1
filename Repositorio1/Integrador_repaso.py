'''
Enunciado/s:
Tabla de Posiciones de Torneo de Ping-Pong
Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
Los datos que se cargarán son:
Nombre del jugador
Edad (validar)
Cantidad de puntos (validar-número entero positivo, hasta 60).
Número de partidos ganados (validar-número entero positivo, hasta 35).
Tipo de saque ("plano", "liftado", "cortado")
Categoría ("elite", "experto", "avanzado")
Se necesita saber
Tema A:
1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive.
2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
3-Porcentaje de jugadores de categoría "experto".
4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”
'''
continuar = True
jugador_elite_plano = 0
menor_edad_cat = ""
nombre_menor50pts = ""
menor_edad_50pts = 0
cant_exp = 0
total_jugadores = 0
suma_edades_avanzado = 0
total_expertos = 0
total_avanzado = 0
elite_plano = 0
elite_liftado = 0
elite_cortado = 0
saque_predominante = ""


while continuar == True:
    nombre = str(input("Ingrese nombre: "))
    cant_puntos = int(input("Ingrese los puntos conseguidos: "))
    while cant_puntos < 0 or cant_puntos > 60: 
        print("Puntaje inválido. Vuelva a intentar, el puntaje debe estar entre 0 y 60 pts")
        cant_puntos = int(input("Ingrese los puntos conseguidos: "))
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        print("Dato incorrecto. Debe ser mayor de edad.")
        edad = int(input("Ingrese su edad: "))
    partidos_ganados = int(input("Cuantos partidos ganó?: "))
    while partidos_ganados < 0 or partidos_ganados > 35:
        print("Número no valido, ingrese un número entre 0 y 35")
        partidos_ganados = int(input("Cuantos partidos ganó?: "))
        
    tipo_saque = str(input("Ingrese el tipo de saque [plano | liftado | cortado]: "))
    while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
        print("Tipo de saque inválido. Por favor ingrese un saque permitido.")
        tipo_saque = str(input("Ingrese el tipo de saque [plano | liftado | cortado]: "))
        
    categoria = str(input("Ingrese a que categoria pertenece [ elite | experto | avanzado]: "))
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        print("Categoria ingresada invalida. Ingrese una categoria registrada: ")
        categoria = str(input("Ingrese a que categoria pertenece [ elite | experto | avanzado]: "))
    
    if categoria == "elite" and tipo_saque == "plano" and 19 >= edad <= 25:
        jugador_elite_plano += 1
        
    if cant_puntos > 50:
        if edad < menor_edad_50pts:
            nombre_menor50pts = nombre
            menor_edad_50pts = edad
            menor_edad_cat = categoria
            
    if categoria == "elite":
        if tipo_saque == "plano":
            elite_plano += 1
        elif tipo_saque == "liftado":
            elite_liftado  += 1
        elif tipo_saque == "cortado":
            elite_cortado += 1
    
    if categoria == "experto":
        total_expertos += 1
    
    if categoria == "avanzado":
        suma_edades_avanzado += edad
        total_avanzado += 1
    
    total_jugadores += 1
    
    desea_continuar = str(input("Desea agregar otro jugador? [si | no]: "))
    if desea_continuar == "no":
        continuar = False


if total_jugadores > 0 :        
    porcentaje_expertos = (total_expertos / total_jugadores * 100)
else:
    porcentaje_expertos = 0

if total_avanzado > 0:
    promedio_edad_avanzado = (suma_edades_avanzado / total_avanzado) 
else:
    promedio_edad_avanzado = 0
    
if elite_plano > elite_liftado and elite_plano > elite_cortado:
    saque_predominante = elite_plano
elif elite_liftado > elite_cortado:
    saque_predominante = elite_liftado
else:
    saque_predominante = elite_cortado
    
print(f"Cantidad de jugadores de la categoría elite con tipo de saque plano y edad entre 19 y 25 años: {jugador_elite_plano}")
print(f"Nombre y categoría del jugador de menor edad con más de 50 puntos: {nombre_menor50pts} de la categoria {menor_edad_50pts}")
print(f"Porcentaje de jugadores de categoría experto: {porcentaje_expertos:.2f}%")
print(f"Promedio de edad de jugadores cuya categoría es avanzado: {promedio_edad_avanzado:.2f}")
print(f"Tipo de saque más usado por jugadores de categoría elite: {saque_predominante}")