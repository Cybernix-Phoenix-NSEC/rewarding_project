import pandas as pd
import time
import matplotlib.pyplot as plt

df = pd.DataFrame()
csv_file = "D:/covid19_cases.csv"


def introduction():
    msg = '''
          The world is perplexed by the outbreak of a new severe acute respiratory syndrome.
          the new coronavirus(COVID-19), reported in December 2019, had its epicentre in Wuhan,
          Hubei province, in The People's Republic Of China and has spread to several countries.
          It was declared as a public health emergency by the World Health Organisation.
           
          We got this dataset from a website with the URL as https://worldometers.info/coronavirus.
          
          Now, this dataset consists of the statistical data of 188 countries of the world regarding
          the number of confirmed cases, the deaths and the recoveries and other related information.

          In this project we are going to analyse the same dataset using Python Pandas on windows machine
          but the project can be run on any machine support Python and Pandas. Besides pandas we also used 
          matplotlib python module for visualization of this dataset. 

          The whole project is divided into four major parts ie reading, analysis, visualization and export.
          All these part are further divided into menus for easy navigation.

          NOTE: Python is case-SENSITIVE so type exact Column Name wherever required.\n\n\n\n'''
    for x in msg:
        print(x, end='')
        time.sleep(0.02)
    wait = input('Press any key to continue.....')

    

def made_by():
    msg = ''' 
            COVID-19 CASES ANALYSIS made by :
            Name                            : Suryaraj Baranwal
            Roll Number                     : 38
            School Name                     : Delhi Public School
            Session                         : 2020-21
            
            Thanks for evaluating my Project.
            \n\n\n
        '''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')


def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen


def clear():
    for x in range(65):
               print()


def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nD A T A   A N A L Y S I S   M E N U  ')
            print('_'*100,'\n')
            print('1.   Show Whole DataFrame')
            print('2.   Show Columns')
            print('3.   Show Top Rows')
            print('4.   Row Bottom Rows')
            print('5.   Show Specific Column')
            print('6.   Add a New Record')
            print('7.   Add a New Column')
            print('8.   Delete a Column')
            print('9.   Delete a Record')
            print('10.  Data Summery')
            print('11.  Exit (Move to main menu)')
            ch = int(input('\n\nEnter your choice:'))
            if ch == 1:
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 2:
                print(df.columns)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 6:
                a = input('Enter Country :')
                b = input('Enter Confirmed cases :')
                c = input('Enter Deaths :')
                d = input('Enter Recoveries :')
                e = input('Enter Active cases :')
                f = input('Enter New Cases :')
                g = input('Enter New Deaths :')
                h = input('Enter New Recoveries :')
                i = input('Enter Deaths/100 Cases :')
                j = input('Enter Recovered/100 Cases :')
                k = input('Enter Deaths/100 Recovered :')
                l = input('Enter Confirmed cases of last week :')
                m = input('Enter 1 week change :')
                n = input('Enter 1 week % increase :')
                o = input('Enter WHO Region :')


                data = {'Country': a, 'Confirmed': b, 'Deaths': c,
                        'Recovered': d, 'Active': e, 'New_Cases': f, 'New_Deaths': g,
                        'New_recovered':h,'Deaths/100_Cases':i,'Recovered/100_Cases':j,
                        'Deaths/100_Recovered':k,'Confirmed_Last_Week':l,'1_week_change':m,
                        '1_week_%_increase':n,'WHO_Region':o}
                
                df = df.append(data, ignore_index=True)
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')

            if ch == 7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name] = col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 8:
                col_name = input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 9:
                index_no = int(
                    input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 10:
                print(df.describe())
                print("\n\n\nPress any key to continue....")
                wait = input()

            if ch == 11:
                break

# name of function      : graph
# purpose               : To generate a Graph menu

def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('1.  LINE graph for region wise confirmed cases\n')
        print('2.  LINE graph for region wise death counts\n')
        print('3.  BAR Graph for region wise recovered cases\n')
        print('4.  BAR Graph for region wise active cases\n')
        print('5.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            g = df.groupby('WHO_Region')
            x = df['WHO_Region'].unique()
            y = g['Confirmed'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('REGION')
            plt.ylabel('NUMBER OF CONFIRMED CASES')
            plt.title('REGION WISE CONFIRMED CASES')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()

        if ch == 2:
            g = df.groupby('WHO_Region')
            x = df['WHO_Region'].unique()
            y = g['Deaths'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('REGION')
            plt.ylabel('NUMBER OF DEATHS')
            plt.title('REGION WISE DEATH CASES')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()
            wait = input()

        if ch == 3:
            g = df.groupby('WHO_Region')
            x = df['WHO_Region'].unique()
            y = g['Recovered'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('REGION')
            plt.ylabel('NUMBER OF RECOVERED CASES')
            plt.title('REGION WISE RECOVERED CASES')
            plt.grid(True)
            plt.bar(x, y)  #bar graph
            plt.show()
            wait = input()

        if ch == 4:
            g = df.groupby('WHO_Region')
            x = df['WHO_Region'].unique()
            y = g['Active'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('REGION')
            plt.ylabel('NUMBER OF ACTIVE CASES')
            plt.title('REGION WISE ACTIVE CASES')
            plt.grid(True)
            plt.bar(x, y)  #bar graph
            plt.show()

        if ch == 5:
            break

# function name          : export_menu
# purpose                : function to generate export menu

def export_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*100)
        print()
        print('1.  CSV File\n')
        print('2.  Excel File\n')
        print('3.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))

        if ch == 1:
            df.to_csv('D:/COVID-19_upgraded.csv')
            print('\n\nCheck your new file "COVID-19_upgraded.csv"  on D: Drive.....')
            wait = input('\n\n\n Press any key to continue.....')

        if ch == 2:
            df.to_excel('D:/COVID-19_upgraded.xls')
            print('\n\nCheck your new file "COVID-19_upgraded.xls"  on D: Drive.....')
            wait = input('\n\n\n Press any key to continue.....')

        if ch == 3:
            break
def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('4.  Export Data\n')
                      print('5.  Exit\n')
                      choice = int(input('Enter your choice :'))

                      if choice == 1:
                                read_csv_file()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 2:
                                data_analysis_menu()
                                wait = input('\n\n Press any key to continue....')

                      if choice == 3:
                                graph()
                                wait = input('\n\n Press any key to continue....')
                      if choice == 4:
                                export_menu()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 5:
                                 break
           clear()
           made_by()


# call your main menu
main_menu()



            


         

