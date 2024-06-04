from fastapi import FastAPI
from api_client import fetch_vulnerabilities
from parser import parse_response
from datetime import datetime

app = FastAPI()

@app.get("/versions")
def get_versions(name: str):
    try:
        response = fetch_vulnerabilities(name)
        versions = parse_response(response)
        return {"name": name, "versions": versions, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    except Exception as e:
        return {"error": str(e)}
