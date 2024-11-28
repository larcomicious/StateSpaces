DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE building (
    building_id SERIAL PRIMARY KEY NOT NULL,
    building_name VARCHAR(25) NOT NULL,
    street INT NOT NULL,
    district VARCHAR(25) NOT NULL,
    city VARCHAR(25) NOT NULL
);

CREATE TABLE agent (
    agent_id SERIAL PRIMARY KEY NOT NULL,
    agent_name VARCHAR(40) NOT NULL,
    contact INT NOT NULL,
    building_id INT,
    FOREIGN KEY(building_id) REFERENCES building(building_id)
);

CREATE TABLE venue (
    venue_id SERIAL PRIMARY KEY NOT NULL,
    venue_name VARCHAR(25) NOT NULL, -- Fixed VARCHAR syntax
    floor_area INT NOT NULL,
    capacity INT NOT NULL,
    renovating BOOLEAN NOT NULL,
    building_id INT, -- Added to reference the building
    agent_id INT, -- Added to reference the agent
    FOREIGN KEY(building_id) REFERENCES building(building_id),
    FOREIGN KEY(agent_id) REFERENCES agent(agent_id)
);

CREATE TABLE floor (
    building_id INT NOT NULL,
    venue_id INT NOT NULL,
    PRIMARY KEY(building_id, venue_id),
    FOREIGN KEY(building_id) REFERENCES building(building_id),
    FOREIGN KEY(venue_id) REFERENCES venue(venue_id)
);

CREATE TABLE venue_type (
    venue_id INT NOT NULL,
    venue_type VARCHAR(25) NOT NULL,
    PRIMARY KEY(venue_id, venue_type),
    FOREIGN KEY(venue_id) REFERENCES venue(venue_id)
);

CREATE TABLE amenity (
    amenity_id SERIAL PRIMARY KEY NOT NULL,
    amenity_type VARCHAR(25) NOT NULL,
    description VARCHAR(255),
    quantity INT NOT NULL,
    venue_id INT,
    FOREIGN KEY(venue_id) REFERENCES venue(venue_id)
);

CREATE TABLE team (
    team_id SERIAL PRIMARY KEY NOT NULL,
    team_name VARCHAR(25) NOT NULL,
    role VARCHAR(25) NOT NULL,
    agent_id INT,
    FOREIGN KEY(agent_id) REFERENCES agent(agent_id)
);

CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY NOT NULL,
    customer_name VARCHAR(40) NOT NULL,
    birth_date DATE NOT NULL,
    contact_no BIGINT NOT NULL
);

CREATE TABLE reservation (
    reservation_id SERIAL PRIMARY KEY NOT NULL,
    reserved_from DATE NOT NULL,
    reserved_to DATE NOT NULL,
    number_of_participants INT NOT NULL, -- Fixed casing for consistency
    venue_id INT NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY(venue_id) REFERENCES venue(venue_id),
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

INSERT INTO building (building_id, building_name, street, district, city)
VALUES
    (1, 'Skyline Tower', 123, 'Downtown', 'Metro City'),
    (2, 'Green Valley Center', 456, 'Uptown', 'Greenfield'),
    (3, 'Oceanview Plaza', 789, 'Coastal', 'Seaview');

INSERT INTO agent (agent_id, agent_name, contact, building_id)
VALUES
    (1, 'Alice Johnson', 76543210, 1),
    (2, 'Bob Smith', 65432109, 1),
    (3, 'Catherine Lee', 54321098, 2),
    (4, 'David Brown', 43210987, 2),
    (5, 'Emily Davis', 32109876, 3);

INSERT INTO customer (customer_id, customer_name, birth_date, contact_no)
VALUES
    (1, 'John Doe', '1985-06-15', 9876543210),
    (2, 'Jane Smith', '1990-03-22', 8765432109),
    (3, 'Michael Brown', '2000-11-05', 7654321098),
    (4, 'Emily Davis', '1995-07-19', 6543210987),
    (5, 'Sarah Wilson', '1988-12-10', 5432109876);

INSERT INTO venue (venue_id, venue_name, floor_area, capacity, renovating, building_id, agent_id)
VALUES
    (1, 'Grand Ballroom', 1000, 500, FALSE, 1, 1),
    (2, 'Conference Room A', 200, 50, TRUE, 1, 2),
    (3, 'Outdoor Garden', 1500, 300, FALSE, 2, 3),
    (4, 'Theater Hall', 800, 400, FALSE, 2, 4),
    (5, 'Meeting Room B', 100, 20, FALSE, 3, 2);

INSERT INTO reservation (reservation_id, reserved_from, reserved_to, number_of_participants, venue_id, customer_id)
VALUES
    (1, '2024-12-01', '2024-12-02', 100, 1, 1),
    (2, '2024-12-03', '2024-12-04', 50, 2, 2),
    (3, '2024-12-05', '2024-12-06', 200, 3, 3),
    (4, '2024-12-07', '2024-12-08', 150, 4, 4),
    (5, '2024-12-09', '2024-12-10', 75, 5, 5);

