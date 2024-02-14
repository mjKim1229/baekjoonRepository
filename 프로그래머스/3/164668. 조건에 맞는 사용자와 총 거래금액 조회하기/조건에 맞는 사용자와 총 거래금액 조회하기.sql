-- 코드를 입력하세요
#완료된 중고거래의 
#총 금액이 70만 이상인 사람 => GROUP BY 사람 , SUM 
#회원 ID, 닉네임, 총거래금액
#총거래 금액 기준 오름차순 

SELECT USER_ID , NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD INNER JOIN USED_GOODS_USER
ON WRITER_ID = USER_ID
WHERE STATUS = 'DONE'
GROUP BY USER_ID 
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES 