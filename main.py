from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class student(BaseModel):
    id: int
    name: str
    grade: int
students = [student(id=1, name="musab", grade=5),
           student(id=2, name="amna", grade=3)]
@app.get("/students")
def get_students():
    return students
@app.post("/students")
def create_student(student: student):
    students.append(student)
    return student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = updated_student
            return updated_student
    return {"error": "Student not found"}
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(i)
            return deleted_student
    return {"error": "Student not found"}
