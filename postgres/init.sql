CREATE TABLE users
( username varchar(25) PRIMARY KEY,
  password varchar(30) NOT NULL
);
INSERT INTO users (username, password) VALUES('admin', 'password');
INSERT INTO users (username, password) VALUES('alice', '1234');
INSERT INTO users (username, password) VALUES('bob', '4321');