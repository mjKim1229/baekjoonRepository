-- 코드를 작성해주세요
select count(*) AS COUNT
from ECOLI_DATA
where (GENOTYPE & 1
OR GENOTYPE & 4)
and not (GENOTYPE & 2)