CREATE TABLE classmates(
    name TEXT PRIMARY KEY
    age INTEGER
    address TEXT
);
-- 모든 열의 데이터를 나열할 때는 컬럼을 명시할 필요 없다.
INSERT INTO classmates values ('홍길동', 23, '전민동');
select * from classmates;
INSERT INTO classmates(name, age) values('홍순범', 23)

-- ID 값을 보고 싶을 경우
SELECT rowid, * from classmates;

-- 컬럼에 null이 들어가면 안 될 경우 not null 속성 주기
create table classmates(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
    );

-- 삭제
select distinct age from classmates;
delete from classmates where rowid = (select rowid from classmates where name='김태우');

create table tests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,   
)
update classmates set age=30 where name = '홍순범';
