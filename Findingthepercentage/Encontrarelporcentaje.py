if __name__ == '__main__':
    Cnt_Alumnos = int(input("Ingrese el numero de "))
    ALumnos_datos = {}
    for _ in range(Cnt_Alumnos):
        name, *line = input("Ingrese el nombre y las calificaciones: ").split()
        nota= list(map(float,line))
        ALumnos_datos[name]=nota

    queryStudent = input("Ingrese el nombre del alumno a consultar: ")
    if(queryStudent in ALumnos_datos):
        querynota=ALumnos_datos[queryStudent]
        notas=sum(querynota)/len(querynota)
        print(f"El Promedio es: {notas:.2f}")
    else:
        print("El estudiante no existe.")