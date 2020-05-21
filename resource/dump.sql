BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','bunnycast@naver.com','010-5012-8587','www.kim.com','2020-05-01 11:41:00');
INSERT INTO "users" VALUES(2,'Park','park@nate.com','010-2429-8474','www.park.com','2020-05-01 11:41:00');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-1111-1111','www.Lee.com','2020-05-01 11:41:00');
INSERT INTO "users" VALUES(4,'Cho','Cho@gmail.com','010-2222-2222','www.cho.com','2020-05-01 11:41:00');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@paran.com','010-3333-3333','www.Yoo.net','2020-05-01 11:41:00');
COMMIT;
