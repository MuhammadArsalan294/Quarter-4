from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "Too Many Requests",
            "message": "You have exceeded the rate limit. Please slow down and try again later.",
        },
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/read")
async def read():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]


@app.get("/login")
@limiter.limit("3/minute")
async def login(request: Request):
    return {"message": "Login successful"}


@app.post("/claude-code")
@limiter.limit("2/5 hours")
async def claude_code(request: Request):
    return {"message": "Claude code executed successfully"}
