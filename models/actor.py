from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class Actor(Base):

    __tablename__ = "actor"

    id = Column(Integer,primary_key = True)
    fname = Column(String)
    alname = Column(String)
    gender = Column(String)

    #movie_casts = relationship("MovieCast", back_populates = "actors")




