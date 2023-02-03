from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.movie import Movie
from models.reviewer import Reviewer

class Rating(Base):

    __tablename__ = "rating"

    movie_id = Column(Integer, ForeignKey ("movie.id"))
    reviewer_id = Column(Integer, ForeignKey("reviewer.id"))
    reviewer_stars = Column(Integer)
    num_o_ratings = Column(Integer)