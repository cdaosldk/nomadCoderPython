from requests import get

websites = (
  "google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com",
  "tiktok.com"
)

results= {}

#매 번 반복문이 실행될 때마다, list에서 each 매개변수로 값을 저장 후 실행
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
    response=get(website)
    print(response.status_code)
    if response.status_code >= 200:
      results[websites] = "ok"
    elif response.status_code >= 100:
      results[websites] = "information response"
    elif response.status_code >= 300:
      results[websites] = "redirection message"
    elif response.status_code >= 400:
      results[websites] = "client error response"
    elif response.status_code >= 500:
      results[websites] = "server error response"
      
print(results)
#String에 변수를 추가하기: f""
#response 200은 웹사이트가 성공적으로 응답했다는 뜻