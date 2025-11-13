thonimport requests
from bs4 import BeautifulSoup

def parse_facebook_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    page_data = {
        "photoURL": soup.find("img", {"class": "profilePic"})["src"],
        "pageName": soup.find("h1").text.strip(),
        "isVerified": "yes" if soup.find("span", {"class": "verified"}) else "no",
        "tag": soup.find("span", {"class": "category"}).text.strip(),
        "reviews": soup.find("div", {"class": "review-count"}).text.strip() if soup.find("div", {"class": "review-count"}) else None,
        "priceRange": soup.find("span", {"class": "price-range"}).text.strip() if soup.find("span", {"class": "price-range"}) else None,
        "location": soup.find("span", {"class": "location"}).text.strip() if soup.find("span", {"class": "location"}) else None,
        "hoursOpen": soup.find("span", {"class": "hours"}).text.strip() if soup.find("span", {"class": "hours"}) else None,
        "followers": soup.find("span", {"class": "follower-count"}).text.strip(),
        "pageSlug": soup.find("meta", {"property": "og:url"})["content"].split('/')[-1],
        "pageLink": soup.find("meta", {"property": "og:url"})["content"]
    }
    
    return page_data