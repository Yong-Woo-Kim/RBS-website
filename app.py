from flask import Flask, render_template, jsonify

app = Flask(__name__)

Contents = [
  {
    'title': 'Teacher',
    'display': 'Teacher Name'
  },
  {
    'title': 'Student',
    'display': 'Student Name'
  },
  {
    'title': 'Event'
  },
  {
    'title': 'mobile',
    'display': '041-555-7777'
  }
]

@app.route('/')
def hello_worls():
  return render_template('home.html', contents= Contents,school='RBS')

@app.route('/teacher')
def list_teacher():
  return jsonify(Contents)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
