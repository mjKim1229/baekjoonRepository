-- 코드를 입력하세요
SELECT EXTRACT(YEAR FROM SALES_DATE) YEAR, EXTRACT(MONTH FROM SALES_DATE) MONTH, GENDER, COUNT(DISTINCT(USER_ID)) USERS 
FROM ONLINE_SALE O_S 
JOIN USER_INFO U_I 
USING (USER_ID)
WHERE GENDER IS NOT NULL 
GROUP BY EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE), GENDER 
ORDER BY EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE), GENDER 
