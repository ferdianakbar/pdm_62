import sqlalchemy.orm as _orm
import models as _models, schemas as _schemas, database as _database
import datetime as _dt

def getMovies(db: _orm.Session, skip: int = 0, limit: int = 10):
    """Movie List"""
    return db.query(_models.Movie).offset(skip).limit(limit).all()

def createMovie(db: _orm.Session, movie: _schemas.MovieCreate):
    """Create Movie"""
    newMovie = _models.Movie(**movie.dict())
    db.add(newMovie)
    db.commit()
    db.refresh(newMovie)
    return newMovie


def getMovie(db: _orm.Session, id: int):
    """Get Movie"""
    return db.query(_models.Movie).filter(_models.Movie.id == id).first()


def deleteMovie(db: _orm.Session, id: int):
    """Delete Movie"""
    db.query(_models.Movie).filter(_models.Movie.id == id).delete()
    db.commit()

def updateMovie(db: _orm.Session, movie: _schemas.MovieInfo, dataMovie: _schemas.MovieCreate):
    """Update Movie"""
    movie.name = dataMovie.nam
    movie.description = dataMovie.description
    movie.rating = dataMovie.rating
    movie.playing_date = movie.playing_date
    movie.last_updated = _dt.datetime.utcnow()
    db.commit()
    db.refresh(movie)
    return movie
