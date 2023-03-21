from flask import Flask, render_template, request
import database as db

app = Flask(__name__)


      
@app.route('/')
def hello_rbs():
  t_name = db.load_teacher_name()
  s_name = db.load_student_name()
  Contents = [{'title': 'Teacher', 'display': t_name},
                 {'title': 'Student', 'display': s_name}]
  return render_template('home.html', contents=Contents, title='RBS')

@app.route('/Teacher')
def display_teacher():
  return render_template('detail-info.html', title='Teachers' )
  
@app.route('/Student')
def display_student():
  return render_template('detail-info.html', title='Students' )

@app.route('/Teachers/apply', methods=['POST'])
def apply_teacher():
  data = request.form
  db.add_teacher(data)
  return render_template('application_submitted.html', application=data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
