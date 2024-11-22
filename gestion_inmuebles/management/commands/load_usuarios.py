import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Perfil, Comuna

class Command(BaseCommand):
    help = "Cargar usuarios en la base de datos desde un archivo JSON."

    def handle(self, *args, **kwargs):
        with open('gestion_inmuebles/management/json/usuarios.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for usuario_data in data["usuarios"]:
                user, created = User.objects.get_or_create(
                    username=usuario_data["username"],
                    defaults={
                        "email": usuario_data["email"],
                        "first_name": usuario_data["first_name"],
                        "last_name": usuario_data["last_name"],
                    }
                )
                if created:
                    user.set_password(usuario_data["password"])
                    user.save()

                    comuna = Comuna.objects.get(pk=usuario_data["comuna_id"])
                    Perfil.objects.create(
                        usuario=user,
                        nombres=usuario_data["nombres"],
                        apellidos=usuario_data["apellidos"],
                        rut=usuario_data["rut"],
                        direccion=usuario_data["direccion"],
                        telefono=usuario_data["telefono"],
                        correo_electronico=usuario_data["email"],
                        tipo_usuario=usuario_data["tipo_usuario"],
                        comuna=comuna
                    )
                    self.stdout.write(self.style.SUCCESS(f"Usuario '{user.username}' creado con su perfil."))
                else:
                    self.stdout.write(self.style.WARNING(f"Usuario '{user.username}' ya existía, se omitió."))

        self.stdout.write(self.style.SUCCESS("Datos de usuarios cargados correctamente."))
