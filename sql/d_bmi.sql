create view d_bmi as
select distinct bmi
    ,case 
        when bmi < 18.5 then 'Abaixo do peso'
        when bmi < 25 then 'Peso normal'
        when bmi < 30 then 'Sobrepeso'
        when bmi < 35 then 'Obesidade grau I'
        when bmi < 40 then 'Obesidade grau II'
        else 'Obesidade grau III' end as IMC_desc
from diabetes
order by 1
