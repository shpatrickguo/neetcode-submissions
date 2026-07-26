-- Write your query below

WITH high_score AS (
SELECT student_id, exam_id, score,
    ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id) AS highest
FROM exam_results
)
SELECT student_id, exam_id, score
FROM high_score
WHERE highest = 1
ORDER BY student_id;

