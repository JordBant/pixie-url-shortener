CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL,
);

-- Collection of All Shortened URLS
CREATE TABLE IF NOT EXISTS Short_Urls (
    owner_id integer NOT NULL, -- ID OF OWNER
    uuid TEXT PRIMARY KEY NOT NULL, -- Unique id of created url
    short_url TEXT NOT NULL, 
    original_url TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    short_url TEXT NOT NULL,
    slug TEXT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Users(id) ON DELETE CASCADE
);