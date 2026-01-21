import requests
from bs4 import BeautifulSoup


def scrape_link(url):
    url = url.strip()  # Clean up the URL input
    headers = {'User-Agent': 'Mozilla/5.0'}
    links = []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return links


def save_links(links, filename='extracted_links.txt'):
    """Save links to a file."""
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')
            print(link)
    print(f"Links saved to {filename}")


if __name__ == "__main__":
    url = input("Please enter the URL to scrape : ")
    links = scrape_link(url)
    if links:  # Check if any links were found
        save_links(links)  # Save the extracted links to a file
    else:
        print("No links found or an error occurred.")
