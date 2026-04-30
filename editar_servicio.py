import csv

def editar_servicio_photocampus():
    archivo = "servicios_photocampus.csv"
    
    while True:
        try:
            id_buscar = input("\nIngrese el ID del paquete que desea editar: ")
            servicios = []
            encontrado = False
            
            try:
                with open(archivo, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    servicios = list(reader)
            except FileNotFoundError:
                print("Error: El archivo de servicios no existe todavía.")
                return

            indice_editar = -1
            for i, s in enumerate(servicios):
                if s["ID Paquete"] == id_buscar:
                    encontrado = True
                    indice_editar = i
                    break
            
            if not encontrado:
                print(f"Ese ID {id_buscar} no existe.")
                opcion = input("¿Quiere volver a intentar? S/N: ").strip().upper()
                if opcion == "S":
                    continue
                else:
                    print("Finalizando ejecución.")
                    break

            print(f"--- Editando Servicio ID: {id_buscar} ---")
            
            while True:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    if nuevo_precio > 0: break
                    print("El precio debe ser mayor a cero.")
                except ValueError:
                    print("Error: Ingrese un valor numerico para el precio.")

            while True:
                nuevo_evento = input("Ingrese el nuevo tipo de evento: ").strip()
                if nuevo_evento.replace(" ", "").isalpha() and nuevo_evento != "":
                    break
                print("Error: El tipo de evento solo debe contener letras.")

            while True:
                try:
                    nueva_duracion = float(input("Ingrese la nueva duracion (horas): "))
                    if nueva_duracion > 0: break
                    print("La duracion debe ser mayor a cero.")
                except ValueError:
                    print("Error: Ingrese un valor numerico para las horas.")

            servicios[indice_editar]["Precio"] = nuevo_precio
            servicios[indice_editar]["Tipo Evento"] = nuevo_evento
            servicios[indice_editar]["Duracion"] = nueva_duracion

            with open(archivo, mode='w', newline='', encoding='utf-8') as file:
                escritor = csv.DictWriter(file, fieldnames=["ID Paquete", "Precio", "Tipo Evento", "Duracion"])
                escritor.writeheader()
                escritor.writerows(servicios)
            
            print(f"Servicio {id_buscar} actualizado exitosamente.")
            break

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break
