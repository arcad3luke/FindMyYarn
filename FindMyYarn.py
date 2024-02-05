from googlesearch import search
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def open_links_in_tabs_with_scrape(links):
    driver = webdriver.Chrome()
    tabs_count = 0

    for link in links:
        try:
            driver.get(link)
            time.sleep(2)  # Adjust sleep duration as needed for the page to load

            # Scraping yarn characteristics from the webpage
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Example: Extracting yarn name and material, adjust as needed based on the webpage structure
            yarn_name = soup.find('h1').text.strip()
            yarn_material = soup.find('span', {'class': 'material'}).text.strip()

            # Print or use the extracted information as needed
            print(f"Yarn Name: {yarn_name}\nMaterial: {yarn_material}\nLink: {link}\n{'='*30}")

            tabs_count += 1
            if tabs_count >= 10:
                break

        except Exception as e:
            print(f"Error processing link: {link}. Error: {e}")

    return driver

# Function to perform a yarn search based on various factors
def yarn_search(material, needle_hook_size, skein_size, weight, dye_batch, yardage, project_count, color_query):
    weight_categories = {
        'lace': 'Lace Weight',
        'superfine': 'Super Fine - Fingering or Sock',
        'fine': 'Fine Weight - Sport',
        'light': 'Light Weight - Double Knit (DK Yarn)',
        'medium': 'Medium Weight - Worsted and Aran',
        'bulky': 'Bulky Weight',
        'superbulky': 'Super Bulky',
        'jumbo': 'Jumbo'
    }

    skein_sizes = {
        '1 ounce': '1 ounce',
        '50 grams': '50 grams',
        '100 grams': '100 grams',
        '200 grams': '200 grams'
    }

    needle_hook_sizes = {
        '1.5 mm': '1.5 mm',
        '1.75 mm': '1.75 mm',
        '2 mm': '2 mm',
        '2.25 mm': '2.25 mm',
        '2.5 mm': '2.5 mm',
        '2.75 mm': '2.75 mm',
        '3 mm': '3 mm',
        '3.25 mm': '3.25 mm',
        '3.5 mm': '3.5 mm',
        '3.75 mm': '3.75 mm',
        '4 mm': '4 mm',
        '4.25 mm': '4.25 mm',
        '4.5 mm': '4.5 mm',
        '5 mm': '5 mm',
        '5.5 mm': '5.5 mm',
        '6 mm': '6 mm',
        '6.5 mm': '6.5 mm',
        '7 mm': '7 mm',
        '7.5 mm': '7.5 mm',
        '8 mm': '8 mm',
        '9 mm': '9 mm',
        '10 mm': '10 mm',
        '12.75 mm': '12.75 mm',
        '15 mm': '15 mm',
        '16 mm': '16 mm',
        '19 mm': '19 mm',
        '25 mm': '25 mm'
    }

    materials = {
        'alpaca': 'Alpaca',
        'wool': 'Wool',
        'bamboo': 'Bamboo',
        'linen': 'Linen',
        'cashmere': 'Cashmere',
        'mohair': 'Mohair',
        'silk': 'Silk',
        'acrylic': 'Acrylic',
        'merino': 'Merino',
        'cotton': 'Cotton',
        'rayon': 'Rayon',
        'blended yarns': 'Blended Yarns',
        'cotton yarn': 'Cotton Yarn',
        'nylon': 'Nylon',
        'polyester': 'Polyester',
        'faux fur': 'Faux Fur',
        'llama': 'Llama',
        'synthetic': 'Synthetic',
        'hemp': 'Hemp',
        'cellulose fibers': 'Cellulose Fibers',
        'angora': 'Angora',
        'cabled yarn': 'Cabled Yarn',
        'bulky': 'Bulky',
        'jumbo weight yarn': 'Jumbo Weight Yarn'
    }

    # Map user input to weight category
    weight_category = weight_categories.get(weight.lower(), 'Unknown Weight')

    # Map user input to skein size
    skein_size_category = skein_sizes.get(skein_size.lower(), 'Unknown Size')

    # Map user input to needle or hook size
    needle_hook_size_category = needle_hook_sizes.get(needle_hook_size.lower(), 'Unknown Size')

    # Map user input to material
    material_category = materials.get(material.lower(), 'Unknown Material')

    # Create the query without dye batch and project count if not provided
    query = f"{material_category} {needle_hook_size_category} {skein_size_category} {weight_category} {dye_batch} {yardage} {project_count} {color_query}" if dye_batch and project_count else f"{material_category} {needle_hook_size_category} {skein_size_category} {weight_category} {dye_batch} {yardage} {color_query}" if dye_batch else f"{material_category} {needle_hook_size_category} {skein_size_category} {weight_category} {yardage} {project_count} {color_query}" if project_count else f"{material_category} {needle_hook_size_category} {skein_size_category} {weight_category} {yardage} {color_query}"

    search_results = search(query, num_results=10)
    return search_results

# Get additional factors from user input
material = input("Material (e.g., wool, cotton): ")
needle_hook_size = input("Needle/Hook Size: ")
skein_size = input("Skein Size (1 ounce, 50 grams, 100 grams, 200 grams): ")
weight = input("Weight (lace, superfine, fine, light, medium, bulky, superbulky, jumbo): ")
dye_batch = input("Dye Batch (optional, press Enter if not applicable): ")
yardage = input("Yardage: ")
project_count = input("Count needed for various projects (optional, press Enter if not applicable): ")

# Perform yarn search based on various factors
search_results = yarn_search(material, needle_hook_size, skein_size, weight, dye_batch, yardage, project_count, "")

# Open links in new tabs with web scraping (limited to 10)
driver = open_links_in_tabs_with_scrape(search_results)

# Wait for user input before exiting
print("Tabs are open. Close the browser manually when you are done.")
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

# Quit the browser when the loop is terminated
driver.quit()
