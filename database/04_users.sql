.mode csv
.import users.csv users

--1. 나이가 30이상인 사람들 뽑아내기
select * from users where age >= 30;
--2. 나이가 30 이상인 사람들의 이름 뽑아내기
select first_name, last_name from users where age >= 30;
--3 users에서 age가 30이상이고 성이 김인 사람의 성과 나이만 뽑아오기
select first_name, age from users where age >= 30 and last_name='김';
--4. 3번과 같은 조건의 사람 수 구하기
select count(*) from users where age >= 30 nd last_name = '김';
--5. 전체 데이터 갯수
select count(*) from users;
--6. 평균 나이
select avg(age) from users;
--7. 30살 이상 사람들의 평균 나이
select avg(age) from users where age >= 30;
--8 계좌 잔액 가장 높은 사람과 액수
select first_name, max(balance) from users;
--9 30살 이상인 사람의 계좌 평균 금액
select avg(balance) from users where age >= 30;
-- wild card
-- 1. _ : 무조건 1개 이상 있어야 함
-- 2. % : 있을 수도, 없을수도 있음!
-- 10. 20대 인 사람들 뽑아 내기
select * from users where age like '2_';
-- 11. 지역번호가 02인 사람 뽑아내기
select * from users where phone like '02-%';
-- 12. 이름이 '준'으로 끝나는 사람
select * from users where first_name like '%준';
-- 13. 중간 번호가 5114 인 사람
select * from users where phone like '%-5114-%';
-- 14. 나이 많은 사람 10명
select * from users order by age desc limit 10;
-- 15. 나이, 성순으로 오름차순 10명
select * from users order by age,last_name asc limit 10;

-- limit, offset 사용하여 몇번째에 있는 사람 호출
-- ex ) 10번째 사람 -> limit 1 offset 9

