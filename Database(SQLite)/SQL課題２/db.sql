-- 課題２
-- １．趣味に映画鑑賞が含まれる社員の名前を一覧で表示せよ。
-- ２．社員の趣味一覧を表示せよ(重複しない)
-- ３．名字が佐藤である社員の、趣味の数を表示せよ。
-- ４．同じ趣味を持つ社員の一覧を表示せよ。

-- 社員テーブル
-- 社員番号,名,部署番号
-- 1,杉山 佑,1
-- 2,佐藤 結菜,2
-- 3,高橋 絵里,3
-- 4,早川 良太,2
-- 5,佐藤 一弥,3
-- 6,佐藤 優穂,1

-- 部署テーブル
-- 部署番号,部署名
-- 1,営業部
-- 2,人事部
-- 3,経理部

-- 趣味テーブル
-- No,社員番号,趣味
-- 1,1,サッカー
-- 2,1,ドライブ
-- 3,1,映画鑑賞
-- 4,2,映画鑑賞
-- 5,2,旅行
-- 6,2,インスタ
-- 7,3,ゲーム
-- 8,4,ドライブ
-- 9,4,料理
-- 10,6,インスタ
-- 11,6,TikTok


CREATE TABLE
    emp_list (
        id TEXT,
        name TEXT,
        divisionNo TEXT
    );

CREATE TABLE
    division_list (
        divisionNo TEXT,
        divisionName TEXT
    );

CREATE TABLE
    hobby_list (
        nomber TEXT,
        id TEXT,
        hobby TEXT
    );

DROP TABLE emp_list;

INSERT INTO emp_list VALUES('1','杉山 佑','1');
INSERT INTO emp_list VALUES('2','佐藤 結菜','2');
INSERT INTO emp_list VALUES('3','高橋 絵里','3');
INSERT INTO emp_list VALUES('4','早川 良太','2');
INSERT INTO emp_list VALUES('5','佐藤 一弥','3');
INSERT INTO emp_list VALUES('6','佐藤 優穂','1');

INSERT INTO division_list VALUES('1','営業部');
INSERT INTO division_list VALUES('2','人事部');
INSERT INTO division_list VALUES('3','経理部');

INSERT INTO hobby_list VALUES('1','1','サッカー');
INSERT INTO hobby_list VALUES('2','1','ドライブ');
INSERT INTO hobby_list VALUES('3','1','映画鑑賞');
INSERT INTO hobby_list VALUES('4','2','映画鑑賞');
INSERT INTO hobby_list VALUES('5','2','旅行');
INSERT INTO hobby_list VALUES('6','2','インスタ');
INSERT INTO hobby_list VALUES('7','3','ゲーム');
INSERT INTO hobby_list VALUES('8','4','ドライブ');
INSERT INTO hobby_list VALUES('9','4','料理');
INSERT INTO hobby_list VALUES('10','6','インスタ');
INSERT INTO hobby_list VALUES('11','6','TikTok');


-- １．趣味に映画鑑賞が含まれる社員の名前を一覧で表示せよ。
SELECT
    emp_list.name AS 名前,
    hobby_list.hobby AS 趣味
FROM
    emp_list
INNER JOIN
    hobby_list ON emp_list.id = hobby_list.id 
WHERE
    hobby ='映画鑑賞';

-- ２．社員の趣味一覧を表示せよ(重複しない)
SELECT DISTINCT
    hobby_list.hobby AS 趣味一覧
FROM 
    hobby_list;

-- ３．名字が佐藤である社員の、趣味の数を表示せよ。
SELECT
    emp_list.name AS 名前,
    COUNT(hobby) AS 趣味の数
FROM
    emp_list
LEFT OUTER JOIN -- INNER JOINだと趣味なし佐藤がはじかれる
    hobby_list ON emp_list.id = hobby_list.id
WHERE -- 「佐藤」前方一致
    emp_list.name LIKE '佐藤%'
GROUP BY
    emp_list.name;

-- ４．同じ趣味を持つ社員の一覧を表示せよ。
SELECT
    hobby_list.hobby AS 趣味,
    GROUP_CONCAT( DISTINCT emp_list.name) AS 社員 -- グループの中身をカンマ区切りえ表示してくれる
FROM
    hobby_list
INNER JOIN
    emp_list ON hobby_list.id = emp_list.id
GROUP BY 
    hobby_list.hobby
HAVING -- 絞り込み 
    COUNT(DISTINCT emp_list.id) > 1 -- HAVING COUNTで重複したデータを1とする。>1がないと全部の趣味が表示される
ORDER BY 
    hobby_list.hobby;


-- ４．同じ趣味を持つ社員の一覧を表示せよ。(別解)
SELECT DISTINCT -- 社員の名前の重複させないように
    hobby_list.hobby AS 趣味,
    emp_list.name AS 社員
FROM
    hobby_list
INNER JOIN
    emp_list ON hobby_list.id = emp_list.id
WHERE
    hobby_list.hobby IN (
        SELECT hobby
        FROM hobby_list
        GROUP BY hobby
        HAVING COUNT(DISTINCT id) > 1
    )
ORDER BY 
    hobby_list.hobby, emp_list.name;