CREATE DATABASE IF NOT EXISTS school_db;
USE school_db;

-- 1. SELECT
SELECT * FROM students;

-- 2. WHERE
SELECT * FROM marks
WHERE mark > 80;

-- 3. JOIN
SELECT
    students.name,
    subjects.subject_name,
    marks.mark
FROM marks
JOIN students ON marks.student_id = students.id
JOIN subjects ON marks.subject_id = subjects.id;

-- 4. GROUP BY
SELECT
    subjects.subject_name,
    AVG(marks.mark) AS average_mark
FROM marks
JOIN subjects ON marks.subject_id = subjects.id
GROUP BY subjects.id, subjects.subject_name;

-- 5. Student-wise Average Marks
SELECT
    students.name,
    AVG(marks.mark) AS average_mark
FROM students
JOIN marks ON students.id = marks.student_id
GROUP BY students.id, students.name;
