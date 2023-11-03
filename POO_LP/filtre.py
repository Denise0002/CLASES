lista_alumnos=[
    {
        "nombre":"yerson",
        "edad":19,
        "hobby":"caminar",
        "flakita":"melody"
    },
    {
        "nombre":"emerson",
        "edad":15,
        "hobby":"dormir",
        "flakita":"melody"
    },
    {
        "nombre":"rony",
        "edad":21,
        "hobby":"comer",
        "flakita":"kiara"
    }
]
print(f"todos mis alumnitos{lista_alumnos}")
fans_kiara=list(filter(lambda par:par ["edad"]>49=="kiara",lista_alumnos))
print(f"los que quieren comer{fans_kiara}")

nuevo_objet=list(map(lambda par:{"nombre_alumno":par["nombre"],"germita":par["flakita"]},lista_alumnos))
print(nuevo_objet)