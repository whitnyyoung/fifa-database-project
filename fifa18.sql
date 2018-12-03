DROP DATABASE IF EXISTS fifa;
CREATE database fifa;
USE fifa;

CREATE TABLE players(
playerID INT NOT NULL UNIQUE, 
play_fname VARCHAR(35) NOT NULL,
play_lname VARCHAR(35) NOT NULL,
play_born DATE NOT NULL,
play_salary INT NOT NULL,
play_networth INT NOT NULL,
primary key(playerID));

CREATE TABLE clubs(
clubID INT NOT NULL UNIQUE,
club_name VARCHAR(35) NOT NULL,
club_city VARCHAR(35) NOT NULL,
club_budget DECIMAL(12,2) NOT NULL,
primary key(clubID));

CREATE TABLE attributes(
attributeID INT NOT NULL UNIQUE,
playerID INT NOT NULL UNIQUE,
attr_agility INT NOT NULL,
attr_crossing INT NOT NULL,
attr_balance INT NOT NULL,
attr_specialty VARCHAR(15),
primary key(attributeID),
foreign key (playerID) REFERENCES players(playerID));

create index cmID on clubs(clubID);
create index cmID on players(play_fname);
create index cmID2 on players(play_lname);

CREATE TABLE club_members(
playerID INT NOT NULL UNIQUE,
clubID INT NOT NULL,
firstName VARCHAR(35) NOT NULL,
lastName VARCHAR(35) NOT NULL,
position VARCHAR(10) NOT NULL,
primary key(playerID),
foreign key(playerID) REFERENCES players(playerID),
foreign key(clubID) REFERENCES clubs(clubID),
foreign key(firstName) REFERENCES players(play_fname),
foreign key(lastName) REFERENCES players(play_lname));


insert into players values(101, 'Cristiano', 'Ronaldo', '85-02-05', 565000, 95500000);
insert into players values(102, 'Lionel', 'Messi', '87-06-24', 565000, 105000000);
insert into players values(103, 'Neymar', 'da Silva Santos, Jr.', '92-02-05', 280000, 123000000);
insert into players values(104, 'Luis', 'Suarez', '87-01-24', 510000, 97000000);
insert into players values(105, 'Manuel', 'Neuer', '86-03-27', 230000, 61000000);

insert into clubs values(1, 'FC Bayern Munich', 'Munich', 640000000.00);
insert into clubs values(2, 'FC Barcelona', 'Barcelona', 914000000.00);
insert into clubs values(3, 'Paris Saint-Germain', 'Paris', 825000000.00);
insert into clubs values(4, 'Real Madrid CF', 'Madrid', 1030000000.00);
insert into clubs values(5, 'Manchester United', 'Old Trafford', 835000000.00);

insert into attributes values(501, 101, 89, 85, 63, 'dribbling');
insert into attributes values(502, 102, 90, 77, 95, 'scoring');
insert into attributes values(503, 103, 96, 75, 82, 'scoring');
insert into attributes values(504, 104, 86, 77, 60, 'passing');
insert into attributes values(505, 105, 89, 85, 63, 'blocking');

insert into club_members values(101, 4, 'Cristiano', 'Ronaldo', 'Forward');
insert into club_members values(102, 2, 'Lionel', 'Messi', 'Forward');
insert into club_members values(103, 3, 'Neymar', 'da Silva Santos, Jr.', 'Forward');
insert into club_members values(104, 2, 'Luis', 'Suarez', 'Forward');
insert into club_members values(105, 1, 'Manuel', 'Neuer', 'Goalkeeper');
