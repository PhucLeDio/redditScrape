import os
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import praw # pip install praw

# Reddit API credentials
client_id = ''
client_secret = ''
user_agent = ''

### check this link to create developer account and get api credentials :>>
#### https://www.reddit.com/prefs/apps

# Create folder to store images
folder_name = 'reddit_images'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

print("Ready!")

# Initialize Reddit instance
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Fetch posts from a subreddit using the Reddit API
subreddit = reddit.subreddit('pics')
posts = subreddit.hot(limit=)  # Adjust the limit as needed

# Extract image URLs from the API and download images
image_urls = set()  # Using a set to avoid duplicates
for post in posts:
    if post.url.endswith(('jpg', 'jpeg', 'png')):
        image_urls.add(post.url)

# Send request to the Reddit page and parse the content
url = 'https://www.reddit.com/r/pics/' # scrape r/pics available to change :>>
headers = {'User-Agent': user_agent}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

print("Exceed charge!")

# Extract image URLs from the HTML
for img_tag in soup.find_all('img'):
    img_url = img_tag.get('src')
    if img_url and img_url.endswith(('jpg', 'jpeg', 'png')):
        image_urls.add(img_url)

# Download all unique images
for i, img_url in enumerate(image_urls):
    try:
        img_data = requests.get(img_url).content
        img_extension = img_url.split('.')[-1]
        img_name = os.path.join(folder_name, f'image_{i+1}.{img_extension}')
        with open(img_name, 'wb') as handler:
            handler.write(img_data)
        print(f'{img_name} downloaded.')
    except Exception as e:
        print(f'Failed to download {img_url}: {e}')

print("Go...go...go...gorgeous!") # wibu tí :>>