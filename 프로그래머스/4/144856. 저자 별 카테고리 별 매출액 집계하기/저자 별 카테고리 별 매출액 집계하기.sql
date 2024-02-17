-- 코드를 입력하세요
#2022년 1월 도서 판매 
# 저자별, 카테고리 별 매출액 (판매량 * 판매가)
# 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES
#저자 ID 오름, 카테고리 내림 

SELECT AUTHOR_ID, AUTHOR_NAME,  CATEGORY, SUM(PRICE*SALES) AS TOTAL_SALES
FROM BOOK INNER JOIN AUTHOR
USING (AUTHOR_ID)
INNER JOIN BOOK_SALES
USING (BOOK_ID)
WHERE DATE_FORMAT(SALES_DATE,"%Y-%m") = '2022-01'
GROUP BY AUTHOR_ID, CATEGORY 
ORDER BY AUTHOR_ID, CATEGORY DESC 
