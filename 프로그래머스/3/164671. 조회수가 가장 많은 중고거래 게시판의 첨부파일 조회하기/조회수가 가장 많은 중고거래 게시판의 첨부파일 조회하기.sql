-- 코드를 입력하세요
SELECT CONCAT("/home/grep/src/",BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) 
AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (
    SELECT BOARD_ID 
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC 
    LIMIT 1 
)
ORDER BY FILE_ID DESC 


# SELECT CONCAT('/home/grep/src/',b.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
# FROM USED_GOODS_BOARD AS a 
# INNER JOIN USED_GOODS_FILE AS b 
# ON a.BOARD_ID = b.BOARD_ID
# WHERE VIEWS = (SELECT max(VIEWS) FROM USED_GOODS_BOARD)
# ORDER BY FILE_ID DESC