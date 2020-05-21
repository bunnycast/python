# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('./resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 전체 조회
c.execute("SELECT * FROM users")

# 커서 위치 변경
# 1개 로우 선택 (커서 1)
# print('One -> \n', c.fetchone())

# # 지정 로우 선택 (커서 위치 1 > 2,3,4,)
# print('Three -> \n', c.fetchmany(size=3))

# # 전체 로우 선택 (커서 위치 4 > 5 > 커서 끝)
# print('All -> \n', c.fetchall())
# print('All -> \n', c.fetchall())

# 순회1
# rows = c.fetchall()
# for row in rows:
#   print('retrieve1 -> ', row)

# 순회2 - 권장
# for row in c.fetchall():
#   print('retrieve2 ->', row)

# 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id asc'):
#   print('retrieve3 -> ', row)
print()

# WHERE Retrieve1 - 튜플로 반환
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 3번만 가져와서 다른 데이터가 없음

# WHERE Retrieve2 - 문자형으로 반환
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s %f %d
print('param2', c.fetchone())
print('param2', c.fetchall()) # 4번만 가져와서 다른 데이터가 없음

# WHERE Retrieve3 - 딕셔너리로 반환 (:Id)
c.execute('SELECT * FROM users WHERE id=:ID', {"ID":5})
print('param3', c.fetchone())
print('param3', c.fetchall()) # 5번만 가져와서 다른 데이터가 없음

# WHERE Retrieve4
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?, ?)", param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d', '%d')" % (3,4,5))
print('param5', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1":2, "id2":4})
print('param6', c.fetchall())

# DUMP 출력 (데이터 마이그레이션)
with conn:
  with open('./resource/dump.sql', 'w') as d:
    for line in conn.iterdump():
      d.write('%s\n' % line)
    print('DUMP Print Complete')

# with 문으로 인해 f.close(), conn,close() 모두 자동 호출되면서 종료