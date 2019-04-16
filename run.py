import re
import os
from dicmaker import removedic1, removedic2, removedic3


#GOAL:HTML소스파일에서 필요한 단어를 뽑아내서 엑셀파일 형태의 사전을 만든다.

def makedictionary():

    # 읽어올 파일들이 들어있는 디렉토리 경로 지정
    path = 'C:/Users/wonbee/Desktop/'


    # 디렉토리에서 파일 목록 가져옴
    file_list = os.listdir(path)

    # 확장자 .html 만 가져옴
    file_list_html = [file for file in file_list if file.endswith(".html")]
    print("file_list_html: {}".format(file_list_html))

    #시간 좀 걸리니까 오래걸려도 작동중이니 기다리라는 뜻
    print('WAIT UNTILL THE END')

    for list in file_list_html:
        # 디렉토리를 돌며 리스트에 있는 파일들 open
        file = open('C:/Users/wonbee/Desktop/{}'.format(list))


        # html 변수에 데이터 저장
        html = file.read()

        #저장할 파일경로와, 파일명 지정, a는 내용에 추가한다는 뜻이다. UTF-8로 인코딩한다.
        f=open('C:/Users/wonbee/desktop/folder/test.txt','a',encoding='utf8')


        for i in range(f is not ' '):

            #HTML태그 삭제
            # <부터 >까지 안에 들어 있는 컨텐츠를 지운다. 그러나 &lt; ~ &gt; 로 바뀐다
            text = re.sub('<.+?>', ',', html, 0, re.I|re.S)

            #한 번 더 지운다.
            text1 = re.sub('&lt;.+?&gt;', ',', text, 0, re.I|re.S)

            # Step 2 : 대문자 누락을 막기 위해 모두 소문자로 변환한다
            body=text1.lower()

            # Step 3 :
            # 특수문자, 숫자 제거
            # ^가-힣.... : 특수문자,숫자 제거해주는 정규표현식. 한글, 영문소문자,대문자 외에는 모두 지우겠다는 뜻이다.
            body1 = re.sub('[^가-힣a-zA-Z]', ',', body).strip()


            # ,을 넣어주는 이유 : 공백을 넣으면 단어가 붙어버려서 다음 정제 때 알아듣지 못한다.
            # 1차 정제:1차 제거사전
            #큰 단어들 제거
            body2 = re.sub(removedic1.result,',',body1)
            #print("".join([s for s in body2.strip().splitlines(True) if s.strip()]))

            #2차 정제: 2차 제거사전 1차
            #1차에서 정제되지 않은 찌꺼기 단어들 제거
            body3 = re.sub(removedic2.result,',',body2)
           # print("".join([s for s in body3.strip().splitlines(True) if s.strip()]))

            #3차 정제: 2차 제거사전 2차
            #찌꺼기의 찌꺼기 제거
            body4 = re.sub(removedic2.result,',',body3)
            #print("".join([s for s in body4.strip().splitlines(True) if s.strip()]))

            #4차 정제: 2차 제거사전 앞자리로 시작 삭제
            body5 = re.sub(removedic2.result1,',',body4)
            #print("".join([s for s in body4.strip().splitlines(True) if s.strip()]))

            #5차 정제: 2차 제거사전 뒷자리로 끝남 삭제
            body6 = re.sub(removedic2.result2,',',body5)
            #print("".join([s for s in body4.strip().splitlines(True) if s.strip()]))
           # print(body6)

            #6차 정제: 3차 제거사전 1차
            #알파벳, 한 글자 제거
            #제대로 작동 안함
            body7 = re.sub(removedic3.result,',',body6)
            #print("".join([s for s in body4.strip().splitlines(True) if s.strip()]))

            #7차 정제: 3차 제거사전 2차
            #제대로 작동 안함
            body8 = re.sub(removedic3.result,',',body7)
            #print("".join([s for s in body4.strip().splitlines(True) if s.strip()]))

            #8차 정제: 2차 제거사전 3차
            #정제된 찌꺼기 제거
            body9 = re.sub(removedic2.result,',',body8)
            #print("".join([s for s in body4.strip().splitlines(True) if s.strip()]))

            #특수문자(,) 제거
            body10 = re.sub('[^가-힣a-zA-Z]', '\n', body9).strip()

            #결과물 줄공백 없이 저장
            f.write("".join([s for s in body10.strip().splitlines(True) if s.strip()]))

            #종료
            f.close()

if __name__ == '__main__':
        makedictionary()
