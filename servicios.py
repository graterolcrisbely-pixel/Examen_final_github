import csv

def registrar_servicio_photocampus():
    archivo = "servicios_photocampus.csv"
    
    try:
        with open(archivo, mode='r', encoding='utf-8') as file:
            pass
    except FileNotFoundError:
        with open(archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID Paquete", "Precio", "Tipo Evento", "Duracion"])

    print("--- Sistema de Registro PhotoCampus ---")

    while True:
        try:
            id_input = input("Ingrese el ID numerico del paquete: ")
            id_paquete = int(id_input)
            
            # Verificar duplicados en el archivo
            duplicado = False
            with open(archivo, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for fila in reader:
                    if fila["ID Paquete"] == str(id_paquete):
                        duplicado = True
                        break
            
            if duplicado:
                print("Error: Este ID ya existe. Ingrese uno diferente.")
            elif id_paquete <= 0:
                print("Error: El ID debe ser un numero positivo.")
            else:
                break
        except ValueError:
            print("Error: El ID debe ser un numero entero.")

    while True:
        try:
            precio = float(input("Ingrese el precio del servicio: "))
            if precio <= 0:
                print("Error: El precio debe ser mayor a cero.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un valor numerico para el precio.")

    while True:
        tipo_evento = input("Ingrese el tipo de evento (Boda, Retrato, etc.): ").strip()
        if tipo_evento.replace(" ", "").isalpha() and tipo_evento != "":
            break
        else:
            print("Error: El tipo de evento solo puede contener letras.")

    while True:
        try:
            duracion = float(input("Ingrese la duracion estimada (horas): "))
            if duracion <= 0:
                print("Error: La duracion debe ser mayor a cero.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un valor numerico para las horas.")

    try:
        with open(archivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([id_paquete, precio, tipo_evento, duracion])
        print(f"\nServicio con ID {id_paquete} registrado exitosamente en PhotoCampus.")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
