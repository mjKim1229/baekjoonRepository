-- 코드를 작성해주세요
select DEPT_ID, DEPT_NAME_EN, AVG_SAL
from HR_DEPARTMENT
join (
    select DEPT_ID, round(avg(SAL)) as AVG_SAL
    from HR_EMPLOYEES join HR_DEPARTMENT using(DEPT_ID)
    group by DEPT_ID) A
USING(DEPT_ID)
order by AVG_SAL desc
