import json
from django.core.management.base import BaseCommand
from ...models import Inmueble, Comuna, Perfil

class Command(BaseCommand):
    help = "Cargar inmuebles en la base de datos desde un archivo JSON."

    def handle(self, *args, **kwargs):
        with open('gestion_inmuebles/management/json/inmuebles.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for inmueble_data in data["inmuebles"]:
                comuna = Comuna.objects.get(pk=inmueble_data["comuna_id"])
                arrendador = Perfil.objects.get(pk=inmueble_data["arrendador_id"])
                
                inmueble, created = Inmueble.objects.get_or_create(
                    nombre=inmueble_data["nombre"],
                    defaults={
                        "descripcion": inmueble_data["descripcion"],
                        "metros_construidos": inmueble_data["metros_construidos"],
                        "metros_totales": inmueble_data["metros_totales"],
                        "cantidad_estacionamientos": inmueble_data["cantidad_estacionamientos"],
                        "cantidad_habitaciones": inmueble_data["cantidad_habitaciones"],
                        "cantidad_banos": inmueble_data["cantidad_banos"],
                        "direccion": inmueble_data["direccion"],
                        "comuna": comuna,
                        "tipo_inmueble": inmueble_data["tipo_inmueble"],
                        "precio_mensual": inmueble_data["precio_mensual"],
                        "arrendador": arrendador
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Inmueble '{inmueble.nombre}' creado."))
                else:
                    self.stdout.write(self.style.WARNING(f"Inmueble '{inmueble.nombre}' ya existía, se omitió."))

        self.stdout.write(self.style.SUCCESS("Datos de inmuebles cargados correctamente."))
