from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from statistics import mean
from collections import defaultdict

app = FastAPI()

class DataItem(BaseModel):
    id: int
    value: float
    timestamp: str

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/data")
async def receive_data(data: List[DataItem]):
    return {"message": "Data received successfully", "data_count": len(data)}

@app.post("/average")
async def calculate_average(data: List[DataItem]):
    avg_value = mean([item.value for item in data])
    return {"average": avg_value}

@app.post("/daily-average")
async def calculate_daily_average(data: List[DataItem]):
    daily_sums = defaultdict(list)
    for item in data:
        date_str = item.timestamp.split("T")[0]
        daily_sums[date_str].append(item.value)
    daily_averages = {date: mean(values) for date, values in daily_sums.items()}
    return {"daily_averages": daily_averages}

@app.post("/best-average")
async def calculate_best_average(data: List[DataItem]):
    daily_sums = defaultdict(list)
    for item in data:
        date_str = item.timestamp.split("T")[0]
        daily_sums[date_str].append(item.value)
    daily_averages = {date: mean(values) for date, values in daily_sums.items()}
    best_day = max(daily_averages, key=daily_averages.get)
    return {"best_day": best_day, "best_average": daily_averages[best_day]}
