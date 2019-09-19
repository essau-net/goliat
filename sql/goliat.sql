-- phpMyAdmin SQL Dump
-- version 4.6.0
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 19-09-2019 a las 18:36:47
-- Versión del servidor: 5.7.12-log
-- Versión de PHP: 7.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `goliat`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `idAct` int(11) NOT NULL,
  `tituloaAct` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `propositoAct` text COLLATE utf8_spanish_ci NOT NULL,
  `progresoAct` int(11) NOT NULL,
  `actFinalizada` tinyint(1) NOT NULL,
  `fechaIniAct` date NOT NULL,
  `fechaFinAct` datetime NOT NULL,
  `fechaPrevistaFin` datetime NOT NULL,
  `iconA` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `idE` int(11) NOT NULL,
  `nomE` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `puestoE` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `tituloE` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `direccionE` varchar(60) COLLATE utf8_spanish_ci NOT NULL,
  `usuarioTipo` varchar(1) COLLATE utf8_spanish_ci NOT NULL,
  `usuarioN` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `contraUsuario` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `imagenUsuario` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `idGrupo` int(11) NOT NULL,
  `encargadoGrupo` int(11) NOT NULL,
  `iconGrupo` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`idAct`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`idE`);

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`idGrupo`),
  ADD KEY `encargadoGrupo` (`encargadoGrupo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `actividad`
--
ALTER TABLE `actividad`
  MODIFY `idAct` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `idE` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `grupo`
--
ALTER TABLE `grupo`
  MODIFY `idGrupo` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
