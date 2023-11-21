# Project2

## Task - 1: 

Sitemap Parser:

This program parses the sitemap files from a given website to extract all the URLs and their date of creation (if available).

Website: The base website used for this demo is CNN (https://cnn.com). CNN has a large sitemap index with multiple sitemap files containing thousands of URLs from their site.

Approach:

The SitemapParser class takes the base URL of a website in the constructor. It first retrieves all the sitemap URLs listed in the robots.txt file. Then, it iterates through each sitemap, downloads the XML content, and extracts the <loc> and <lastmod> elements to get the URL and date of creation. This data is stored in a Pandas DataFrame and exported to a CSV file named after the sitemap.

Finally, the list of DataFrames is returned containing URLs and dates extracted from all sitemaps.

## Task - 2:

Reddit API Fetcher: This program fetches post data from a specified subreddit using the Reddit API.

Overview: The RedditAPIFetcher class handles making the API request and converting the JSON response into a Pandas DataFrame.

Key features:

Specify subreddit and number of posts to retrieve
Makes API request to retrieve posts
Extracts post data into a dictionary
Stores post data in a Pandas DataFrame
Returns the DataFrame and saves to a CSV file
Usage


