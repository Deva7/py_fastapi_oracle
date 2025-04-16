from fastapi import FastAPI, HTTPException
import uvicorn
from src import get_db_connection
from src.models.Employee import Employee
from typing import List
app = FastAPI()

@app.get("/employees", response_model=List[Employee])
async def get_employees():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, department FROM employees")
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
        if employees:
            res = [Employee(id=row[0], name=row[1], department=row[2]) for row in employees]
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)