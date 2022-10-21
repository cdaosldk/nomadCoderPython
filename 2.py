from requests import get
from bs4 import BeautifulSoup

def extract_jk_jobs(keyword):
  base_url = "https://www.jobkorea.co.kr/Search/?stext="
  keyword = "python"
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website")
  else:
    results=[]
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('div', class_="post")
    for job in jobs:
      anchors = soup.find_all('a')
      anchor = anchors[1]
      anchor_ti = anchors[2]
      link = anchor['href']
      company = anchor.find('a', class_ = "title")
      title = anchor_ti.find('a', class_ = "title")
      p = soup.find('p', class_= "option")
      exp, edu, kind, loc_s, loc_l, date = p.find_all('span', class_="exp")
      job_data = {
        'title': title.string,
        'company' : company.string,
        'exp' : exp.sting,
        'edu' : edu.string,
        'kind' : kind.string,
        'loc s' : loc_s.string,
        'loc l' : loc_l.string,
        'date' : date.string,
        'link' : f"https://www.jobkorea.co.kr/{link}"
        }
      results.append(job_data)
    return results