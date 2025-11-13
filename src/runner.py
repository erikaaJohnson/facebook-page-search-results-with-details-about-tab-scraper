thonimport json
import time
from extractors.facebook_parser import parse_facebook_page
from extractors.utils_time import wait_for_scroll

def main():
    search_urls = ["https://www.facebook.com/search/pages/?q=example"]
    results = []
    
    for url in search_urls:
        page_data = parse_facebook_page(url)
        results.append(page_data)
        wait_for_scroll()
    
    with open("output.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()