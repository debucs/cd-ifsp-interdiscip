create view d_bmi as
select -1 as bmi_id, 'N/A' as bmi_desc
    union select 1, 'Abaixo do peso'
    union select 2, 'Peso normal'
    union select 3, 'Sobrepeso'
    union select 4, 'Obesidade grau I'
    union select 5, 'Obesidade grau II'
    union select 6, 'Obesidade grau III'
from diabetes
