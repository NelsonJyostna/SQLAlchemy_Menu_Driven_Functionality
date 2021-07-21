from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

from sqlalchemy.orm import mapper, sessionmaker

url='mysql://root:NElson@26@localhost:3306/db3'

ENGINE=create_engine(url)


class Employee:
    def __init__(self,eid, ename, exp, esal, edesg, eaddr):
        self.eid=eid
        self.ename=ename
        self.exp=exp
        self.esal=esal
        self.edesg=edesg
        self.eaddr=eaddr

    def __str__(self):
        return f' Emp Id : {self.eid}, Emp Name : {self.ename}, Emp Exp : {self.exp}, Emp Sal : {self.esal}, Emp Designation : {self.edesg}, Emp Address : {self.eaddr}'


md=MetaData()

et=Table('emp_table', md, Column('eid', Integer, primary_key=True),
                          Column('ename', String(20)),
                          Column('exp', Float),
                          Column('esal', Float),
                          Column('edesg', String(30)),
                          Column('eaddr', String(20))
         )

mapper(Employee, et)
md.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

while True:
    try:
      ch=int(input("Enter a choice : 1. Add \t  2. Show \t 3. Update \t 4. Delete \t 5. Exist"))
    except Exception as e:
        print("Exception occured", e)
        continue
    if ch==1:
       try: 
        id=int(input("enter ur id :"))
        name=input("Enter ur name :")
        exp=float(input("Enter ur experience :"))
        salery=float(input("Enter ur salery :"))
        desg=input("Enter ur designation :")
        addr=input("Enter ur address :")
        e1=Employee(id, name, exp, salery, desg, addr )
        sess.add(e1)
        sess.commit()
       except Exception as e:
           print("Exception occured ", e)
           continue
    elif ch==2:
            emp_rows=sess.query(Employee)
            for emp in emp_rows:
                print(emp)
    elif ch==3:
        print("Update code")
        try: 
         ch_up=int(input("Enter a choice for update : \t 1. Update by name \t 2. Update by addr"))
        except Exception as e:
           print("Exception occured", e)
           continue
        if ch_up==1:
           try: 
            id1=int(input("Enter ur id :"))
            name =input("Enter ur NEW name :")
            sess.query(Employee).filter(Employee.eid==id1).update({Employee.ename:name})
            print("Updated name")
            sess.commit()
            print("Ur name is updated successfully")
           except Exception as e:
               print("Exception occured", e)
               continue
        elif ch_up==2:
           try:
            id2=int(input("Enter ur id :"))
            addres=input("Enter ur NEW address :")
            sess.query(Employee).filter(Employee.eid==id2).update({Employee.eaddr:addres})
            print("Updated name")
            sess.commit()
            print("Ur Address is updated successfully")
           except Exception as e:
               print("Exception occured", e)
               continue
        else:
            print(ch_up,"U have entered wrong choice")

    elif ch==4:
          print("Delete code")
          try: 
           ch_de=int(input("Enter a choice for Delete : \t 1. Delete by name \t 2. Delete by addr"))
          except Exception as e:
             print("Exception occured", e)
             continue
          if ch_de==1:
             try: 
              name =input("Enter ur name :")
              empobj=sess.query(Employee).filter(Employee.ename==name)
              empobj.delete()
              sess.commit()
              print("Ur name is deleted successfully")
             except Exception as e:
                 print("Exception occured", e)
                 continue
          elif ch_de==2:
             try: 
              addres=input("Enter ur address :")
              empobj=sess.query(Employee).filter(Employee.eaddr==addres)
              empobj.delete()
              sess.commit()
              print("Ur Address is deleted successfully")
             except Exception as e:
               print("Exception occured", e)
               continue
          else:
             print(ch_de,"U have entered wrong choice")
             #continue
    elif ch==5:
         print("Existed succesfully")
         break
    else:
        print(ch,"You have entered wrong choice")
            
