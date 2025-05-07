# -- 코드를 작성해주세요

select ID, FISH_NAME, LENGTH
from FISH_INFO A 
join FISH_NAME_INFO 
using (FISH_TYPE)
where (A.FISH_TYPE, A.LENGTH) 
in 
    (select FISH_TYPE, MAX(LENGTH)
    from FISH_INFO
    group by FISH_TYPE)
order by ID
