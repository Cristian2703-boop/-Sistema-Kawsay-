from paciente import Paciente
from medico import Medico
from cita import Cita

pacientes = []
medicos = []
citas = []
atenciones = []


def registrar_paciente():
    print("\n--- REGISTRO DE PACIENTE ---")

    codigo = input("Ingrese el código del paciente: ")

    # Verificar que el código no esté repetido
    for paciente in pacientes:
        if paciente.codigo == codigo:
            print("Error: El código ya está registrado.")
            return

    nombre = input("Ingrese el nombre: ")

    try:
        edad = int(input("Ingrese la edad: "))

        if edad < 0 or edad > 120:
            print("Error: La edad debe estar entre 0 y 120.")
            return

    except ValueError:
        print("Error: La edad debe ser un número.")
        return

    nuevo_paciente = Paciente(codigo, nombre, edad)
    pacientes.append(nuevo_paciente)

    print("Paciente registrado correctamente.")


def registrar_medico():
    print("\n--- REGISTRO DE MÉDICO ---")

    codigo = input("Ingrese el código del médico: ")

    # Verificar que el código no esté repetido
    for medico in medicos:
        if medico.codigo == codigo:
            print("Error: El código ya está registrado.")
            return

    nombre = input("Ingrese el nombre: ")
    especialidad = input("Ingrese la especialidad: ")

    nuevo_medico = Medico(codigo, nombre, especialidad)
    medicos.append(nuevo_medico)

    print("Médico registrado correctamente.")


def buscar_paciente(codigo):
    for paciente in pacientes:
        if paciente.codigo == codigo:
            return paciente

    return None


def buscar_medico(codigo):
    for medico in medicos:
        if medico.codigo == codigo:
            return medico

    return None


def programar_cita():
    print("\n--- PROGRAMAR CITA ---")

    codigo_cita = input("Ingrese el código de la cita: ")

    for cita in citas:
        if cita.codigo == codigo_cita:
            print("Error: El código de la cita ya está registrado.")
            return

    codigo_paciente = input("Ingrese el código del paciente: ")
    paciente = buscar_paciente(codigo_paciente)

    if paciente is None:
        print("Error: El paciente no está registrado.")
        return

    codigo_medico = input("Ingrese el código del médico: ")
    medico = buscar_medico(codigo_medico)

    if medico is None:
        print("Error: El médico no está registrado.")
        return

    fecha = input("Ingrese la fecha de la cita: ")

    nueva_cita = Cita(codigo_cita, paciente, medico, fecha)
    citas.append(nueva_cita)

    print("Cita programada correctamente.")


def registrar_atencion():
    print("\n--- REGISTRO DE ATENCIÓN ---")

    codigo_paciente = input("Ingrese el código del paciente: ")
    paciente = buscar_paciente(codigo_paciente)

    if paciente is None:
        print("Error: El paciente no está registrado.")
        return

    codigo_medico = input("Ingrese el código del médico: ")
    medico = buscar_medico(codigo_medico)

    if medico is None:
        print("Error: El médico no está registrado.")
        return

    descripcion = input("Ingrese la descripción de la atención: ")

    atencion = {
        "codigo_paciente": paciente.codigo,
        "codigo_medico": medico.codigo,
        "descripcion": descripcion
    }

    atenciones.append(atencion)

    print("Atención registrada correctamente.")


def consultar_historial():
    print("\n--- HISTORIAL DE ATENCIONES ---")

    codigo = input("Ingrese el código del paciente: ")
    paciente = buscar_paciente(codigo)

    if paciente is None:
        print("Error: El paciente no está registrado.")
        return

    print(f"\nHistorial de: {paciente.nombre}")

    encontrado = False

    for atencion in atenciones:
        if atencion["codigo_paciente"] == codigo:
            print(f"Médico: {atencion['codigo_medico']}")
            print(f"Descripción: {atencion['descripcion']}")
            print("-----------------------------")
            encontrado = True

    if not encontrado:
        print("Este paciente no tiene atenciones registradas.")


def buscar_por_especialidad():
    print("\n--- BÚSQUEDA POR ESPECIALIDAD ---")

    especialidad = input("Ingrese la especialidad que desea buscar: ")

    resultado = filter(
        lambda medico: medico.especialidad.lower() == especialidad.lower(),
        medicos
    )

    encontrados = list(resultado)

    if encontrados:
        print("\nMédicos encontrados:")

        for medico in encontrados:
            print(medico.resumen())
    else:
        print("No se encontraron médicos con esa especialidad.")