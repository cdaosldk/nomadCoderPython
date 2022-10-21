from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

wwr = extract_wwr_jobs(keyword)
wwrs = wwr
#range: 지정한만큰 항목이 포함된 일련의 숫자를 준다
file = open(f"{keyword}.csv", "w")
file.write("Position, Company, Location, URL\n")

for wwr in wwrs:
  file.write(f"{wwr['title']},{wwr['location']},{wwr['company']},{wwr['link']}\n")

file.close()

"""
wwr = extract_wwr_jobs(keyword)
wwrs = wwr
#range: 지정한만큰 항목이 포함된 일련의 숫자를 준다
for wwr in wwrs:
  print(wwr)
  print("/////\n/////")
"""
