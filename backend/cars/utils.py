# cars/utils.py
import json
import requests
from bs4 import BeautifulSoup
from .models import Car  # Import your Car model

def scrape_otomoto_html(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the script tag with the id 'listing-json-ld'
        script_tag = soup.find('script', {'id': 'listing-json-ld'})

        if script_tag:
            # Extract the content of the script tag
            json_data = script_tag.string

            # Parse the JSON data
            data = json.loads(json_data)

            # Now 'data' contains the structured information
            # Example: extracting car details and saving to the Car model
            for offer in data['mainEntity']['itemListElement']:
                car_name = offer['itemOffered']['name']
                brand = offer['itemOffered']['brand']
                fuel_type = offer['itemOffered'].get('fuelType', 'undefined')
                mileage = offer['itemOffered'].get('mileageFromOdometer', {}).get('value', 'undefined')

                # Save the extracted data to your Car model
                Car.objects.create(
                    car_name=car_name,
                    brand=brand,
                    fuel_type=fuel_type,
                    mileage=mileage,
                )

                print(f"Saved {car_name} to the Car model.")

            return data
        else:
            print("Script tag not found.")
            return None

    else:
        print(f"Failed to fetch HTML from {url}. Status code: {response.status_code}")
        return None
