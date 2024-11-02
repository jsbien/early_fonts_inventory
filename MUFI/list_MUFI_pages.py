# ChatGPT 4o implementing specification by Janusz S. Bień
# 2024-11-02
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Define the starting URL and maximum depth for crawling
start_url = "https://mufi.info/"
max_depth = 5

# Initialize a set to store unique URLs and avoid duplicates
urls = set()

# Function to recursively collect links up to the specified depth
def collect_links(url, depth):
    # Stop if maximum depth is reached
    if depth > max_depth:
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all anchor tags with href attributes
        for link in soup.find_all("a", href=True):
            # Extract the href attribute
            href = link["href"]

            # Ensure the correct path structure for URLs starting with '?p='
            if href.startswith("?p="):
                # Prepend 'q.php' to links that only start with '?p='
                href = "q.php" + href
            
            # Resolve the full URL
            full_url = urljoin(url, href)
            
            # Check if the URL belongs to the mufi.info domain
            parsed_url = urlparse(full_url)
            if parsed_url.netloc == "mufi.info" and full_url not in urls:
                urls.add(full_url)
                # Recursively collect links from this page, increasing the depth
                collect_links(full_url, depth + 1)
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Start crawling from the initial URL at depth 1
collect_links(start_url, 1)

# Save URLs in the plain text format required for changedetection.io
with open("mufi_urls_to_monitor.txt", "w") as file:
    for url in urls:
        file.write(f"{url} mufi, subpages\n")

print("URLs saved to mufi_urls_to_monitor.txt")