SELECT count(USER_ID) as USERS
FROM USER_INFO
WHERE YEAR(JOINED) = '2021' and AGE BETWEEN 20 AND 29 
