-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 22, 2021 at 01:05 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `day` date NOT NULL,
  `usn` varchar(15) NOT NULL,
  `presence` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`day`, `usn`, `presence`) VALUES
('2021-09-21', '4SN18CS008', 1),
('2021-09-21', '4SN18CS049', 1),
('2021-09-21', '4SN18CS069', 0),
('2021-09-21', '4SN18CS072', 1),
('2021-09-21', '4SN18CS076', 1),
('2021-09-21', '4SN18CS083', 0),
('2021-09-22', '4SN18CS008', 1),
('2021-09-22', '4SN18CS049', 1),
('2021-09-22', '4SN18CS072', 1),
('2021-09-22', '4SN18CS076', 1),
('2021-09-22', '4SN18CS083', 0),
('2021-09-23', '4SN18CS008', 1),
('2021-09-23', '4SN18CS049', 0),
('2021-09-23', '4SN18CS069', 1),
('2021-09-23', '4SN18CS072', 1),
('2021-09-23', '4SN18CS076', 0),
('2021-09-23', '4SN18CS083', 1);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `usn` varchar(15) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `semester` decimal(1,0) DEFAULT NULL,
  `branch` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`usn`, `name`, `semester`, `branch`) VALUES
('4SN18CS008', 'Ankit Bangera', '7', 'CS'),
('4SN18CS049', 'Manmith SK', '7', 'CS'),
('4SN18CS069', 'Rachan N Jadav', '7', 'CS'),
('4SN18CS072', 'Ranisha', '7', 'CS'),
('4SN18CS076', 'Sahan KJ', '7', 'CS'),
('4SN18CS083', 'Shibin Joseph', '7', 'CS');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`day`,`usn`),
  ADD KEY `usn` (`usn`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`usn`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`usn`) REFERENCES `students` (`usn`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
