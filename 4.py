from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from requests import get

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options = options)
#print(browser.page_source)

def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs?q="
  
  response = get(f"{base_url}{keyword}")
  
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", attrs={"aria-label": "pagination"})
  if pagination == None:
    return 1
  pages = pagination.find("div a")#recursive, 재귀
  

get_page_count("python")