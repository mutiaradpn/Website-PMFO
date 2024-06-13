-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 22 Bulan Mei 2024 pada 16.00
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `optik`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `akun`
--

CREATE TABLE `akun` (
  `id` int(11) NOT NULL,
  `namadepan` varchar(200) NOT NULL,
  `namabelakang` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `akun`
--

INSERT INTO `akun` (`id`, `namadepan`, `namabelakang`, `email`, `username`, `password`) VALUES
(4, 'aji', 'sasongko', 'jisong710@gmail.com', 'jisong710', '123456'),
(5, 'aji', 'sasongko', 'jisong710@gmail.com', 'jisong710', '1234456'),
(6, 'aji', 'sasongko', 'jisong710@gmail.com', 'jisong710', '1234456'),
(7, 'Ivah Puspita', 'Payangan', 'ivahpuspita46@gmail.com', 'ivahpuspita', 'ivah123'),
(8, 'Adzka', 'zahratu', 'zahratuadzka@gmail.com', 'adzka', '123'),
(9, 'bagus', 'pras', 'bpras747@gmail.com', 'baguspras', 'baguspras');

-- --------------------------------------------------------

--
-- Struktur dari tabel `inputber`
--

CREATE TABLE `inputber` (
  `id` int(11) NOT NULL,
  `tanggal` varchar(200) NOT NULL,
  `osnr` float NOT NULL,
  `hasil` varchar(200) NOT NULL,
  `kanal` int(11) NOT NULL,
  `qfactor` float NOT NULL,
  `redaman` float NOT NULL,
  `panjang` int(11) NOT NULL,
  `power` int(11) NOT NULL,
  `spasi_kanal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `inputber`
--

INSERT INTO `inputber` (`id`, `tanggal`, `osnr`, `hasil`, `kanal`, `qfactor`, `redaman`, `panjang`, `power`, `spasi_kanal`) VALUES
(46, '2024-05-22 20:38:50.587120', 123, 'optimal', 8, 123, 123, 123, 123, 123123);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `akun`
--
ALTER TABLE `akun`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `inputber`
--
ALTER TABLE `inputber`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `akun`
--
ALTER TABLE `akun`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `inputber`
--
ALTER TABLE `inputber`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
