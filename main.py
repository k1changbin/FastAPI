from fastapi import FastAPI
import json
import uvicorn
from model import Course

app = FastAPI()

FILE_PATH = "courses.json"

@app.get("/")
async def hello_world():
    return {"msg": "오픈소스소프트웨어 실습-4  FastAPI"}

@app.get("/courses")
async def get_courses():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@app.post("/courses")
async def add_course(course: Course):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data.append(course.model_dump())
    
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return {"msg": "과목 등록"}

if __name__ == "__main__":
    uvicorn.run("main:app", host= "0.0.0.0", port=8000, reload=True)