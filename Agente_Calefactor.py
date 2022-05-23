#creacion de la funcion
def funcionAgente():
    #se crean los estados donde 0 indica caliente y 1 frio 
    estados_objetivos={'estadoSala':'0','estadoComedor':'0','estadoHabitacion':'0'}
    #el costo siempre inicia en cero
    costo=0

    #se inicia la calefacción y por lo tanto aumenta uno el costo
    print("----Calefacción encendida----")
    costo+=1
    print("Costo actual: "+str(costo)) #mostrando el costo

    #saber la temperatura de la sala
    estadoInicialSala=input("Ingrese 0 si la sala esta caliente y 1 si esta fria: ") 
    #saber la temperatura del comedor
    estadoInicialComedor=input("Ingrese 0 si el comedor esta caliente y 1 si esta fria: ") 
    #saber la temperatura de la habitacion 
    estadoInicialHabitacion=input("Ingrese 0 si la habitacion esta caliente y 1 si esta fria: ") 

    #reunir los datos ingresados por el usuario
    estados_objetivos['estadoSala'] = estadoInicialSala
    estados_objetivos['estadoComedor'] = estadoInicialComedor
    estados_objetivos['estadoHabitacion'] = estadoInicialHabitacion

    #mostrar el array del estado inicial de cada una de las zonas
    print("El estado inicial de cada zona es:" + str(estados_objetivos))

    #recorrer la zona 1 que es la sala
    for zona1 in range(1):
        if estadoInicialSala == '0': #Si la sala ya esta caliente
            print("Calefacción - Zona de la Sala")
            print("La Sala ya esta caliente")
            estados_objetivos['estadoSala'] = '0' #asignando el estado de 0 a la sala
            print("Costo actual: "+str(costo)) #mostrando costo 
        elif estadoInicialSala == '1': #Si la sala esta fria
            print("Calefacción - Zona de la Sala")
            print("La Sala esta fría")
            print("Calentando Sala...")
            estados_objetivos['estadoSala'] = '0' #asignando el estado de 0 a la sala
            costo+=1                              #aumentando el costo  
            print("Sala calentada con éxito")
            print("Costo actual: "+str(costo))    #mostrando el costo

    #recorrer la zona 2 que es el comedor
    for zona2 in range(1):
        if estadoInicialComedor == '0': #si el comedor ya esta caliente
            print("Calefacción - Zona de Comedor")
            print("El comedor ya esta caliente")
            estados_objetivos['estadoComedor'] = '0' #asignando el estado de 0 al comedor
            print("Costo actual: "+str(costo))        #mostrando costo
        elif estadoInicialComedor == '1':#Si el comedor esta frio
            print("Calefacción - Zona de Comedor")
            print("El Comedor esta frío")
            print("Calentando Comedor...")
            estados_objetivos['estadoComedor'] = '0' #asignando el estado de 0 al comedor
            costo+=1                                 #aumentando el costo
            print("Comedor calentado con éxito")
            print("Costo actual: "+str(costo))      #mostrando el costo

    #recorrer la zona 3 que es la habitacion
    for zona3 in range(1):
        if estadoInicialHabitacion == '0': #Si la habitación ya esta caliente
            print("Calefacción - Zona de Habitación")
            print("La Habitación ya esta caliente")
            estados_objetivos['estadoHabitacion'] = '0' #asignando el estado de 0 a la habitación
            print("Costo actual: "+str(costo))          #mostrando el costo
        elif estadoInicialHabitacion == '1': #Si la habitación esta fria
            print("Calefacción - Zona Habitación")
            print("La Habitación esta fría")
            print("Calentando Habitación...")
            estados_objetivos['estadoHabitacion'] = '0' #asignando el estado de 0 a la habitación
            costo+=1                                    #aumentando el costo
            print("Habitación calentada con éxito")
            print("Costo actual: "+str(costo))          #mostrando el costo

    #estado y costo final
    print("El estado final de cada zona es el siguiente: ")
    print(estados_objetivos)
    print("Costo Final: " + str(costo))
    

        
#llamando a la funcion 
funcionAgente()