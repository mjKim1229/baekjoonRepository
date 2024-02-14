-- 코드를 입력하세요
#조회수 가장 높은 중고 거래 게시물에 대한 첨부 파일 경로 
#첨부파일 경로 : FILE ID 기준 내림차순 
#기본 경로 : /home/grep/src/
#게시글 ID로 디렉토리 경로 
#파일 이름 : 파일 ID , 이름, 확장자 

SELECT CONCAT("/home/grep/src/",BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID 
= (
    SELECT BOARD_ID 
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC 
    LIMIT 1
    )
ORDER BY FILE_ID DESC 
