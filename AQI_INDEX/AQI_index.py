# importing pandas packages
print("----------------------------------------------------------------------------------------------------------------")
 
print("-----------------WELCOME  TO  AIR QUALITY INDEX INDIA 2015-2020------------------------")
print("--------------------------------------------DEVELOPED  BY------------------------------------------------") 
print("----------------------------------1. XXXXXXXXXXXXXXXXXXX  CLASS-XII ----------------------------") 
print("----------------------------------2.                                 ---------------------------") 
print("----------------------------------3.                                 ---------------------------")
#Importing the excel file using read_excel function of pandas module 
# Show the Air Gas Production Index of India (2015-2020) data post conversion into the dataframe  
dT=pa.read_csv(r"city_day.csv")
print("TOXIC GASES PRODUCTION 2015-2020  \n")
print(dT)
# dA=pa.read_csv(r"a.csv")
# Show the Air Gas Production Index of India (2015-2020) data post conversion into the dataframe  
# print("\n AIR QUALITY INDEX INDIA 2015-2020  \n")
# print(dA)
# User-Interactive Display of Extracted Information
print("Choose and Enter A Number  between  1  and  10  To See \n ")
print("The Total Toxic Gases Produced  Year Wise  --1 \n ") 
print("The Total Toxic Gases Produced City Wise --2 \n") 
print("Each Category of Toxic Gases Produced  Year Wise –3 \n") 
print("Each Category of Toxic Gases Produced  City  Wise -4 \n")
print("A particular toxic gas produced as per your choice City Wise -5 \n")
print("A particular toxic gas produced as per your choice Year wise -6 \n")
#Give next choice for showing  average production of each category of gases ( coding like sum)
#Give next choice for showing  the lowest and the  highest produced gases in each category using maximum and minimum
#Give next choices for plotting for comparison ( choice 3 , choice 4 , average choice 7 )

#Here user will input his/her chosen number
choice=input("Enter  the   number   of  your   choice  ( Between 1  to 10 ) :-  ")
if  choice  ==  '1'  :
    print(  "  The Total Toxic Gases Produced  Year Wise   = ") 
    a=dT.groupby(['Date','City'])['NO2'].sum() 
    print(a)
elif choice == '2':
    print(" \n The Total Toxic Gases Produced City Wise  = ")
    b=dT.groupby(['City'])['NO2','CO','SO2'].sum() 
    print(b)
elif choice == '3':
    print("\n Each Category of Toxic Gases Produced  Year Wise  = ")
    c=dT.groupby(['Date'])['NO2'].sum() 
    d=dT.groupby(['Date'])['CO'].sum()
    e=dT.groupby(['Date'])['SO2'].sum()
    print("\n NO2 PRODUCED  = ", c )
    print("\n CO PRODUCED  = ", d )
    print("\n SO2 PRODUCED  = ", e )
elif choice == '4':
    print("Each Category of Toxic Gases Produced  City Wise  = ")
    f=dT.groupby(['City'])['NO2'].sum() 
    g=dT.groupby(['City'])['CO'].sum()
    h=dT.groupby(['City'])['SO2'].sum()
    print("\n NO2 PRODUCED  = ", f )
    print("\n CO PRODUCED  = ", g )
    print("\n SO2 PRODUCED  = ", h )
elif choice == '5':
    print("A particular toxic gas produced as per your choice City Wise -5  \n")
    gas=input("Enter the Number for a Toxic Gas of your choice as  1 - CO / 2 - SO2 / 3 - NO2 : -- ")
    if gas == '1':
        i=dT.groupby(['City'])['CO'].sum() 
        print("The Total of CO Produced City Wise  = ", i)
    elif gas == '2':
        i=dT.groupby(['City'])['SO2'].sum() 
        print("The Total of SO2 Produced City Wise  = ", i)
    #.code like wise for gas = 3
#.Code like wise for choice = 6 , 7 , 8 & 9 

print("The Graphical Comparison of  Total Toxic Gases Produced  - 10 \n")
# importing matplotlib packages

import  matplotlib.pyplot  as  plt
c=(dT['NO2'].sum() )
d=(dT['CO'].sum())
e=(dT['SO2'].sum())
x=[c,d,e]
y=['NO2', 'CO2', 'SO2']
plt.bar(y,x)
plt.title('Comparison of  Total Toxic Gases Produced', color='red') 
plt.xlabel("Gases",  color='red',  fontsize=13)
plt.ylabel ('Status', color='red', fontsize=13) 
plt.show()
