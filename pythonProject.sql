-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pythonProject
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pythonProject` ;

-- -----------------------------------------------------
-- Schema pythonProject
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pythonProject` DEFAULT CHARACTER SET utf8 ;
USE `pythonProject` ;

-- -----------------------------------------------------
-- Table `pythonProject`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pythonProject`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `delsired_datel` DATE NULL,
  `item_type` VARCHAR(200) NULL,
  `quanity` INT NULL,
  `size` VARCHAR(45) NULL,
  `details` VARCHAR(355) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
