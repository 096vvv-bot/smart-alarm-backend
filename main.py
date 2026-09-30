from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"status": "ok", "message": "Smart Alarm Backend is running!"}


@app.post("/update-status")
def update_status(data: dict):
  return {"success": True, "received": data}


@app.get("/security-status")
def get_status():
  return {"threat_level": "normal"}
