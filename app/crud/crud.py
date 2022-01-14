from fastapi import HTTPException,status

class Crud:
    def create(db,row):
        db.add(row)
        db.commit()
        db.refresh(row)

        return row
    
    def get_all(table,db):
        res = db.query(table).all()

        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Data Found")
