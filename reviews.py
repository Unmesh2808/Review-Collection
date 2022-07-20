from bs4 import BeautifulSoup as Bs
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Wel\\Desktop\\chromedriver.exe")

ratings = []
name = []
comment = []

driver.get("https://www.trustpilot.com/review/spacex.com")
content = driver.page_source
parsed_content = Bs(content, 'html.parser')
for each in parsed_content.findAll("article", attrs={"class":"paper_paper__1PY90 paper_square__lJX8a card_card__lQWDv styles_reviewCard__hcAvl"}):
    names = each.find("div", attrs={"class":"typography_typography__QgicV typography_bodysmall__irytL typography_weight-medium__UNMDK typography_fontstyle-normal__kHyN3 styles_consumerName__dP8Um"}) 
    comments = each.find("p", attrs={"class":"typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3"})
    name.append(names.text)
    comment.append(comments.text)

df = pd.DataFrame({"Name":name, "Reviews":comment})
df.to_excel("reviews.xlsx", index = False)

   