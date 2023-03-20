import sqlite3

conn = sqlite3.connect('rbs.db', check_same_thread=False)
c = conn.cursor()

def load_teacher_name():
  result = c.execute('select name from teacher')
  t_name = result.fetchall()
  return t_name
  