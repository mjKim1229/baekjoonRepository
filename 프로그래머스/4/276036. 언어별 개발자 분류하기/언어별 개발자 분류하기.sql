WITH A AS (SELECT * 
FROM SKILLCODES INNER JOIN DEVELOPERS 
WHERE SKILL_CODE & CODE = CODE) 

# SELECT DISTINCT ID, FIRST_NAME, LAST_NAME, EMAIL , CASE 
#     WHEN CATEGORY = 'Front End' OR NAME = 'PYTHON' THEN 'A'  
#     WHEN NAME = 'C#' THEN 'B'
#     WHEN CATEGORY = 'Front End' THEN 'C' END AS GRADE 
# FROM A

SELECT GRADE, ID, EMAIL
FROM (
    SELECT DISTINCT ID, FIRST_NAME, LAST_NAME, EMAIL , CASE 
    WHEN ID IN (
        (SELECT ID
        FROM A 
        WHERE CATEGORY = 'Front End') INTERSECT 
        (SELECT ID 
        FROM A 
        WHERE NAME = 'PYTHON')) THEN 'A'  
    WHEN ID IN (SELECT ID FROM A WHERE NAME = 'C#') THEN 'B'
    WHEN CATEGORY = 'Front End' THEN 'C' END AS GRADE
    FROM A) B 
WHERE GRADE IS NOT NULL 
ORDER BY GRADE , ID 

      
# ((SELECT ID
# FROM A 
# WHERE CATEGORY = 'FRONT END') 
# INTERSECT 
# (SELECT ID 
#  FROM A 
#  WHERE NAME = 'PYTHON'))



