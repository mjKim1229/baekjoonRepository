-- 코드를 입력하세요
#2022년 4월 13일 
#취소되지 않은 
# 흉부외과 (CS) 진료 예약 내역 
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
# 진료 예약 일시 오름차순 
SELECT APNT_NO, PT_NAME, PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM PATIENT INNER JOIN APPOINTMENT A
USING (PT_NO)
INNER JOIN DOCTOR
ON MDDR_ID = DR_ID
WHERE DATE_FORMAT(APNT_YMD,"%Y-%m-%d") = '2022-04-13'
AND APNT_CNCL_YN = 'N'
AND A.MCDP_CD = 'CS'
ORDER BY APNT_YMD