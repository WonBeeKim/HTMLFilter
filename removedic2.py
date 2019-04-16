#대략적인 단어들이 제거된 뒤 남는 찌꺼기 단어 정제를 위해 2번 제거사전을 만듦.
#
# #2차 삭제파일의 경로
#file = open('C:/Users/wonbee/2차삭제.txt',"r", encoding = "utf-8")
file = open('C:/Users/Solugate/PycharmProjects/Crawler/dicmaker/2차삭제.txt',"r", encoding = "utf-8")

# 텍스트 추출
html = file.read()

# 소문자변환
body=html.lower()

#단어 앞뒤로 줄바꿈 삽입 \n~\n
#해당 txt파일 맨앞과 맨뒤에 \n 입력해주기
#,, 안에 있는 단어만 삭제가 됨
#ex) ,word,
result = ",|,".join(body.split())


#해당 단어로 시작하거나 끝나는 단어를 삭제하기 위함
#ex),Ithinksotoo,->think 1차에서 제거->,I,sotoo,->여기서 too를 지우고 싶은 경우 too, 삭제가 필요->,I,so,
#해당 txt파일 맨앞에 \n 입력해주기
result1 = "|,".join(body.split())

#해당 txt파일 맨앞과 맨뒤에 \n 입력해주기
result2 = ",|".join(body.split())

print(result2)
