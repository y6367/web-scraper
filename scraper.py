import requests, time
import json
from bs4 import BeautifulSoup

def scrape_all_quotes():
    all_quotes = []
    page = 1

    while True:
        url = f"http://quotes.toscrape.com/page/{page}/"    
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for quote_div in soup.find_all("div", class_="quote"):
            text = quote_div.find("span", class_="text").get_text()
            author = quote_div.find("small", class_="author").get_text()
            all_quotes.append({"quote": text, "author": author})

        next_button = soup.find("li", class_="next")
        if not next_button:
            break

        page += 1
        print(f"Scraped page {page - 1}, total so far: {len(all_quotes)}")
        time.sleep(1)
    
    return all_quotes

# data = scrape_all_quotes()
# print(f"Done! Total quotes: {len(data)}")

# count = 1
# for quote in data:
#     print(f"Quote #{count}: {quote.get('quote')} - {quote.get('author')}")
#     count += 1

url = "https://stats.nba.com/stats/leagueLeaders"

params = {
    "LeagueID": "00",
    "PerMode": "PerGame",
    "Scope": "S",
    "Season": "2025-26",
    "SeasonType": "Regular Season",
    "StatCategory": "PTS"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
    "Host": "stats.nba.com"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

# the data comes back in a weird format — headers and rows are separate
columns = data["resultSet"]["headers"]
rows = data["resultSet"]["rowSet"]

for row in rows[:10]:  # first 10 players
    player = dict(zip(columns, row))
    print(f"{player['PLAYER']} - {player['PTS']} PPG")


# url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v3/competitions/8/seasons/2025/players/stats/leaderboard?_sort=goals%3Adesc&country=&_limit=10"
# headers = {
#     "Origin": "https://www.premierleague.com",
#     "Referer": "https://www.premierleague.com/"
# }

# response = requests.get(url, headers = headers)
# data = response.json()

nba_url = requests.get("https://www.nba.com/stats/leaders?SeasonType=Regular+Season")

print(nba_url.status_code)
print("hi")

# for players in data["data"]:
#     name = players["playerMetadata"]["name"]
#     team = players["playerMetadata"]["currentTeam"]["name"]
#     goals = players["stats"]["goals"]
#     print(f"{name} ({team}) - {goals} goals")

# response = requests.get("http://quotes.toscrape.com")
# print(response.status_code)

# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify()[:1000])

# quote = soup.find("div", class_="quote")
# print(quote)

# all_quotes = soup.find_all("div", class_="quote")
# print(all_quotes)

# for div in all_quotes:
    # text = div.find("span", class_="text").get_text()
    # print(div.find("span", class_="text").get_text())

# text = quote.find("span", class_="text").get_text()
# print(text)