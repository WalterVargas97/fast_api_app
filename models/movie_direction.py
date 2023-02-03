from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from config.database import Base

class Movie_direction(Base):
    __tablename__ = "movie_direction"
    id = Column(Integer, primary_key=True, index=True)
    director_id = Column(Integer, ForeignKey("director.id") ) 
    movie_id = Column (Integer, ForeignKey("movie.id" ))