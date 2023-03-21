import sqlite3

conn = sqlite3.connect('rbs.db', check_same_thread=False)
c = conn.cursor()

def make_list(dic):
  result = ''
  i = 0
  
  for k, v in dic:
    i += 1
    if i is len(dic):
      result = result + v
    else:
      result = result + v + ','
  return result

def load_teacher_name():
  result = c.execute('select "display", name from teacher')
  t_name = result.fetchall()
  result = make_list(t_name)
  return result

def load_student_name():
  result = c.execute('select "display", name from student')
  s_name = result.fetchall()
  result = make_list(s_name)
  return result

def load_teacher(id):
  result = c.execute('select * from teacher where id = ?',(id)).fetchall()
  print(type(result))

load_teacher('1')