import pyodbc

newtable = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=xxy;UID=sa;PWD=azmiao')
cursor = newtable.cursor()

#建表
cursor.execute("""
                if objectproperty(OBJECT_ID(N'book'),'IsTable')=1    
                    drop table book
                    Create Table book
                    (
                        bno char(10) primary key,
                        bname nvarchar(20),
                        writer nvarchar(20),
                        chubandate date,
                        price float,
                        banci int,
                        type nvarchar(20)
                    )
               """)#图书信息表

cursor.execute("""
                if objectproperty(OBJECT_ID(N'ruku'),'IsTable')=1    
                    drop table ruku
                    Create Table ruku
                    (
                        bno char(10) primary key,
                        rukudate date,
                        num int,
                        depname nvarchar(20)
                    )
               """)#入库信息表

cursor.execute("""
                if objectproperty(OBJECT_ID(N'sell'),'IsTable')=1    
                    drop table sell
                    Create Table sell
                    (
                        bno char(10) primary key,
                        sellnum int,
                        sellcheck int
                    )
               """)#稿费信息表

cursor.execute("""
                if objectproperty(OBJECT_ID(N'book_admin'),'IsTable')=1    
                    drop table book_admin
                    Create Table book_admin
                    (
		                admin_id nvarchar(20) NOT NULL,
		                admin_pass nvarchar(20) DEFAULT NULL,
		                primary key (admin_id)
		            )
               """)#管理员信息表

cursor.execute("""
                if objectproperty(OBJECT_ID(N'book_writer'),'IsTable')=1    
                    drop table book_writer
                    Create Table book_writer
                    (
		                writer_id nvarchar(20) NOT NULL,
		                writer_pass nvarchar(20) DEFAULT NULL,
		            )
               """)#作者信息表

#插入数据
cursor.execute("""
               insert into book values ('A10001','自然科学','李华','2010-01-02','28','5','H1');
               insert into book values ('A11238','数据计算','张三','2012-11-21','32','2','D1');
               insert into book values ('B10026','统计设计','张越','2020-01-28','20','1','D1');
               insert into book values ('C14188','过程分析','张三','2008-12-31','19','7','D1');
               insert into book values ('C12686','数据结构分解','贾路','2018-05-30','25','5','M2');
               insert into book values ('C11238','优化演算','陈前','2017-03-03','40','2','K4');
               insert into book values ('D18615','金融学','叶伟','2012-11-05','19','5','B1');
               insert into book values ('E10256','工程学','王五','2016-09-10','20','3','E3');
               insert into book values ('F12560','西方经济论','曹泽','2019-02-28','26','5','B1');
                """)#插入书的信息

cursor.execute("""
               insert into ruku values ('A10001','2010-01-30','5000','仓库01');
               insert into ruku values ('A11238','2012-12-10','5000','仓库01');
               insert into ruku values ('B10026','2020-03-01','3000','仓库01');
               insert into ruku values ('C14188','2009-01-15','10000','仓库01');
               insert into ruku values ('C12686','2018-06-26','5000','仓库02');
               insert into ruku values ('C11238','2017-03-19','4000','仓库02');
               insert into ruku values ('D18615','2012-11-30','5000','仓库01');
               insert into ruku values ('E10256','2016-09-29','5000','仓库02');
               insert into ruku values ('F12560','2019-03-20','5000','仓库01');
                """)#插入入库信息

cursor.execute("""
               insert into sell values ('A10001','4500','6750');
               insert into sell values ('A11238','4500','9000');
               insert into sell values ('B10026','3000','3300');
               insert into sell values ('C14188','9000','19800');
               insert into sell values ('C12686','5000','8500');
               insert into sell values ('C11238','2500','5750');
               insert into sell values ('D18615','4000','3600');
               insert into sell values ('E10256','4500','7200');
               insert into sell values ('F12560','5000','6500');
               """)#插入销售信息

cursor.execute("""
               insert into book_admin values ('admin','admin')
               """)#插入管理员信息

cursor.execute("""
               insert into book_writer values ('李华','lihua');
               insert into book_writer values ('张三','zhangsan');
               insert into book_writer values ('张越','zhangyue');
               insert into book_writer values ('贾路','jialu');
               insert into book_writer values ('陈前','chenqian');
               insert into book_writer values ('叶伟','yewei');
               insert into book_writer values ('王五','wangwu');
               insert into book_writer values ('曹泽','caoze');
                """)#插入作者的信息

cursor.commit()
cursor.close()