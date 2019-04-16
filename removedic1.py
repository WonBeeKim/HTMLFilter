import re

#1차 삭제파일의 경로
#Path to 1stdic file
file = open('C:/Users/wonbee/1stdic.txt',"r", encoding = "utf-8")

# 텍스트 추출
#Text extraction
html = file.read()

# 소문자변환
#convert to lowercase
body=html.lower()

# \s+ : 공백과 매칭
# \s+ : matching with space
pattern = re.compile('\s+')

#|를 입력하는 이유:단어를 나누는 경계임.
#단어 사이에 줄바꿈 대신 | 삽입
#Why enter | : The boundary between words.
#Insert | instead of \n between words
result = re.sub(pattern, '|', body)

print(result)
