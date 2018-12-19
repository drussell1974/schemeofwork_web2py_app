-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: db764008810.hosting-data.io
-- Generation Time: Dec 15, 2018 at 07:30 AM
-- Server version: 5.5.60-0+deb7u1-log
-- PHP Version: 7.0.33-0+deb9u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db764008810`
--

-- --------------------------------------------------------

--
-- Table structure for table `sow_ks123_pathway`
--

CREATE TABLE `sow_ks123_pathway` (
  `id` int(11) NOT NULL,
  `objective` varchar(1000) NOT NULL,
  `year_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `subject_purpose_id` int(11) DEFAULT NULL,
  `Abstraction` varchar(5) DEFAULT NULL,
  `Decomposition` varchar(5) DEFAULT NULL,
  `AlgorithmicThinking` varchar(5) DEFAULT NULL,
  `Evaluation` varchar(5) DEFAULT NULL,
  `Generalisation` varchar(5) DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sow_ks123_pathway`
--

INSERT INTO `sow_ks123_pathway` (`id`, `objective`, `year_id`, `topic_id`, `subject_purpose_id`, `Abstraction`, `Decomposition`, `AlgorithmicThinking`, `Evaluation`, `Generalisation`, `created`, `created_by`, `published`) VALUES
(1, 'Understands what an algorithm is and is able to express simple linear (non-branching) algorithms symbolically. (AL)', 1, 1, 2, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(2, 'Understands that computers need precise instructions. (AL)', 1, 1, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(3, 'Demonstrates care and precision to avoid errors. (AL)', 1, 1, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(4, 'Understands that algorithms are implemented on digital devices as programs. (AL)', 2, 1, 2, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(5, 'Designs simple algorithms using loops, and selection i.e. if statements. (AL)', 2, 1, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(6, 'Uses logical reasoning to predict outcomes. (AL)', 2, 1, 3, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(7, 'Detects and corrects errors i.e. debugging, in algorithms. (AL)', 2, 1, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(8, 'Designs solutions (algorithms) that use repetition and two-way selection i.e. if, then and else. (AL)', 3, 1, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(9, 'Uses diagrams to express solutions. (AB)', 3, 1, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(10, 'Uses logical reasoning to predict outputs, showing an awareness of inputs. (AL)', 3, 1, 2, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(11, 'Shows an awareness of tasks best completed by humans or computers. (EV)', 4, 1, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(12, 'Designs solutions by decomposing a problem and creates a sub-solution for each of these parts. (DE) (AL) (AB)', 4, 1, 1, 'TRUE', 'TRUE', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(13, 'Recognises that different solutions exist for the same problem. (AL) (AB)', 4, 1, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(14, 'Understands that iteration is the repetition of a process such as a loop. (AL)', 5, 1, 2, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(15, 'Recognises that different algorithms exist for the same problem. (AL) (GE)', 5, 1, 3, '', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(16, 'Represents solutions using a structured notation. (AL) (AB)', 5, 1, 2, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(17, 'Can identify similarities and differences in situations and can use these to solve problems (pattern recognition). (GE)', 5, 1, 1, '', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(18, 'Understands a recursive solution to a problem repeatedly applies the same solution to smaller instances of the problem. (AL) (GE)', 6, 1, 1, '', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(19, 'Recognises that some problems share the same characteristics and use the same algorithm to solve both. (AL) (GE)', 6, 1, 1, '', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(20, 'Understands the notion of performance for algorithms and appreciates that some algorithms have different performance characteristics for the same task. (AL) (EV)', 6, 1, 3, '', '', 'TRUE', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(21, 'Recognises that the design of an algorithm is distinct from its expression in a programming language (which will depend on the programming constructs available). (AL) (AB)', 7, 1, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(22, 'Evaluates the effectiveness of algorithms and models for similar problems. (AL) (AB) (GE)', 7, 1, 2, 'TRUE', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(23, 'Recognises where information can be filtered out in generalizing problem solutions. (AL) (AB) (GE)', 7, 1, 1, 'TRUE', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(24, 'Uses logical reasoning to explain how an algorithm works. (AL) (AB) (DE)', 7, 1, 2, 'TRUE', 'TRUE', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(25, 'Represents algorithms using structured language. (AL) (DE) (AB)', 7, 1, 1, 'TRUE', 'TRUE', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(26, 'Designs a solution to a problem that depends on solutions to smaller instances of the same problem (recursion). (AL) (DE) (AB) (GE)', 8, 1, 1, 'TRUE', 'TRUE', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(27, 'Understands that some problems cannot be solved computationally. (AB) (GE)', 8, 1, 3, 'TRUE', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(28, 'Knows that users can develop their own programs, and can demonstrate this by creating a simple program in an environment that does not rely on text e.g. programmable robots etc. (AL)', 1, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(29, ' Executes, checks and changes programs. (AL)', 1, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(30, 'Understands that programs execute by following precise instructions. (AL)', 1, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(31, 'Uses arithmetic operators, if statements, and loops, within programs. (AL)', 2, 2, 3, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(32, 'Uses logical reasoning to predict the behaviour of programs. (AL)', 2, 2, 3, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(33, 'Detects and corrects simple semantic errors i.e. debugging, in programs. (AL)', 2, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(34, 'Creates programs that implement algorithms to achieve given goals. (AL)', 3, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(35, 'Declares and assigns variables. (AB)', 3, 2, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(36, 'Uses post-tested loop e.g. until, and a sequence of selection statements in programs, including an if, then and else statement. (AL)', 3, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(37, 'Understands the difference between, and appropriately uses if and if, then and else statements. (AL)', 4, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(38, ' Uses a variable and relational operators within a loop to govern termination. (AL) (GE)', 4, 2, 1, '', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(39, 'Designs, writes and debugs modular programs using procedures. (AL) (DE) (AB) (GE)', 4, 2, 1, 'TRUE', 'TRUE', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(40, 'Knows that a procedure can be used to hide the detail with sub-solution. (AL) (DE) (AB) (GE)', 4, 2, 1, 'TRUE', 'TRUE', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(41, 'Understands that programming bridges the gap between algorithmic solutions and computers. (AB)', 5, 2, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(42, 'Has practical experience of a high-level textual language, including using standard libraries when programming. (AB) (AL)', 5, 2, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(43, 'Uses a range of operators and expressions e.g. Boolean, and applies them in the context of program control. (AL)', 5, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(44, 'Selects the appropriate data types. (AL) (AB)', 5, 2, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(45, 'Uses nested selection statements. (AL)', 6, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(46, 'Appreciates the need for, and writes, custom functions including use of parameters. (AL) (AB)', 6, 2, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(47, 'Knows the difference between, and uses appropriately, procedures and functions. (AL) (AB)', 6, 2, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(48, 'Understands and uses negation with operators. (AL)', 6, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(49, 'Uses and manipulates one dimensional data structures. (AB)', 6, 2, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(50, 'Detects and corrects syntactical errors. (AL)', 6, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(51, 'Appreciates the effect of the scope of a variable e.g. a local variable cannot be accessed from outside its function. (AB) (AL)', 7, 2, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(52, 'Understands and applies parameter passing. (AB) (GE) (DE)', 7, 2, 1, 'TRUE', 'TRUE', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(53, 'Understands the difference between, and uses, both pre-tested e.g. while, and post-tested e.g. until loops. (AL)', 7, 2, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(54, 'Applies a modular approach to error detection and correction. (AB) (DE) (GE)', 7, 2, 1, 'TRUE', 'TRUE', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(55, 'Designs and writes nested modular programs that enforce reusability utilising sub-routines wherever possible. (AL) (AB) (GE) (DE)', 8, 2, 1, 'TRUE', 'TRUE', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(56, 'Understands the difference between While loop and For loop, which uses a loop counter. (AL) (AB)', 8, 2, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(57, 'Understands and uses two dimensional data structures. (AB) (DE)', 8, 2, 1, 'TRUE', 'TRUE', '', '', '', '0000-00-00 00:00:00', 0, 1),
(58, 'Recognises that digital content can be represented in many forms. (AB) (GE)', 1, 3, 3, 'TRUE', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(59, 'Distinguishes between some of these forms and can explain the different ways that they communicate information. (AB)', 1, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(60, 'Recognises different types of data: text, number. (AB) (GE)', 2, 3, 3, 'TRUE', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(61, 'Appreciates that programs can work with different types of data. (GE)', 2, 3, 3, '', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(62, 'Recognises that data can be structured in tables to make it useful. (AB) (DE)', 2, 3, 3, 'TRUE', 'TRUE', '', '', '', '0000-00-00 00:00:00', 0, 1),
(63, 'Understands the difference between data and information. (AB)', 3, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(64, 'Knows why sorting data in a flat file can improve searching for information. (EV)', 3, 3, 3, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(65, 'Uses filters or can perform single criteria searches for information.(AL)', 3, 3, 3, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(66, 'Performs more complex searches for information e.g. using Boolean and relational operators. (AL) (GE) (EV)', 4, 3, 3, '', '', 'TRUE', 'TRUE', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(67, 'Analyses and evaluates data and information, and recognises that poor quality data leads to unreliable results, and inaccurate conclusions. (AL) (EV)', 4, 3, 3, '', '', 'TRUE', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(68, 'Knows that digital computers use binary to represent all data. (AB)', 5, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(69, 'Understands how bit patterns represent numbers and images. (AB)', 5, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(70, 'Knows that computers transfer data in binary. (AB)', 5, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(71, 'Understands the relationship between binary and file size (uncompressed). (AB)', 5, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(72, 'Defines data types: real numbers and Boolean. (AB)', 5, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(73, 'Queries data on one table using a typical query language. (AB)', 5, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(74, 'Understands how numbers, images, sounds and character sets use the same bit patterns. (AB) (GE)', 6, 3, 3, 'TRUE', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(75, 'Performs simple operations using bit patterns e.g. binary addition. (AB) (AL)', 6, 3, 3, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(76, 'Understands the relationship between resolution and colour depth, including the effect on file size. (AB)', 6, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(77, 'Distinguishes between data used in a simple program (a variable) and the storage structure for that data. (AB)', 6, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(78, 'Knows the relationship between data representation and data quality. (AB)', 7, 3, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(79, 'Understands the relationship between binary and electrical circuits, including Boolean logic. (AB)', 7, 3, 2, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(80, 'Understands how and why values are data typed in many different languages when manipulated within programs. (AB)', 7, 3, 2, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(81, 'Performs operations using bit patterns e.g. conversion between binary and hexadecimal, binary subtraction etc. (AB) (AL) (GE)', 8, 3, 2, 'TRUE', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(82, 'Understands and can explain the need for data compression, and performs simple compression methods. (AL) (AB)', 8, 3, 2, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(83, 'Knows what a relational database is, and understands the benefits of storing data in multiple tables. (AB) (GE) (DE)', 8, 3, 1, 'TRUE', 'TRUE', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(84, 'Understands that computers have no intelligence and that computers can do nothing unless a program is executed. (AL)', 1, 4, 3, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(85, 'Recognises that all software executed on digital devices is programmed. (AL) (AB) (GE)', 1, 4, 1, 'TRUE', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(86, 'Recognises that a range of digital devices can be considered a computer. (AB) (GE) ', 2, 4, 1, 'TRUE', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(87, 'Recognises and can use a range of input and output devices.', 2, 4, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(88, 'Understands how programs specify the function of a general purpose computer. (AB)', 2, 4, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(89, 'Knows that computers collect data from various input devices, including sensors and application software. (AB)', 3, 4, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(90, 'Understands the difference between hardware and application software, and their roles within a computer system. (AB)', 3, 4, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(91, 'Understands why and when computers are used. (EV)', 4, 4, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(92, 'Understands the main functions of the operating system. (DE) (AB)', 4, 4, 1, 'TRUE', 'TRUE', '', '', '', '0000-00-00 00:00:00', 0, 1),
(93, 'Knows the difference between physical, wireless and mobile networks. (AB)', 4, 4, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(94, 'Recognises and understands the function of the main internal parts of basic computer architecture. (AB)', 5, 4, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(95, 'Understands the concepts behind the fetch-execute cycle. (AB) (AL)', 5, 4, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(96, 'Knows that there is a range of operating systems and application software for the same hardware. (AB)', 5, 4, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(97, 'Understands the von Neumann architecture in relation to the fetchexecute cycle, including how data is stored in memory. (AB) (GE)', 6, 4, 1, 'TRUE', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(98, 'Understands the basic function and operation of location addressable memory.(AB)', 6, 4, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(99, 'Knows that processors have instruction sets and that these relate to low-level instructions carried out by a computer. (AB) (AL) (GE)', 7, 4, 1, 'TRUE', '', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(100, 'Has practical experience of a small (hypothetical) low level programming language. (AB) (AL) (DE) (GE)', 8, 4, 1, 'TRUE', 'TRUE', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(101, 'Understands and can explain Moores Law. (GE)', 8, 4, 3, '', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(102, 'Understands and can explain multitasking by computers. (AB) (AL) (DE)', 8, 4, 1, 'TRUE', 'TRUE', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(103, 'Obtains content from the world wide web using a web browser. (AL)', 1, 5, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(104, 'Understands the importance of communicating safely and respectfully online, and the need for keeping personal information private. (EV)', 1, 5, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(105, 'Knows what to do when concerned about content or being contacted. (AL)', 1, 5, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(106, 'Navigates the web and can carry out simple web searches to collect digital content. (AL) (EV)', 2, 5, 1, '', '', 'TRUE', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(107, 'Demonstrates use of computers safely and responsibly, knowing a range of ways to report unacceptable content and contact when online.', 2, 5, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(108, 'Understands the difference between the internet and internet service e.g. world wide web. (AB)', 3, 5, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(109, 'Shows an awareness of, and can use a range of internet services e.g. VOIP.', 3, 5, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(110, 'Recognises what is acceptable and unacceptable behaviour when using technologies and online services.', 3, 5, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(111, 'Understands how to effectively use search engines, and knows how search results are selected, including that search engines use web crawler programs. (AB) (GE) (EV)', 4, 5, 1, 'TRUE', '', '', 'TRUE', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(112, 'Selects, combines and uses internet services. (EV)', 4, 5, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(113, 'Demonstrates responsible use of technologies and online services, and knows a range of ways to report concerns.', 4, 5, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(114, 'Understands how search engines rank search results. (AL)', 5, 5, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(115, 'Understands how to construct static web pages using HTML and CSS. (AL) (AB)', 5, 5, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(116, 'Understands data transmission between digital computers over networks, including the internet i.e. IP addresses and packet switching. (AL) (AB)', 5, 5, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(117, 'Knows the names of hardware e.g. hubs, routers, switches, and the names of protocols e.g. SMTP, iMAP, POP, FTP, TCP/ IP, associated with networking computer systems. (AB)', 6, 5, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(118, 'Uses technologies and online services securely, and knows how to identify and\r\nreport inappropriate conduct. (AL)', 6, 5, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(119, 'Knows the purpose of the hardware and protocols associated with networking computer systems. (AB) (AL)', 7, 5, 1, 'TRUE', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(120, 'Understands the client-server model including how dynamic web pages use server-side scripting and that web servers process and store data entered by users. (AL) (AB) (DE)', 7, 5, 1, 'TRUE', 'TRUE', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(121, 'Recognises that persistence of data on the internet requires careful protection of online identity and privacy.', 7, 5, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(122, 'Understands the hardware associated with networking computer systems, including WANs and LANs, understands their purpose and how they work, including MAC addresses. (AB) (AL) (DE) (GE)', 8, 5, 1, 'TRUE', 'TRUE', 'TRUE', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(123, 'Uses software under the control of the teacher to create, store and edit digital content using appropriate file and folder names. (AB) (GE) (DE)', 1, 6, 1, 'TRUE', 'TRUE', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(124, 'Understands that people interact with computers.', 1, 6, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(125, 'Shares their use of technology in school.', 1, 6, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(126, 'Knows common uses of information technology beyond the classroom. (GE)', 1, 6, 1, '', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(127, 'Talks about their work and makes changes to improve it. (EV)', 1, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(128, 'Uses technology with increasing independence to purposefully organise digital content. (AB)', 2, 6, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(129, 'Shows an awareness for the quality of digital content collected. (EV)', 2, 6, 3, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(130, 'Uses a variety of software to manipulate and present digital content: data and information. (AL)', 2, 6, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(131, 'Shares their experiences of technology in school and beyond the classroom. (GE) (EV)', 2, 6, 1, '', '', '', 'TRUE', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(132, 'Talks about their work and makes improvements to solutions based on feedback received.(EV)', 2, 6, 3, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(133, 'Collects, organises and presents data and information in digital content. (AB)', 3, 6, 3, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(134, 'Creates digital content to achieve a given goal through combining software packages and internet services to communicate with a wider audience e.g. blogging. (AL)', 3, 6, 1, '', '', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(135, 'Makes appropriate improvements to solutions based on feedback received, and can comment on the success of the solution. (EV)', 3, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(136, 'Makes judgements about digital content when evaluating and repurposing it for a given audience. (EV) (GE)', 4, 6, 1, '', '', '', 'TRUE', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(137, 'Recognises the audience when designing and creating digital content. (EV)', 4, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(138, 'Understands the potential of information technology for collaboration when computers are networked. (GE)', 4, 6, 1, '', '', '', '', 'TRUE', '0000-00-00 00:00:00', 0, 1),
(139, 'Uses criteria to evaluate the quality of solutions, can identify improvements making some refinements to the solution, and future solutions. (EV)', 4, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(140, 'Evaluates the appropriateness of digital devices, internet services and application software to achieve given goals. (EV)', 5, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(141, 'Recognises ethical issues surrounding the application of information technology beyond school.', 5, 6, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(142, 'Designs criteria to critically evaluate the quality of solutions, uses the criteria to identify improvements and can make appropriate refinements to the solution. (EV)', 5, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(143, 'Justifies the choice of and independently combines and uses multiple digital devices, internet services and application software to achieve given goals. (EV', 6, 6, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(144, 'Evaluates the trustworthiness of digital content and considers the usability of visual design features when designing and creating digital artifacts for a known audience. (EV)', 6, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(145, 'Identifies and explains how the use of technology can impact on society.', 6, 6, 1, '', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(146, 'Designs criteria for users to evaluate the quality of solutions, uses the feedback from the users to identify improvements and can make appropriate refinements to the solution. (EV)', 6, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(147, 'Undertakes creative projects that collect, analyse, and evaluate data to meet the needs of a known user group. (AL) (DE) (EV)', 7, 6, 1, '', 'TRUE', 'TRUE', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(148, 'Effectively designs and creates digital artefacts for a wider or remote audience. (AL) (DE)', 7, 6, 1, '', 'TRUE', 'TRUE', '', '', '0000-00-00 00:00:00', 0, 1),
(149, 'Considers the properties of media when importing them into digital artefacts. (AB)', 7, 6, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(150, 'Documents user feedback, the improvements identified and the refinements made to the solution. (AB)', 7, 6, 1, 'TRUE', '', '', '', '', '0000-00-00 00:00:00', 0, 1),
(151, 'Explains and justifies how the use of technology impacts on society, from the perspective of social, economical, political, legal, ethical and moral issues. (EV)', 7, 6, 1, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1),
(152, 'Understands the ethical issues surrounding the application of information technology, and the existence of legal frameworks governing its use e.g. Data Protection Act, Computer Misuse Act, Copyright etc. (EV)', 8, 6, 3, '', '', '', 'TRUE', '', '0000-00-00 00:00:00', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sow_ks123_pathway`
--
ALTER TABLE `sow_ks123_pathway`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_sow_pathway_topic1_idx` (`topic_id`),
  ADD KEY `fk_sow_pathway_year_idx` (`year_id`),
  ADD KEY `fk_sow_pathway_subject_purpose_idx` (`subject_purpose_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sow_ks123_pathway`
--
ALTER TABLE `sow_ks123_pathway`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=153;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `sow_ks123_pathway`
--
ALTER TABLE `sow_ks123_pathway`
  ADD CONSTRAINT `fk_sow_pathway_subject_purpose` FOREIGN KEY (`subject_purpose_id`) REFERENCES `sow_subject_purpose` (`id`),
  ADD CONSTRAINT `fk_sow_pathway_topic` FOREIGN KEY (`topic_id`) REFERENCES `sow_topic` (`id`),
  ADD CONSTRAINT `fk_sow_pathway_year` FOREIGN KEY (`year_id`) REFERENCES `sow_year` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
