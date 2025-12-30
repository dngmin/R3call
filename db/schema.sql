CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    word TEXT UNIQUE,
    pronunciation TEXT,
    meaning TEXT,
    count INTEGER DEFAULT 0
)