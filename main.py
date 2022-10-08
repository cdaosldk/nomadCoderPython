websites = (
  "google.com",
  "https://airbnb.com",
  "https://twitter.com",
  "https://facebook.com",
  "https://tiktok.com"
)
#매 번 반복문이 실행될 때마다, list에서 each 매개변수로 값을 저장 후 실행
for website in websites:
  if not website.startswith("https://"):
    print("have to fix")
    website = f"https://{website}"
  print(website)
#String에 변수를 추가하기: f""