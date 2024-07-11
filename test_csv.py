import csv  
file_path = "MOCK_DATA.csv"
file = open(file_path,"r")
csv_reader = csv.reader(file) # create reader
header = next(csv_reader) # header : ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address']
print(header)
for row in csv_reader:
    print(row)
    print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]} : ") # ['1', 'Morrie', 'Volett', 'mvolett0@squarespace.com', 'Male', '85.80.229.90']
file.close()

with open(file_path,"a") as file : # With :- used to open-file and auto Close-file 
 csv_write = csv.writer(file) # Create Write
 new_row = ['11', 'Hassan', 'Mohamed', 'Hassan554@who.int', 'Male', '186.79.27.94']
 new_row2 = ['12', 'Ahmed', 'Hassan', 'Ahmed666@who.int', 'Male', '186.79.27.94']
 print(new_row) # ['11', 'Hassan', 'Mohamed', 'Hassan554@who.int', 'Male', '186.79.27.94']
 print(new_row2) # ['12', 'Ahmed', 'Hassan', 'Ahmed666@who.int', 'Male', '186.79.27.94']


