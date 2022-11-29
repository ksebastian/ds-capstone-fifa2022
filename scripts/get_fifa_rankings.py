from bs4 import BeautifulSoup
import sys


def get_rankings():
    original_stdout = sys.stdout
    with open('../data/rankings.csv', 'w') as f:
        sys.stdout = f
        for page in range(1, 6):
            url = "./rankings_table_" + str(page) + ".html"
            page = open(url)
            soup = BeautifulSoup(page.read())

            ranks = soup.find_all('h6', {'class': 'ff-m-0'})
            countries = soup.find_all('span', {'class': 'd-none d-lg-block'})
            codes = soup.find_all('span', {'class': 'd-block d-lg-none'})

            for (code, country, rank) in zip(codes, countries, ranks):
                print(code.text.strip(), country.text.strip(), rank.text.strip(), sep=",")

        sys.stdout = original_stdout


if __name__ == "__main__":
    get_rankings()
