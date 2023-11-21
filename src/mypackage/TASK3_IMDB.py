import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MovieDataScraper:
    def __init__(self):
        self.api_key = 'c3e8916e'
        self.base_url = 'https://imdb-api.com'

    def get_movie_ids(self, query, max_results=500):
        #Finds the moveids, and store the ids
        ids = []
        page = 1
        while len(ids) < max_results:
            #Format the params
            params = {'s': query, 'page': page, 'apikey': self.api_key}
            #Query the API
            resp = requests.get(self.base_url, params=params)
            #Get the response int the form of json
            data = resp.json().get('Search', [])
            if not data:
                break
            ids.extend(r['imdbID'] for r in data)
            page += 1
        #now ids have the movie id's based on the max_result value mentioned
        return ids[:max_results]

    def get_movie_details(self, movie_id):
        #Now get the movie details using the move id and api key
        params = {'i': movie_id, 'apikey': self.api_key}
        #Make an API call
        resp = requests.get(self.base_url, params=params)
        return resp.json()

    def scrape_movies_data(self, query, max_results=500):
        movie_ids = self.get_movie_ids(query, max_results)
        #Store the movie data in the form of list of dict's
        movies_data = []
        for movie_id in movie_ids:
            movie = self.get_movie_details(movie_id)
            movies_data.append({
                'title': movie.get('Title', ''),
                'year': movie.get('Year', ''),
                'rated': movie.get('Rated'),
                'released': movie.get('Released'),
                'runtime': movie.get('Runtime'),
                'genre': movie.get('Genre'),
                'director': movie.get('Director'),
                'actors': movie.get('Actors'),
                'plot': movie.get('Plot'),
                'awards': movie.get('Awards')
            })
        #return the data frame
        return pd.DataFrame(movies_data)

    def save_movies_data_csv(self, df, filename='IMDBmovies.csv'):
        #Store the data set in the form of csv file
        df.to_csv(filename)

    def plot_year_distribution(self, df):
        #Year wise movie release distribution plot
        plt.figure(figsize=(10, 10))
        sns.histplot(df['year'], bins=20, kde=True)
        plt.title('Distribution of Movie Years')
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.savefig('year_distribution.png')
        plt.show()

    def plot_rating_distribution(self, df):
        #Rating Plot
        plt.figure(figsize=(10, 10))
        sns.countplot(x='rated', data=df)
        plt.title('Distribution of Movie Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.savefig('rating_distribution.png')
        plt.show()

    def plot_runtime_by_genre(self, df):
        #Genre wise runtime plot
        plt.figure(figsize=(10, 10))
        sns.boxplot(x='genre', y='runtime', data=df)
        plt.title('Runtime Distribution Across Genres')
        plt.xlabel('Genre')
        plt.ylabel('Runtime (minutes)')
        plt.xticks(rotation=90, ha='right')
        plt.savefig('runtime_by_genre.png')
        plt.show()

    def plot_top_directors_awards(self, df, top_n=10):
        #Top directors plot
        top_directors = df.groupby('director')['awards'].sum().nlargest(top_n).index
        top_directors_df = df[df['director'].isin(top_directors)]

        plt.figure(figsize=(10, 10))
        sns.barplot(x='director', y='awards', data=top_directors_df)
        plt.title(f'Top {top_n} Directors by Awards')
        plt.xlabel('Director')
        plt.ylabel('Awards')
        plt.xticks(rotation=90, ha='right')
        plt.savefig('top_directors_awards.png')
        plt.show()
