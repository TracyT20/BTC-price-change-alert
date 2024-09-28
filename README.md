# BTC-price-change-alert
Receive an email containing a recent and relevant news article, if the price of BTC changes by +-3%  between yesterday and the day before

This program was built using data from several APIs

## Installation Guide
### 1. Clone the Repository
Clone the repository using Git:

```bash
git clone https://github.com/TracyT20/BTC-price-change-alert.git

```

### 2. Change into the project directory

```bash
cd BTC-price-change-alert
```
### 3. Install dependencies:
The project dependencies are listed in the requirements.txt file. To install them, run the following command:

```bash
pip install -r requirements.txt
```
### 3. Configuration:

This project uses the alphavantage.co API to retrieve Bitcoin price data.
Sign up at [www.alphavantage.co](https://www.alphavantage.co/support/#api-key) to get an API key.

Create a .env file in the root directory of the project, and add the following:

```bash
price_api_key=your_alphavantage_api_key
```
It also used the newsapi.org API to get relevant news articles.
Sign up at [www.newsapi.org](https://newsapi.org/register) to get an API key.

and add the following to your environmental variables:

```bash
news_apikey=your_newsapi_key
```


### 4. Run program:
You can run the application using the following command:

```bash
python main.py
```

## Contributing

Contributions are always welcome!

If you'd like to contribute to this project, follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push the changes to your fork (git push origin feature-name).

Submit a pull request.
