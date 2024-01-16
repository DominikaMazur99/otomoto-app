# utils.py

import json
import requests
from bs4 import BeautifulSoup
from .models import Car  # Import your Car model

def scrape_otomoto_html(url, num_pages=1):
    for page in range(1, num_pages + 1):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)

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
                # Extracting car details and saving to the Car model
                for offer in data['mainEntity']['itemListElement']:
                    car_name = offer['itemOffered'].get('name', None)
                    brand = offer['itemOffered'].get('brand', None)
                    fuel_type = offer['itemOffered'].get('fuelType', None)

                    # Fetch 'mileage' from specific HTML element or class name
                    mileage_element = offer['itemOffered'].find('span', {'class': 'mileage-class'})
                    mileage_value = mileage_element.text if mileage_element else None
                    mileage = int(mileage_value) if mileage_value and mileage_value.isdigit() else None

                    # Fetch 'price' from specific HTML element or class name
                    price_element = offer.find('span', {'class': 'price-class'})
                    price_value = price_element.text if price_element else None
                    price = float(price_value.replace('PLN', '').replace(' ', '').replace(',', '.')) if price_value else None

                    # Extract the 'model' value from specific HTML element or class name
                    model_element = offer['itemOffered'].find('div', {'class': 'model-class'})
                    model = model_element.text if model_element else None

                    # Extract the 'modelDate' value
                    model_date = offer['itemOffered'].get('modelDate', None)

                    # Check if 'modelDate' is a number before assigning to 'year'
                    year = int(model_date) if model_date and model_date.isdigit() else None

                    # Save the extracted data to your Car model
                    Car.objects.create(
                        car_name=car_name,
                        brand=brand,
                        fuel_type=fuel_type,
                        mileage=mileage,
                        price=price,
                        model=model,
                        year=year  # Assuming 'year' is a field in your Car model
                    )

                    print(f"Saved {car_name} to the Car model.")

            else:
                print("Script tag not found.")

        else:
            print(f"Failed to fetch HTML from {page_url}. Status code: {response.status_code}")

# Example usage: scrape_otomoto_html('https://www.otomoto.pl/osobowe/', num_pages=5)
