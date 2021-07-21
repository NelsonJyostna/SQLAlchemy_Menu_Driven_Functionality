from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

from sqlalchemy.orm import mapper, sessionmaker

url='mysql://root:NElson@26@localhost:3306/db2'

ENGINE=create_engine(url)

class Student:
    def __init__(self,r, n, m):
        self.rn=r
        self.name=n
        self.marks=m

    def __str__(self):
        return f'Roll No : {self.rn}, Name - {self.name}, Marks - {self.marks}'

md=MetaData()

st=Table('stud_table', md, Column('rn', Integer, primary_key=True),
                          Column('name', String(20)),
                          Column('marks', Float)
         )

mapper(Student, st)
md.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

while True:
    ch=int(input("ENter a choice : 1. Add \t 2. Show \t 3. Update \t 4.Delete \t 5.Exit "))
    if ch==1:
      try:  
       rollno=int(input("Enter a roll no : "))
       n=input("ENter a name : ")
       m=int(input("Enter a marks : "))
       s1=Student(rollno, n, m)
       sess.add(s1)
       sess.commit()
       print("Added sucessfully")
      except Exception as e:
         print("Exception Occured", e)
    elif ch==2:
         stud_rows=sess.query(Student)
         if stud_rows==[]:
             print("Ur list is empty") 
         else:
            stud_rows=sess.query(Student)
            for stud in stud_rows:
                print(stud)
    elif ch==3:
        print("Update code")
        ch=int(input("ENter a choice : 1.update by name \t 2. update by marks"))
        if ch==1:
            ro=int(input("enter a roll no for updation :"))
            m=input("Enter a new name for updated : ")
            sess.query(Student).filter(Student.rn==ro).update({Student.name:m})
            print("Updated name")
            sess.commit()
        elif ch==2:
            ro=int(input("enter a roll no for updation :"))
            m=int(input("Enter a new marks for updated : "))
            sess.query(Student).filter(Student.rn==ro).update({Student.marks:m})
            print("Updated marks")
            sess.commit()
        else:
            print(ch, "U have entered wrong choice")
    elif ch==4:
        print("Delete code")
        ch=int(input("ENter a choice : 1.Delete by name \t 2. Delete by marks"))
        if ch==1:
           m=input("Enter a name for deletion : ")
           studobj=sess.query(Student).filter(Student.name==m)
           studobj.delete()
           print("Deleted by name")
           sess.commit()
        elif ch==2:
            m=int(input("Enter a marks for deletion : "))
            studobj=sess.query(Student).filter(Student.marks==m)
            studobj.delete()
            sess.commit()
            print("Deleted by marks")
        else:
            print(ch, "U have entered wrong choice")
    elif ch==5:
        print("Existed Successfully")
        break
    else:
        print(ch, "U have entered wrong choice")
    

