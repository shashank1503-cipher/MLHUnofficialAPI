## MLH UnofficialAPI
Added MLH scraper to scrape hackathons from MLH's website for 2022 & 2021 season. The code currently works on my PC only. To make it work on your PC too, go through the following instructions.

## API Endpoints
Stored the scraped data in MongoDB using pymongo and fetch data using FastAPI.

```
GET /
```
Return all data
```
GET /year/{year}
```
Returns all the hackathons from a specific season. Currently has only 2022 and 2021 season data

```
GET /year/{year}/month/{month}
```
Returns all the hackathons from a specific month of a season. Currently has only 2022 and 2021 season data.

```
GET /name/{name}
```

Returns all the hackathons having that name.
