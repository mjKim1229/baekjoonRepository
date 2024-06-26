-- 코드를 입력하세요
#2022년 3월 
#오프라인, 온라인 판매 날짜, 상품ID, 유저ID, 판매량
# 오프라인 USER_ID null 
#판매일 기준 오름차순, 상품 id 오름차순, 유저 id 오름차순 

(
    SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE DATE_FORMAT(SALES_DATE, "%Y-%m") = '2022-03'
)
UNION  
(
    SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT 
    FROM OFFLINE_SALE 
    WHERE DATE_FORMAT(SALES_DATE, "%Y-%m") = '2022-03'
)
ORDER BY SALES_DATE, PRODUCT_ID , USER_ID 

