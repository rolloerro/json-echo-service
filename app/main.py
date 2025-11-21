from fastapi import FastAPI
from uuid import uuid4
from datetime import datetime
from app.models import EchoRequest, EchoResponse

app = FastAPI(title="JSON Echo Service")

@app.post("/echo", response_model=EchoResponse)
async def echo(payload: EchoRequest):
    return EchoResponse(
        received=payload.data,
        timestamp=datetime.utcnow().isoformat(),
        request_id=str(uuid4())
    )

@app.get("/ping")
async def ping():
    return {"status": "ok"}
