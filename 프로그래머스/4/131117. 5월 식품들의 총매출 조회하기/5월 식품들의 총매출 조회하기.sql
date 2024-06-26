-- 코드를 입력하세요
#생산일자 = 202년 5월 PRODUCE_DATE
#식품 ID, 식품 이름, 총매출
#총매출 내림차순 , 식품 ID 오름차순 

SELECT PRODUCT_ID, PRODUCT_NAME, SUM(PRICE*AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT INNER JOIN 
FOOD_ORDER USING (PRODUCT_ID)
WHERE DATE_FORMAT(PRODUCE_DATE,"%Y-%m") = '2022-05'
GROUP BY PRODUCT_ID 
ORDER BY TOTAL_SALES DESC, PRODUCT_ID 
