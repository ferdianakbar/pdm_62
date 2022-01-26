from shutil import move
import uvicorn
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models as models, schemas as _schemas, crud
from database import db_engine, SessionLocal


models.Base.metadata.create_all(bind=db_engine)

app = FastAPI()

def get_database_session():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/movies", response_model=List[_schemas.MovieInfo])
def movieList(skip: int = 0, limit = 0, db: Session =  Depends(get_database_session)):
    return crud.getMovies(db=db,  skip=skip, limit = limit)

@app.post("/api/movie", response_model=_schemas.MovieInfo)
def createMovie(movie: _schemas.MovieCreate, db: Session =  Depends(get_database_session)):
    return crud.createMovie(db=db,  movie= movie)

@app.get("/api/movie/{id}", response_model=_schemas.MovieInfo)
def getMovie(id: int, db: Session =  Depends(get_database_session)):
    movie = crud.getMovie(db, id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.put("/api/movie/{id}", response_model=_schemas.MovieInfo)
def getMovie(id: int, dataMovie: _schemas.MovieCreate, db: Session =  Depends(get_database_session)):
    movie = crud.getMovie(db, id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    updatedMovie = crud.updateMovie(db, movie, dataMovie)
    return updatedMovie

@app.delete("/api/movie/{id}")
def getMovie(id: int, db: Session =  Depends(get_database_session)):
    movie = crud.getMovie(db, id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    crud.deleteMovie(db, id)
    return {
        "message": f"Successfully delete movie with id: {id}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)