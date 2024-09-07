from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import arrow
from starlette.middleware.cors import CORSMiddleware
import json  # Import json for parsing JSON data
import uvicorn

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{path:path}")
@app.post("/{path:path}")
@app.put("/{path:path}")
@app.delete("/{path:path}")
async def hello_world(path: str, request: Request):
    body_bytes = await request.body()
    body_str = body_bytes.decode('utf-8')

    response_content = {
        "msg": "Hello, World!" + " at " + arrow.now().format("YYYY-MM-DD HH:mm:ss"),
        "request": {
            "query": str(request.query_params),
            "path": path,
            "data": body_str,  # Use the decoded string here
            "clientIp": request.headers.get("x-forwarded-for"),
        },
    }
    return JSONResponse(response_content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)