import re
import os
from dicmaker import removedic1, removedic2, removedic3


#GOAL:HTML소스파일에서 필요한 단어를 뽑아내서 엑셀파일 형태의 사전을 만든다.
#GOAL: Draw out the necessary words from the HTML source file and make an Excel file-type dictionary.

def makedictionary():

    # 읽어올 파일들이 들어있는 디렉토리 경로 지정
    # Specify the directory path that contains the files to be read
    path = 'C:/Users/wonbee/Desktop/'


    # 디렉토리에서 파일 목록 가져옴
    #Importing a list of files from a directory
    file_list = os.listdir(path)

    # 확장자 .html 만 가져옴
    #Import only .html extension
    file_list_html = [file for file in file_list if file.endswith(".html")]
    print("file_list_html: {}".format(file_list_html))

    #시간 좀 걸리니까 오래걸려도 작동중이니 기다리라는 뜻
    print('WAIT UNTILL THE END')

    for list in file_list_html:
        # 디렉토리를 돌며 리스트에 있는 파일들 open
        #Open the files in the list in the directory
        file = open('C:/Users/wonbee/Desktop/{}'.format(list))


        # html 변수에 데이터 저장
        #Store data in html variable
        html = file.read()

        #저장할 파일경로와, 파일명 지정, a는 내용에 추가한다는 뜻이다. UTF-8로 인코딩한다.
        #File path to save, file name designation, 'a' means to add to the content. Encodes with UTF-8.
        f=open('C:/Users/wonbee/desktop/folder/test.txt','a',encoding='utf8')


        for i in range(f is not ' '):

            #HTML태그 삭제
            # <부터 >까지 안에 들어 있는 컨텐츠를 지운다. 그러나 &lt; ~ &gt; 로 바뀐다
            #remove HTML Tag
            #Erase the contents from < to >. But it changes to &lt;~&gt;.
            text = re.sub('<.+?>', ',', html, 0, re.I|re.S)

            #한 번 더 지운다.
            #So we will remove one more time
            text1 = re.sub('&lt;.+?&gt;', ',', text, 0, re.I|re.S)

            #누락을 막기 위해 모두 소문자로 변환한다
            #All lowercase letters are converted to prevent omission.
            body=text1.lower()

          
            # 특수문자, 숫자 제거
            # ^가-힣.... : 특수문자,숫자 제거해주는 정규표현식. 한글, 영문소문자,대문자 외에는 모두 지우겠다는 뜻이다.
            # remove special character, number.
            # ^가-힣 : Regular expressions that remove numbers and special character.
            #This means will erase all but except Korean, English-language, and uppercase letters.
            body1 = re.sub('[^가-힣a-zA-Z]', ',', body).strip()


            # ,을 넣어주는 이유 : 공백을 넣으면 단어가 붙어버려서 다음 정제 때 알아듣지 못한다.
            # 1차 정제:1차 제거사전
            #큰 단어들 제거
            # Why to put ',' in: If you put a blank space, the word will stick and you won't understand it at the next filtering step.
            # Primary filtering:The First Dictionary of Removal
            # Remove big words
            body2 = re.sub(removedic1.result,',',body1)
    

            #2차 정제: 2차 제거사전 1차
            #1차에서 정제되지 않은 찌꺼기 단어들 제거
            #2nd filtering : Secondary elimination dictionary 1st
            #Remove unrefined waste words from 1st step
            body3 = re.sub(removedic2.result,',',body2)


            #3차 정제: 2차 제거사전 2차
            #찌꺼기의 찌꺼기 제거
            #3rd filtering : Secondary elimination dictionary 2nd
            #Remove unrefined waste words from 2nd step
            body4 = re.sub(removedic2.result,',',body3)
 

            #4차 정제: 2차 제거사전 앞자리로 시작 삭제
            #4th filtering : 2nddic Remove Start with
            body5 = re.sub(removedic2.result1,',',body4)


            #5차 정제: 2차 제거사전 뒷자리로 끝남 삭제
            #5th filtering : 2nddic Remove end with
            body6 = re.sub(removedic2.result2,',',body5)

            
            #6차 정제: 3차 제거사전 1차
            #알파벳, 한 글자 제거
            #6th filtering : 3rd Removal Dictionary 1st
            #Remove alphabet, one character
            body7 = re.sub(removedic3.result,',',body6)


            #7차 정제: 3차 제거사전 2차
            #7th filtering : 3rd Removal Dictionary 2nd
            body8 = re.sub(removedic3.result,',',body7)


            #8차 정제: 2차 제거사전 3차
            #정제된 찌꺼기 제거
            #8th filtering : 2nd Removal dictionary 3rd
            #Remove final useless words
            body9 = re.sub(removedic2.result,',',body8)


            #특수문자(,) 제거
            #Remove special character
            body10 = re.sub('[^가-힣a-zA-Z]', '\n', body9).strip()

            #결과물 줄공백 없이 저장
            #Save deliverables without spaces
            f.write("".join([s for s in body10.strip().splitlines(True) if s.strip()]))

            #종료
            #Bye
            f.close()

if __name__ == '__main__':
        makedictionary()
