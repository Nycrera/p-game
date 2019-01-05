CREATE TABLE `users` (
	`id` smallint NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(255) NOT NULL UNIQUE,
	`password` VARCHAR(255) NOT NULL,
	`points` int NOT NULL DEFAULT 0,
	`banned` tinyint NOT NULL DEFAULT 0,
	`admin` tinyint NOT NULL DEFAULT 0,
	PRIMARY KEY (`id`)
);