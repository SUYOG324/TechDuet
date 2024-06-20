create database Flipkart;

create table Flipkart.Users
(
UserID int,
UNAME varchar(50),
Phone int
)
insert into Flipkart.Users(UserID,UNAME,Phone) values(1,'sam',1234567890);
insert into Flipkart.Users(UserID,UNAME,Phone) values(2,'Ram',0987654321);
insert into Flipkart.Users(UserID,UNAME,Phone) values(3,'ravi',1234567899);
create table Flipkart.categories
(
ID int,
categoryname varchar(50),
PcatID int,
avail varchar(50)
)

insert into Flipkart.categories(ID,categoryname,PcatID,avail) values(856,'electronic',542,'avail');
insert into Flipkart.categories(ID,categoryname,PcatID,avail) values(866,'clothing',442,'avail');
insert into Flipkart.categories(ID,categoryname,PcatID,avail) values(256,'grocery',242,'unavail');
create table Flipkart.product
(
ID int,
Pname varchar(50),
catID int,
price float, 
Quantity int,
avail varchar(50)
)

insert into Flipkart.product(ID,Pname,catID,price,Quantity,avail) values(875,'laptop',4528,21000,956,avail);
insert into Flipkart.product(ID,Pname,catID,price,Quantity,avail) values(975,'book',4728,1000,56,avail);
insert into Flipkart.product(ID,Pname,catID,price,Quantity,avail) values(665,'chairs',2228,2000,56,avail);
create table Flipkart.productvarient
(
ID int,
PID int,
color varchar(50),
size int,
price float,
Quantity int
)

insert into Flipkart.productvarient(ID,PID,color,size,price,Quantity) values(985,5462,'black',7,450,98);
insert into Flipkart.productvarient(ID,PID,color,size,price,Quantity) values(685,4462,'black',7,350,68);
insert into Flipkart.productvarient(ID,PID,color,size,price,Quantity) values(985,5462,'brown',17,250,18);
create table Flipkart.Carts
( 
ID int,
UserID int,
PID int,
PVID int,
Quantity int

)

insert into Flipkart.Carts(ID,UserID,PID,PVID,Quantity) values(1,2,3,4,5);
insert into Flipkart.Carts(ID,UserID,PID,PVID,Quantity) values(6,7,8,9,10);
insert into Flipkart.Carts(ID,UserID,PID,PVID,Quantity) values(11,12,13,14,15);
create table Flipkart.shippingaddress
(
ID int,
UserID int,
Fulladdress varchar(50),
Pincode int,
State varchar(50)
)

insert into Flipkart.shippingaddress(ID,UserID,Fulladdress,Pincode,State) values(19,20,'g20 linkroad',425863,'goa');
insert into Flipkart.shippingaddress(ID,UserID,Fulladdress,Pincode,State) values(25,30,'l50 rajroad',475853,'kerla');
insert into Flipkart.shippingaddress(ID,UserID,Fulladdress,Pincode,State) values(29,32,'pharmaroad',412453,'punjab');
create table Flipkart.order
(
OID int,
Quantity int
)

insert into Flipkart.order(OID,Quantity) values(456,48);
insert into Flipkart.order(OID,Quantity) values(556,68);
insert into Flipkart.order(OID,Quantity) values(656,78);
create table Flipkart.Orderitems
(
ID int,
OID int,
PID int,
PVID int,
PNAME varchar(50),
Color varchar(50),
Size int,
Price float,
Quantity int,
Totalamount float
)

insert into Flipkart.Orderitems(ID,OID,PID,PVID,PNAME,Color,Size,Price,Quantity,Totalamount) values(34,852,7410,74569,'shoes','black',9,15000,65,17000);
insert into Flipkart.Orderitems(ID,OID,PID,PVID,PNAME,Color,Size,Price,Quantity,Totalamount) values(44,952,8310,94569,'shoes','white',5,11000,93,15000);
insert into Flipkart.Orderitems(ID,OID,PID,PVID,PNAME,Color,Size,Price,Quantity,Totalamount) values(54,102,4310,98569,'shoes','blue',11,19000,45,22000);
create table Flipkart.wishlist
(
ID int,
UserID int,
PID int,
PVID int
)

insert into Flipkart.wishlist(ID,UserID,PID,PVID) values(65,68795,9854,4128);
insert into Flipkart.wishlist(ID,UserID,PID,PVID) values(55,58795,7854,3128);
insert into Flipkart.wishlist(ID,UserID,PID,PVID) values(25,28795,5654,2928);