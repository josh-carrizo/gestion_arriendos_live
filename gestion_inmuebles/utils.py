import re

def validar_rut(rut):
    rut = rut.upper().replace("-", "").replace(".", "")
    rut_body = rut[:-1]
    dv = rut[-1] #digito verificador

    if not rut_body.isdigit() or (dv not in "0123456789K"):
        return False

    suma = 0
    multiplicador = 2

    for digito in reversed(rut_body):
        suma += int(digito) * multiplicador
        multiplicador = 9 if multiplicador == 7 else multiplicador + 1

    dv_calculado = str(11 - (suma % 11))
    if dv_calculado == "10":
        dv_calculado = "K"
    elif dv_calculado == "11":
        dv_calculado = "0"

    return dv_calculado == dv