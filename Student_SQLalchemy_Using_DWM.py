from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL='mysql://root:NElson@26@localhost:3306/db1'
ENGINE=create_engine(DB_URL)
print("ENgine Created")


Base=declarative_base()
print(Base)

class Student(Base):
      __tablename__='st1'
      rn=Column(Integer, primary_key=True)
      name=Column(String(23))
      marks=Column(Float)

      def __str__(self):
          return f'Roll No: {self.rn}, Name :{self.name}, Marks :{self.marks}'


Base.metadata.create_all(ENGINE)
print("table created")

Session=sessionmaker(bind=ENGINE)
sess=Session()

s1=Student(rn=1, name='abc', marks=10)
#sess.add(s1)
#print("added")

result=sess.query(Student)

for stu in result:
    print(stu)
    
sess.commit()
print("committed")


