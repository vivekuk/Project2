import requests
import pandas as pd
from lxml import etree

class SitemapParser:
    def __init__(self, base_url):
        # Initialize the SitemapParser with a base URL
        self.base_url = base_url
        # List to store discovered sitemap URLs
        self.sitemaps = []

    def retrieve_sitemaps(self):
        # Retrieve sitemap URLs from the robots.txt file
        response = requests.get(self.base_url + '/robots.txt')
        for line in response.text.splitlines():
            if line.startswith('Sitemap:'):
                # Extract and store sitemap URLs
                sitemap_url = line.split(': ')[1]
                self.sitemaps.append(sitemap_url)

    def parse_individual_sitemap(self, sitemap_url):
        # Parse individual sitemap and extract URLs and creation dates
        response = requests.get(sitemap_url)
        root = etree.fromstring(response.content)
        urls = []
        for elem in root:
            temp = []
            for i in elem:
                temp.append(i.text)
            # Add None for missing creation date
            if len(temp) == 1:
                temp.append(None)
            urls.append(temp[:2])
        return urls

    def parse_all_sitemaps(self):
        # Retrieve sitemaps and parse their content
        self.retrieve_sitemaps()
        all_urls = []
        all_dataframes = []
        print("Number of Sitemaps:", len(self.sitemaps))
        for sitemap in self.sitemaps:
            try:
                urls = self.parse_individual_sitemap(sitemap)
                all_urls.extend(urls)
                # Create a DataFrame for each sitemap and store them
                df = pd.DataFrame(all_urls, columns=['url', "date_of_creation"])
                df.to_csv("Sitemap_{}.csv".format(sitemap.replace('/', '_').replace(':', '_').replace('.', '_')))
                all_dataframes.append(df)
            except:
                pass
        # Return the DataFrame from the last processed sitemap
        return all_dataframes

# Create an instance of SitemapParser for 'https://cnn.com'
parser = SitemapParser('https://cnn.com')
all_dataframes = parser.parse_all_sitemaps()