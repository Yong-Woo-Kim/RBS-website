from flask import Flask, render_template, jsonify
import database as db

app = Flask(__name__)
  
@app.route('/')
def hello_rbs():
  result = ''
  i = 0
  t_name = db.load_teacher_name()
  for k, v in t_name:
    i += 1
    if i is len(t_name):
      result = result + v
    else:
      result = result + v + ','
  teacher_name = [{'title': 'Teacher', 'display': result}]
  return render_template('home.html', contents=teacher_name, school='RBS')


@app.route('/teacher')
def list_teacher():
  return jsonify(Contents)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
