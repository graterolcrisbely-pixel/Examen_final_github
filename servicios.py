import csv

class GestionPhotoCampus:
    def __init__(self, archivo_csv="servicios_photocampus.csv"):
        self.archivo_csv = archivo_csv
        self.preparar_archivo()

    def preparar_archivo(self):
        """Verifica si el archivo existe intentando abrirlo, si no, lo crea con encabezados."""
        try:
            with open(self.archivo_csv, mode='r', encoding='utf-8') as file:
                pass
        except FileNotFoundError:
            with open(self.archivo_csv, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Nombre Paquete", "Precio", "Tipo Evento", "Duracion"])

    def servicio_existe(self, nombre_paquete):
        """Verifica si el paquete ya esta en el archivo CSV."""
        try:
            with open(self.archivo_csv, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for fila in reader:
                    if fila["Nombre Paquete"].lower() == nombre_paquete.strip().lower():
                        return True
            return False
        except FileNotFoundError:
            return False

    def solicitar_dato_numerico(self, mensaje, tipo):
        """Solicita un valor numerico (float) y no sale hasta que sea valido."""
        while True:
            try:
                valor = float(input(mensaje))
                if valor <= 0:
                    print("El valor debe ser mayor a cero.")
                    continue
                return valor
            except ValueError:
                print("Error: Entrada invalida. Por favor ingrese solo numeros.")

    def solicitar_tipo_evento(self):
        """Solicita el tipo de evento y valida que solo contenga letras."""
        while True:
            evento = input("Ingrese el tipo de evento (ej. Boda, Retrato): ").strip()
            # Quitamos espacios para validar solo letras
            if evento.replace(" ", "").isalpha():
                return evento
            else:
                print("Error: El tipo de evento solo debe contener letras.")

    def registrar_servicio(self):
        """Metodo principal para capturar datos y registrar el servicio."""
        print("\n--- Registro de Nuevo Servicio PhotoCampus ---")
        
        nombre = input("Nombre del paquete fotografico: ").strip()
        
        if self.servicio_existe(nombre):
            print(f"Error: El paquete '{nombre}' ya esta registrado.")
            return

        precio = self.solicitar_dato_numerico("Ingrese el precio: ", float)
        tipo_evento = self.solicitar_tipo_evento()
        duracion = self.solicitar_dato_numerico("Ingrese la duracion estimada (en horas): ", float)

        try:
            with open(self.archivo_csv, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([nombre, precio, tipo_evento, duracion])
            print(f"Servicio '{nombre}' guardado exitosamente.")
        except Exception as e:
            print(f"No se pudo guardar el archivo: {e}")

# --- Ejecucion del programa ---
sistema = GestionPhotoCampus()
sistema.registrar_servicio()