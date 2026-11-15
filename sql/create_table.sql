


CREATE TABLE property (
    Property_ID INT AUTO_INCREMENT PRIMARY KEY,
    Apartment_type VARCHAR(100),
    Price_per_sq_ft DECIMAL(10,2),
    Area INT,
    Price BIGINT,
    Status VARCHAR(50),
    Location VARCHAR(150),
    Locality VARCHAR(100),
    City VARCHAR(100)
);