-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 30, 2023 alle 23:09
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `zona_di_lavoro_malaguti_leonardo`
--

CREATE TABLE `zona_di_lavoro_malaguti_leonardo` (
  `id` int(30) NOT NULL,
  `nome_zona` varchar(30) NOT NULL,
  `numero_clienti` int(30) NOT NULL,
  `id_dipendente` varchar(30) NOT NULL,
  `numero_dipenmdenti` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `zona_di_lavoro_malaguti_leonardo`
--

INSERT INTO `zona_di_lavoro_malaguti_leonardo` (`id`, `nome_zona`, `numero_clienti`, `id_dipendente`, `numero_dipenmdenti`) VALUES
(2, 'capo_passero', 99, '7', 200),
(3, 'cagliari', -15, '2', 9);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zona_di_lavoro_malaguti_leonardo`
--
ALTER TABLE `zona_di_lavoro_malaguti_leonardo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zona_di_lavoro_malaguti_leonardo`
--
ALTER TABLE `zona_di_lavoro_malaguti_leonardo`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
