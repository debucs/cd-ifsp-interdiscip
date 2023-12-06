CREATE OR REPLACE VIEW D_HighBP as 
select 0 as HighBP, 'Sem pressao alta' as HighBP_desc
union select 1, 'Com pressao alta'
