
# Para poder seguir usando el programa más de una vez
corriendo = True

while corriendo:

    # Imprimir primer menú
    print("\nMenú Principal:\n\n1. Operaciones Matemáticas\n2. Captura de Datos\n3. Salir\n")

    # Dar al usuario a elegir una opción
    choice1 = int(input("Seleccionar un número del menú: "))

    if choice1 == 1: # Operaciones Matemáticas

        while choice1 == 1: 
            print("\n\nUsted Seleccionó Menú de Matemáticas: \n\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Regresar\n")
            choice2 = int(input("Elegir un número del menú: "))

            if choice2 == 1: # Suma
                print("\nSeleccionó Suma\n")
                a = int(input("Seleccione el primer número: "))
                b = int(input("Seleccione el segundo número: "))
                print("\nEl resultado es " + str(a+b))

            elif choice2 == 2: # Resta
                print("Seleccionó Resta\n")
                a = int(input("Seleccione el primer número: "))
                b = int(input("Seleccione el segundo número: "))
                print("\nEl resultado es " + str(a-b))
            
            elif choice2 == 3: # Multiplicación
                print("Seleccionó Multiplicación\n")
                a = int(input("Seleccione el primer número: "))
                b = int(input("Seleccione el segundo número: "))
                print("\nEl resultado es " + str(a*b))

            elif choice2 == 4: # División
                print("Seleccionó División\n")
                a = float(input("Seleccione el primer número: "))
                b = float(input("Seleccione el segundo número: "))
                print("\nEl resultado es " + str(a/b))

            elif choice2 == 5: # Regresar
                choice1 = -1
                break

            else:
                print("Esa no es una elección válida, por favor selecciona una de las opciones del menú\n")

        seguirUsando = int(input("Desea seguir usando los menús?\n1. Si\n2. No\n"))
        if seguirUsando != 1:
            corriendo = False


    elif choice1 == 2: # Captura de Datos
        while choice1 == 2: 
            print("\n\nUsted seleccionó \n\nMenú de Captura de Datos: \n\n1. Información Laboral\n2. Información Académica\n3. Información Personal\n4. Regresar")
            choice2 = int(input("Elegir un número del menú: "))

            if choice2 == 1: # Información Laboral
                print("Seleccionó Información Laboral\n")
                nombre = input("Escriba su nombre: ")
                apellido = input("Escriba su apellido: ")
                correo = input("Escriba su correo: ")
                print("\n---------- Información Laboral ----------\nNombre: " + nombre + " " + apellido + "\nCorreo: " + correo + "\n")

            elif choice2 == 2: # Información Académica
                print("Seleccionó Información Académica\n")
                nombre = input("Escriba su nombre: ")
                apellido = input("Escriba su apellido: ")
                matricula = input("Escriba su matricula: ")
                print("\n---------- Información Académica ----------\nNombre: " + nombre + " " + apellido + "\nMatricula: " + matricula + "\n")
            
            elif choice2 == 3: # Información Personal
                print("Seleccionó Información Personal\n")
                nombre = input("Escriba su nombre: ")
                apellido = input("Escriba su apellido: ")
                telefono = input("Escriba su telefono: ")
                print("\n---------- Información Personal ----------\nNombre: " + nombre + " " + apellido + "\nTelefono: " + telefono + "\n")

            elif choice2 == 4: # Regresar
                choice1 = -1
                break

            else:
                print("Esa no es una elección válida, por favor selecciona una de las opciones del menú\n")
        
        seguirUsando = int(input("Desea seguir usando los menús?\n1. Si\n2. No\n"))
        if seguirUsando != 1:
            corriendo = False

    elif choice1 == 3: # Salir
        print("Adiós")
        corriendo = False
        break

    else:
        print("Esa no es una elección válida, por favor selecciona una de las opciones del menú\n")