from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from config.database import Base

class Genres(Base):

    __tablename__ = "genres"

    id = Column(Integer,primary_key = True, index = True)
    title = Column(String)

    
