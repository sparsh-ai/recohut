CREATE TABLE IF NOT EXISTS car_data (
    id SERIAL PRIMARY KEY,
    model VARCHAR(50), 
    year INTEGER,
    price INTEGER,
    transmission VARCHAR(50),
    mileage INTEGER,
    fuelType VARCHAR(50),
    tax INTEGER,
    mpg FLOAT,
    engineSize FLOAT,

    -- additional field
    suggestedPrice INTEGER
);