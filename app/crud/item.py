from fastapi import HTTPException,status

class Item:
    def create(self,db,row):
        db.add(row)
        db.commit()
        db.refresh(row)

        return row
    
    def get_all(self,db,table,id:int=-1):
        if id ==-1:
            res = db.query(table).all()
        else:
            res = db.query(table).filter(
                table.id == id
            ).first()

        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
            
        return res
    
    def put(self,db,table,id,row,user_id):
        res_query = db.query(table).filter(id==id)
        
        res = res_query.first()
        
        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
        
        if res.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
            
        res_query.update(row.dict(), synchronize_session=False)
        db.commit()
        return res_query.first()
        

    def delete(self,db,table,id,user_id):
        res = db.query(table).filter(id==id).first()
        
        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No Data Found")
        
        if res.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
        
        db.delete(res)
        db.commit()
        
        return {"message":"Content deleted"}
        

item_obj = Item()
