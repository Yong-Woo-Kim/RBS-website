from flask import Flask, render_template
import database as db

app = Flask(__name__)


      
@app.route('/')
def hello_rbs():
  t_name = db.load_teacher_name()
  s_name = db.load_student_name()
  Contents = [{'title': 'Teacher', 'display': t_name},
                 {'title': 'Student', 'display': s_name}]
  return render_template('home.html', contents=Contents, school='RBS')


@app.route('/Teacher')
def display_teacher():
  return render_template('detail-info.html', contents='Teachers' )
  
@app.route('/Student')
def display_student():
  return render_template('detail-info.html', contents='Students' )

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
