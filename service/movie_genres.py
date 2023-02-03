from models.movie_genres import  Movie_genres as MovieGenresModel
from schemas.movie_genres import Movie_genres


class MovieGenresService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_movie_genres(self,id_movie:int):
        result = self.db.query(MovieGenresModel).filter(MovieGenresModel.movie_id == id_movie).all()
        return result
    
    def create_movie_genres(self,movie_genres: MovieGenresModel):
        new_Mgenres = MovieGenresModel(
            movie_id = movie_genres.movie_id,
            gen_id = movie_genres.gen_id
        )
        self.db.add(new_Mgenres)
        self.db.commit()
        return