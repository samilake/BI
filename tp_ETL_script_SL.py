def get_gender(gdr):
    if str.upper(gdr) in ['F','M']: return str.upper(gdr);
    else: return 'unknown'

def get_state(st):
    if st != "": return st
    else: return 'unknown'

cle = 0
import MySQLdb as mysql  #Manipuler BD Mysql
db = mysql.connect(host="localhost", user="root", passwd="", db="source_DB")  #Connexion, curseur - table source
cursor_source = db.cursor()
db = mysql.connect(host="localhost", user="root", passwd="", db="clients_DB") #Connexion, curseur - table destination
cursor_destination = db.cursor()

cursor_source.execute('select id, first_name, last_name, email, gender, ville from client_data')
for row in cursor_source.fetchall():
    id, first_name, last_name, email, gender, state = row
    cle=cle+1
    cursor_destination.execute("INSERT INTO clients VALUES (%s, %s,'%s','%s','%s','%s','%s')" %
                              (cle, id, first_name, last_name, get_gender(gender[0]), email, get_state(state)))
db.commit()
cursor_source.close()

import csv #Connexion - table source
with open('week_cust.csv', 'rt') as csvfile:
     sreader = csv.reader(csvfile, delimiter=',', quotechar=',')
     next(csvfile)
     for row in sreader:
        id,first_name,last_name,email,gender,state = row
        cle=cle+1
        cursor_destination.execute("INSERT INTO clients VALUES (%s, %s,'%s','%s','%s','%s','%s')" %
                                  (cle, id, first_name, last_name, get_gender(gender[0]), email, get_state(state)))
db.commit()

import json
f = open('cust_data.json')
cust_data= json.load(f)
for tmp in cust_data:
    id = tmp['id']
    first_name = tmp['first_name']
    last_name = tmp['last_name']
    email = tmp['email']
    try:
        gender = tmp['gender']
    except KeyError:
        gender = " "
    pass
    state = tmp['ville']
    cle=cle+1
    cursor_destination.execute("INSERT INTO clients VALUES (%s, %s,'%s','%s','%s','%s','%s')" %
                              (cle, id, first_name, last_name, get_gender(gender[0]), email, get_state(state)))
db.commit()
cursor_destination.close()
print('All tables loaded')