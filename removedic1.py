import re

#1차 삭제파일의 경로
#file = open('C:/Users/wonbee/1차삭제.txt',"r", encoding = "utf-8")
file = open('C:/Users/Solugate/PycharmProjects/Crawler/dicmaker/1차삭제.txt',"r", encoding = "utf-8")

# 텍스트 추출
html = file.read()

# 소문자변환
body=html.lower()

# \s+ 공백과 매칭
pattern = re.compile('\s+')

#|를 입력하는 이유:단어를 나누는 경계임.
#단어 사이에 줄바꿈 대신 | 삽입
result = re.sub(pattern, '|', body)

print(result)