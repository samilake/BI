/****** Script for SelectTopNRows command from SSMS  ******/
      SELECT 'Customers', Count(*) FROM [Session_stg].[dbo].[Customers]
UNION SELECT 'Employees', Count(*) FROM [Session_stg].[dbo].[Employees]
UNION SELECT 'inventory', Count(*) FROM [Session_stg].[dbo].[inventory]
UNION SELECT 'Products', Count(*) FROM [Session_stg].[dbo].[Products]
UNION SELECT 'Sales', Count(*) FROM [Session_stg].[dbo].[Sales]
UNION SELECT 'suppliers', Count(*) FROM [Session_stg].[dbo].[suppliers]
