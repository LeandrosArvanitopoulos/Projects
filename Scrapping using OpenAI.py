import requests
from bs4 import *
from openai import OpenAI


ai = OpenAI(api_key="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")

url = "https://www.e-food.gr/shops?user_address=9968323"

prompt = "Find the menu of the restaurants named Μπαρμπαγιάννης"


def scrapeSite(url, prompt):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator="\n", strip=True)

    else:
        print("Error")

    print(text)
    searchSite(text, prompt)


def searchSite(webside_text, prompt):
    completion = ai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": f"Analyze a website's content and search for {prompt}",
            },
            {
                "role": "user",
                "content": f"This is the content of the website {webside_text}",
            },
        ],
    )

    searchResult = completion["messages"][0]["content"]

    print(f"Search Results: {searchResult}")
    return searchResult
    # #print(soup.prettify())
    # #print(soup.find_all('div', class_='shop-name'))
    # for shop in soup.find_all('div', class_='shop-name'):
    #     #print(shop.text)
    #     prompt = prompt + "\n" + shop.text
    # #print(prompt)
    # return prompt


scrapeSite(url, prompt)
