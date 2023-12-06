CREATE EXTERNAL TABLE IF NOT EXISTS `diabetes_data`.`diabetes` (
  `Diabetes_012` int,
  `HighBP` int,
  `HighChol` int,
  `CholCheck` int,
  `BMI` int,
  `Smoker` int,
  `Stroke` int,
  `HeartDiseaseorAttack` int,
  `PhysActivity` int,
  `Fruits` int,
  `Veggies` int,
  `HvyAlcoholConsump` int,
  `AnyHealthcare` int,
  `NoDocbcCost` int,
  `GenHlth` int,
  `MentHlth` int,
  `PhysHlth` int,
  `DiffWalk` int,
  `Sex` int,
  `Age` int,
  `Education` int,
  `Income` int
) COMMENT "dataset com indicadores de saude para deteccao de diabetes"
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ('field.delim' = ',')
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://ifsp-cd-interdisciplinar/table_diabetes/'
TBLPROPERTIES ('classification' = 'csv');
