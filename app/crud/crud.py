from fastapi import HTTPException,status

class Crud:
    def create(self,db,row):
        db.add(row)
        db.commit()
        db.refresh(row)

        return row
    
    def get_all(self,db,table):
        res = db.query(table).all()

        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
            
        return res
    
    def delete(self,db,table,id):
        res = db.query(table).filter(id==id).all()
        
        db.delete(res)
        db.commit()
        
