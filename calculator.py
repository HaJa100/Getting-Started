from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import math

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class CalcRequest(BaseModel):
    expression: str

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.post("/api/calc")
async def calculate(request: CalcRequest):
    try:
        # Safely evaluate the expression (use eval cautiously in production)
        result = eval(request.expression, {"__builtins__": {}}, {"sqrt": math.sqrt, "pow": pow, "abs": abs})
        return {"result": result, "error": None}
    except Exception as e:
        return {"result": None, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)