import requests
import pandas as pd
from lxml import etree
import requests
import pandas as pd
from lxml import etree

class SitemapParser:
    """
    A class for parsing sitemaps from a given base URL.

    Attributes:
    - base_url (str): The base URL for which sitemaps will be parsed.
    - sitemaps (list): A list to store discovered sitemap URLs.

    Methods:
    - retrieve_sitemaps(): Retrieves sitemap URLs from the robots.txt file of the base URL.
    - parse_individual_sitemap(sitemap_url): Parses an individual sitemap and extracts URLs and creation dates.
    - parse_all_sitemaps(): Retrieves and parses all sitemaps, storing the data in DataFrames and CSV files.

    Usage:
    ```python
    parser = SitemapParser("https://example.com")
    parser.parse_all_sitemaps()
    ```
    """

    def __init__(self):
        """
        Initialize the SitemapParser with a base URL.

        Parameters:
        - base_url (str): The base URL for which sitemaps will be parsed.
        """
        self.base_url = "https://cnn.com"
        self.sitemaps = []

    def retrieve_sitemaps(self):
        """
        Retrieve sitemap URLs from the robots.txt file of the base URL.
        """
        response = requests.get(self.base_url + '/robots.txt')
        for line in response.text.splitlines():
            if line.startswith('Sitemap:'):
                sitemap_url = line.split(': ')[1]
                self.sitemaps.append(sitemap_url)

    def parse_individual_sitemap(self, sitemap_url):
        """
        Parse an individual sitemap and extract URLs and creation dates.

        Parameters:
        - sitemap_url (str): The URL of the sitemap to be parsed.

        Returns:
        - list: A list of lists containing URLs and their creation dates.
        """
        response = requests.get(sitemap_url)
        root = etree.fromstring(response.content)
        urls = []
        for elem in root:
            temp = []
            for i in elem:
                temp.append(i.text)
            if len(temp) == 1:
                temp.append(None)
            urls.append(temp[:2])
        return urls

    def parse_all_sitemaps(self):
        """
        Retrieve all sitemaps and parse their content, storing data in DataFrames and CSV files.

        Returns:
        - list: A list of DataFrames, one for each processed sitemap.
        """
        self.retrieve_sitemaps()
        all_urls = []
        all_dataframes = []
        for sitemap in self.sitemaps:
            try:
                urls = self.parse_individual_sitemap(sitemap)
                all_urls.extend(urls)
                df = pd.DataFrame(all_urls, columns=['url', 'date_of_creation'])
                df.to_csv("Sitemap_{}.csv".format(sitemap.replace('/', '_').replace(':', '_').replace('.', '_')))
                all_dataframes.append(df)
            except:
                pass
        return all_dataframes
