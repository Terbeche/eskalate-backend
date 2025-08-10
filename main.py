from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, database
from app.api.restaurants import router as restaurants_router
from app.api.meals import router as meals_router

app = FastAPI(title="Food Management API", version="1.0.0")

origins = [
    "http://localhost:3000",
    "http://localhost:3001", 
    "http://localhost:3002",
    "http://127.0.0.1:3000",
    "https://*.herokuapp.com",
    "https://*.vercel.app",
    "https://*.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)

# Include modular routers
app.include_router(restaurants_router)
app.include_router(meals_router)

@app.get("/")
def root():
    return {"message": "Food Management API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
