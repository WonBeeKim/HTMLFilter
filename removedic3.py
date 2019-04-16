
#3차 삭제파일의 경로
file = open('C:/Users/wonbee/3차삭제.txt',"r", encoding = "utf-8")

# 텍스트 추출
html = file.read()

# 소문자변환
body=html.lower()


#단어 앞뒤로 줄바꿈 삽입 ,~, : 콤마 안에 있는 단어만 삭제
#해당 txt파일 맨앞과 맨뒤에 , 입력해주기
result = ",|,".join(body.split())

print(result)
