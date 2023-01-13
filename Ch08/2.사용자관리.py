"""
날짜 : 2023/01/13
이름 : 박가영
내용 : 파이썬 사용자 관리 프로그램 실습
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                user='root', 
                password='1234', 
                db='java2db', 
                charset='utf8')

cur = conn.cursor()

while True:
    print('0: 종료, 1: 등록, 2: 조회, 3: 검색, 4: 삭제')
    answer = 0

    try:
        answer = int(input('선택 : '))
    except:
        print('숫자를 입력하세요.')
        continue

    if answer == 0:
        break
    elif answer == 1:
        user = list(input('아이디, 이름, 휴대폰, 나이 순으로 입력 : ').split())
        cur.execute("insert into `user3` values ('{}','{}','{}','{}')".format(user[0], user[1], user[2], user[3]))
        conn.commit()
        print('등록완료...')
    elif answer == 2:
        cur.execute("select * from `user3`")
        conn.commit()
        for row in cur.fetchall():
            print('------------------')
            print('|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3]))
    
    elif answer == 3:
        name = input('이름 검색 :')
        cur.execute("select * from `user3` where `name`='%s'" % name)
        conn.commit()
        for row in cur.fetchall():
            print('아이디 : ', row[0])
            print('이름 : ', row[1])
            print('휴대폰 : ', row[2])
            print('나이 : ', row[3])
    elif answer == 4:
        uid = input('삭제할 아이디 :')
        cur.execute("delete from `user3` where `uid`='{}'".format(uid))
        conn.commit()
        print('삭제되었습니다.')
    else:
        print('0 ~ 4 중에서 입력하세요.')

# 데이터베이스 종료
conn.close()
print('프로그램 종료...')

