from models.genres import Genres as GenresModel
from schemas.genres import Genres


class GenresService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_genres(self,id_genres:int):
        result = self.db.query(GenresModel).filter(GenresModel.id == id_genres).all()
        return result
    
    def create_movie_cast(self,genres:GenresModel):
        new_genres = GenresModel(
        genres_title = genres.title
        )
        self.db.add(new_genres)
        self.db.commit()
        return