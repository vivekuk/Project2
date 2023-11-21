import pandas as pd
import requests

class RedditAPIFetcher:
    def __init__(self, query,limit=1000):
        self.query = query
        self.API = f"https://www.reddit.com/r/{self.query}.json"
        self.params = {"limit": limit}

    def API_CALL(self):
        try:
            # Make API request
            headers = {"User-Agent": "App/1.0 (by QueryUsername)"}
            resp = requests.get(self.API, params = self.params,headers=headers)
            resp.raise_for_status()  #if there is any error, raise the error
            # Extract data into DataFrame
            data = resp.json()
            reddit_posts = []
            for post_data in data.get("data", {}).get("children", []):
                post = post_data.get("data", {})
                reddit_posts.append({
                    "title": post.get("title"),
                    "score": post.get("score"),
                    "subreddit": self.query,
                    "num_comments": post.get("num_comments"),
                    "author": post.get("author"),
                    "created_utc": post.get("created_utc"),
                    "url": post.get("url"),
                    "selftext": post.get("selftext"),
                    "upvote_ratio": post.get("upvote_ratio"),
                    "is_original_content": post.get("is_original_content"),
                    "is_video": post.get("is_video"),
                    "link_flair_text": post.get("link_flair_text"),
                    "domain": post.get("domain"),
                    "stickied": post.get("stickied"),
                    "is_locked": post.get("locked"),
                    "spoiler": post.get("spoiler"),
                    "num_awards": post.get("total_awards_received"),
                    "author_flair_text": post.get("author_flair_text"),
                    "gilded": post.get("gilded"),
                    "is_crosspostable": post.get("is_crosspostable"),
                    "media": post.get("media"),
                    "post_hint": post.get("post_hint"),
                    "thumbnail": post.get("thumbnail"),
                    "upvote_ratio": post.get("upvote_ratio"),
                    "is_original_content": post.get("is_original_content"),
                    "is_video": post.get("is_video"),
                    "link_flair_text": post.get("link_flair_text"),
                    "domain": post.get("domain"),
                    "stickied": post.get("stickied"),
                    "is_locked": post.get("locked"),
                    "spoiler": post.get("spoiler"),
                    "num_awards": post.get("total_awards_received"),
                    "author_flair_text": post.get("author_flair_text"),
                    "gilded": post.get("gilded"),
                    "is_crosspostable": post.get("is_crosspostable"),
                    "media": post.get("media"),
                    "post_hint": post.get("post_hint"),
                    "thumbnail": post.get("thumbnail"),
                })
            #store it as a dataframe
            self.reddit_posts = pd.DataFrame(reddit_posts)
            return self.reddit_posts

        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None

    def get_data(self):
        self.API_CALL()
        self.reddit_posts.to_csv("Reddit_Task2_data.csv")
        return self.reddit_posts
        
        
