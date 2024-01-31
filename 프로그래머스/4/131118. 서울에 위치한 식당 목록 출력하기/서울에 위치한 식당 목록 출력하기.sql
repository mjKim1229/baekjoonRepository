-- 코드를 입력하세요

SELECT REST_ID, REST_NAME, FOOD_TYPE,  FAVORITES, ADDRESS, 
ROUND(AVG(REVIEW_SCORE),2) AS SCORE 
FROM REST_INFO INNER JOIN REST_REVIEW USING(REST_ID)
WHERE SUBSTR(ADDRESS,1,2) = '서울'
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC 








# SELECT b.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, 
# a.ADDRESS, ROUND(AVG(b.REVIEW_SCORE),2) AS SCORE
# FROM REST_INFO AS a 
# INNER JOIN REST_REVIEW AS b 
# ON a.REST_ID = b.REST_ID
# WHERE SUBSTR(ADDRESS,1,2) = "서울" 
# GROUP BY b.REST_ID
# ORDER BY SCORE DESC, a.FAVORITES DESC