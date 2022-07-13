-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recipes_belt_prep
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `recipes_belt_prep` ;

-- -----------------------------------------------------
-- Schema recipes_belt_prep
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipes_belt_prep` DEFAULT CHARACTER SET utf8 ;
USE `recipes_belt_prep` ;

-- -----------------------------------------------------
-- Table `recipes_belt_prep`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `recipes_belt_prep`.`users` ;

CREATE TABLE IF NOT EXISTS `recipes_belt_prep`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(50) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes_belt_prep`.`recipes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `recipes_belt_prep`.`recipes` ;

CREATE TABLE IF NOT EXISTS `recipes_belt_prep`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `instructions` VARCHAR(255) NULL,
  `under_30` TINYINT(2) NULL,
  `date_made` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `recipes_belt_prep`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
