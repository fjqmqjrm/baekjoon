SELECT A.DEPT_ID, B.DEPT_NAME_EN, ROUND(AVG(A.SAL),0) AS AVG_SAL
FROM HR_EMPLOYEES A INNER JOIN HR_DEPARTMENT B
ON A.DEPT_ID = B.DEPT_ID
GROUP BY A.DEPT_ID
ORDER BY AVG_SAL DESC;
