import psycopg2

hostname= 'localhost'
database = 'Register'
username= 'postgres'
pwd='Avinash2001'
port_id = 5432
conn = None
cur = None
try:
    
   conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password=pwd,
    port = port_id)
   
   cur = conn.cursor()
   
   create_script = ''' CREATE TABLE data (
                        id int PRIMARY key,
                        name varchar(40) Not NULL,
                        salary int,
                        dept_id  varchar(30))'''
                        
                        
   cur.execute(create_script)
   insert_script = 'INSERT INTO data(id,name,salary,dept_id) VALUES(%S,%S,%S,%S)'
   insert_value=(1,'James',120000,'D1')
   cur.execute(insert_script, insert_value)
   
   conn.commit()                
   


   conn.close()
except Exception as error:
    print(error)
    
finally:
    if cur is not None:
        
      cur.close()
    if conn is not None:
        
       conn.close()    
       

