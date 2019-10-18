-- phpMyAdmin SQL Dump
-- version 5.0.0-alpha1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 16, 2019 at 12:40 PM
-- Server version: 5.7.27-log
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `goliat`
--

-- --------------------------------------------------------

--
-- Table structure for table `actividad`
--

CREATE TABLE `actividad` (
  `idAct` int(11) NOT NULL,
  `tituloaAct` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `propositoAct` text COLLATE utf8_spanish_ci,
  `progresoAct` int(11) DEFAULT NULL,
  `actFinalizada` tinyint(1) DEFAULT NULL,
  `fechaIniAct` date NOT NULL,
  `fechaFinAct` datetime DEFAULT NULL,
  `fechaPrevistaFin` datetime DEFAULT NULL,
  `iconA` blob
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cronograma`
--

CREATE TABLE `cronograma` (
  `idCronograma` int(11) NOT NULL,
  `idE` int(11) NOT NULL,
  `idGrupo` int(11) NOT NULL,
  `idAct` int(11) NOT NULL,
  `idSub` int(11) NOT NULL,
  `nombreProyecto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `empleado`
--

CREATE TABLE `empleado` (
  `idE` int(11) NOT NULL,
  `nombresE` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `apellidosE` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `fechaNacimientoE` date DEFAULT NULL,
  `numeroE` int(18) DEFAULT NULL,
  `puestoE` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tituloE` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `paisE` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estadoE` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ciudadE` int(11) DEFAULT NULL,
  `usuarioTipo` varchar(1) COLLATE utf8_spanish_ci DEFAULT NULL,
  `usuarioE` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `contraUsuario` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `imagenUsuario` blob
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grupo`
--

CREATE TABLE `grupo` (
  `idGrupo` int(11) NOT NULL,
  `encargadoGrupo` int(11) NOT NULL,
  `iconGrupo` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sub_actividad`
--

CREATE TABLE `sub_actividad` (
  `idSub` int(11) NOT NULL,
  `idAct` int(11) NOT NULL,
  `tituloSub` varchar(50) NOT NULL,
  `propositoSub` text NOT NULL,
  `progresoSub` int(11) NOT NULL,
  `subActFinalizada` tinyint(1) NOT NULL,
  `fechaIniSub` datetime NOT NULL,
  `fechaPrevistaFinSub` datetime NOT NULL,
  `fechaFinSub` int(11) NOT NULL,
  `iconSub` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`idAct`);

--
-- Indexes for table `cronograma`
--
ALTER TABLE `cronograma`
  ADD PRIMARY KEY (`idCronograma`),
  ADD KEY `idE` (`idE`),
  ADD KEY `idGrupo` (`idGrupo`),
  ADD KEY `idAct` (`idAct`),
  ADD KEY `idSub` (`idSub`);

--
-- Indexes for table `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`idE`);

--
-- Indexes for table `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`idGrupo`),
  ADD KEY `encargadoGrupo` (`encargadoGrupo`);

--
-- Indexes for table `sub_actividad`
--
ALTER TABLE `sub_actividad`
  ADD PRIMARY KEY (`idSub`),
  ADD KEY `idAct` (`idAct`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actividad`
--
ALTER TABLE `actividad`
  MODIFY `idAct` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cronograma`
--
ALTER TABLE `cronograma`
  MODIFY `idCronograma` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `empleado`
--
ALTER TABLE `empleado`
  MODIFY `idE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `grupo`
--
ALTER TABLE `grupo`
  MODIFY `idGrupo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sub_actividad`
--
ALTER TABLE `sub_actividad`
  MODIFY `idSub` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cronograma`
--
ALTER TABLE `cronograma`
  ADD CONSTRAINT `cronograma_ibfk_1` FOREIGN KEY (`idAct`) REFERENCES `actividad` (`idAct`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cronograma_ibfk_2` FOREIGN KEY (`idGrupo`) REFERENCES `grupo` (`idGrupo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cronograma_ibfk_3` FOREIGN KEY (`idE`) REFERENCES `empleado` (`idE`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cronograma_ibfk_4` FOREIGN KEY (`idSub`) REFERENCES `sub_actividad` (`idSub`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `grupo`
--
ALTER TABLE `grupo`
  ADD CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`encargadoGrupo`) REFERENCES `empleado` (`idE`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sub_actividad`
--
ALTER TABLE `sub_actividad`
  ADD CONSTRAINT `sub_actividad_ibfk_1` FOREIGN KEY (`idAct`) REFERENCES `actividad` (`idAct`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

