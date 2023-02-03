from models.moviedirection import Movie_direction as MovieDirectionModel
from schemas.movie_direction import MovieDirection


class MovieDirectionService():
    def __init__(self,db) -> None:
        self.db = db
    
    def get_movie_direction(self,id_movie:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.movie_id == id_movie).all()
        return result
    
    def create_movie_direction(self,movie_direction:MovieDirectionModel):
        new_direction = MovieDirectionModel(
            director_id = movie_direction.director_id,
            movie_id = movie_direction.movie_id
        )
        self.db.add(new_direction)
        self.db.commit()
        return
    