from flask import Flask, render_template, jsonify
import database as db

app = Flask(__name__)

Contents = [{
  'title': 'Teacher',
  'display': 'Teacher Name'
}, {
  'title': 'Student',
  'display': 'Student Name'
}, {
  'title': 'Event'
}, {
  'title': 'mobile',
  'display': '041-555-7777'
}]


@app.route('/')
def hello_rbs():
  result = []
  t_name = db.load_teacher_name()
  # for row in t_name:
  #   result.append(row)
  
  print(result)
  return render_template('home.html', contents=t_name, school='RBS')


@app.route('/teacher')
def list_teacher():
  return jsonify(Contents)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
