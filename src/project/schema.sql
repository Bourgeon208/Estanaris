DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS character;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE character (
    id INTEGER,
    user_id INTEGER NOT NULL,
    alive INTEGER NOT NULL,
    name TEXT NOT NULL,
    house TEXT NOT NULL UNIQUE,
    attribute TEXT NOT NULL,
    profession TEXT NOT NULL,
    xp INTEGER NOT NULL,
    skills TEXT NOT NULL,
    location TEXT NOT NULL,
    profession_en TEXT NOT NULL,
    renown INTEGER NOT NULL,
    reputation INTEGER NOT NULL,
    lv INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    alignment_lc INTEGER NOT NULL,
    alignment_ge INTEGER NOT NULL,
    classe TEXT NOT NULL,
    dv INTEGER NOT NULL,
    spell_attribute TEXT,
    spells_known TEXT,
    feats TEXT,
    lores TEXT,
    items_worn TEXT,
    items TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id), PRIMARY KEY(id)
 );
