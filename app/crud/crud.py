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
    
    def put(self,db,table,id,row):
        res_query = db.query(table).filter(id==id)
        
        res = res_query.first()
        
        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
        
        if res.id != id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
        try:
            for key in row.dict():
                if key != 'id':
                    res.key = row.dict()[key]
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Column is not here")
            
        res_query.update(res, synchronize_session=False)
        db.commit()
        return res_query.first()
        

    def delete(self,db,table,id):
        res = db.query(table).filter(id==id).first()
        
        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
        
        db.delete(res)
        db.commit()
        
        return {"message":"Content deleted"}
        

crud_obj = Crud()
