'''
Create CSV file for product selling for 6 Months ( Prod_No | Prod_Name | Jan | Feb | Mar | Apr | May | Jun) for 5 products.
Perform following operations.
'''
import csv
import pandas as pd
header=['Prod_No' , 'Prod_Name' , 'Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun']
rows=[['P01','Nvidea Graphics cards',1500,30000,14000,15700,14000,13500],
      ['P02','MSI Graphics cards',16000,13000,14000,15700,14000,35000],
      ['P03','CPU cooler',6000,13000,4000,15700,14000,9000],
      ['P04','SSD',18000,13000,14000,15700,14000,13500],
      ['P05','HDD',16000,13000,8000,15400,15000,11500]]
with open("E:\\22BCA01\\python\\product.csv",'w',newline='') as write_file:
    records=csv.writer(write_file)
    records.writerow(header)
    records.writerows(rows)
# 1. Add 12 Records. Take input from user.
with open("E:\\22BCA01\\python\\product.csv",'r') as read_file:
    filedata=csv.reader(read_file)
    data=list(filedata)
with open("E:\\22BCA01\\python\\product.csv",'w',newline='') as write_file:
    insert_records=csv.writer(write_file)
    print("Enter product information:\n")
    for i in range(12):
        print("Product -{}".format(i+1))
        prod_no=input("Product no.:")
        prod_name=input("Product name:")
        print("Sells Information(In Months):")
        jan=int(input("January: "))
        feb=int(input("February: "))
        march=int(input("March: "))
        april=int(input("April: "))
        may=int(input("May: "))
        june=int(input("June: "))
        Prod_info=[prod_no,prod_name,jan,feb,march,april,may,june]
        data.append(Prod_info)
    insert_records.writerows(data)
# 2. Create dataframe.
df=pd.read_csv("E:\\22BCA01\\python\\product.csv",header=0)
# 3. Change Column Name Product No, Product Name, January, February, March, April, May, June.
new_header=['Product_NO','Product_Name','January','February','March','April','May','June']
df=df.set_axis(new_header, axis='columns')
# 4. Add column "Total Sell" to count total of all month and "Average Sell"
df['Total Sell']=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
df['Average Sell']=df['Total Sell']/6
df
# 5. Add 2 row at the end.
df.loc[17]= ['P18', 'Power Supply Unit',12000,7000,7400,4300,12000,7000,49700,8283.33]
df.loc[18]= ['P19', 'USB',2000,1100,2200,2300,2100,1800,11500,1916.67]
# 6. Add 2 row after 3rd row.
df.loc[2.5]=['P20','Type-C cable',5000,5000,5000,5000,5000,5000,30000,5000]
df.loc[2.6]=['P21','Network Card',6000,6000,6000,6000,6000,6000,36000,6000]
df=df.sort_index().reset_index(drop=True)
df
# 7. Print first 5 row.
df.head()
# 8. Print Last 5 row.
df.tail()
# 9. Print row 6 to 10.
df.loc[6:10]
# 10. Print only product name.
df['Product_Name']
# 11. Print sell of January month with product id and product name.
df[['January','Product_NO','Product_Name']]
# 12. Print only those product id , product name where january sell is > 5000 and February sell is >8000
print(df[(df["January"] > 5000) & (df["February"] > 8000)][["Product_NO", "Product_Name"]])
# 13. Print record in sorting order of Product name.
sorted_name=df.sort_values(by='Product_Name')
sorted_name
# 14. Display only odd index number column record.
df.loc[1::2]
# 15. Display alternate row.
df.loc[::2]
