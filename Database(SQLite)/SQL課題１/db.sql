-- 課題１
-- １．性別が男である生徒の名前を一覧で表示せよ。
-- ２．1教科でも30点以下の点数を取った生徒の名前を一覧で表示せよ。
-- 　　ただし、重複は許さないものとする。
-- ３．性別ごとに、最も高かった試験の点数を表示せよ。
-- ４．教科ごとの試験の平均点が50点以下である教科を表示せよ。
-- ５．試験結果テーブルの点数の右に、その教科の平均点を表示せよ。

-- 学生テーブル
-- 学籍番号,氏名,性別
-- 0001,長岡 一馬,男
-- 0002,中本 知佳,女
-- 0003,松本 義文,男
-- 0004,佐竹 友香,女

-- 試験結果テーブル
-- 学籍番号,教科,点数
-- 0001,国語,30
-- 0001,英語,30
-- 0002,国語,70
-- 0002,数学,80
-- 0003,理科,92
-- 0004,社会,90
-- 0004,理科,35
-- 0004,英語,22

CREATE TABLE
    student_data (
        id TEXT,
        name TEXT,
        gender TEXT
    );

CREATE TABLE
    test_result (
        id TEXT,
        subject TEXT,
        score INTEGER
    );

INSERT INTO student_data VALUES('001', '長岡 一馬','男');
INSERT INTO student_data VALUES('002', '中本 知佳','女');
INSERT INTO student_data VALUES('003', '松本 義文','男');
INSERT INTO student_data VALUES('004', '佐竹 友香','女');

INSERT INTO test_result VALUES('001', '国語',30);
INSERT INTO test_result VALUES('001', '英語',30);
INSERT INTO test_result VALUES('002', '国語',70);
INSERT INTO test_result VALUES('002', '数学',80);
INSERT INTO test_result VALUES('003', '理科',92);
INSERT INTO test_result VALUES('004', '社会',90);
INSERT INTO test_result VALUES('004', '理科',35);
INSERT INTO test_result VALUES('004', '英語',22);

-- 性別が男である生徒の名前を一覧で表示せよ。
SELECT name FROM student_data WHERE gender = '男';

-- 1教科でも30点以下の点数を取った生徒の名前を一覧で表示せよ。
-- ただし、重複は許さないものとする。

SELECT DISTINCT -- DISTINCT:重複データを削除
    student_data.name,
    test_result.score
FROM 
    student_data 
INNER JOIN 
    test_result ON student_data.id = test_result.id 
WHERE 
    test_result.score <= 30;

-- 性別ごとに、最も高かった試験の点数を表示せよ。

SELECT
    student_data.gender,
    MAX(score) -- (test_result.score)省略
FROM
    student_data
INNER JOIN
    test_result ON student_data.id = test_result.id
GROUP BY gender; -- グループ化して男女それぞれの結果を表示

-- 教科ごとの試験の平均点が50点以下である教科を表示せよ。
SELECT 
    subject AS 教科,
    AVG(score) AS 平均点
FROM
    test_result
GROUP BY 
    subject
HAVING -- グループ化された結果を絞り込み
    AVG(score) <= 50
ORDER BY 
    平均点 ASC;

-- 試験結果テーブルの点数の右に、その教科の平均点を表示せよ。
SELECT -- 表示させたい項目(試験結果、平均)
    test_result.id,
    student_data.name AS 名前,
    test_result.subject AS 教科,
    test_result.score AS 点数,
    (SELECT 
        AVG(score)
    FROM 
        test_result AS 結果
    WHERE
        結果.subject = test_result.subject) AS 教科平均
FROM
    student_data
INNER JOIN
    test_result 
ON
    student_data.id = test_result.id
ORDER BY
    student_data.id,test_result.subject;
