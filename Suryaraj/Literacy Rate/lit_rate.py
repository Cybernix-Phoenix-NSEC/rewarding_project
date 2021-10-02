#Project Name       : LITERACY RATE ANALYSIS SYSTEM of INDIA 
#Owner              : SURYARAJ BARANWAL


#Importing Necessary Modules
import pandas as pd
import time
import matplotlib.pyplot as plt

#Project Title
print("-------------------------------")
print("LITERACY RATE ANALYSIS OF INDIA")
print("-------------------------------")


#Introduction
msg ='''\nEducation is the foremost important tool for change of the
society and betterment of nation. Better education and literacy
prompt a more noteworthy mindfulness and furthermore contributes
in enhancement of economical and social conditions.

\nMinistry of Human Resource Development  releases a data on literacy
which can be exceptionally valuable in examining different elements
influencing education rate of a state or an area.

\nLiteracy also provides better employment prospects and gives a
higher socio-economic status. Increased literacy rate also leads
to decreased population growth rate and thus a country's
resources better shared among less people.

\nCensus of India pegged average literacy rate to be 74.4% in 2011
while National Statistical Commission surveyed literacy to be
77.7% in 2017–18.

\nThe data used is between year 1951 and year 2011

\nThe data used is as per the census released by government
every 10 years; so please, whenever a year is asked use from these
1951,1961,1971,1981,1991,2001,2011

\n**********************************
Thank You For Evaluating Our Project
**********************************\n
''' 
for x in msg:
    print(x, end='')
    time.sleep(0.002)
wait = input('Press enter key to continue.....')


print("\n\n--------------------------------------")
print("LITERACY RATE ANALYSIS SYSTEM OF INDIA")
print("--------------------------------------")
while True:
    print("\n\n\n><><><><><><><><><><")
    print("Main Menu:======--->")#Menu to choose what to be done
    mainmenu='''\n1. Read CSV/Excel File
              \n2. Data Analysis
              \n3. Data Manipulation
              \n4. Data Visualisation
              \n5. Export Data
              \n6. EXIT'''
    print(mainmenu)#This will print the visual menu
    cho=int(input("\nEnter your choice :-- "))



#For Reading CSV/Excel file:----
    
    if cho==1:
        print("\n\nREADING CSV/EXCEL FILE")
        print("***********************")
        #Sub-Menu of Reading CSV/Excel file
        print('''\n1. Read Excel File to create and Display DataFrame
                \n2. Read CSV File to create and Display DataFrame
                \n3. To use self-imported dataset
                \n4. GO TO MAIN MENU''')
        ch1=int(input("\nEnter your choice: "))
        if ch1==2:  #For Reading CSV File to create and Display DataFrame
            filename=input("Enter the file name with extension .CSV  : ")
            df=pd.read_csv(filename)
            print(df)
            print("\nFile retrieved successfully!!")
        elif ch1==1:  #For Reading Excel File to create and Display DataFrame
            filename=input("Enter the file name with extension .XLSX  : ")
            df=pd.read_excel(filename)
            print(df)
            print("\nFile retrieved successfully!!")
        elif ch1==3: #For using pre_existing dataset
            df=pd.read_excel([Your file location])
            print(df)
            print("\nFile retrieved successfully!!")
        elif ch1==4: #This will print Visual Menu
            pass
        else: # If the Number choosed is not an option
            print("xxxxxxxxxxxxxx")
            print("INVALID CHOICE")
            print("xxxxxxxxxxxxxx")



# For Data Analysis of the imported Dataframe:----

    elif cho==2: 
        print("\n\nDATA FRAME ANALYSIS")
        print("********************")
        #Sub-Menu of Data Analysis
        print('''\n1. To dislay Top record(s)
                \n 2. To display Bottom record(s)
                \n 3. To display Literacy Rate of a Particular Year
                \n 4. To display Literacy Rate of Numerous Years
                \n 5. To display States with Literacy Rate >= n% in a year
                \n 6. To display states with Maximum Literacy Rate
                \n 7. To display Average Literacy of India
                \n 8. To display complete statistics of the dataframe
                \n 9. To display complete information about dataframe
                \n 10. To find Maximum, Minimum and Average Literacy Rate in a Year
                \n 11. GO TO MAIN MENU''')
        ch2=int(input("\nEnter your choice:  "))
        if ch2==1: #For dislaying Top record(s)
            n=int(input("Enter the number of records to be displayed : "))
            print("Top",n,"records from the dataframe")
            print(df.head(n))
        elif ch2==2: #For displaying Bottom record(s)
            n=int(input("Enter the number of records to be displayed : "))
            print("Bottom",n,"records from the dataframe")
            print(df.tail(n))
        elif ch2==3: #For displaying Literacy Rate of a Particular Year
            print("Name of the columns\n",df.columns)
            col=eval(input("Enter the year whose literacy rate to be displayed : "))
            print(df[col])
        elif ch2==4: #For displaying Literacy Rate of Numerous Years
            print("Name of the columns\n",df.columns)
            col=eval(input("Enter the years as list in square bracket like [1951,2001,..] : "))
            print(df[col])
        elif ch2==5: #For displaying States with Literacy Rate >= n% in a year
            yr=int(input("Enter Year   :    "))
            n=float(input("Enter Percentage  :  (%)"))
            df1=df.loc[(df[yr]>n)]
            df1=df1.sort_values(by=yr,ascending=False)
            print(df1)
        elif ch2==6: #For displaying states with Maximum Literacy Rate
            yr=int(input("Enter Year   :    "))
            print()
            print("State with maximum Literacy in the year-",yr)
            x=df[yr].max()
            print(df.loc[(df[yr]==x)])
        elif ch2==7: # For displaying Average Literacy of India
            print("Average Literacy of India :--")
            x=df.mean()
            print(x)
        elif ch2==8: # For displaying complete statistics of the dataframe
            print("Complete Statistics :--")
            print(df.describe())
        elif ch2==9: # For displaying complete information about dataframe
            print("Information about dataframe :--")
            print(df.info())
        elif ch2==10: # For finding Maximum, Minimum and Average Literacy Rate in a Year
            yr=int(input("Enter Year   :    "))
            print("\nMaximum Literacy: ")
            x=df[yr].max() #This will give Maximum Rate
            print(df.loc[(df[yr]==x)])
            print("===========")
            print("Minimum Literacy: ")
            y=df[yr].min() #This will give Minimum Rate
            print(df.loc[(df[yr]==y)])
            avg=df[yr].mean() #This will give Average Rate 
            print("===========")
            print("Average Literacy in the year",yr,"in INDIA=",avg)
        elif ch2==11: #This will print Visual Menu
            pass
        else: # If the Number choosed is not an option
            print("xxxxxxxxxxxxxx")
            print("INVALID CHOICE")
            print("xxxxxxxxxxxxxx")



#For Data Manipulation of the imported DataFrame:----

    elif cho==3:
        print("\n\nDATA FRAME MANIPULATION")
        print("***********************")
        #Sub-Menu of Data Manipulation
        print('''\n1. Insert a Row
                 \n2. Insert a Column
                 \n3. Delete a Row
                 \n4. Delete a Column
                 \n5. Update a Cell Value
                 \n6. GO TO MAIN MENU''')
        ch3=int(input("\nEnter your choice: "))
        if ch3==1: #For inserting a new Row
            df1=pd.DataFrame()
            col=df.columns
            print(col)
            print(df.head(1))
            j=0
            lst=[]
            lst1=eval(input("Enter a list of values in the sequence of columns: "))
            print(lst1)
            s1=pd.Series(lst1,index=df.columns)
            df1=df.append(s1,ignore_index=True)
            print("\nNew row inserted\n")
            print(df1)
        elif ch3==2: #For inserting a new Column
            n=int(input("Total Number Of States/UTs: "))
            yr=int(input("Enter Year of Literacy : "))
            lst_literacy=[]
            for i in range(n):
                lrate=float(input("Enter literacy rate : "))
                lst_literacy.append(lrate)
            df[yr]=lst_literacy
            print("New Column Insertd\n")
            print(df)
        elif ch3==3: #For deleting an existing Column
            print("List of States-\n",df['State/ UTs'])
            n=int(input("Enter the index number of the State for row deletion :"))
            ch=input("\nDo you really want to delete  this row (y/n)?")
            if ch=='y' or ch=='Y':
                df.drop(index=n,inplace=True)
                print(df)
                print("Row of index no- ",n,"deleted successfully!!!")
            else:
                pass
        elif ch3==4: #For deleting an existing Row
            print(df.columns)
            col=int(input("Enter column name to be deleted from the above : "))
            ch=input("\nDo you really want to delete  column(y/n)?")
            if ch=='y' or ch=='Y':
                del df[col]
                print("Column- ",col,"deleted successfully!!!")
                print(df)
            else:
                pass
        elif ch3==5: #For updating a cell value
            print(df)
            row_idx=int(input("Enter row index for edit : "))
            col_idx=int(input("Enter column label/index for edit : "))
            x=df.loc[row_idx,col_idx]
            ch=input("\nDo you really want to overwrite the value of selected cell(y/n)?")
            if ch=='y' or ch=='Y':
                val=eval(input("Enter new value : "))
                df.loc[row_idx,col_idx]=val
                print("\nValue overwritten Successfully!!!")
                print(df)
            else:
                pass
        elif ch3==6: #This will print Visual Menu
            pass
        else: # If the Number choosed is not an option
            print("xxxxxxxxxxxxxx")
            print("INVALID CHOICE")
            print("xxxxxxxxxxxxxx")



#For Data Visualisation of imported DataFrame:----

    elif cho==4:
        print("\n\nDATA VISUALISATION")
        print("******************")
        #Sub-Menu of Data Visualisation 
        print("\n1. Line Chart of a Particular Year")
        print("2. Bar Chart for different Years")
        print("3. Histogram for a Year")
        print("4. Line Chart for Average Literacy Rate (Year wise)")
        print("5. GO TO MAIN MENU")
        ch4=int(input("\nEnter your choice:"))
        if ch4==1: #For displaying a line chart of a particular year of states
            year=int(input("Enter Year of Literacy : "))
            df1=df.sort_values(by=[year],ascending=False)
            n=int(input("Enter number of states (1-34) : "))
            print(df1.head(n))
            df1.plot(x ='State/ UTs', y=year, kind = 'line',rot=75)
            plt.xlabel("State/UT Name-->", color='b',fontsize=12)
            plt.ylabel("Literacy Rate (%)-->", color='b',fontsize=12)
            plt.title("Indian State(s) Literacy Analysis ") 
            plt.show()
        elif ch4==2: #For displaying a bar chart of different years
            year=eval(input("Enter Year of Literacy as list like[1951,2011]: "))
            n=int(input("Enter number of states (1-34) : "))
            print(df.head(n))
            df1=df.head(n)
            df1.plot(x='State/ UTs',y=year,kind='bar',rot=75)
            plt.xlabel("State/UT Name-->", color='r',fontsize=12)
            plt.ylabel("Literacy Rate (%)-->", color='r',fontsize=12)
            plt.title("Indian State(s) Literacy Analysis (Bar Graph)") 
            plt.show()
        elif ch4==3: #For displaying a histogram of a particular year
            year=int(input("Enter Year of Literacy : "))
            df.hist(column=year,color='r',edgecolor='black')
            plt.xlabel("Literacy Rate (%)-->", color='r',fontsize=12)
            plt.ylabel("No. of States -->", color='r',fontsize=12)
            plt.title("All Indian State(s) Literacy Analysis of \nYear-") 
            plt.show()
        elif ch4==4: #For displaying a line chart of average literacy of india per year
            print("Line Chart for Average Literacy Rate('INDIA')") 
            s1=df.mean()
            mylabel=s1.index
            plt.plot(mylabel,s1.values,linestyle='dashed',linewidth=3,color='r',
                     marker='o',mfc='b',ms=10)
            plt.xlabel("Year-->", color='b',fontsize=12)
            plt.ylabel("Literacy Rate (%) of India -->", color='b',fontsize=12)
            plt.title("India's Average Literacy Rate Analysis - 1951 to 2011") 
            plt.grid()
            plt.show()
        elif ch4==5: #This will print Visual Menu
            pass
        else: # If the Number choosed is not an option
            print("xxxxxxxxxxxxxx")
            print("INVALID CHOICE")
            print("xxxxxxxxxxxxxx")



#For exporting data to other formats:----

    elif cho==5:
        print("\n\nEXPORTING DATA")
        #Sub-Menu for Exporting Data
        print("**************")
        print('\n1. CSV File')
        print('2. Excel File')
        print('3. GO TO MAIN MENU')
        ch5=int(input('\nEnter your Choice : '))
        if ch5==1:
            df.to_csv([Your file location])
            print('\n\nCheck your new file "literacy_rate.csv"  on D: Drive ,Folder SURYA')
        elif ch5==2:
            df.to_excel([Your file location])
            print('\n\nCheck your new file "literacy_rate.xlsx"  on D: Drive, Folder SURYA')
        elif ch5==3: #This will print Visual Menu
            pass
        else: # If the Number choosed is not an option
            print("xxxxxxxxxxxxxx")
            print("INVALID CHOICE")
            print("xxxxxxxxxxxxxx")
            


#For Exiting from the program:----

    elif cho==6:
        t=input("Do you really want to exit?(y/n)")
        if t=='n' or t=='N':
            pass
        elif t=='Y' or t=='y':
            print("\n\nTHANK YOU FOR EVALUATING ! :)")
            break
        else: # If the Number choosed is not an option
            print("xxxxxxxxxxxxxx")
            print("INVALID CHOICE")
            print("xxxxxxxxxxxxxx")
    else: # If the Number choosed is not an option
        print("xxxxxxxxxxxxxx")
        print("INVALID CHOICE")
        print("xxxxxxxxxxxxxx")



#Termination of Program/Project:----

print("\nHOPE U LIKED IT!!")
print("\n\n******************************************************************")
            
    



            
