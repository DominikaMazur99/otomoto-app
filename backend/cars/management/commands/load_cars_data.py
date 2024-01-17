from django.core.management.base import BaseCommand
from cars.utils import scrape_otomoto_html

class Command(BaseCommand):
    help = 'Fetches data from API and loads it into the Car model'

    def handle(self, *args, **options):
        url = 'https://www.otomoto.pl/osobowe/'
        data = scrape_otomoto_html(url)

        if data:
            print(f"Received data: {data}")
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to load data'))
