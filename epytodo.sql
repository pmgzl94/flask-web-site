drop database if exists epytodo;
CREATE database epytodo;

USE epytodo;

CREATE TABLE user ( 
user_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
username VARCHAR(100) NOT NULL,
password VARCHAR(64) NOT NULL
);

CREATE TABLE task (
task_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(100) NOT NULL,
begin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
end TIMESTAMP DEFAULT NULL,
status VARCHAR(100) DEFAULT 'not started'
);

create table user_has_task_table (
fk_user_id INT(6) UNSIGNED,
FOREIGN KEY (fk_user_id) REFERENCES user(user_id),
fk_task_id INT(6) UNSIGNED,
FOREIGN KEY (fk_task_id) REFERENCES task(task_id)
);
