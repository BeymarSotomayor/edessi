-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-10-2025 a las 22:13:10
-- Versión del servidor: 11.8.3-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `edessi`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_category`
--

CREATE TABLE `administrador_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador_category`
--

INSERT INTO `administrador_category` (`id`, `name`, `slug`) VALUES
(1, 'Juegos', 'juegos'),
(2, 'Programas', 'programas'),
(3, 'Audífonos', 'audifonos'),
(4, 'Cargadores', 'cargadores'),
(6, 'Fuentes', 'fuentes'),
(7, 'Memorias RAM', 'memorias-ram'),
(8, 'Memorias SSD', 'memorias-ssd'),
(9, 'Memorias HDD', 'memorias-hdd'),
(10, 'Tarjetas Gráficas', 'tarjetas-graficas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_client`
--

CREATE TABLE `administrador_client` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador_client`
--

INSERT INTO `administrador_client` (`id`, `name`, `last_name`, `email`, `phone`) VALUES
(1, 'Beymar', 'Sotomayor', NULL, '+591 71435956'),
(2, 'Juan', 'Javier Limachi', NULL, '+591 71435956'),
(4, 'Damaris', 'Gozalvez', NULL, '+591 71435956'),
(5, 'Armando', 'Sotomayor', NULL, '+59171103796');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_company`
--

CREATE TABLE `administrador_company` (
  `id` bigint(20) NOT NULL,
  `logo_img` varchar(100) DEFAULT NULL,
  `name_company` varchar(150) NOT NULL,
  `phone_company` varchar(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `nit` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador_company`
--

INSERT INTO `administrador_company` (`id`, `logo_img`, `name_company`, `phone_company`, `address`, `nit`) VALUES
(1, 'img_empresa/logo-edessi.png', 'Empresa de Desarrollo De Software y Servicios Informáticos', '+591 71435956', 'PC EDESSI GAME, CALLE JORDÁN ENTRE 16 DE JULIO Y ANTEZANA CALLE JORDÁN ENTRE 16 DE JULIO Y, C. Antezana, Cochabamba', 45678922);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_machine`
--

CREATE TABLE `administrador_machine` (
  `id` bigint(20) NOT NULL,
  `ticket` int(11) NOT NULL,
  `img_machine` varchar(100) DEFAULT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `detail` varchar(100) DEFAULT NULL,
  `problem` longtext DEFAULT NULL,
  `diagnostic` longtext DEFAULT NULL,
  `position` int(11) DEFAULT NULL,
  `accessories` longtext DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `price_aprox` decimal(10,2) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `delivery_in` datetime(6) DEFAULT NULL,
  `client_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador_machine`
--

INSERT INTO `administrador_machine` (`id`, `ticket`, `img_machine`, `brand`, `model`, `detail`, `problem`, `diagnostic`, `position`, `accessories`, `status`, `price_aprox`, `price`, `created_at`, `delivery_in`, `client_id`) VALUES
(1, 1, 'img_maquinas/17587526335475523967992998715914.jpg', 'LENOVO', 'Ideapad Gaming 3 82K1', 'Ninguno', 'No ingresa al sistema', 'Falla en el arranque del sistema', 1, 'USB de mause', 'En proceso', 70.00, 70.00, '2025-09-24 22:26:20.116658', '2025-10-03 01:01:00.000000', 1),
(19, 7, '', 'HP', 'Pavilion 2000', 'touch rajado', 'La pantalla se ve pixeleada, con una coloracion opaca', '', 3, '', 'Entregado', 520.00, 520.00, '2025-10-02 08:04:47.049000', '2025-10-03 04:03:00.000000', 2),
(24, 1, '', 'HP', 'Hp pavilion', 'touch en mal estado', 'No ingresas al sistema\r\npantall de azul de windows', '', 1, '', 'Pausado', 150.00, NULL, '2025-09-25 15:09:41.542585', '2025-10-03 22:15:00.000000', 4),
(25, 2, '', 'DELL', 'Inspirion 3000', NULL, '', '', 2, '', 'Reparación', 570.00, 0.00, '2025-09-25 21:42:03.675240', NULL, 2),
(26, 3, '', NULL, NULL, NULL, '', '', 2, '', 'Diagnóstico', 70.00, 0.00, '2025-09-25 22:49:14.302440', '2025-10-02 16:49:00.000000', 4),
(27, 1, '', NULL, NULL, NULL, '', '', 2, '', 'Entregado', 1490.00, 1400.00, '2025-09-28 21:49:54.228121', NULL, 4),
(32, 1, '', NULL, NULL, NULL, '', '', 1, '', 'Terminado', 0.00, 15.00, '2025-10-02 13:27:44.852952', NULL, 5),
(33, 3, '', NULL, NULL, NULL, '', '', 2, '', 'Recibido', 0.00, 0.00, '2025-10-02 19:47:59.063269', NULL, 5),
(34, 4, '', NULL, NULL, NULL, '', '', 3, '', 'En Revisión', 0.00, 0.00, '2025-10-02 19:48:04.801675', NULL, 5),
(35, 5, '', NULL, NULL, NULL, '', '', 3, '', 'Diagnóstico', 0.00, 0.00, '2025-10-02 19:48:14.009161', NULL, 5),
(36, 6, '', NULL, NULL, NULL, '', '', 3, '', 'Reparación', 0.00, 0.00, '2025-10-02 19:48:23.593917', NULL, 5),
(37, 7, '', NULL, NULL, NULL, '', '', 4, '', 'Pausado', 0.00, 0.00, '2025-10-02 19:48:30.037594', NULL, 5),
(38, 8, '', NULL, NULL, NULL, '', '', 4, '', 'Cancelado', 0.00, 0.00, '2025-10-02 19:48:37.945331', NULL, 5),
(39, 9, '', NULL, NULL, NULL, '', '', 4, '', 'En proceso', 0.00, 0.00, '2025-10-02 19:48:51.901814', NULL, 5),
(40, 10, '', NULL, NULL, NULL, '', '', 5, '', 'Terminado', 0.00, 0.00, '2025-10-02 19:49:12.886156', NULL, 5),
(41, 11, '', NULL, NULL, NULL, '', '', 5, '', 'Por entregar', 0.00, 0.00, '2025-10-02 19:49:20.359445', NULL, 5),
(42, 12, '', NULL, NULL, NULL, '', '', NULL, '', 'Entregado', 0.00, 0.00, '2025-10-02 19:49:30.526806', NULL, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_machine_services`
--

CREATE TABLE `administrador_machine_services` (
  `id` bigint(20) NOT NULL,
  `machine_id` bigint(20) NOT NULL,
  `service_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador_machine_services`
--

INSERT INTO `administrador_machine_services` (`id`, `machine_id`, `service_id`) VALUES
(2, 1, 1),
(6, 19, 1),
(8, 19, 4),
(7, 19, 10),
(13, 24, 1),
(14, 24, 2),
(76, 25, 2),
(78, 25, 5),
(77, 25, 10),
(38, 26, 1),
(63, 27, 1),
(64, 27, 2),
(65, 27, 3),
(66, 27, 4),
(67, 27, 5),
(68, 27, 6),
(69, 27, 7),
(70, 27, 8),
(71, 27, 9),
(72, 27, 10),
(73, 27, 11),
(74, 27, 12),
(75, 27, 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_product`
--

CREATE TABLE `administrador_product` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `detail` longtext DEFAULT NULL,
  `img_background` varchar(100) DEFAULT NULL,
  `img_name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador_product`
--

INSERT INTO `administrador_product` (`id`, `name`, `detail`, `img_background`, `img_name`, `price`, `category_id`) VALUES
(1, 'Demon\'s Souls', 'Juego de accion para motras tus capacidades de batalla', 'img_productos/demonsouls-bg.jpg', 'img_productos_name/demonsouls-logo.png', NULL, 1),
(2, 'Rachet', '', 'img_productos/ratchet-bg.jpg', 'img_productos_name/ratchet-logo.png', NULL, 1),
(3, 'Returnal', '', 'img_productos/returnal-bg.jpg', 'img_productos_name/returnal-logo.png', NULL, 1),
(4, 'Resident Evil', '', 'img_productos/re-bg.jpg', 'img_productos_name/re-logo.png', NULL, 1),
(5, 'Ram Kingston', 'Ram DDR4 3200 MHz', 'img_productos/2.jpg', '', 270.00, 7),
(7, 'Autodesk Autocad 2025', 'Programa de ingenieria y arquitectura', 'img_productos/autocad-bg.jpg', 'img_productos_name/autocad-logo.png', NULL, 2),
(8, 'Davinci Resolve', 'Programa de edición de video', 'img_productos/daresolve-bg.jpg', 'img_productos_name/daresolve-logo.png', NULL, 2),
(9, 'Eset NOD 32', 'Antivirus', 'img_productos/eset-bg.jpg', 'img_productos_name/eset-logo.png', NULL, 2),
(10, 'Lumion pro', 'Programa de renderización', 'img_productos/lumion-bg.jpg', 'img_productos_name/lumion-logo.png', 25.00, 2),
(11, 'Autodesk Revit 2025', 'Diseña edificios e infraestructuras en 3D. Crea proyectos más ecológicos. Transforma el mundo.', 'img_productos/revit-bg.png', 'img_productos_name/revit-logo_CRxT933.png', NULL, 2),
(12, 'Graphisoft Archicad', 'software de Modelado de Información de Construcción (BIM) que permite a arquitectos, diseñadores y constructores crear un \"Edificio Virtual\" con toda la información del proyecto integrada en un solo archivo, desde el diseño conceptual hasta la operación.', 'img_productos/archicad-bg.png', 'img_productos_name/archicad-logo.png', NULL, 2),
(13, 'Autodesk Inventor', 'es una herramienta de CAD 3D especializada en el diseño mecánico, que permite a los ingenieros y diseñadores crear modelos virtuales de productos, realizar simulaciones, generar documentación técnica y colaborar en proyectos de manufactura, validando el diseño antes de su fabricación física.', 'img_productos/inventor-bg.png', 'img_productos_name/inventor-logo.png', NULL, 2),
(14, 'Sony WH-CH520 Negro', 'Sony WH-CH520 Negro', 'img_productos/default-bg_5LQYzet.png', 'img_productos_name/Sony_WH-CH520_Negro.png', 260.00, 3),
(15, 'HAVIT H2016D', 'HAVIT H2016D', 'img_productos/default-bg.png', 'img_productos_name/HAVIT_H2016D_79UCyPI.png', 200.00, 3),
(16, 'HAVIT H2233d', '', 'img_productos/default-bg_klDiWyL.png', 'img_productos_name/HAVIT_H2233d_UOUUw8g.png', 160.00, 3),
(17, 'Sony WH-CH520 Azul', '', 'img_productos/default-bg_zhZGJWc.png', 'img_productos_name/Sony_WH-CH520_Azul.png', 100.00, 3),
(18, 'Meetion HP021 Gaming', '', 'img_productos/default-bg_S3iDgVi.png', 'img_productos_name/Meetion_HP021_Gaming.png', 350.00, 3),
(19, 'Redlemon W4000', '', 'img_productos/default-bg_HyoelZu.png', 'img_productos_name/Redlemon_W4000.png', 210.00, 3),
(20, 'Cyzone Rosa', '', 'img_productos/default-bg_Szob60J.png', 'img_productos_name/Cyzone_Rosa.png', 150.00, 3),
(21, 'Audífono Inalámbrico Tecpods T10', '', 'img_productos/default-bg_cKc8RQ5.png', 'img_productos_name/Audífono_Inalambrico_Tecpods_T10.png', 140.00, 3),
(22, 'Audífono Inalámbrico Tomate T-062BT', '', 'img_productos/default-bg_I6s1GDL.png', 'img_productos_name/Audífono_Inalambrico_Tomate_T-062BT.png', 140.00, 3),
(23, 'Audífono Inalámbrico TWS Thinkplus HT38', '', 'img_productos/default-bg_7dUpbOp.png', 'img_productos_name/Audífono_Inalambrico_TWS_Thinkplus_HT38.png', 210.00, 3),
(24, 'Audífono Inalámbrico Y50 Huawei', '', 'img_productos/default-bg_LM458Ew.png', 'img_productos_name/Audífono_Inalambrico_Y50_Huawei.png', 250.00, 3),
(25, 'Audífono Inalámbrico BTH022N Bluetooth', '', 'img_productos/default-bg_xSUk90L.png', 'img_productos_name/Audífonos_Inalámbricos_BTH022N_Bluetooth.png', 130.00, 3),
(26, 'Audífono Inalámbrico Earbuds Bluetooth TWS Waterproof RGB', '', 'img_productos/default-bg_GRXnQTY.png', 'img_productos_name/Audífonos_Inalámbricos_Earbuds_Bluetooth_TWS_Waterproof_RGB.png', 160.00, 3),
(27, 'Audífono Inalámbrico Billboard Azul', '', 'img_productos/default-bg_BgAEvba.png', 'img_productos_name/Auricular_Inalambrico_Billboard_Azul.png', 160.00, 3),
(28, 'Auricular Inalambrico Tomate T-498BT', '', 'img_productos/default-bg_4OGuAmj.png', 'img_productos_name/Auricular_Inalambrico_Tomate_T-498BT.png', 140.00, 3),
(29, 'Fuente Alimentación Corsair CX650 650 W 80 Plus Bronze', '', 'img_productos/fuente-bg.png', 'img_productos_name/Fuente_Alimentación_Corsair_CX650_650_W_80_Plus_Bronze.png', 999.99, 6),
(30, 'RM850e ATX 850W Cybenetics 80 Plus Gold Modular', 'RM850e ATX 3.1 PCIe 5.1 850W Cybenetics 80 Plus Gold Modular', 'img_productos/fuente-bg_pFB2iiE.png', 'img_productos_name/Fuente_Alimentación_Corsair_RMe_Series.png', 1499.99, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_service`
--

CREATE TABLE `administrador_service` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador_service`
--

INSERT INTO `administrador_service` (`id`, `name`, `price`) VALUES
(1, 'Instalación de sistema operativo (Windows)', 70.00),
(2, 'Reparación de Bisagra', 80.00),
(3, 'Limpieza de Polvo', 50.00),
(4, 'Cambio de pasta termica(No especial)', 80.00),
(5, 'Cambio de pasta térmica(Especial)', 120.00),
(6, 'Mantenimiento de software', 45.00),
(7, 'Limpieza de cabezal', 80.00),
(8, 'Cambio de rodillos', 120.00),
(9, 'Cambio de cabezales', 80.00),
(10, 'Cambio de teclado(Interno)', 370.00),
(11, 'Cambio de teclado(externo)', 270.00),
(12, 'Cambio de plug de carga', 45.00),
(13, 'Cambio de pantalla', 60.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add company', 8, 'add_company'),
(30, 'Can change company', 8, 'change_company'),
(31, 'Can delete company', 8, 'delete_company'),
(32, 'Can view company', 8, 'view_company'),
(33, 'Can add service', 9, 'add_service'),
(34, 'Can change service', 9, 'change_service'),
(35, 'Can delete service', 9, 'delete_service'),
(36, 'Can view service', 9, 'view_service'),
(37, 'Can add client', 10, 'add_client'),
(38, 'Can change client', 10, 'change_client'),
(39, 'Can delete client', 10, 'delete_client'),
(40, 'Can view client', 10, 'view_client'),
(41, 'Can add product', 11, 'add_product'),
(42, 'Can change product', 11, 'change_product'),
(43, 'Can delete product', 11, 'delete_product'),
(44, 'Can view product', 11, 'view_product'),
(45, 'Can add machine', 12, 'add_machine'),
(46, 'Can change machine', 12, 'change_machine'),
(47, 'Can delete machine', 12, 'delete_machine'),
(48, 'Can view machine', 12, 'view_machine');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$VPplYjgRZ5QMcknUWuxGZb$0ez9xoB0Fx1K7bG5spt8ytwgB/GmNHzgUY/cdA9XMxQ=', '2025-10-02 19:22:05.835325', 1, 'beymar', '', '', 'beymar@gmail.com', 1, 1, '2025-09-24 22:14:27.197604');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'administrador', 'category'),
(10, 'administrador', 'client'),
(8, 'administrador', 'company'),
(12, 'administrador', 'machine'),
(11, 'administrador', 'product'),
(9, 'administrador', 'service'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-09-24 22:13:09.923932'),
(2, 'auth', '0001_initial', '2025-09-24 22:13:10.135618'),
(3, 'admin', '0001_initial', '2025-09-24 22:13:10.179545'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-09-24 22:13:10.185190'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-09-24 22:13:10.189861'),
(6, 'administrador', '0001_initial', '2025-09-24 22:13:10.337167'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-09-24 22:13:10.377864'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-09-24 22:13:10.399566'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-09-24 22:13:10.414506'),
(10, 'auth', '0004_alter_user_username_opts', '2025-09-24 22:13:10.419963'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-09-24 22:13:10.439049'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-09-24 22:13:10.440321'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-09-24 22:13:10.445809'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-09-24 22:13:10.460306'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-09-24 22:13:10.474559'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-09-24 22:13:10.489593'),
(17, 'auth', '0011_update_proxy_permissions', '2025-09-24 22:13:10.497434'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-09-24 22:13:10.512226'),
(19, 'sessions', '0001_initial', '2025-09-24 22:13:10.531408'),
(20, 'administrador', '0002_alter_machine_price_alter_machine_price_aprox', '2025-09-26 02:16:13.833774'),
(21, 'administrador', '0003_alter_machine_ticket', '2025-10-02 18:50:27.425828');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0zb1yc2hvs4qkhkfc2swnx1ogsey9itc', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1jtR:9rSXFUj3bN6fgkSJTfBcdcgl-YhSxTkLfYoM2vGNRms', '2025-10-09 11:12:09.001060'),
('2ywyz3vvzd61vsa3yax0a71fumlj415c', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v3gJw:KtxndMwk0cQhv-9puuoPdaC7p5Fn82YZvWZf_zePZZI', '2025-10-14 19:47:32.619735'),
('3ewvnty8jv606fib82qs7fjkcit45b09', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v4Jfl:YovAw39L8FRq2ECAZ0C1YqmyZCYsAJqBZXbLNqYslOU', '2025-10-16 13:48:41.382074'),
('73lrwwzggk8yobum01nsmhw7bul4y9ma', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v3wAV:8R8paHNqXFk2VgZHx0r_1r9Qq3dlmdYLn03Kih-1Rgo', '2025-10-15 12:42:51.472922'),
('91qknu1mdspm14y6iuipimzvb87qmi1l', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v3KZ0:yXviHAtsgpkqBH3CH16maORxGvF9AF1qY0zXKM4fWB8', '2025-10-13 20:33:38.004458'),
('afa4tbf16u2ig1m9za3dz98bxop0a20v', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v3RmW:kYVjVni31JKevmsXMKBbQsQsxVbpD-IxwQuwEsknuMw', '2025-10-14 04:16:04.753294'),
('btu8hg79upwoe7n5jom9y7yhw1q6nq1k', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1cz6:gKAIrzA1Atl_PAKOvY7gXlYVK0DeSjpiGqG-6uYk_vc', '2025-10-09 03:49:32.841443'),
('c2ng1jjtwaahe14qblxx0fnknj3onert', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v44cQ:3Zmo-UckZPqgN7NKvQ6SLchuJ1x_8p6OUcxvIDFjO4E', '2025-10-15 21:44:14.325429'),
('c4hllr3y42wm2402leue1ejnc4m6gq09', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v2zA5:rpiA8afbb_McuLlVTOpWCh3i_Pmi0zhMwpbSCgASloc', '2025-10-12 21:42:29.377343'),
('d3mwu5it6al4hfgbf3wjqe95i8vryh3g', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1XqB:1qPCj1z0dPPtMhBzKywnWjUg-YGcyrzkZfpF67Y-FK8', '2025-10-08 22:19:59.373442'),
('ehv85kg7kh6qp9vfjqjafrly5dgo1za5', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1Xs5:MH5ILbGDQpUiEauh_27sLhtr85YT79LrVm6MWjEkrTE', '2025-10-08 22:21:57.155922'),
('f1zbu2dcnnp0ffqz76wv1rsz92l1fbpn', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v45kI:XN7EqxNioae1C3OhIHESCLUgZg3bQwM4tIPrQNHw_e4', '2025-10-15 22:56:26.452389'),
('fxf09sfm892mtqb1md83otb3k13glmyb', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v4OEH:pVbz8sMZFcEmnr5z4ygyADk3zkOT7nY3Tf3uz2Sdsf8', '2025-10-16 18:40:37.413534'),
('jqqy2y4cbnfp83hxh44d2d7i37olr3ze', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v4LVQ:hYzaZ7w6TyWNzKInq3lWRd-zi8pRE-W8zrLOY5EptcE', '2025-10-16 15:46:08.566022'),
('kn0mvujxvraq8yvn8u86knhbmbglsgxz', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1nYK:x1GGkSvOOgzkT5kis4v8g9DpIXQfxNeVphte4dUMbw4', '2025-10-09 15:06:36.552054'),
('le9guvv74ndmuouv1hb1skfn3ju6egts', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1YXw:VWvuZLx4w9joyyzd4bxIZAvKG7YUb5FJxwMVnP0AWlI', '2025-10-08 23:05:12.046646'),
('mvhxcim71pwe220fxtoh7z8cru5tdlok', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1mVY:ZnmkhuQejRQMw7YtiJTvI_iT_XjwMbvz2eu_VXH1Nkk', '2025-10-09 13:59:40.817606'),
('otr4j2mzai22hlbpgb33eamidpuql5t5', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v4KOR:08UseJNQGNIZ1Sv0EbojWs2uLvIinciGvtqWGrWj8t0', '2025-10-16 14:34:51.422660'),
('p72nsf228gnwbmjtcim92edigdqqzxnr', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v4Oqm:aeBbmrws2lm2Av29mpSRySizTt2-1Xh5jBYtZ7NKhtY', '2025-10-16 19:20:24.323691'),
('rqo208hs9xdyk4mifbyq5j0tss6ptkqb', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1jnd:flD_3ebTuu1Q313VQm-BKleqvzkZwjklp_85muAVjVs', '2025-10-09 11:06:09.409583'),
('soc5rjz50fb4ovvdkrnsbjxlfhtqobpw', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v4OsP:tKzfyvRPVqao38a4dPjZjtQ90nsF--1TYWLx25CszF8', '2025-10-16 19:22:05.836829'),
('trssbdcs6e9dzjc05tmjxap7y0tyxsen', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v4Lu8:913QTGbgMwt-k_sHA02R3spfm3uCx2Sgp-Ftffddj58', '2025-10-16 16:11:40.843609'),
('w0ggbt9a1vj9okscnsuo173atskwp9yw', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v3gEF:ZVTN0ak9M9HTl5qBSrPQyZt2LIGnrFV_4iu4N6KkNvM', '2025-10-14 19:41:39.660625'),
('w57mny9m0cu7a6eukkcam4bjx53ei8o9', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1kp4:ujm_-ssyMA1KrNiXPpy35W21XiRy3AT-rC5wmvM2tVg', '2025-10-09 12:11:42.836305'),
('wr8sug7pin8kuib1nd4jijmhpv3zny8h', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1xVr:-Ji9dF1Pmabw3kH7rFFL0Qz_1I7ki_vHgJDvTT4gfQU', '2025-10-10 01:44:43.233070'),
('xuq6c8uysy0e86gij8adsu394pe4y9a0', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v1aDA:UUL3GIcZ0YEGjLB1egwX-kG09b419yBip0X1RmckiVE', '2025-10-09 00:51:52.207837'),
('z06wo8g00tqxgqi3rl13hckwr0l7lk20', '.eJxVjDsOwjAQBe_iGlnrT-KEkp4zWOv1Lg4gR4qTCnF3iJQC2jcz76UibmuJW-MlTlmdlVGn3y0hPbjuIN-x3mZNc12XKeld0Qdt-jpnfl4O9--gYCvfusuQ-gCJnR3dCMIGE7EI0wBekCx4YxyY4MURBe4tewELJEFg6Kx6fwD0vjgX:1v2zh2:z-z2J0tPlMkKBoSlalT4w65kU_J87jP2P3SfGwQ66Rk', '2025-10-12 22:16:32.454569');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador_category`
--
ALTER TABLE `administrador_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indices de la tabla `administrador_client`
--
ALTER TABLE `administrador_client`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_client_name_lastname` (`name`,`last_name`);

--
-- Indices de la tabla `administrador_company`
--
ALTER TABLE `administrador_company`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `administrador_machine`
--
ALTER TABLE `administrador_machine`
  ADD PRIMARY KEY (`id`),
  ADD KEY `administrador_machin_client_id_40d1ac46_fk_administr` (`client_id`);

--
-- Indices de la tabla `administrador_machine_services`
--
ALTER TABLE `administrador_machine_services`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `administrador_machine_se_machine_id_service_id_613018cb_uniq` (`machine_id`,`service_id`),
  ADD KEY `administrador_machin_service_id_f61cc36f_fk_administr` (`service_id`);

--
-- Indices de la tabla `administrador_product`
--
ALTER TABLE `administrador_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `administrador_produc_category_id_a7706692_fk_administr` (`category_id`);

--
-- Indices de la tabla `administrador_service`
--
ALTER TABLE `administrador_service`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador_category`
--
ALTER TABLE `administrador_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `administrador_client`
--
ALTER TABLE `administrador_client`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `administrador_company`
--
ALTER TABLE `administrador_company`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `administrador_machine`
--
ALTER TABLE `administrador_machine`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `administrador_machine_services`
--
ALTER TABLE `administrador_machine_services`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- AUTO_INCREMENT de la tabla `administrador_product`
--
ALTER TABLE `administrador_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `administrador_service`
--
ALTER TABLE `administrador_service`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador_machine`
--
ALTER TABLE `administrador_machine`
  ADD CONSTRAINT `administrador_machin_client_id_40d1ac46_fk_administr` FOREIGN KEY (`client_id`) REFERENCES `administrador_client` (`id`);

--
-- Filtros para la tabla `administrador_machine_services`
--
ALTER TABLE `administrador_machine_services`
  ADD CONSTRAINT `administrador_machin_machine_id_6453e972_fk_administr` FOREIGN KEY (`machine_id`) REFERENCES `administrador_machine` (`id`),
  ADD CONSTRAINT `administrador_machin_service_id_f61cc36f_fk_administr` FOREIGN KEY (`service_id`) REFERENCES `administrador_service` (`id`);

--
-- Filtros para la tabla `administrador_product`
--
ALTER TABLE `administrador_product`
  ADD CONSTRAINT `administrador_produc_category_id_a7706692_fk_administr` FOREIGN KEY (`category_id`) REFERENCES `administrador_category` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
