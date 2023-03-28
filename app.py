from flask import Flask, render_template, request, redirect
import database as db

app = Flask(__name__)

@app.route('/')
def hello_rbs():
  t_name = db.load_teacher_name()
  s_name = db.load_student_name()
  Contents = [{
    'title': 'Teacher',
    'display': t_name
  }, {
    'title': 'Student',
    'display': s_name
  }]
  return render_template('home.html', contents=Contents, title='RBS')

@app.route('/Teacher')
def display_teacher():
  tbl_column = db.read_table_column()
  Contents = db.load_teacher()
  return render_template('detail-info.html',
                         tbl_head=tbl_column,
                         contents=Contents,
                         title='Teachers')


@app.route('/update/<t_name>')
def update(t_name):
  teacher = db.select_teacher(t_name)
  teacher = list(teacher[0])
  return render_template('application_submitted.html',
                         application=teacher,
                         info='update')


# @app.route('/Student')
# def display_student():
#   return render_template('detail-info.html', title='Students')


@app.route('/apply/update', methods=['POST'])
def update_teacher():
  data = request.form
  db.update_teacher(data)
  return redirect('/Teacher')

@app.route('/apply/insert', methods=['POST'])
def insert_teacher():
  data = request.form
  print(data)
  # db.add_teacher(data)
  return 'hello'  #render_template('application_submitted.html', application=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
