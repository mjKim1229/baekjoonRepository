-- 코드를 입력하세요
#자동차 종류 : 트럭인 대여 기록 
#대여금액 
#대여금액 내림차순, 대여 ID 내림 
#HISTORY_ID	FEE

WITH A AS 
(
    SELECT CAR_ID, HISTORY_ID, DATEDIFF(END_DATE,START_DATE) + 1 AS PERIOD, 
    CASE 
        WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 7 THEN '7일 이상'
        ELSE NULL END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
)
    
SELECT HISTORY_ID, ROUND(PERIOD * DAILY_FEE * ((100-IFNULL(DISCOUNT_RATE,0))/100)) AS FEE 
FROM A INNER JOIN CAR_RENTAL_COMPANY_CAR 
USING (CAR_ID)
LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN
USING (CAR_TYPE, DURATION_TYPE)
WHERE CAR_TYPE = '트럭'
ORDER BY FEE DESC , HISTORY_ID DESC 


