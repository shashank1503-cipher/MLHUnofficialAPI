from fastapi import FastAPI
from AddToDB import fetchFromDb
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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