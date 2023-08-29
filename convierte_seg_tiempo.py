
def conv_seg(total_segundos):
    """Programa que convierte los segundos en formato de tiempo."""
    if total_segundos == 0:
        return "0s"

    años = 0     # 1 año ---> 31536000 segundos
    dias = 0     # 1 dia ---> 86400 segundos
    horas = 0    # 1 hora ---> 3600 segundos
    minutos = 0  # 1 minuto ---> 60 segundos

    if total_segundos >= 31536000:
        años = total_segundos//31536000
        total_segundos = total_segundos % 31536000
    else:
        años = 0

    if total_segundos >= 86400:
        dias = total_segundos//86400
        total_segundos = total_segundos % 86400
    else:
        dias = 0

    if total_segundos >= 3600:
        horas = total_segundos//3600
        total_segundos = total_segundos % 3600
    else:
        horas = 0

    if total_segundos >= 60:
        minutos = total_segundos//60
        total_segundos = total_segundos % 60
    else:
        minutos = 0

    segundos = total_segundos

    hms = []
    if años > 0:
        hms.append(str(años)+"a")
    if dias > 0:
        hms.append(str(dias)+"d")
    if horas > 0:
        hms.append(str(horas)+"h")
    if minutos > 0:
        hms.append(str(minutos)+"m")
    if segundos > 0:
        hms.append(str(segundos)+"s")
    return " ".join(hms)

print(conv_seg(333898601))








