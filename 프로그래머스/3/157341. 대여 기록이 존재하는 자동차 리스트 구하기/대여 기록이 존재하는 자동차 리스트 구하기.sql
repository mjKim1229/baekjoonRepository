-- 코드를 입력하세요

SELECT DISTINCT CAR_ID 
FROM CAR_RENTAL_COMPANY_CAR
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY
USING (CAR_ID)
WHERE CAR_TYPE = "세단" 
AND MONTH(START_DATE) = 10
ORDER BY CAR_ID DESC 

# AND '2022-10' BETWEEN DATE_FORMAT(START_DATE,"%Y-%m") AND 
# DATE_FORMAT(END_DATE,"%Y-%m")




# SELECT DISTINCT(b.CAR_ID)
# FROM CAR_RENTAL_COMPANY_CAR AS a 
# INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS b 
# ON a.CAR_ID = b.CAR_ID
# WHERE MONTH(START_DATE) = 10 AND CAR_TYPE = '세단'
# ORDER BY b.CAR_ID DESC