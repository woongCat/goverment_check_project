import os
import sys
import urllib.request
from dotenv import load_dotenv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# .env 파일 로드
load_dotenv()

# 환경 변수 읽기
client_id = os.getenv("API_ID")
client_secret = os.getenv("API_PW")

encText = urllib.parse.quote("국회의원")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)