from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options = options)

#print(browser.page_source)
base_url = "https://www.indeed.com/jobs?q="
search_term = "python"

browser.get(f"{base_url}{search_term}")
results = []
soup = BeautifulSoup(browser.page_source, "html.parser")  
job_list = soup.find('ul', class_= "jobsearch-ResultsList css-0")
jobs = job_list.find_all('li', recursive = False)
#ul 바로밑 li만을 찾아낼 것이다
for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
  #find는 찾은 element를 주거나 None을 준다
  if zone == None:#job li에서 job을 추출한다
    anchor = job.select_one("h2 a")
    title = anchor['aria-label']
    link = anchor['href']
    company = job.find("span",class_="companyName")
    region = job.find("div",class_="companyLocation")
    job_data = {
      'link' : f"https://www.indeed.com{link}",
      'company' : company.string,
      'location' : region.string,
      'position' : title
    }
    results.append(job_data)

  
#beaifulsoup은 검색결과를 list와 dictionary로 만든다
print(results)
"""
    h2 = job.find("h2",class_="jobTitle")
    a = h2.find("a")
  else:
    print('mosaic li')
    #mosaic-zone을 가진 li 구분, 필요없음
    #None은 무언가 없을때 사용하는 자료형이다
"""
