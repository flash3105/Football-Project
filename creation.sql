CREATE DATABASE IF NOT EXISTS player_profiles;

USE player_profiles;

CREATE TABLE IF NOT EXISTS players (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    age INT,
    birth_date DATE,
    birth_place VARCHAR(255),
    birth_country VARCHAR(255),
    nationality VARCHAR(255),
    height VARCHAR(50),
    weight VARCHAR(50),
    number INT,
    position VARCHAR(50),
    photo_url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS api_responses (
    response_id INT AUTO_INCREMENT PRIMARY KEY,
    get_request VARCHAR(255),
    player_id INT,
    parameters_player INT,
    errors JSON,
    results INT,
    paging_current INT,
    paging_total INT,
    FOREIGN KEY (player_id) REFERENCES players(id)
);
