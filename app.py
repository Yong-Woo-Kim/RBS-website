from flask import Flask, render_template, jsonify
import database as db

app = Flask(__name__)
  
@app.route('/')
def hello_rbs():
  t_result = ''
  i = 0
  t_name = db.load_teacher_name()
  for k, v in t_name:
    i += 1
    if i is len(t_name):
      t_result = t_result + v
    else:
      t_result = t_result + v + ','
      
  s_result = ''
  i = 0
  s_name = db.load_student_name()
  for k, v in s_name:
    i += 1
    if i is len(s_name):
      s_result = s_result + v
    else:
      s_result = s_result + v + ','
      
  Contents = [{'title': 'Teacher', 'display': t_result},
                 {'title': 'Student', 'display': s_result}]
  return render_template('home.html', contents=Contents, school='RBS')


@app.route('/teacher')
def list_teacher():
  return 'hello' #jsonify(Contents)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
