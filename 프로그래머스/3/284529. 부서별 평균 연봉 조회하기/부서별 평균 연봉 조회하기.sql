-- 코드를 작성해주세요
SELECT DEPT_ID, DEPT_NAME_EN, AVG_SAL
FROM HR_DEPARTMENT
JOIN
(
    SELECT DEPT_ID, ROUND(AVG(SAL), 0) AS AVG_SAL
    FROM HR_EMPLOYEES
    GROUP BY DEPT_ID
 ) B
USING(DEPT_ID)
ORDER BY AVG_SAL DESC 
