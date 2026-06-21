from fastapi import FastAPI
from pydantic import BaseModel
from app.workflow import build_workflow
import asyncio

app = FastAPI()
workflow = build_workflow()

class QueryRequest(BaseModel):
    query: str

@app.post("/research")
async def research(request: QueryRequest):

    loop = asyncio.get_event_loop()

    result = await loop.run_in_executor(
        None,
        lambda: workflow.invoke({
            "query": request.query,
            "papers": [],
            "extracted_data": [],
            "gaps": "",
            "final_output": ""
        })
    )

    return {"result": result["final_output"]}