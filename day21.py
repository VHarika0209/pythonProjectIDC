import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.thehindu.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    print("📰 Top The Hindu News Headlines:\n")
    headlines = soup.find_all('h3')

    # Print the first 10 headlines
    for i, headline in enumerate(headlines[:10], 1):
        print(f"{i}. {headline.get_text(strip=True)}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

