from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorEmail, SuscriptorSMS

#Crear canal
canal = CanalNoticias("Noticias del día")

#Crear suscriptores
suscriptor1 = SuscriptorEmail("Juan")
suscriptor2 = SuscriptorSMS("María")

#Suscribir al canal
canal.suscribir(suscriptor1)
canal.suscribir(suscriptor2)

#Publicar mensaje
canal.publicar("¡Últimas noticias! El clima será soleado mañana.")

#Imprimir mensajes recibidos por cada suscriptor
print(f"Canal: {canal.nombre}")
print(f"Último mensaje: {canal.ultimo_mensaje}")
print()

for observador in canal.observadores:
    print(f"{observador} ha recibido los siguientes mensajes:")
    for mensaje in observador.mensajes:
        print(f" - {mensaje}")
    print()