from models.reviewer import Reviewer as ReviewerModel
from schemas.reviewer import Reviewer

class ReviewerService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_reviewers(self) -> ReviewerModel:
        result = self.db.query(ReviewerModel).all()
        return result 
    
    def create_reviewer(self, reviewer:ReviewerModel):
        new_reviewer = ReviewerModel(
        reviewer_name = reviewer.name
        )
        
        