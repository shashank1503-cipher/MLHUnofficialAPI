from fastapi import FastAPI
from AddToDB import fetchFromDb
app = FastAPI()
@app.get("/")
async def root():
    return fetchFromDb({})
@app.get("/year/")
async def read_year():
    year = 2022
    return fetchFromDb({'year':str(year)})
@app.get("/year/{year}")
async def read_year(year:int = 2022):
    return fetchFromDb({'year':str(year)})
@app.get("/year/{year}/month/{month}")
async def read_month(year:int,month:str):
    return fetchFromDb({'year':str(year),'eventDate':{'$regex':'^'+month.capitalize()}})
@app.get("/name/{name}")
async def read_name(name:str):
    return fetchFromDb({'eventName':name})