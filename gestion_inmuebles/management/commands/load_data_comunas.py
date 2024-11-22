import json
from django.core.management.base import BaseCommand
from ...models import Region, Comuna  

class Command(BaseCommand):
    help = "Cargar datos de regiones y comunas en la base de datos desde un archivo JSON."

    def handle(self, *args, **kwargs):
        with open('gestion_inmuebles/management/json/regiones_y_comunas.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for region_data in data["regions"]:
                nombre_region = region_data["name"]
                numero_region = region_data["number"]
                
                region, created = Region.objects.get_or_create(
                    nombre_region=nombre_region,
                    numero_region=numero_region
                )
                
                for comuna_data in region_data["communes"]:
                    nombre_comuna = comuna_data["name"]
                    codigo_postal = comuna_data["postalCode"]
                    
                    Comuna.objects.get_or_create(
                        nombre_comuna=nombre_comuna,
                        codigo_postal=codigo_postal,
                        region=region
                    )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Región '{nombre_region}' creada con sus comunas."))
                else:
                    self.stdout.write(self.style.WARNING(f"Región '{nombre_region}' ya existía, se omitieron duplicados."))

        self.stdout.write(self.style.SUCCESS("Datos de regiones y comunas cargados correctamente."))
