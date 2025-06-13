CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
username TEXT NOT NULL UNIQUE,
email TEXT NOT NULL UNIQUE,
date_of_birth DATE NOT NULL
password_hash TEXT NOT NULL,
);

-- Collection of All Shortened URLS
CREATE TABLE IF NOT EXISTS Short_Urls (
    uuid TEXT PRIMARY KEY NOT NULL, -- Unique id of created url
    owner_id integer NOT NULL, -- ID OF OWNER
    short_url TEXT NOT NULL, 
    original_url TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    slug TEXT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Users(id) ON DELETE CASCADE
);