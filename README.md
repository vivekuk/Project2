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

1. Specify subreddit and number of posts to retrieve
2. Makes API request to retrieve posts
3. Extracts post data into a dictionary
4. Stores post data in a Pandas DataFrame
5. Returns the DataFrame and saves to a CSV file

## Task - 3:

# Movie Data Scraper

This program scrapes movie data from the IMDb API and analyzes it.

## Overview

The `MovieDataScraper` class handles:

- Querying the API to get movie IDs and details
- Scraping data for multiple movies into a Pandas DataFrame
- Saving the DataFrame to a CSV
- Generating plots for analysis

## Methodology

- The IMDb API is used to search for movie IDs and fetch details 
- Movie IDs are retrieved in batches using pagination
- Details are fetched for each ID to build the final dataset
- Plots are generated using Matplotlib and Seaborn
  
## Usage

Basic steps to use:

1. Instantiate `MovieDataScraper` 
2. Call `scrape_movies_data()` with a search query 
3. Access the returned DataFrame
4. Call data visualization methods for analysis plots
5. Call `save_movies_data_csv()` to export data



## Visualizations

The plots below provide some sample analysis on the scraped data:


![Rating Distribution](visualizations/rating_distribution.png)

Description: 
Distribution of Movie Ratings

This bar graph shows the distribution of movie ratings in the United States. The most common movie rating is PG, followed by PG-13, TV-14, and TV-G. The least common movie ratings are TV-MA, R, and Not Rated.

PG movies are the most common type of movie released.
PG-13 movies are also very common, but they are slightly less common than PG movies.
R movies are the second least common type of movie released 

![Runtime For Different Genres](visualizations/runtime_by_genre.png)

Description:
Runtime Distribution Across Genres

This graph shows the average runtime of movies in each genre, as well as the range of runtimes within each genre. The genres are listed on the y-axis, and the runtimes are listed on the x-axis.
The average runtime of movies varies widely across genres. For example, documentaries have an average runtime of 87 minutes, while musicals have an average runtime of 122 minutes.
The range of runtimes within each genre is also large. For example, the shortest documentary is 25 minutes long, while the longest is 164 minutes long.
However, there are some trends in the data. For example, comedies tend to be shorter than dramas, and action movies tend to be longer than documentaries.

![Year Wise Movie Distributions](visualizations/year_distribution.png)

Decription: 

Distribution of Movie Years

This graph shows the distribution of movie years, based on the release dates of over 100,000 movies. The x-axis shows the movie year, and the y-axis shows the number of movies released in that year. It shows the most movies were released in the 1980s, followed by the 1990s, the 2000s, and the 2010s. The fewest movies were released in the 1920s and 1930s.
The global film industry has grown significantly over time.

