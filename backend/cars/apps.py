from django.apps import AppConfig

class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    # def ready(self):
    #     # Import your management command and call it
    #     from cars.management.commands.load_cars_data import Command
    #     Command().handle()
