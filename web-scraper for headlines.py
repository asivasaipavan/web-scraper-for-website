import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"

def fetch_html(url):
    """Fetch page HTML using requests."""
    response = requests.get(url)
    response.raise_for_status()  
    return response.text

def extract_headlines(html):
    """Extract headlines from the HTML page using BeautifulSoup."""
    soup = BeautifulSoup(html, "html.parser")
    
    headlines = []

    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines

def save_headlines(headlines):
    """Save scraped headlines to a text file."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(line + "\n")

def main():
    print("Fetching news headlines...")

    try:
        html = fetch_html(URL)
        headlines = extract_headlines(html)

        if headlines:
            save_headlines(headlines)
            print(f"Scraped {len(headlines)} headlines successfully!")
            print(f"Saved to {OUTPUT_FILE}")
        else:
            print("No headlines found.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
