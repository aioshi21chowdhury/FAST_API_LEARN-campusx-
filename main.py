from fastapi import FastAPI,Path,HTTPException,Query
import json
app=FastAPI()

def load_data():
    with open('patients.json') as f:
        data= json.load(f)
    return data    
        
    
    
@app.get("/")
def hello():
    return {"message":"Patient Management System"}

@app.get("/about")
def know():
    return {"manage the patient records and appointments"}

@app.get('/view')
def view():
    data=load_data()
    
    return data

# video 4
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description="put the id of the patient",example="P00x")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # else:(was returning a json )
    #     return {"error:no such patient"}
    raise HTTPException(status_code=404,detail="data not found")


#query parameter
@app.get('/sort')
def sort_patient(sort_by:str=Query(...,description="sort on height"),order:str=Query('asc',description="ascending or descending sorting")):
    vaild_data=['height',"weight","bmi"]
    if sort_by not in vaild_data:
        raise HTTPException(status_code=400,detail="invalid enquiry")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="invalid ask")
    # load the function
    data=load_data()
    
    sort_order=True if order=="decs" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    
    return sorted_data
    # for testing -->http://127.0.0.1:8000/sort?sort_by=bmi&order=desc