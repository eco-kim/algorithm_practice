SELECT a.ANIMAL_ID, a.NAME
FROM ANIMAL_OUTS a
LEFT JOIN ANIMAL_INS b on a.ANIMAL_ID = b.ANIMAL_ID
WHERE INTAKE_CONDITION is null;

--https://programmers.co.kr/learn/courses/30/lessons/59042