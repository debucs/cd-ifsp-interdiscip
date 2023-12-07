## Estudo de indicadores de saúde na predição de Diabetes e Pré-diabetes

### cd-ifsp-interdiscip
Trabalho desenvolvido e apresentado para o Trabalho Interdisciplinar do curso de Espec. Ciência de Dados no IFSP-Campinas - 2o Semestre 2023.

Disciplinas "Tecnologias de Big Data" e "Aprendizado de Máquina"

### Integrantes do Grupo: 
[Geovana Lopes Batista CP302170X](https://github.com//)<br>
[Isabela Moreira Silva CP3021734](https://github.com//)<br>
[Mateus Rodrigues Braga Nascimento CP3024261](https://github.com/debucs/)<br>


---

## Doenças Crônicas: Diabetes

Doenças crônicas são aquelas que não podem ser resolvidas em um curto prazo, de até três meses, e podem perdurar a vida toda. Elas também não são consideradas emergências médicas por não causarem risco à vida em um curto período de tempo. Porém, segundo a OMS, estudos feitos entre 2000 e 2019 mostraram que doenças crônicas não transmissíveis representam 7 das 10 maiores causas de morte do mundo.

Dentre essas doenças está a diabetes, uma doença crônica, metabólica, cuja característica é o aumento do nível de glicose no sangue. A diabetes é dividida em dois tipos: a tipo I, menos comum, que não pode ser evitada, causada pela diminuição ou ausência completa da produção de insulina pelo pâncreas e a tipo II, mais comum, geralmente acontece quando o corpo adquire resistência a insulina ou o pâncreas passa a não produzir insulina suficiente.

Também segundo a OMS, em 2019 a diabetes foi a sexta maior causa de mortes nas Américas, ocasionando mais de 284 mil mortes. Além disso, no mundo todo foi observado um aumento de 70% das mortes por diabetes entre 2000 e 2019.

Os principais fatores relacionados a alta incidência de diabetes é o sobrepeso e obesidade, alimentação inadequada (geralmente rica em açúcares) e falta de atividade. O diagnóstico precoce e tratamento evitam que pacientes crônicos desenvolvam outros problemas de saúde relativos a diabetes como: cegueira, amputação de membros inferiores, doenças renais, cardíacas e câncer. Além disso, quando descoberta precocemente, ainda no estágio de pré-diabetes, ela pode ser revertida.

Doenças crônicas relacionadas à alimentação inadequada foram responsáveis pelo gasto de, aproximadamente, 3,45 bilhões de reais no SUS em 2018, sendo 30% desse total usado apenas para o tratamento de pessoas com diabetes. Portanto, o investimento em ferramentas que auxiliem o diagnóstico precoce dessas doenças promove uma melhor qualidade de vida para os pacientes e gera economia para o sistema de saúde.


---
### Dataset inicial

https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

---
### Variáveis do dataset
Diabetes: 0 (sem diabetes), 1 (pré-diabetes) e 2 (diabetes)

HighBP: pressão alta (0 - não, 1 - sim)

HighChol: colesterol alto (0 - não, 1 - sim)

CholCheck: exames nos últimos 5 anos (0 - não, 1 - sim)

BMI: Índice de Massa Corpórea - IMC:
 - abaixo de 18,49: abaixo do peso
 - entre 18,5 e 24,99: peso normal
 - entre 25 e 29,99: sobrepeso
 - entre 30 e 34,99: obesidade grau I
 - entre 35 e 39,99: obesidade grau II
 - acima de 40: obesidade grau III

Smoker: fumante (0 - não, 1 - sim)

Stroke: Acidente Vascular Cerebral - AVC (0 - nunca teve, 1 - já teve)

HeartDiseaseorAttack: doença coronariana ou infarto do miocárdio (0 - não, 1 - sim)

PhysActivity: atividade física nos últimos 30 dias (0 - não, 1 - sim)

Fruits: consome fruta uma ou mais vezes por dia (0 - não, 1 - sim)

Veggies: consome vegetais uma ou mais vezes por dia (0 - não, 1 - sim)

HvyAlcoholConsump: alto consumo de álcool - homens adultos mais de 14 doses por semana, mulheres adultas mais de 7 doses por semana (0 - não, 1 - sim)

AnyHealthcare: algum tipo de plano de saúde (0 - não, 1 - sim)

NoDocbcCost: algum momento nos últimos 12 meses de necessidade de ir ao médico, porém não conseguiu por falta de dinheiro (0 - não, 1 - sim)

GenHlth: saúde em geral (1 = excelente, 2 = muito boa, 3 = boa, 4 = razoável, 5 = ruim)

MentHlth: por quantos dias, nos últimos 30 dias, teve algum problema de saúde mental (estresse, depressão e problemas com emoções)

PhysHlth: por quantos dias, nos últimos 30 dias, ficou doente ou teve algum ferimento

DiffWalk: dificuldade para caminhar ou subir escadas (0 - não, 1 - sim)

Sex: sexo (0 - feminino, 1 - masculino)

Age: idade (1 = 18-24 anos, 2 = 25-29 anos, 3 = 30-34 anos, 4 = 35-39 anos, 5 = 40-44anos, 6 = 45-49 anos, 7 = 50-54 anos, 8 = 55-59 anos, 9 = 60-64 anos, 10 = 65-69 anos, 11 = 70-74 anos, 12 = 75-79 anos, 13 = 80+ anos

Education: grau de escolaridade

Income: renda

---
### Arquitetura de referencia

![ Arquitetura de referencia do projeto.](/arquitetura/aws_arch2.png)

Utilizamos um bucket S3 para receber o arquivo original do dataset. Usando Cloud9 Terminal, descompactar e copiar para um segundo bucket o csv de interesse.
Através do Athena, criamos um database no Glue que lê o arquivo csv como uma tabela. O database foi enriquecido com views que davam descrição aos temas.
Através do Sagemaker, o dado bruto foi utilizado dentro de um notebook jupyter para treinamento e teste dos modelos estudado e apresentados.



---

### Algoritmos de Aprendizado de Máquina Estudados

#### KNN
#### Regressão Logística
#### Árvore de Decisão

---

## Conclusões

Apesar de todos os modelos terem alcançado uma acurácia e precisão muito boas, quando olhamos a matriz de confusão percebemos que ele apresenta um viés bastante alto para uma determinada categoria (no caso, não ter diabetes). Isso aconteceu porque os dados também apresentam um número muito maior de pessoas que não tem diabetes.

No caso do nosso estudo é preferível que o modelo cometesse o erro do tipo I (falso positivo), pois isso leva as pessoas a procurarem ajuda médica. No caso do erro tipo II (falso negativo) as pessoas poderiam deixar de buscar ajuda médica pois acreditariam que está tudo certo com a saúde, quando na verdade não está e eles deveriam procurar ajuda.
Considerando esses fatores, a Árvore de Decisão foi o modelo que chegou mais próximo da necessidade desse caso. Porém, ele ainda precisa ser aperfeiçoado para que haja uma diminuição do erro do tipo II.

Futuramente pretendemos tentar novos modelos (na literatura está descrito que redes neurais dão melhores resultados neste tipo de situação), além de tentar equilibrar melhor a distribuição dos dados, para que o modelo não fique enviesado para um resultado específico. Depois de aperfeiçoado o modelo, pretendemos expandi-lo para outras doenças crônicas. 
