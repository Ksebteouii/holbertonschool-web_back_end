
-- Creates a table called users with
-- edge cases to ensure it never fails
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` varchar(255) NOT NULL UNIQUE,
    `name` varchar(255)
);
