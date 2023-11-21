# Project2

## Task - 1: 

Sitemap Parser:

This program parses the sitemap files from a given website to extract all the URLs and their date of creation (if available).

Website: The base website used for this demo is CNN (https://cnn.com). CNN has a large sitemap index with multiple sitemap files containing thousands of URLs from their site.

Approach:

The SitemapParser class takes the base URL of a website in the constructor. It first retrieves all the sitemap URLs listed in the robots.txt file. Then, it iterates through each sitemap, downloads the XML content, and extracts the <loc> and <lastmod> elements to get the URL and date of creation. This data is stored in a Pandas DataFrame and exported to a CSV file named after the sitemap.

Finally, the list of DataFrames is returned containing URLs and dates extracted from all sitemaps.
