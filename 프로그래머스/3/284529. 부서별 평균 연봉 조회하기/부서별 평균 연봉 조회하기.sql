-- 코드를 작성해주세요

select DEPT_ID, DEPT_NAME_EN, round(avg(SAL)) as AVG_SAL
from HR_EMPLOYEES join HR_DEPARTMENT using(DEPT_ID)
group by DEPT_ID
order by AVG_SAL desc