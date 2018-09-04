create database if not exists `CLIENTS_DB`;

USE `CLIENTS_DB`;

create table clients (
	cl_key INT PRIMARY KEY,
	cl_original_id  INT,
	cl_first_name VARCHAR(50),
	cl_last_name VARCHAR(50),
	cl_gender VARCHAR(10),
	cl_email VARCHAR(50),
	cl_state VARCHAR(50)
);