from mensajes import mensaje_1, mensaje_2, mensaje_3


def obtener_analisis(tipo, respuestas):
    tipo_a = 0
    tipo_b = 0

    for registro in respuestas:
        tipo_pregunta = registro.pregunta.tipo.nombre.lower()

        if tipo_pregunta == tipo:
            if registro.respuesta == 1:
                tipo_a = tipo_a + 1
            else:
                tipo_b = tipo_b + 1

    res = tipo_a - tipo_b

    if res > 0:
        tipo_res = "A"
    else:
        tipo_res = "B"

    return abs(res), tipo_res;


def obtener_resultado(tipo, res, tipo_res):
    tipos = tipo.split("-")
    mensaje = ""

    if 1 <= res <= 3:
        return mensaje_1
    elif 5 <= res <= 7:
        if tipo_res == "A":
            mensaje = mensaje_2.format(tipos[0])
        else:
            mensaje = mensaje_2.format(tipos[1])
    elif 9 <= res <= 11:
        if tipo_res == "A":
            mensaje = mensaje_3.format(tipos[0])
        else:
            mensaje = mensaje_3.format(tipos[1])
    return mensaje




