import csv

def eliminar_servicio_photocampus():
    archivo = "servicios_photocampus.csv"
    
    while True:
        try:
            id_eliminar = input("\nIngrese el ID del paquete que desea eliminar: ")
            servicios = []
            encontrado = False

            try:
                with open(archivo, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    servicios = list(reader)
            except FileNotFoundError:
                print("Error: El archivo no existe. Registre un servicio primero.")
                return

            servicio_a_quitar = None
            for s in servicios:
                if s["ID Paquete"] == id_eliminar:
                    encontrado = True
                    servicio_a_quitar = s
                    break

            if not encontrado:
                print(f"Ese ID {id_eliminar} no existe.")
                opcion = input("¿Quiere volver a intentar? S/N: ").strip().upper()
                if opcion == "S":
                    continue
                else:
                    print("Finalizando ejecución.")
                    break

            confirmar = input(f"¿Está seguro de eliminar el servicio {id_eliminar}? (S/N): ").strip().upper()
            if confirmar == "S":

                servicios = [s for s in servicios if s["ID Paquete"] != id_eliminar]

                with open(archivo, mode='w', newline='', encoding='utf-8') as file:
                    campos = ["ID Paquete", "Precio", "Tipo Evento", "Duracion"]
                    escritor = csv.DictWriter(file, fieldnames=campos)
                    escritor.writeheader()
                    escritor.writerows(servicios)
                
                print(f"Servicio {id_eliminar} eliminado exitosamente.")
                break
            else:
                print("Operación cancelada.")
                break

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break

eliminar_servicio_photocampus()