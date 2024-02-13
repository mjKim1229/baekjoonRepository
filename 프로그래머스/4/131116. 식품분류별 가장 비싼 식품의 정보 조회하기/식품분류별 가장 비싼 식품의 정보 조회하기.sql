-- 코드를 입력하세요
#식품 분류별 가격이 가장 비싼 식품의 분류, 가격, 이름
# 식품 분류 : '과자', '국', '김치', '식용유'
# 식품 가격 기준 내림차순 
# SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
# FROM FOOD_PRODUCT
# WHERE (CATEGORY, PRICE, PRODUCT_NAME)
# IN (SELECT CATEGORY	, MAX(PRICE), PRODUCT_NAME	
#     FROM FOOD_PRODUCT
#     GROUP BY CATEGORY	
#     )
# AND CATEGORY IN ('과자', '국', '김치', '식용유')
# ORDER BY MAX_PRICE DESC

SELECT CATEGORY, PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) in  
(
    SELECT CATEGORY, MAX(PRICE)
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
    HAVING CATEGORY IN ('과자', '국', '김치', '식용유')
)
ORDER BY PRICE DESC 