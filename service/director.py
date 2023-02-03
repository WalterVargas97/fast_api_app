from models.director import  Director as DirectorModel
from schemas.director import Director

class DirectorService():
    def __init__(self,db) -> None:
        self.db = db
        

    def get_directors(self) -> DirectorModel:
        result = self.db.query(DirectorModel).all
        return result
    def get_director_by_id(self,id:int):
        result = self.db.query(DirectorModel).filter(DirectorModel.id == id).first()
        return result
    #falta por nombre 
    
    def create_director(self,director: DirectorModel):
        new_director = DirectorModel(
        director_first_name = director.fname,
        director_last_name = director.lname
        )
        self.db.add(new_director)
        self.db.commit()
        return
    
    def update_director(self, fname:str, data:Director):
        director.id = data.id
        director = self.db.query(DirectorModel).filter(DirectorModel.fname==fname).first()
        director.lname = data.lname
        self.db.commit()
        
    def delete_director(self,lname:str):
        self.db.query(DirectorModel).filter(DirectorModel.lname==lname).delete()
        self.db.commit()
        return    