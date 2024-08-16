select 
nome,
case 
when cast(ANO_INGRESSO_2022 as float) = 2022.0 and (ANOS_PM_2020 is not null or FASE_2021 is not null) then 'Aluno PM anteriormente'
when cast(ANO_INGRESSO_2022 as float) = 2021.0 and (ANOS_PM_2020 is not null) then 'Aluno PM anteriormente'
else 'Primeira vez como aluno PM'
end Participação,
case 
when ANOS_PM_2020 = 0 then 2020
when ANOS_PM_2020 = 1 then 2019
when ANOS_PM_2020 = 2 then 2018
when ANOS_PM_2020 = 3 then 2017
when ANOS_PM_2020 = 4 then 2016
when ANOS_PM_2020 is null and SINALIZADOR_INGRESSANTE_2021 is not null then 2021
when ANOS_PM_2020 is null and SINALIZADOR_INGRESSANTE_2021 is null and ANO_INGRESSO_2022 is not null then 2022
end AnoInicio, 
case 
when ANOS_PM_2020 is not null and SINALIZADOR_INGRESSANTE_2021 is null and ANO_INGRESSO_2022 is not null then 'Reingressou em 2022'
when ANOS_PM_2020 is not null and SINALIZADOR_INGRESSANTE_2021 is not null and ANO_INGRESSO_2022 is null then 'Terminou os estudos em 2021'
when ANOS_PM_2020 is not null and SINALIZADOR_INGRESSANTE_2021 is null and ANO_INGRESSO_2022 is null then 'Terminou os estudos em 2020'
else 'Não interrompeu os estudos'
end TerminoEstudo,
case 
when left(FASE_TURMA_2020,1) = left(FASE_2021,1) then 'Permaneceu na mesma fase'
when left(FASE_TURMA_2020,1) <> left(FASE_2021,1) then 'Passou de fase'
when left(FASE_TURMA_2020,1) is not null and FASE_2021 is null then 'Terminou os estudos'
end Fase2020_2021,
PEDRA_2020,
PONTO_VIRADA_2020,
case 
when left(FASE_2022,1) = left(FASE_2021,1) then 'Permaneceu na mesma fase'
when left(FASE_2022,1) <> left(FASE_2021,1) then 'Passou de fase'
when left(FASE_2021,1) is not null and left(FASE_2022,1) is null then 'Terminou os estudos'
end Fase2021_2022,
PEDRA_2021,
PONTO_VIRADA_2021,
PEDRA_2022,
PONTO_VIRADA_2022,
case
when ANOS_PM_2020 is not null 
and SINALIZADOR_INGRESSANTE_2021 is null 
and ANO_INGRESSO_2022 is not null then case when ANOS_PM_2020 = 0 then 2022-2020
when ANOS_PM_2020 = 1 then 2022-2019
when ANOS_PM_2020 = 2 then 2022-2018
when ANOS_PM_2020 = 3 then 2022-2017
when ANOS_PM_2020 = 4 then 2022-2016
end
when ANOS_PM_2020 is not null 
and SINALIZADOR_INGRESSANTE_2021 is not null 
and ANO_INGRESSO_2022 is not null then case when ANOS_PM_2020 = 0 then 2022-2020
when ANOS_PM_2020 = 1 then 2022-2019
when ANOS_PM_2020 = 2 then 2022-2018
when ANOS_PM_2020 = 3 then 2022-2017
when ANOS_PM_2020 = 4 then 2022-2016
end
when ANOS_PM_2020 is not null 
and SINALIZADOR_INGRESSANTE_2021 is not null 
and ANO_INGRESSO_2022 is null then case 
when ANOS_PM_2020 = 0 then 2021-2020
when ANOS_PM_2020 = 1 then 2021-2019
when ANOS_PM_2020 = 2 then 2021-2018
when ANOS_PM_2020 = 3 then 2021-2017
when ANOS_PM_2020 = 4 then 2021-2016
end
when ANOS_PM_2020 is not null and SINALIZADOR_INGRESSANTE_2021 is null and ANO_INGRESSO_2022 is null then ANOS_PM_2020
when ANOS_PM_2020 is null and SINALIZADOR_INGRESSANTE_2021 is not null and ANO_INGRESSO_2022 is null then 0
when ANOS_PM_2020 is null and SINALIZADOR_INGRESSANTE_2021 is null and ANO_INGRESSO_2022 is not null then 0
when ANOS_PM_2020 is null and SINALIZADOR_INGRESSANTE_2021 is not null and ANO_INGRESSO_2022 is not null then 1
end AnosPM,
IPV_2020,
IPV_2021,
IPV_2022,
INDE_2020,
INDE_2021,
INDE_2022,
IEG_2020,
IEG_2021,
IEG_2022,
IDA_2020,
IDA_2021,
IDA_2022,
IAA_2020,
IAA_2021,
IAA_2022,
IPS_2020,
IPS_2021,
IPP_2022,
IAN_2020,
IAN_2021,
IAN_2022,
left(FASE_TURMA_2020,1) FASE_2020,
left(FASE_2021,1) FASE_2021,
left(FASE_2022,1) FASE_2022,
IPS_2022,
IPP_2020,
IPP_2021
from dados_finais