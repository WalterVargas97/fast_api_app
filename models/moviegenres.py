from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from config.database import Base
from models.movie import Movie
from models.genres import Genres


class Movie_genres(Base):

    __tablename__ = "movie_genres"
    id = Column(Integer, primary_key=True, index=True)

    movie_id = Column(Integer,ForeignKey("movie.id"))
    gen_id = Column (Integer, ForeignKey("genres.id"))
