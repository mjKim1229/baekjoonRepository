-- 코드를 입력하세요
#서울에 위치한 식당들 
# 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소
#리뷰 평균 점수 (소수점 3번째 자리에서 반올림)
# 평균 점수 기준으로 내림차순 정렬, 즐겨찾기 수 내림차순 
SELECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS , SCORE
FROM REST_INFO
INNER JOIN 
(
    SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
    FROM REST_REVIEW
    GROUP BY REST_ID 
) A 
USING(REST_ID)
WHERE SUBSTRING(ADDRESS,1,2) = '서울'
ORDER BY SCORE DESC, FAVORITES DESC 