-- 코드를 입력하세요
SELECT a.FLAVOR  
FROM FIRST_HALF AS a 
INNER JOIN 
(SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM JULY
GROUP BY FLAVOR
)AS b 
ON a.FLAVOR = b.FLAVOR 
ORDER BY a.TOTAL_ORDER + b.TOTAL_ORDER DESC
LIMIT 3
