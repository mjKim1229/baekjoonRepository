-- 코드를 입력하세요
SELECT a.FLAVOR
FROM FIRST_HALF as a INNER JOIN ICECREAM_INFO as b 
WHERE a.FLAVOR = b.FLAVOR and a.TOTAL_ORDER > 3000 
and b.INGREDIENT_TYPE = 'fruit_based'

