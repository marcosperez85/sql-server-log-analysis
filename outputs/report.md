# Access Log Analysis

## Exploración inicial
**Objetivo**
Analizar cantidad de registros, período cubierto y cantidad de usuarios únicos.

| FECHA INICIAL       | FECHA FINAL         | DURACION          |   CANTIDAD FILAS |   CANT IP UNICAS |   CANT ID UNICOS |
|:--------------------|:--------------------|:------------------|-----------------:|-----------------:|-----------------:|
| 2024-01-27 05:49:47 | 2026-07-13 04:41:18 | 897 days 22:51:31 |              100 |              100 |               63 |

---

## Análisis de los endpoints más usados
**Objetivo**
Indicar cuánto es el porcentaje de uso de cada endpoint

| ENDPOINT         |   CANT PETICIONES |   PORCENTAJE |
|:-----------------|------------------:|-------------:|
| /api/cart        |                16 |           16 |
| /api/search      |                12 |           12 |
| /health          |                12 |           12 |
| /api/auth/logout |                10 |           10 |
| /api/products    |                 9 |            9 |
| /metrics         |                 9 |            9 |
| /api/payments    |                 8 |            8 |
| /api/users       |                 8 |            8 |
| /api/checkout    |                 7 |            7 |
| /api/auth/login  |                 5 |            5 |
| /api/orders      |                 4 |            4 |

---

## Análisis de errores por cada endpoint
**Objetivo**
Indicar cuántos usuarios se ven afectados con requests fallidos y la ocurrencia de cada uno

| ENDPOINT         |   ERRORES TOTALES |   USUARIOS AFECTADOS |   RESPONSE TIME PROMEDIO |   STATUS_CODE |
|:-----------------|------------------:|---------------------:|-------------------------:|--------------:|
| /api/cart        |                 3 |                    2 |                 13177.3  |           503 |
| /api/search      |                 3 |                    2 |                   142.67 |           404 |
| /api/payments    |                 2 |                    2 |                 15323    |           502 |
| /api/products    |                 2 |                    2 |                 23122.5  |           500 |
| /api/checkout    |                 2 |                    1 |                   327.5  |           401 |
| /api/products    |                 2 |                    1 |                 23469    |           503 |
| /health          |                 2 |                    1 |                  2517.5  |           503 |
| /metrics         |                 2 |                    2 |                   159.5  |           403 |
| /api/cart        |                 2 |                    2 |                 12452    |           502 |
| /api/checkout    |                 2 |                    2 |                 15053.5  |           500 |
| /api/products    |                 2 |                    1 |                   368.5  |           404 |
| /api/search      |                 2 |                    1 |                   302.5  |           401 |
| /metrics         |                 2 |                    0 |                   322.5  |           401 |
| /health          |                 2 |                    0 |                   105    |           403 |
| /api/search      |                 1 |                    0 |                    86    |           403 |
| /api/cart        |                 1 |                    1 |                    33    |           404 |
| /api/orders      |                 1 |                    1 |                    36    |           401 |
| /health          |                 1 |                    1 |                  2360    |           502 |
| /api/users       |                 1 |                    0 |                 21292    |           500 |
| /api/orders      |                 1 |                    1 |                   180    |           404 |
| /api/users       |                 1 |                    0 |                   456    |           401 |
| /api/auth/logout |                 1 |                    1 |                 12692    |           502 |
| /api/checkout    |                 1 |                    1 |                 13663    |           503 |
| /api/checkout    |                 1 |                    1 |                  1690    |           502 |
| /api/auth/logout |                 1 |                    0 |                  8135    |           503 |
| /api/payments    |                 1 |                    0 |                  8884    |           500 |
| /health          |                 1 |                    1 |                 17791    |           500 |
| /api/users       |                 1 |                    1 |                   223    |           400 |
| /api/payments    |                 1 |                    1 |                   477    |           401 |
| /api/auth/logout |                 1 |                    1 |                   102    |           403 |
| /health          |                 1 |                    0 |                   275    |           400 |
| /api/auth/login  |                 1 |                    0 |                 11654    |           503 |
| /api/auth/logout |                 1 |                    1 |                   299    |           404 |

---

##  Performance de los requests exitosos a cada endpoint
**Objetivo**
Indicar cuánto tarda el 90 y 95% de los requests exitosos

| ENDPOINT         |   CANT REQUESTS |   p90 RANK |   p95 RANK |   TIEMPO MAXIMO |
|:-----------------|----------------:|-----------:|-----------:|----------------:|
| /api/auth/logout |               6 |      482   |     489    |             496 |
| /api/payments    |               4 |      481.1 |     487.55 |             494 |
| /api/products    |               3 |      460.6 |     474.3  |             488 |
| /api/auth/login  |               4 |      405.5 |     410.75 |             416 |
| /api/orders      |               2 |      395.7 |     400.85 |             406 |
| /api/cart        |              10 |      347.4 |     367.2  |             387 |
| /api/users       |               5 |      306.6 |     312.8  |             319 |
| /api/search      |               6 |      261   |     269    |             277 |
| /api/checkout    |               1 |      268   |     268    |             268 |
| /health          |               5 |      262.4 |     263.2  |             264 |
| /metrics         |               5 |      207.8 |     222.4  |             237 |

---

## Picos de tráfico según la hora
**Objetivo**
Identificar picos de tráfico según la hora para planificar capacidad y poder escalar a futuro.
Para esto busco la hora a la cual se da la mayor cantidad de requests y el mayor tiempo de respuesta para cada endpoint

|   HORA | ENDPOINT         |   CANT REQUESTS |   RESPONSE TIME AVG |
|-------:|:-----------------|----------------:|--------------------:|
|      7 | /api/search      |               3 |               203   |
|      9 | /api/search      |               2 |                86.5 |
|     15 | /api/auth/logout |               2 |               182.5 |
|     12 | /metrics         |               2 |                95   |
|      5 | /health          |               2 |               138.5 |
|     12 | /api/auth/logout |               2 |               482   |
|      0 | /api/products    |               2 |              9839.5 |
|     14 | /api/auth/logout |               2 |             10413.5 |
|      6 | /api/users       |               2 |               149   |
|      3 | /api/payments    |               2 |               485.5 |
|     23 | /api/cart        |               2 |              8283   |
|     17 | /api/cart        |               2 |               218   |
|     11 | /health          |               2 |              1312   |
|     16 | /api/cart        |               2 |              7806.5 |
|     18 | /api/cart        |               2 |               129.5 |
|     12 | /health          |               2 |               708.5 |
|     15 | /health          |               2 |              1991.5 |
|     18 | /api/users       |               1 |               319   |
|     23 | /health          |               1 |                67   |
|     18 | /api/orders      |               1 |               180   |
|     21 | /api/search      |               1 |                86   |
|      8 | /metrics         |               1 |               162   |
|     12 | /api/payments    |               1 |             10777   |
|     21 | /api/auth/logout |               1 |               299   |
|     17 | /metrics         |               1 |               293   |
|      6 | /api/auth/login  |               1 |               183   |
|     14 | /api/cart        |               1 |                77   |
|     17 | /api/products    |               1 |               334   |
|      5 | /api/cart        |               1 |             17433   |
|     23 | /api/search      |               1 |               405   |
|      0 | /api/cart        |               1 |                73   |
|      7 | /api/payments    |               1 |              8884   |
|     17 | /api/checkout    |               1 |               289   |
|      4 | /api/cart        |               1 |                33   |
|     21 | /api/cart        |               1 |                30   |
|      8 | /api/checkout    |               1 |              1690   |
|      5 | /api/search      |               1 |               277   |
|      1 | /api/cart        |               1 |              8083   |
|     22 | /api/search      |               1 |                87   |
|     18 | /api/checkout    |               1 |             28253   |
|     17 | /api/search      |               1 |               322   |
|     16 | /metrics         |               1 |               237   |
|     13 | /api/products    |               1 |             26948   |
|     18 | /api/auth/login  |               1 |               416   |
|      4 | /api/products    |               1 |             26781   |
|      4 | /metrics         |               1 |                 9   |
|      0 | /api/orders      |               1 |               406   |
|     19 | /api/search      |               1 |               200   |
|      7 | /api/cart        |               1 |               132   |
|      9 | /metrics         |               1 |                76   |
|     14 | /api/payments    |               1 |               108   |
|      3 | /api/auth/logout |               1 |               317   |
|      5 | /api/products    |               1 |             20157   |
|      2 | /api/products    |               1 |               488   |
|     16 | /api/products    |               1 |               355   |
|      9 | /api/users       |               1 |             21292   |
|      0 | /health          |               1 |             17791   |
|      5 | /api/auth/login  |               1 |             11654   |
|     21 | /api/checkout    |               1 |              1854   |
|     14 | /api/checkout    |               1 |               366   |
|      2 | /api/users       |               1 |               223   |
|      5 | /api/users       |               1 |               288   |
|     22 | /api/auth/login  |               1 |               125   |
|     18 | /api/auth/logout |               1 |               292   |
|     17 | /api/orders      |               1 |               303   |
|     14 | /api/orders      |               1 |                36   |
|     19 | /api/auth/login  |               1 |               381   |
|      3 | /metrics         |               1 |               164   |
|      0 | /api/auth/logout |               1 |                55   |
|      8 | /api/payments    |               1 |             19869   |
|     19 | /health          |               1 |               275   |
|      3 | /api/products    |               1 |               351   |
|     20 | /api/users       |               1 |               456   |
|     19 | /api/payments    |               1 |               451   |
|     11 | /api/cart        |               1 |              7471   |
|      6 | /metrics         |               1 |               352   |
|     12 | /api/checkout    |               1 |               268   |
|      8 | /api/users       |               1 |                64   |
|     16 | /api/search      |               1 |                19   |
|      2 | /api/checkout    |               1 |             13663   |
|     21 | /health          |               1 |               105   |
|      0 | /api/payments    |               1 |               428   |

---

## Ranking de requests más lentos
**Objetivo**
Identificar los tres requests exitosos con mayor tiempo de respuesta para cada endpoint.

| TIMESTAMP           | ENDPOINT         |   RESPONSE TIME | USER_ID   |   RN |
|:--------------------|:-----------------|----------------:|:----------|-----:|
| 2024-09-17 06:02:07 | /api/auth/login  |             183 | 1784      |    3 |
| 2024-12-12 19:04:00 | /api/auth/login  |             381 | <NA>      |    2 |
| 2026-01-09 18:30:47 | /api/auth/login  |             416 | 8954      |    1 |
| 2025-12-04 03:53:16 | /api/auth/logout |             317 | <NA>      |    3 |
| 2026-06-22 12:34:33 | /api/auth/logout |             468 | 8383      |    2 |
| 2024-08-25 12:47:51 | /api/auth/logout |             496 | 6420      |    1 |
| 2025-11-17 17:02:28 | /api/cart        |             250 | <NA>      |    3 |
| 2025-12-01 23:29:55 | /api/cart        |             343 | 1506      |    2 |
| 2026-01-29 16:16:52 | /api/cart        |             387 | 9214      |    1 |
| 2024-08-26 12:08:23 | /api/checkout    |             268 | <NA>      |    1 |
| 2024-11-15 17:45:08 | /api/orders      |             303 | 9981      |    2 |
| 2025-02-23 00:05:50 | /api/orders      |             406 | 6676      |    1 |
| 2025-01-09 00:43:40 | /api/payments    |             428 | 1062      |    3 |
| 2025-08-22 19:27:29 | /api/payments    |             451 | <NA>      |    2 |
| 2025-03-05 03:38:57 | /api/payments    |             494 | 1098      |    1 |
| 2024-06-25 17:37:04 | /api/products    |             334 | 432       |    3 |
| 2025-08-11 03:05:14 | /api/products    |             351 | <NA>      |    2 |
| 2025-01-12 02:14:42 | /api/products    |             488 | <NA>      |    1 |
| 2024-04-10 07:26:14 | /api/search      |             207 | 2683      |    3 |
| 2025-11-08 07:34:16 | /api/search      |             245 | 6216      |    2 |
| 2024-06-19 05:03:57 | /api/search      |             277 | <NA>      |    1 |
| 2025-01-11 02:54:58 | /api/users       |             223 | 2765      |    3 |
| 2024-12-02 05:14:46 | /api/users       |             288 | 8686      |    2 |
| 2025-05-16 18:11:31 | /api/users       |             319 | 6276      |    1 |
| 2024-01-27 05:49:47 | /health          |             177 | <NA>      |    3 |
| 2025-01-14 12:06:25 | /health          |             260 | <NA>      |    2 |
| 2026-01-07 11:54:57 | /health          |             264 | <NA>      |    1 |
| 2025-02-25 09:15:39 | /metrics         |              76 | <NA>      |    3 |
| 2026-01-05 03:00:43 | /metrics         |             164 | 4790      |    2 |
| 2025-03-23 16:48:27 | /metrics         |             237 | 9850      |    1 |

---

## Comparación con el período anterior
**Objetivo**
Comparación del response time de cada endpoint con la fecha anterior registrada

| FECHA               | ENDPOINT         |   RESPONSE TIME ACTUAL | PERIODO ANTERIOR   | DIFFERENCE   |
|:--------------------|:-----------------|-----------------------:|:-------------------|:-------------|
| 2024-01-27 00:00:00 | /health          |                    177 | 105                | 72           |
| 2024-02-25 00:00:00 | /api/cart        |                    132 | 30                 | 102          |
| 2024-04-10 00:00:00 | /api/search      |                    207 | 405                | -198         |
| 2024-05-26 00:00:00 | /api/payments    |                    108 | 428                | -320         |
| 2024-06-09 00:00:00 | /api/cart        |                     30 | 16223              | -16193       |
| 2024-06-19 00:00:00 | /api/search      |                    277 | 142                | 135          |
| 2024-06-25 00:00:00 | /api/products    |                    334 | 488                | -154         |
| 2024-07-18 00:00:00 | /metrics         |                      9 | 162                | -153         |
| 2024-08-25 00:00:00 | /api/auth/logout |                    496 | 8135               | -7639        |
| 2024-08-26 00:00:00 | /api/checkout    |                    268 | 289                | -21          |
| 2024-09-17 00:00:00 | /api/auth/login  |                    183 | 381                | -198         |
| 2024-11-01 00:00:00 | /api/users       |                     64 | 288                | -224         |
| 2024-11-13 00:00:00 | /api/search      |                    142 | 157                | -15          |
| 2024-11-15 00:00:00 | /api/orders      |                    303 | 406                | -103         |
| 2024-11-28 00:00:00 | /api/cart        |                    186 | 209                | -23          |
| 2024-12-02 00:00:00 | /api/users       |                    288 | 21292              | -21004       |
| 2024-12-12 00:00:00 | /api/auth/login  |                    381 | 11654              | -11273       |
| 2025-01-09 00:00:00 | /api/payments    |                    428 | 494                | -66          |
| 2025-01-11 00:00:00 | /api/users       |                    223 | 319                | -96          |
| 2025-01-11 00:00:00 | /api/auth/logout |                    292 | 55                 | 237          |
| 2025-01-12 00:00:00 | /api/products    |                    488 | 19297              | -18809       |
| 2025-01-14 00:00:00 | /health          |                    260 | 275                | -15          |
| 2025-02-05 00:00:00 | /api/cart        |                    209 | 15226              | -15017       |
| 2025-02-23 00:00:00 | /api/orders      |                    406 | 36                 | 370          |
| 2025-02-25 00:00:00 | /metrics         |                     76 | 237                | -161         |
| 2025-03-05 00:00:00 | /api/payments    |                    494 | 451                | 43           |
| 2025-03-20 00:00:00 | /api/search      |                    157 | 87                 | 70           |
| 2025-03-23 00:00:00 | /metrics         |                    237 | 157                | 80           |
| 2025-03-26 00:00:00 | /api/auth/logout |                     55 | 102                | -47          |
| 2025-04-14 00:00:00 | /api/cart        |                     73 | 50                 | 23           |
| 2025-05-16 00:00:00 | /api/users       |                    319 | 456                | -137         |
| 2025-06-26 00:00:00 | /api/search      |                     31 | 200                | -169         |
| 2025-08-11 00:00:00 | /api/products    |                    351 | 26781              | -26430       |
| 2025-08-22 00:00:00 | /api/payments    |                    451 | 8884               | -8433        |
| 2025-08-31 00:00:00 | /api/cart        |                     50 | 250                | -200         |
| 2025-11-07 00:00:00 | /metrics         |                     33 | 164                | -131         |
| 2025-11-08 00:00:00 | /api/search      |                    245 | 86                 | 159          |
| 2025-11-17 00:00:00 | /api/cart        |                    250 | 343                | -93          |
| 2025-12-01 00:00:00 | /api/cart        |                    343 | 387                | -44          |
| 2025-12-04 00:00:00 | /api/auth/logout |                    317 | 12692              | -12375       |
| 2026-01-05 00:00:00 | /metrics         |                    164 | 352                | -188         |
| 2026-01-07 00:00:00 | /health          |                    264 | 67                 | 197          |
| 2026-01-09 00:00:00 | /api/auth/login  |                    416 | 125                | 291          |
| 2026-01-28 00:00:00 | /health          |                     67 | 100                | -33          |
| 2026-01-29 00:00:00 | /api/cart        |                    387 | 77                 | 310          |
| 2026-01-31 00:00:00 | /api/users       |                     75 | 223                | -148         |
| 2026-02-16 00:00:00 | /api/cart        |                     77 | 7471               | -7394        |
| 2026-03-06 00:00:00 | /api/auth/login  |                    125 | <NA>               | <NA>         |
| 2026-03-26 00:00:00 | /health          |                    100 | <NA>               | <NA>         |
| 2026-05-10 00:00:00 | /api/auth/logout |                    263 | 468                | -205         |
| 2026-06-22 00:00:00 | /api/auth/logout |                    468 | <NA>               | <NA>         |

---

# Recomendaciones


1. Hallazgo: /api/search presenta un p95 de 2.5 s durante las horas pico (14:00–16:00), concentrando además el mayor volumen de solicitudes.
Impacto potencial: Un aumento en la latencia sobre este endpoint puede degradar la experiencia de la mayoría de los usuarios y aumentar el consumo de recursos del backend.
Recomendación: Evaluar la incorporación de un mecanismo de caché para respuestas frecuentes y revisar el plan de ejecución de las consultas a la base de datos para reducir el tiempo de respuesta en las horas de mayor carga.

2. Prueba de recomendacion 2

3. Prueba de recomendacion 3
