/****** Script for SelectTopNRows command from SSMS  ******/
      SELECT 'DimCustomer', Count(*) FROM [northwind][dbo].[DimCustomer]
UNION SELECT 'DimDate', Count(*) FROM [northwind][dbo].[DimDate]
UNION SELECT 'DimEmployee', Count(*) FROM [northwind][dbo].[DimEmployee]
UNION SELECT 'DimProduct', Count(*) FROM [northwind][dbo].[DimProduct]
UNION SELECT 'DimSupplier', Count(*) FROM [northwind][dbo].[DimSupplier]
UNION SELECT 'FactInventoryDailySnapshot', Count(*) FROM [northwind][dbo].[FactInventoryDailySnapshot]
UNION SELECT 'FactSales', Count(*) FROM [northwind][dbo].[FactSales]

