import sqlite3

conn = sqlite3.connect('rbs.db', check_same_thread=False)
c = conn.cursor()


def load_teacher_name():
  result = c.execute('select "display", name from teacher')
  t_name = result.fetchall()
  return t_name

def load_student_name():
  result = c.execute('select "display", name from student')
  s_name = result.fetchall()
  return s_name