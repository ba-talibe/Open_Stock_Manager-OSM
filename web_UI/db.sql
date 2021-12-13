

CREATE TABLE IF NOT EXISTS articles (
	id integer auto_increment,
	code varchar(50),
    designation varchar(100),
	descriptions varchar(500),
	quantite integer,
    primary key(id, code)
);