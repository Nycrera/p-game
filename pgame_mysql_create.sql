CREATE TABLE `users` (
	`id` smallint NOT NULL AUTO_INCREMENT,
	`username` TEXT NOT NULL UNIQUE,
	`password` TEXT NOT NULL,
	`points` int NOT NULL DEFAULT '0',
	`banned` tinyint NOT NULL DEFAULT '0',
	`admin` tinyint NOT NULL DEFAULT '0',
	PRIMARY KEY (`id`)
);

