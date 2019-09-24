--$ 데이터 베이스 생성 sqlite3 db.sqlite3
--$ .database
--$ CSV 파일로 테이블 생성
.mode CSV
.import hellodb.csv example
--$ 테이블 조회
select * from example
--$ 스키마 조회
.schema examples