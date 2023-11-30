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
-- Struttura della tabella `clienti_leonardo_malaguti`
--

CREATE TABLE `clienti_leonardo_malaguti` (
  `id` int(250) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `posizione_lavorativa` varchar(30) NOT NULL,
  `data_di_assunzione` date NOT NULL,
  `data_corrente` date NOT NULL,
  `luogo_di_nascita` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `clienti_leonardo_malaguti`
--

INSERT INTO `clienti_leonardo_malaguti` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `data_di_assunzione`, `data_corrente`, `luogo_di_nascita`) VALUES
(1, 'rr', 'tt', 'yu', '0000-00-00', '0000-00-00', 'oi'),
(89, 'harma', 'sing', 'tt', '2023-10-12', '2023-10-15', 'ii'),
(90, 'leonardo', 'malaguti', 'sottopagato', '0000-00-00', '0000-00-00', 'corre');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `clienti_leonardo_malaguti`
--
ALTER TABLE `clienti_leonardo_malaguti`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `clienti_leonardo_malaguti`
--
ALTER TABLE `clienti_leonardo_malaguti`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=91;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
