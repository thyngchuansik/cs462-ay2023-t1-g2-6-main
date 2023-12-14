
import csv
from playwright.sync_api import sync_playwright

# Initialize Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()

    # Create a CSV file for data storage
    with open('data/addr.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["long", "lat", "location"])

        page = context.new_page()
        page.goto('https://www.fakexy.com/fake-address-generator-sg') 

        for _ in range(100):  # Refresh the page 100 times
            page.reload()
            long = page.locator('xpath=/html/body/div[4]/div/div[1]/table/tbody/tr[8]/td[2]').inner_text()
            lat = page.locator('xpath=/html/body/div[4]/div/div[1]/table/tbody/tr[7]/td[2]').inner_text()
            location = page.locator('xpath=/html/body/div[4]/div/div[1]/table/tbody/tr[1]/td[2]').inner_text()
            print(long,lat,location)
            csv_writer.writerow([long, lat, location])

    context.close()
    browser.close()
