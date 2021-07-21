from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL='mysql://root:NElson@26@localhost:3306/db1'

ENGINE=create_engine(DB_URL)

Base=declarative_base()

class Student(Base):
    __tablename__='st2'
    rn=Column(Integer, primary_key=True)
    name=Column(String(20))
    marks=Column(Integer)

    def __str__(self):
        return f' Roll No : {self.rn}, Name={self.name}, Marks={self.marks}'


Base.metadata.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()
while True:
    try:
        ch=int(input("Enter a choice : 1. Add \t  2.show \t  3.Update \t  4.Delete \t 5.Exist"))
    except Exception as e:
        print("Exception Occured", e)

    if ch==1:
        r=int(input("Enter a roll no :"))
        name=input("Enter a name : ")
        marks=int(input("Enter a marks :"))
        s1=Student(rn=r, name=name, marks=marks)
        sess.add(s1)
        sess.commit()
    elif ch==2:
         res=sess.query(Student)
         for stu in res:
             print(stu)
    elif ch==3:
        print("Update Code")
        ch_up=int(input("ENter a choice : 1. Update by name \t  2. Update by marks"))
        if ch_up==1:
            r1=int(input("Enter a roll no for updating the name : "))
            name=input("Enter a new name :")
            sess.query(Student).filter(Student.rn==r1).update({Student.name:name})
            sess.commit()
            print("Updated by name")
        elif ch_up==2:
             r2=int(input("Enter a roll no for updating the marks :"))
             marks=int(input("Enter a new marks :"))
             sess.query(Student).filter(Student.rn==r2).update({Student.marks:marks})
             sess.commit()
             print("Updated by marks")
        else:
             print(ch_up, "U have entered wrong choice")
    elif ch==4:
        print("Delete code")
        ch_de=int(input("Enter a choice : 1.Delete by name \t 2. Delete by marks"))
        if ch_de==1:
            name=input("Enter a name for deletion : ")
            sess.query(Student).filter(Student.name==name).delete()
            sess.commit()
            print("Delete by name")
        elif ch_de==2:
            mark=input("Enter a marks :")
            sess.query(Student).filter(Student.marks==mark).delete()
            sess.commit()
            print("Delete by name")
        else:
             print(ch_de, "U have entered wrong choice")
    else:
        print(ch, "U have entered wrong choice")
        
