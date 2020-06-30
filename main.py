from intents import Intents
from scraping import Scraping

about = Scraping().homePage()

products = []
products.extend(Scraping().pcGames())
products.extend(Scraping().pcGamesOnSale())
products.extend(Scraping().xboxProducts())
products.extend(Scraping().playstationProducts())

Scraping().exit()

data = {
    "Store": about,
    "Products": products
}

Intents(data=data).createIntents()
