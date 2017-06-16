-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-06-2017 a las 00:49:20
-- Versión del servidor: 10.1.16-MariaDB
-- Versión de PHP: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;


--
-- Base de datos: `supermercado`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_compra_temp`
--

CREATE TABLE `detalle_compra_temp` (
  `id_detalle_compra` int(10) NOT NULL,
  `id_producto` int(10) NOT NULL,
  `cantidad` int(10) NOT NULL,
  `valor` bigint(20) NOT NULL,
  `user` varchar(50) NOT NULL,
  `fecha_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_factura`
--

CREATE TABLE `detalle_factura` (
  `id_detalle` int(10) NOT NULL,
  `id_producto` int(10) NOT NULL,
  `cantidad` int(10) NOT NULL,
  `valor` bigint(20) NOT NULL,
  `user` varchar(50) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `id_factura` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `detalle_factura`
--

INSERT INTO `detalle_factura` (`id_detalle`, `id_producto`, `cantidad`, `valor`, `user`, `fecha_registro`, `id_factura`) VALUES
(1, 12, 2, 3000, 'usuario', '2017-04-22 18:11:22', 7),
(2, 12, 5, 7500, 'usuario', '2017-04-22 18:11:31', 7),
(3, 11, 2, 3000, 'usuario', '2017-04-22 18:11:35', 7),
(4, 12, 3, 4500, 'usuario', '2017-04-22 18:15:54', 7),
(5, 12, 3, 4500, 'usuario', '2017-04-22 18:17:00', 7),
(6, 1, 1, 1500, 'usuario', '2017-04-22 18:41:17', 7),
(7, 1, 1, 1500, 'usuario', '2017-04-22 19:08:16', 7),
(8, 12, 2, 3000, 'usuario', '2017-04-22 18:11:22', 11),
(9, 12, 5, 7500, 'usuario', '2017-04-22 18:11:31', 11),
(10, 11, 2, 3000, 'usuario', '2017-04-22 18:11:35', 11),
(11, 12, 3, 4500, 'usuario', '2017-04-22 18:15:54', 11),
(12, 12, 3, 4500, 'usuario', '2017-04-22 18:17:00', 11),
(13, 1, 1, 1500, 'usuario', '2017-04-22 18:41:17', 11),
(14, 1, 1, 1500, 'usuario', '2017-04-22 19:08:16', 11),
(15, 12, 2, 3000, 'usuario', '2017-04-22 18:11:22', 12),
(16, 12, 5, 7500, 'usuario', '2017-04-22 18:11:31', 12),
(17, 11, 2, 3000, 'usuario', '2017-04-22 18:11:35', 12),
(18, 12, 3, 4500, 'usuario', '2017-04-22 18:15:54', 12),
(19, 12, 3, 4500, 'usuario', '2017-04-22 18:17:00', 12),
(20, 1, 1, 1500, 'usuario', '2017-04-22 18:41:17', 12),
(21, 1, 1, 1500, 'usuario', '2017-04-22 19:08:16', 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `id_fatura` int(10) NOT NULL,
  `user` varchar(30) NOT NULL,
  `total` bigint(20) NOT NULL,
  `fecha_factura` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `factura`
--

INSERT INTO `factura` (`id_fatura`, `user`, `total`, `fecha_factura`) VALUES
(1, '2', 24000, '2017-04-22 18:43:20'),
(2, '2', 24000, '2017-04-22 19:05:29'),
(3, '2', 24000, '2017-04-22 19:06:28'),
(4, '2', 25500, '2017-04-22 19:08:30'),
(5, '2', 25500, '2017-04-22 19:09:33'),
(6, '2', 25500, '2017-04-22 19:10:35'),
(7, '2', 25500, '2017-04-22 19:11:30'),
(8, '2', 25500, '2017-04-22 19:11:57'),
(9, '2', 25500, '2017-04-22 19:12:50'),
(10, '2', 25500, '2017-04-22 19:14:56'),
(11, '2', 25500, '2017-04-22 19:17:35'),
(12, '2', 25500, '2017-04-22 19:28:45');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `logs`
--

CREATE TABLE `logs` (
  `id` int(2) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `intentos` varchar(10) NOT NULL,
  `ip` varchar(20) NOT NULL,
  `hora_ingreso` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `logs`
--

INSERT INTO `logs` (`id`, `fecha_ingreso`, `usuario`, `intentos`, `ip`, `hora_ingreso`) VALUES
(1, '2017-04-18', 'asdasd', 'Fallo', '127.0.0.1', '20:29:05'),
(2, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:29:11'),
(3, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:33:37'),
(4, '2017-04-18', 'asd', 'Fallo', '127.0.0.1', '20:34:27'),
(5, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:34:34'),
(6, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:38:39'),
(7, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:39:36'),
(8, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:41:25'),
(9, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:46:07'),
(10, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:46:45'),
(11, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:48:11'),
(12, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:51:29'),
(13, '2017-04-18', 'admin', 'ok', '127.0.0.1', '20:51:51'),
(14, '2017-04-18', 'usuario', 'ok', '127.0.0.1', '20:52:13'),
(15, '2017-04-18', 'admin', 'ok', '127.0.0.1', '21:11:11'),
(16, '2017-04-18', 'admin', 'ok', '127.0.0.1', '21:28:09'),
(17, '2017-04-18', 'admin', 'ok', '127.0.0.1', '21:28:44'),
(18, '2017-04-18', 'admin', 'ok', '127.0.0.1', '21:29:22'),
(19, '2017-04-18', 'admin', 'ok', '127.0.0.1', '21:31:38'),
(20, '2017-04-18', 'admin', 'ok', '127.0.0.1', '21:41:24'),
(21, '2017-04-18', 'usuario', 'ok', '127.0.0.1', '21:41:33'),
(22, '2017-04-18', 'admin', 'ok', '127.0.0.1', '21:58:48'),
(23, '2017-04-18', 'usuario', 'ok', '127.0.0.1', '21:58:58'),
(24, '2017-04-18', 'usuario', 'ok', '127.0.0.1', '22:00:07'),
(25, '2017-04-18', 'usuario', 'ok', '127.0.0.1', '22:04:28'),
(26, '2017-04-18', 'usuario', 'ok', '127.0.0.1', '22:05:20'),
(27, '2017-04-18', 'admin', 'ok', '127.0.0.1', '22:19:56'),
(28, '2017-04-18', 'usuario', 'ok', '127.0.0.1', '22:20:13'),
(29, '2017-04-22', 'admin', 'ok', '127.0.0.1', '16:15:28'),
(30, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '16:15:37'),
(31, '2017-04-22', 'uaurio', 'Fallo', '127.0.0.1', '16:18:39'),
(32, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '16:18:51'),
(33, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:04:00'),
(34, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:07:23'),
(35, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:08:18'),
(36, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:09:17'),
(37, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:47:10'),
(38, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:48:22'),
(39, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:49:54'),
(40, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '17:53:10'),
(41, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '18:10:16'),
(42, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '18:11:14'),
(43, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '18:15:46'),
(44, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '18:16:56'),
(45, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '18:41:10'),
(46, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '18:43:09'),
(47, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:05:24'),
(48, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:06:24'),
(49, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:08:10'),
(50, '2017-04-22', 'usuario', 'Fallo', '127.0.0.1', '19:09:24'),
(51, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:09:29'),
(52, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:10:30'),
(53, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:11:27'),
(54, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:11:54'),
(55, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:12:45'),
(56, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:14:53'),
(57, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:17:32'),
(58, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:28:09'),
(59, '2017-04-22', 'usuario', 'ok', '127.0.0.1', '19:28:40'),
(60, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:04:06'),
(61, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:07:09'),
(62, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:08:03'),
(63, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:08:39'),
(64, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:09:00'),
(65, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:10:59'),
(66, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:12:59'),
(67, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:14:08'),
(68, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:15:24'),
(69, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:16:34'),
(70, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:19:29'),
(71, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:20:18'),
(72, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:21:00'),
(73, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:22:41'),
(74, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:24:44'),
(75, '2017-04-25', 'usuario', 'ok', '127.0.0.1', '20:25:39'),
(76, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:04:09'),
(77, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:11:18'),
(78, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:11:45'),
(79, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:12:47'),
(80, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:13:25'),
(81, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:13:48'),
(82, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:25:38'),
(83, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:26:48'),
(84, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:38:45'),
(85, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:42:57'),
(86, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:44:25'),
(87, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '08:59:30'),
(88, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:13:43'),
(89, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:15:16'),
(90, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:15:35'),
(91, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:20:49'),
(92, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:27:29'),
(93, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:42:23'),
(94, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:46:39'),
(95, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:48:45'),
(96, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:52:33'),
(97, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:53:31'),
(98, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '09:54:45'),
(99, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '10:37:14'),
(100, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '10:45:43'),
(101, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '10:50:57'),
(102, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '10:52:26'),
(103, '2017-04-26', 'admin', 'ok', '127.0.0.1', '10:52:59'),
(104, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '11:30:26'),
(105, '2017-04-26', 'admin', 'ok', '127.0.0.1', '11:30:33'),
(106, '2017-04-26', 'usuario', 'ok', '127.0.0.1', '11:45:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `premios`
--

CREATE TABLE `premios` (
  `id` int(11) NOT NULL,
  `premio` varchar(100) NOT NULL,
  `puntos` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `premios`
--

INSERT INTO `premios` (`id`, `premio`, `puntos`) VALUES
(1, 'Olla Arrocera', 20),
(2, 'Lampara de Techo', 15),
(3, 'Juego de Cocina', 25),
(4, 'Televisor 14 Pulgadas', 50);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `premios_cambiados`
--

CREATE TABLE `premios_cambiados` (
  `id` int(4) NOT NULL,
  `idpremio` int(4) NOT NULL,
  `user` varchar(50) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `premios_cambiados`
--

INSERT INTO `premios_cambiados` (`id`, `idpremio`, `user`, `fecha`) VALUES
(1, 3, 'usuario', '2017-04-26');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(2) NOT NULL,
  `producto` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `val_unit` varchar(10) NOT NULL,
  `stock` int(10) NOT NULL,
  `stock_minimo` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `producto`, `descripcion`, `val_unit`, `stock`, `stock_minimo`) VALUES
(1, 'Manzana', 'Fresca', '1500', 20, 15),
(2, 'Poma Madura', 'Fruta Fresca', '1600', 10, 20),
(3, 'axion', 'lavaplatos', '15000', 10, 5),
(4, 'Flores', 'Rojas', '1500', 15, 10),
(5, 'mango', 'verde', '1000', 10, 5),
(6, 'rosas', 'blancas', '1000', 12, 15),
(7, 'arroz', 'roa', '1600', 10, 5),
(8, 'fresas', 'verdes', '1000', 10, 5),
(9, 'moras', 'congeladas', '16000', 10, 5),
(10, 'peras', 'peras', '1000', 1000, 5),
(11, 'papaya', '', '2000', 10, 15),
(12, 'Aguacate', 'Maduro', '1500', 5, 10),
(13, 'arequipe', 'delicioso', '1000', 10, 15),
(14, 'computador', 'Ram: 4GB DD:1TB', '2000000', 10, 5),
(15, 'Lapiceros', 'BIC', '1000', 5, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `id` int(2) NOT NULL,
  `tipo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_usuario`
--

INSERT INTO `tipo_usuario` (`id`, `tipo`) VALUES
(1, 'ADMINISTRADOR'),
(2, 'CLIENTE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(2) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `tipo_user` int(2) NOT NULL,
  `fecha_registro` date NOT NULL,
  `puntos` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `email`, `pass`, `nombre`, `tipo_user`, `fecha_registro`, `puntos`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'Jhon James Cano', 1, '2017-04-15', 0),
(2, 'cliente', '827ccb0eea8a706c4c34a16891f84e7b', 'Vianey Patricia Ceballos', 2, '2017-04-17', 30),
(3, 'yeison.velasquez@gmail.com', '827ccb0eea8a706c4c34a16891f84e7b', 'yeison velasquez', 1, '2017-04-18', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `detalle_compra_temp`
--
ALTER TABLE `detalle_compra_temp`
  ADD PRIMARY KEY (`id_detalle_compra`);

--
-- Indices de la tabla `detalle_factura`
--
ALTER TABLE `detalle_factura`
  ADD PRIMARY KEY (`id_detalle`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id_fatura`);

--
-- Indices de la tabla `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `premios`
--
ALTER TABLE `premios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `premios_cambiados`
--
ALTER TABLE `premios_cambiados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `detalle_compra_temp`
--
ALTER TABLE `detalle_compra_temp`
  MODIFY `id_detalle_compra` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `detalle_factura`
--
ALTER TABLE `detalle_factura`
  MODIFY `id_detalle` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `id_fatura` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT de la tabla `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;
--
-- AUTO_INCREMENT de la tabla `premios`
--
ALTER TABLE `premios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `premios_cambiados`
--
ALTER TABLE `premios_cambiados`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
