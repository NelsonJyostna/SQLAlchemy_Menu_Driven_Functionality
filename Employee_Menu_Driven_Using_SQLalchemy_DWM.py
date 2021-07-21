from sqlalchemy import Table, Column, Integer, Float, create_engine, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL='mysql://root:NElson@26@localhost:3306/db1'


Engine=create_engine(DB_URL)

Base=declarative_base()

class Employee(Base):
      __tablename__='st5'
      eid=Column(Integer, primary_key=True)
      ename=Column(String(20))
      esal=Column(Float)
      edesg=Column(String(20))
      eaddr=Column(String(20))

      def __str__(self):
          return f'Employee Id :{self.eid}, Employee Name : {self.ename}, Emp Salery : {self.esal}, Emp Designation : {self.edesg}, Emp Address : {self.eaddr}'

Base.metadata.create_all(Engine)

Session=sessionmaker(bind=Engine)
sess=Session()

while True:
        ch=int(input("Enter a choice : 1. Add \t 2. Show  \t 3.Update \t 4. Delete \t 5. Exist "))
        if ch==1:
          id=int(input("Enter a roll no : "))
          name=input("ENter a name : ")
          sal=int(input("Enter a Salery : "))
          desg=input("Enter a designation : ")
          addr=input("Enter a address : ")
          e1=Employee(eid=id, ename=name, esal=sal, edesg=desg, eaddr=addr)
          sess.add(e1)
          sess.commit()
          print("Added Successfully")
        elif ch==2:
          emp_obj=sess.query(Employee)
          for emp in emp_obj:
             print(emp)
        elif ch==3:
          print("Update Code")
          ch_up=int(input("Enter a choice : 1. By name \t 2. By addr"))
          if ch_up==1:
             id1=int(input("Enter a id for updatation code :"))
             name=input("ENter a new name :")
             sess.query(Employee).filter(Employee.eid==id1).update({Employee.ename : name})
             sess.commit()
             print("UPdated by name")
          elif ch_up==2:
             id2=int(input("Enter a id for updatation code :"))
             addr2=input("Enter address : ")
             sess.query(Employee).filter(Employee.eid==id2).update({Employee.eaddr :addr2})
             sess.commit()
             print("Updated by address")
          else:
              print(ch_up, "u have entered wrong choice")
        elif ch==4:
           print("Delete Code")
           ch_de=int(input("Enter a choice : 1. By name \t 2. By addr"))
           if ch_de==1:
              name=input("Enter a name for deletion  :")
              sess.query(Employee).filter(Employee.ename==name).delete()
              sess.commit()
              print("Name Deleted")
           elif ch_de==2:
              addr=input("Enter address for deletion :")
              sess.query(Employee).filter(Employee.eaddr==addr).delete()
              sess.commit()
              print("Address Deleted")
           else:
               print(ch_de, "U have entered wrong choice")
        else:
           print(ch, "U have entered wrong choice")
                         
             
             
         
         



