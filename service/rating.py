from models.rating import Rating as RatingModel
from schemas.rating import Rating

class RatingService():
    def __init__(self,db) -> None:
        self.db = db
    
    def get_ratings(self,id_movie:int):
        result = self.db.query(RatingModel).filter(RatingModel.movie_id == id_movie).all()
        return result
    
    def create_rating(self,rating:RatingModel):
        new_rating = RatingModel(
            movie_id = rating.movie_id,
            reviewer_id = rating.reviewer_id,
            reviewer_stars = rating.reviewer_stars,
            num_o_ratings = rating.num_o_ratings
            
        )
    