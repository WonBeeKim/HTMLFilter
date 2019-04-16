#대략적인 단어들이 제거된 뒤 남는 찌꺼기 단어 정제를 위해 2번 제거사전을 만듦.
#
#2차 삭제파일의 경로
#Path to 2nddic file
file = open('C:/Users/wonbee/2차삭제.txt',"r", encoding = "utf-8")

# 텍스트 추출
#Text extraction
html = file.read()

# 소문자변환
#convert to lowercase
body=html.lower()

#단어 앞뒤로 , 삽입 ,~,
#해당 txt파일 맨앞과 맨뒤에 , 입력해주기
#,, 안에 있는 단어만 삭제가 됨
#Insert the word , back and forth ,~,
#Enter , at the beginning and the end of the txt file
# Only words inside between , , will be deleted
#ex) ,word,
result = ",|,".join(body.split())


#해당 단어로 시작하거나 끝나는 단어를 삭제하기 위함
#ex),Ithinksotoo,->think 1차에서 제거->,I,sotoo,->여기서 too를 지우고 싶은 경우 too, 삭제가 필요->,I,so,
#해당 txt파일 맨앞에 , 입력해주기
#To delete a word that begins or ends with that word
#ex),Ithinksotoo,->Remove from 1st round of thinking->,I,sotoo,->If you want to delete the 'too' here, delete 'too,' -> ,I,so,
#Enter , in front of txt file for that
result1 = "|,".join(body.split())


#해당 txt파일 맨앞과 맨뒤에 , 입력해주기
#Enter , at the beginning and the end of the txt file
result2 = ",|".join(body.split())
