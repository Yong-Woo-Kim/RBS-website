import sqlite3

conn = sqlite3.connect('rbs.db', check_same_thread=False)
c = conn.cursor()
id = 0


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

def load_teacher():
    result = c.execute('select * from teacher')
    teacher_info = result.fetchall()
    return teacher_info


def read_table_column():
    query = 'select group_concat(name) from pragma_table_info("teacher")'
    result = c.execute(query).fetchall()
    column_info = list(result[0])
    list_name = list(column_info[0].split(','))
    return list_name

def select_teacher(t_name):
    result = c.execute(f'SELECT * FROM teacher WHERE name="{t_name}"')
    teacher_data = result.fetchall()
    return teacher_data
  
def load_student_name():
  result = c.execute('select "display", name from student')
  s_name = result.fetchall()
  result = make_list(s_name)
  return result

def add_teacher(data):
  c.execute(
    'INSERT INTO teacher (name, birthday, gender, mobile, address) VALUES (?,?,?,?,?)',
    (data['name'], data['birthday'], data['gender'], data['mobile'],
     data['address']))
  conn.commit()

def update_teacher(data):
  c.execute(
    'UPDATE teacher SET birthday=?, gender=?, mobile=?, address=?, career=?, charge=? WHERE name=?',
    (data['birthday'], data['gender'], data['mobile'],
     data['address'], data['career'], data['charge'], data['name'] ))
  conn.commit()

