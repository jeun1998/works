# 우편정보 파일 자료 읽기
# 키보드에서 입력한 동이름으로 해당 주소 정보 출력

def zipProcess():
    dongIrum = '서초1동'
    # print(dongIrum)

    with open(r'zipcode.txt', mode='r', encoding='utf-8') as f:
        # line = f.read()  # 전체 행 읽기
        line = f.readline()  # 한 행 읽기

        # print(line)
        # 주소 문자열 자르기
        # lines = line.split('\t')
        # lines = line.split(chr(9))
        # print(lines)  
        
        while line:
            lines = line.split(chr(9))
            if lines[3].startswith(dongIrum):
                print(lines)

            line = f.readline()

if __name__ == '__main__':
    zipProcess()