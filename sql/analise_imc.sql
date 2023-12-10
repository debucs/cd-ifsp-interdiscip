select 
    d_bmi.bmi_desc
    ,count(1) as qtde
    ,avg(f.bmi) as media_imc
    ,sum(case when diabetes_012 = 1 then 1.0 else 0.0 end)/count(1)  pct_prediabetes
    ,sum(case when diabetes_012 = 2 then 1.0 else 0.0 end)/count(1)  pct_diabetes
    ,sum(case when diabetes_012 > 0 then 1.0 else 0.0 end)/count(1)  pct_pre_or_diabetes
from 
    diabetes F 
    LEFT JOIN d_bmi d_bmi  
        on f.bmi_id = d_bmi.bmi_id
group by
    d_bmi.bmi_desc
order by
    3
