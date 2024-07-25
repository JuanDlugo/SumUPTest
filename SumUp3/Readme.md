# ELT Project

## Prerequisitos

1. Docker
2. Git

## Configuración del Proyecto

### 1. Clonar el repositorio


git clone <URL_DEL_REPOSITORIO>
cd SUMUP3

### 2. Construir la imagen de Docker

docker build -t elt-project .

### 3. Ejecutar el contenedor de Docker

docker run elt-project

### Resultados esperados
Después de ejecutar el contenedor, deberías ver los siguientes resultados en la consola:

[5 rows x 11 columns]
La UF de hoy (23.Jul.2024) es 37588.65
Se guardó en la BDD la UF hasta el día 09.Ago.2024
Top 10 Stores by Transacted Amount:
                        store_name  total_amount
0                    Nec Ante Ltd          9383
1             Sem Ut Cursus Corp.          8909
2                 Magnis Dis Inc.          7334
3            Blandit At Nisi Inc.          7326
4     Volutpat Nunc Sit Institute          6853
5               Mauris Aliquam PC          6739
6      Mauris Sit Amet Associates          6722
7  Ultrices Posuere Cubilia Corp.          6143
8       Pede Ultrices Corporation          5946
9  Sapien Nunc Pulvinar Institute          5926

Top 10 Products Sold:
            product_name  total_sold
0              sit amet           4
1            at, velit.           4
2       volutpat. Nulla           3
3     ultricies ornare,           3
4       posuere cubilia           3
5     natoque penatibus           3
6  fringilla, porttitor           3
7              eu neque           3
8          dolor. Fusce           3
9             dolor sit           3

Average Transacted Amount per Store Typology and Country:
    typology         country  avg_amount
0    Beauty         Austria  584.750000
1    Beauty          Brazil  435.000000
2    Beauty         Ireland  558.000000
3    Beauty           Italy  452.500000
4    Beauty     Netherlands  373.666667
..      ...             ...         ...
62  Service          Mexico  602.000000
63  Service       Singapore  443.333333
64  Service    South Africa  614.666667
65  Service         Ukraine  387.200000
66  Service  United Kingdom  563.375000

[67 rows x 3 columns]

Percentage of Transactions per Device Type:
    type  percentage
0     1   23.770492
1     2   19.057377
2     3   18.032787
3     4   21.721311
4     5   17.418033

Average Time for First 5 Transactions per Store in Days:
    store_id  avg_time_days
0         3     243.924142