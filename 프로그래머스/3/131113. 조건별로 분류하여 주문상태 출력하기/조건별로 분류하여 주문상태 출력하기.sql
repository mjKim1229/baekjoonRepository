-- 코드를 입력하세요
#5월 1일 기준 
#OUT_DATE (출고 일자) <= 5월 1일 : 출고 완료 
#나머지 : 출고 대기 
#미정(NULL) : 출고미정 
# 주문 ID, 제품 ID , 출고일자, 출고 여부 
#주문 ID 기준 오름 차순 
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,"%Y-%m-%d") AS OUT_DATE, 
CASE
    WHEN OUT_DATE <= "2022-05-01" THEN "출고완료"
    WHEN OUT_DATE > "2022-05-01" THEN "출고대기"
    ELSE "출고미정" END AS 출고여부 
FROM FOOD_ORDER
ORDER BY ORDER_ID
