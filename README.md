# soupScrape

A thing that help you to scrape image from reddit.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install library.

```bash
pip install requests beautifulsoup4
```
```bash
pip install praw
```

## Usage

```python
python scrape.py
```

## More information

If you want to scrape image in another page just change the url and the sub reddit
Example:

```
url = 'https://www.reddit.com/r/Naruto/'
```
so
```
subreddit = reddit.subreddit('Naruto')
```

## Way to get api

[RedditDev](https://www.reddit.com/prefs/apps)
