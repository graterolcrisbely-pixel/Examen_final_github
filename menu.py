from servicios import *

def menu_principal():
    while True:
        print("\n" + "~" * 35)
        print("      MENU PHOTOCAMPUS")
        print("~" * 35)
        print("1. Registrar nuevo servicio")
        print("2. Editar servicio por ID")
        print("3. Eliminar servicio por ID")
        print("4. Salir")
        print("~" * 35)
        
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            # Llama a la funcion de registro en servicios.py
            registrar_servicio_photocampus()
        
        elif opcion == "2":
            # Llama a la funcion de edicion en servicios.py
            editar_servicio_photocampus()
            
        elif opcion == "3":
            # Llama a la funcion de eliminacion en servicios.py
            eliminar_servicio_photocampus()
            
        elif opcion == "4":
            print("Ejecucion finalizada. Gracias por usar el sistema.")
            break
            
        else:
            print("Error: Opcion no reconocida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()