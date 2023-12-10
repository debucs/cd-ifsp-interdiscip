CREATE EXTERNAL TABLE IF NOT EXISTS `diabetes`.`diabetes` (
  `diabetes_012` int,
  `highbp` int,
  `highchol` int,
  `cholcheck` int,
  `bmi` float,
  `bmi_id` int,
  `smoker` int,
  `stroke` int,
  `heartdiseaseorattack` int,
  `physactivity` int,
  `fruits` int,
  `veggies` int,
  `hvyalcoholconsump` int,
  `anyhealthcare` int,
  `nodocbccost` int,
  `genhlth` int,
  `menthlth` int,
  `physhlth` int,
  `diffwalk` int,
  `sex` int,
  `age` int,
  `education` int,
  `income` int
) COMMENT "Tabela principal - modelo de dados diabetes"
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://ifsp-cd-raw/diabetes/'
TBLPROPERTIES ('classification' = 'parquet');
