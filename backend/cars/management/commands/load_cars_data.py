# cars/management/commands/load_cars_data.py

from django.core.management.base import BaseCommand
from cars.utils import scrape_otomoto_html

class Command(BaseCommand):
    help = 'Fetches data from API and loads it into the Car model'

    def handle(self, *args, **options):
        url = 'https://www.otomoto.pl/osobowe/'
        data = scrape_otomoto_html(url)

        if data:
            print(f"Received data: {data}")

            # Uncomment the following lines to save data to the Car model
            # for now, let's just print the information
            for offer in data['mainEntity']['itemListElement']:
                car_name = offer['itemOffered'].get('name', None)
                brand = offer['itemOffered'].get('brand', None)
                fuel_type = offer['itemOffered'].get('fuelType', None)
                mileage = offer['itemOffered']['mileageFromOdometer'].get('value', None)
                price_specification = offer.get('priceSpecification', {})
                price = price_specification.get('price', None)
                model_date = offer['itemOffered'].get('modelDate', None)
                year = int(model_date) if model_date and model_date.isdigit() else None

                print(f"Car Name: {car_name}, Brand: {brand}, Fuel Type: {fuel_type}, Mileage: {mileage}, Price: {price}, Year: {year}")

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to load data'))
