import random
import requests
from datetime import datetime, timedelta
import smtplib
import os
# ## STEP 2: Use https://newsapi.org
#When BTC price increase/decreases by 3% between yesterday and the day before yesterday, send an email to yourself with a random news article.

def get_news():
    parameters2 = {
        "from": day_b4_yest,
        "q": "bitcoin",
        "to": yesterday,
        "language": "en",
        "domains": "coindesk.com",
        "apiKey": os.environ["news_apikey"]
    }
    response = requests.get("https://newsapi.org/v2/everything", params=parameters2)
    response.raise_for_status()
    news = response.json()
    total_results=int(news["totalResults"])
    print(total_results)
    random_news_item=random.randint(0,total_results-1)
    news_title=news["articles"][random_news_item]["title"]
    news_description=news["articles"][random_news_item]["description"]
    print(news_title)

    my_email=os.environ["email"]
    password=os.environ["Password"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,
                            msg=f"Subject: BTC:{direction}{abs(percent_difference)}%\n\nHeadline: {news_title}\nBrief:{news_description}")


## STEP 1: Use https://www.alphavantage.co
# check bitcoin prices to see if there has been a +-3% change in price between yesterday and the day before
yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
print(yesterday)
day_b4_yest = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')
print(day_b4_yest)
parameters={
    "function":"DIGITAL_CURRENCY_DAILY",
    "symbol":"BTC",
    "market":"GBP",
    "apikey":os.environ["price_api_key"]
}
url = 'https://www.alphavantage.co/query'
r = requests.get(url,params=parameters)
r.raise_for_status()
market_data = r.json()
print(market_data)
yesterday_close_price = float(market_data["Time Series (Digital Currency Daily)"][yesterday]['4. close'])
print(yesterday_close_price)
day_b4_open_price=float(market_data["Time Series (Digital Currency Daily)"][day_b4_yest]['1. open'])
print(day_b4_open_price)
percent_difference=((day_b4_open_price-yesterday_close_price)/day_b4_open_price)*100
print(percent_difference)
if percent_difference >= 3:
    direction="Up"
    get_news()
elif percent_difference <= -3:
    direction="Down"
    get_news()
else:
    pass


