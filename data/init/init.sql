CREATE TABLE IF NOT EXISTS locations (
    location_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL
);

INSERT INTO locations (name, city, country) VALUES
('New_York_Office', 'New York', 'USA'),
('London_Office', 'London', 'UK'),
('Tokyo_Office', 'Tokyo', 'Japan'),
('Berlin_Office', 'Berlin', 'Germany'),
('Sydney_Office', 'Sydney', 'Australia');
