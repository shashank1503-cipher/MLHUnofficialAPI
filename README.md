## MLH UnofficialAPI
Added MLH scraper to scrape hackathons from MLH's website for 2022 & 2021 season. The code currently works on my PC only. To make it work on your PC too, go through the following instructions.

## API
Stored the scraped data in MongoDB using pymongo and fetch data using FastAPI. Will deploy soon

## Instructions
- Install Dependencies using following command 

  ```bash
  pip install -r requirements.txt
  ```
- Install Chrome Web Driver for your chromium version from [here](https://sites.google.com/chromium.org/driver/)
- Extract the driver to C:/bin
- Add C:/bin to Path
- Good to go now

## Work Under Progress
Soon I will deploy this scraper as an API so that there is no need for above instructions.
