import requests
from bs4 import BeautifulSoup

# URL of the HTML content
url = "https://untitled-master.github.io/chesspuzzlesapi/"

# Fetch the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all puzzle div elements
puzzle_divs = soup.find_all("div", class_="puzzle")

# Loop through puzzle divs and extract img and move values
for puzzle in puzzle_divs:
  img_tag = puzzle.find("p", class_="img")
  move_tag = puzzle.find("p", class_="move")
  rating = puzzle.find("p", class_="rating")
  c_move = puzzle.find("p", class_="c_move")

  if img_tag and move_tag:
    img_url = img_tag.text.strip()
    move = move_tag.text.strip()
    rating = rating.text.strip()
    c_move = c_move.text.strip()

    print("Image URL:", img_url)
    print("Move:", move)
    print("Rating:", rating)
    print("Correct Move:", c_move)
    print()
