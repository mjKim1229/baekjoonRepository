-- 코드를 입력하세요
#식품 분류별 가격이 가장 비싼 식품의 분류, 가격, 이름
# 식품 분류 : '과자', '국', '김치', '식용유'
# 식품 가격 기준 내림차순 

#식품 분류별 가장 비싼 식품의 분류 , 가격 (SUBQUERY)
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME 
FROM 
(
    SELECT *, RANK() OVER (PARTITION BY CATEGORY ORDER BY PRICE DESC) AS 'RANK'
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')  
) A 
WHERE A.RANK = 1 
ORDER BY MAX_PRICE DESC 

