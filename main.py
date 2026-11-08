from funciones import (
    registrar_paciente,
    registrar_medico,
    programar_cita,
    registrar_atencion,
    consultar_historial,
    buscar_por_especialidad
)


def mostrar_menu():
    print("\n========== SISTEMA KAWSAY ==========")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Programar cita")
    print("4. Registrar atención")
    print("5. Consultar historial")
    print("6. Buscar médico por especialidad")
    print("7. Salir")
    print("====================================")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_paciente()

        elif opcion == "2":
            registrar_medico()

        elif opcion == "3":
            programar_cita()

        elif opcion == "4":
            registrar_atencion()

        elif opcion == "5":
            consultar_historial()

        elif opcion == "6":
            buscar_por_especialidad()

        elif opcion == "7":
            print("Gracias por utilizar el Sistema Kawsay.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()