# Oluenreittauspalvelu

Käyttäjänä haluan arvostella oluen.

Käyttäjänä haluan tarkastella omia arvostelujani.

```
SELECT rating.id AS rating_id, rating.date AS rating_date, rating.date_modified AS rating_date_modified, rating.rating AS rating_rating, rating.comment AS rating_comment, rating.account_id AS rating_account_id, rating.beer_id AS rating_beer_id 
FROM rating 
WHERE rating.account_id = ?
```

Käyttäjänä haluan muokata vanhoja arvostelujani tai poistaa niitä.

Käyttäjänä haluan listata arvosteluja, jotta näen, mitä muut juovat.

- Arvostelun haku
```
SELECT rating.id AS rating_id, rating.date AS rating_date, rating.date_modified AS rating_date_modified, rating.rating AS rating_rating, rating.comment AS rating_comment, rating.account_id AS rating_account_id, rating.beer_id AS rating_beer_id 
FROM rating
```
- Arvosteluun liittyvän oluen haku
```
SELECT beer.id AS beer_id, beer.name AS beer_name 
FROM beer 
WHERE beer.id = ?
```

Käyttäjänä haluan listata oluita, jotta löydän mieleiseni.

Käyttäjänä haluan nähdä oluen saamien arvostelujen keskiarvon.

Käyttäjänä haluan nähdä millä maulla muut käyttäjät ovat kuvailleet kutakin olutta, jotta voin valita itselleni makuuni sopivan oluen (esim. banaanisen oluen).

- Kolmen ylläolevan storyn yhteenvetokysely
```
SELECT Beer.name, AVG(Rating.rating), flavormax.name 
FROM Flavor, Rating_flavor, Rating, Beer, 
(SELECT MAX(flavorcounts.num) AS maxflavor, flavorcounts.name AS name 
FROM 
(SELECT Flavor.name AS name, COUNT(Flavor.name) AS num 
FROM Flavor, Rating_flavor, Rating, Beer 
WHERE Flavor.id = Rating_flavor.flavor_id 
AND Rating.id = Rating_flavor.rating_id 
AND Beer.id = Rating.beer_id) flavorcounts 
GROUP BY flavorcounts.name) flavormax 
WHERE Flavor.id = Rating_flavor.flavor_id 
AND Rating.id = Rating_flavor.rating_id 
AND Beer.id = Rating.beer_id 
GROUP BY Beer.id 
ORDER BY AVG(Rating.rating) DESC
```

Ylläpitäjänä haluan lisätä palveluun uusia oluita ja makuja, jotta palvelu pysyy tuoreena.

Ylläpitäjänä haluan poistaa tai muokata asiattomia tai muuten epäsopivia arvosteluja.

