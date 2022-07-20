import pandas as pd
from bs4 import BeautifulSoup as Bs
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Wel\\Desktop\\chromedriver.exe")

products = []
prices = []
details = []

driver.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=01de3a56-0734-4574-809e-cc40d216971d")
content = driver.page_source
parsed_content = Bs(content,'html.parser')
for eachproduct in parsed_content.findAll("a", href=True, attrs={"class":"_1fQZEK"}):
    name = eachproduct.find("div", attrs= {"class":"_4rR01T"})
    detail = eachproduct.find("ul", attrs= {"class":"_1xgFaf"})
    price = eachproduct.find("div", attrs= {"class":"_30jeq3"})
    products.append(name.text)
    details.append(detail.text)
    prices.append(price.text)

df = pd.DataFrame({"Product":products, "Specs": details, "Prices":prices})
df.to_excel("Mobilephones123.xlsx", index=False)
