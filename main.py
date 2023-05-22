import requests
import selectorlib


URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extracter = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extracter.extract(source)["tours"]
    return value

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
