import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning
from twilio.rest import Client


warnings.simplefilter('ignore', InsecureRequestWarning)

account_sid = ''
auth_token = ''

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = ''
NEWS_API_KEY = ''

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

PARAMETERS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': API_KEY
}

NEWS_PARAMETERS = {
    'qInTitle': COMPANY_NAME,
    'apiKey': NEWS_API_KEY
}


# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=PARAMETERS, verify=False)
response.raise_for_status()
data = response.json()
daily_data = data['Time Series (Daily)']
yesterday_value = [value for (key, value) in daily_data.items()][0]['4. close']
print(yesterday_value)



# Get the day before yesterday's closing stock price
day_bef_value = [value for (key, value) in daily_data.items()][1]['4. close']
print(day_bef_value)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
diff = abs(float(yesterday_value) - float(day_bef_value))
print(diff)

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
diff_percent = (diff / float(yesterday_value)) * 100
print(diff_percent)

# - If TODO4 percentage is greater than 0.5 then print("Get News").
# - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# - Use Python slice operator to create a list that contains the first 3 articles.

if diff_percent > 0.5:
    response2 = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS, verify=False)
    response2.raise_for_status()
    news_data = response2.json()
    articles_data = news_data['articles'][:3]
    print(articles_data)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles_data]
print(formatted_articles)

#TODO 9. - Send each article as a separate message via Twilio.
client = Client(account_sid, auth_token)

for article in formatted_articles:
    message = client.messages.create(
            body=article,
            from_="",
            to="",
        )
    print(message.status)



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

