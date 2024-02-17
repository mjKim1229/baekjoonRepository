-- 코드를 입력하세요
#식품 분류별 가격이 가장 비싼 식품의 분류, 가격, 이름
# 식품 분류 : '과자', '국', '김치', '식용유'
# 식품 가격 기준 내림차순 

#식품 분류별 가장 비싼 식품의 분류 , 가격 (SUBQUERY)

SELECT CATEGORY, PRICE, PRODUCT_NAME 
FROM FOOD_PRODUCT
WHERE (CATEGORY,PRICE) IN 
(   SELECT CATEGORY, MAX(PRICE) AS PRICE 
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY 
    HAVING CATEGORY IN ('과자', '국', '김치', '식용유') 
)
ORDER BY PRICE DESC 
