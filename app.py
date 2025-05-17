from flask import Flask, jsonify, abort

app = Flask(__name__)

teachers = {
    1: {"name": "Ali Ahmed", "courses": [101, 102]},
    2: {"name": "Fatima Noor", "courses": [103, 104]},
    3: {"name": "Yusuf Patel", "courses": [105]}
}

students = {
    1: {"name": "Sara Khan", "enrolled": [101, 103]},
    2: {"name": "Omar Salim", "enrolled": [102, 104]},
    3: {"name": "Laila Hussein", "enrolled": [101, 102, 105]}
}

courses = {
    101: {"title": "Beginner Qur'an"},
    102: {"title": "Intermediate Arabic"},
    103: {"title": "Advanced Tafsir"},
    104: {"title": "Arabic Grammar Essentials"},
    105: {"title": "Modern Standard Arabic Conversation"}
}

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def list_student_courses(student_id):
    student = students.get(student_id)
    if not student:
        abort(404, description="Student not found")
    course_list = [
        {
            "id": cid,
            "title": courses[cid]['title'],
            "student_name": student['name']
        }
        for cid in student['enrolled']
    ]
    return jsonify({
        "student_id": student_id,
        "student_name": student['name'],
        "courses": course_list
    })

@app.route('/teachers/<int:teacher_id>/courses', methods=['GET'])
def list_teacher_courses(teacher_id):
    teacher = teachers.get(teacher_id)
    if not teacher:
        abort(404, description="Teacher not found")
    course_list = [
        {
            "id": cid,
            "title": courses[cid]['title'],
            "teacher_name": teacher['name']
        }
        for cid in teacher['courses']
    ]
    return jsonify({
        "teacher_id": teacher_id,
        "teacher_name": teacher['name'],
        "courses": course_list
    })

# An endpoint to view everything.
@app.route('/all-data', methods=['GET'])
def all_data():
    teachers_list = [
        {
            "id": tid,
            "name": tinfo['name'],
            "courses": [
                {"id": cid, "title": courses[cid]['title']} 
                for cid in tinfo['courses']
            ]
        }
        for tid, tinfo in teachers.items()
    ]
    students_list = [
        {
            "id": sid,
            "name": sinfo['name'],
            "enrolled_courses": [
                {"id": cid, "title": courses[cid]['title']} 
                for cid in sinfo['enrolled']
            ]
        }
        for sid, sinfo in students.items()
    ]
    courses_list = [
        {"id": cid, "title": cinfo['title']} 
        for cid, cinfo in courses.items()
    ]

    return jsonify({
        "teachers": teachers_list,
        "students": students_list,
        "courses": courses_list
    })

if __name__ == '__main__':
    app.run(debug=True)
