-- 코드를 입력하세요
SELECT b.TITLE, b.BOARD_ID, 
r.REPLY_ID, r.WRITER_ID , r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD as b
INNER JOIN USED_GOODS_REPLY as r
WHERE b.BOARD_ID = r.BOARD_ID and YEAR(b.CREATED_DATE) = 2022 and MONTH(b.CREATED_DATE) = 10 
ORDER BY r.CREATED_DATE, b.TITLE 
