
#This is US bike share Project
#Importing necessary packages
import numpy as np
import pandas as pd
import datetime
import timeit
import time

search=['CITY','MONTH','DAY','FILTER']
history=[] # This list it maitained to record all the operations done by the user

dx=pd.DataFrame(columns=search)#All the recored data in list is loaded into dataframe


pd.options.mode.chained_assignment = None#to manage exceptions while multiple assignments
'''Maintaining a dictionary called CITY_DATA in order to access the csv files of a respectice city'''
CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }
'''Days represents list of week days'''
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


'''Months represents list of few months'''
months=['January','February','March','April','May','June','July','August']
def calculate(cty,mth,dy,df):
     
    ''' This function performs all the descriptive statistics on the input given by the user .
    
        It has 4 arguments 
        
        1.cty represents city name
        2.mth represents month name
        3.dy represents day name
        4.df is my data frame into which the CSV file of a corresponding city is loaded
        
        These 4 arguments are used in choosing the type of operation or something like that'''
    
    des_mth=mth # Copying the month name into variable des_mth
    des_city=cty # Copying the city name into variable des_city
    des_dy=dy  #Copying the day name into variable des_dy
    Filter_applied=''
    '''The below 4 lines of code of df are used to add extracolumns in the data frame df initially'''
    
    '''The first line represents converting the Start Time column of dataframe into datetime 
    The reason for converting it into  date time module is that we can extract information from the Start time column
    such as month numbers and day of the week names into seperate columns for easy accessing whenever filters are applied'''
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] =df['Start Time'].dt.month
    df['dayofweek'] = df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    
    '''The below code deals with choosing the user's filtering type and  appropirate creations of new data frames'''
    
    '''When i call this function from my main funtion , i will pass -1 if the respective filter is not choosen
    
    For example : if filter choosen is month(January) and city is chicago then my arguments will be  
                    
                  cty="chicago" , mth="January and dy=-1
                  
    Another example : if filter is none and city is washington , then my arguments will be
                  
                  cty="washington" , mth=-1 and dy=-1 '''
        
    '''After copying the argument variables into local variables
        
        if des_mth==-1 and des_dy==-1 ,indicates that there is no Filter(none) since des_mth=-1 and des_dy=-1
        
        if des_mth==-1 and des_dy!=-1 indicates that filter is day since des_mth=-1 and des_dy is other than -1
        
        if des_mth!=-1 and des_dy==-1 indicates that filter is month since des_dy=-1 and des_mth is other than -1
         
        if des_mth!=-1 and des_dy!=-1 indicates that both month and day filters are applied since both are not equal to -1
         
        
        '''
    '''resultant df is my dataframe on which i am going to perform operations'''
    if des_mth==-1 and des_dy==-1:#Filter - none
        resultant_df=df.copy(deep=True)# if no filter is applied then just copy all contents of df to resulant_df
    elif des_mth!=-1 and des_dy==-1:#filter - month
        resultant_df=df[df.month==des_mth]#Selecting rows which has given month value by using boolean technique
    elif des_mth==-1 and des_dy!=-1:#filter - day
        resultant_df=df[df.dayofweek==des_dy]##Selecting rows which has given month value by using boolean technique
    elif des_mth!=-1 and  des_dy!=-1:
        resultant_df=df[(df.month==des_mth )&(df.dayofweek==des_dy)]#Selecting both rows and columns using boolean and (&)
        
    ''' In below few lines of code , Format variable is assigned to type of fiter that has been inputted '''
    
    if des_mth==-1 and des_dy==-1:
        Filter_applied="none"
    elif des_mth!=-1 and des_dy!=-1:
        Filter_applied="both"
    elif des_mth!=-1 and des_dy==-1:
        Filter_applied="month"                                  
    elif des_mth==-1 and des_dy!=-1:
        Filter_applied="day"
        
    '''The below code performs the operations on the data sets.'''
    
    '''The methods used in below code are :'''
    
    '''Count method is used to count the number of data items'''
    
    '''timeit.defaultult timer is used to calculate the timetaken to calculate each statistic'''
    
    '''Value_counts() is used to count the frequncy of items in a column and there by getting maximum value.
       It is the most used function in my code.'''
    
    '''For calculating the popular trip , Start Station and End Station columns are concatinated 
       into another  column named Trip  using map function for easy accessing '''
    
    '''min() is used to get the minimum value , which it is used in getting earliest birthday year'''
    
    '''max() is use to get the maximum value, which it is used in getting the recent birthday year'''
    
    '''Since mean() can give the average , it is used in getting the average trip duration'''
    
    '''sum() is used to get the total trip duration '''
    
    '''The print Statement [Calculating the statistics] represents that a  new statistic is being calculated'''
    
    print("\nCity choosed :",des_city," Format choosen : ",Filter_applied)
    if Filter_applied=="none" or Filter_applied=="both" or Filter_applied=="month" or Filter_applied=="day":
        print("Total number of Trips :",resultant_df['Start Time'].count())#Counts total number of rows in dataframe
        
        '''Calculating the popular month'''
        print("\nCalculating the Statistics...")
        popular_month=months[int(resultant_df['month'].value_counts().idxmax()-1)]
        start_time=timeit.default_timer()
        print("Most Popular Month : ",popular_month," Count : ",resultant_df['month'].value_counts().max(),".")
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n") 
        
        '''Calculating the popular day'''
        print("Calculating the Statistics...")
        start_time=timeit.default_timer()
        popular_day= resultant_df['dayofweek'].value_counts().idxmax()
        print("Most popular day of week :",popular_day,".")
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n") 
        
        '''Calculating the popular hour '''
        print("Calculating the Statistics...")
        start_time=timeit.default_timer()
        popular_hour=(resultant_df['hour'].value_counts().idxmax())
        print("Most popular Hour(24hr-format):",popular_hour,"hrs.")
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n")
        
        '''Calculating the popular start station'''
        print("Calculating the Statistics...")
        start_time=timeit.default_timer()
        print("The most common start station and its frequency:",resultant_df['Start Station'].value_counts()[resultant_df['Start Station'].value_counts() == resultant_df['Start Station'].value_counts().max()])
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n")
        
        '''Calculating the popular endstation'''
        print("Calculating the Statistics...")
        start_time=timeit.default_timer()
        print("The most common End station and its frequency:",resultant_df['End Station'].value_counts()[resultant_df['End Station'].value_counts() == resultant_df['End Station'].value_counts().max()])
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n")
        
        '''Creating a new column which contains the trip details (eg : a to b) .It becomes easy for calculating 
           the popular trip'''
        resultant_df['Trip'] = resultant_df['Start Station'].map(str) +" to "+ resultant_df['End Station']
        '''Calculating popular trip'''
        print("Calculating the Statistics...")
        start_time=timeit.default_timer()
        print("The most common Trip and its frequency:",resultant_df['Trip'].value_counts()[resultant_df['Trip'].value_counts() == resultant_df['Trip'].value_counts().max()])
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n")
        
        '''Calculating the total Trip duration and average trip duration'''
        print("Calculating the Statistics...")
        start_time=timeit.default_timer()
        total_time=resultant_df['Trip Duration'].sum()
        print("Total Time of Trips :",total_time)
        print("Total Average Time of Trips :",resultant_df['Trip Duration'].mean())
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n")
        
        '''Calculating the types of users and their counts'''
        print("Calculating the Statistics...")
        print("Counts of each user type :")
        start_time=timeit.default_timer()
        print(resultant_df['User Type'].value_counts())
        end_time=timeit.default_timer()
        print("The process took : ",end_time-start_time," secs..\n")
        
        
        if des_city!="washington":  # Since washnigton.csv does not ahave Gender data and Birth year data
            
            '''Calculating the Gender distribution'''
            print("Calculating the Statistics...")
            print("Gender distribution :")
            start_time=timeit.default_timer()
            print(resultant_df['Gender'].value_counts())
            end_time=timeit.default_timer()
            print("The process took : ",end_time-start_time," secs..\n")
            
            '''Calculating the Common birth year ,Earliest birth year and Recent birth year'''
            print("Calculating Statistics...")
            start_time=timeit.default_timer()
            print("The most common Birth year and its frequency:",int(resultant_df['Birth Year'].value_counts()[resultant_df['Birth Year'].value_counts() == resultant_df['Birth Year'].value_counts().max()]))
            print("Earliest birth year :",int(resultant_df['Birth Year'].min()))
            print("Recent Birth Year :",int(resultant_df['Birth Year'].max()))
            end_time=timeit.default_timer()
            print("The process took : ",end_time-start_time," secs..\n")
            
def city_name():
    
    '''This function will take the city name as input and returns it to the function which called it.
    
       If the user gives a wrong input ,then it will recursively call itself and asks customer to try again '''
    
    print("\nWould you like to have a glance on data of Newyork or Washington or Chicago?Select your choice.")   
    city=input().lower()
    if city!="chicago" and city!="newyork" and city!="washington":
        print("\nPlease select the valid Input.The input ",city," is invalid input.Please give another try\n")
        return city_name()
    return city
    
def get_filters(f_type):
    
    '''The function get_filters() is used to get the input values of respcetive filter and also manages the 
    
    Wrong inputs given by the user.The function takes month value or day value or both as inputs and converts it into
    
    title case(Since my months and days lists elements are in title case).This function checks the input given by user
    
    and checks whether the values are in the months and days lists accordingly.If the values dont match then it is going 
    
    to recursively call the function again and asks usert to give correct input .This function takes filter type as 
    
    argument and returns the month number and day names to the function which called get_filters() function.'''
    index=0
    m=''
    d=''
    index1=0
    if f_type=="month":
        print("\nEnter month")
        m=input().title()#Inputs month name since filter is month
        if m not in months:
            print("Please give valid input")
            return get_filters("month")
        return int(months.index(m))+1
    
    elif f_type=="day":
        print("\nEnter day of the week , eg.Sunday...etc",)
        d=input().title()#Converting it into title case
        if d not in days:
            print("Please give valid input")
            return get_filters("day")
        return d
    
def get_filter_type():
    
    '''The function is used to get filter type.If the input given is wrong then it recursively calls the process
    
       with an error message'''
    print("\nWould you like to filter the data by month or day or both? If you dont want any filters select none")
    
    dat=input() #The variable dat takes input filter and returns the value to main() function.
    
    if dat!="month" and dat!="day" and dat!="none" and dat!="both":
        print("\nPlease select the valid Input!")
        return get_filter_type()#recursively calls if wrong filter given by user
    
    return dat 

def additional_data(x):
    
    ''' The function additional data prints the details of the 5 users at a time and incrementing to next 5 users iteratively
    
    using slicing procedure'''
    z=''                
    g1=0 
    g=5
    while True:
        if g1==0: 
            print("First five user details :")
            print(x[g1:g])
            g1+=5
            g+=5
            history.append(["-","-","-","Raw Data"])
        else:
            print("Next five user details")
            print(x[g1:g])#The two values will take multiples of 5 values every time which prints details of 5 users
            history.append(["-","-","-","Raw Data"])
            g1+=5   
            g+=5#By Incrementing both the values by 5 ,the slicing will be pointed to next 5 users and continues
        z=input("Would you like to have a glance on more data?Press yes else press no")   
        if z=="no":    
            break
        elif z!="no" and z!="yes":
            print("Wrong input detected")
            break


def main():
    '''Here , main function is the  function which handles all the user input's , function calls 
  
   and user related operations. The below function initially calls  city_name() function which is used to input

   the city name. After reading the city name the corresponding CSV file is being loaded into a dataframe df using 
   
   the dictionary CITY_NAME . Then the function asks the user to input the type of filter . The funtion get_filter_type
   
   is called to get the input filter that is choosen by User. The if else loop is used to clasify the types of filters 
   
   and based on that necessary arguments(city name ,month , day ,dataframe ) have been passed into calculate() function.
   
   If the filter is month then the day argument value will be -1 .If filter is day , then the month argument will be -1.
   
   If both month and day are not equal to -1 , then the filter is both. If both month and day are equal to -1 ,then the 
   
   filter is none.The funcitons city_name() and get_filter_type() can also handle wrong inputs given by user. After getting
   
   the filter type ,then it calls the get_filters() function to give the input values by passing filter type as argument. 
   
   This function is an infinite loop asking user to proceed further or not and breaking the loop when ever user presses 'n' . 
   
   This function also asks users whether to have a glance on additional data.
  
  ''' 
    
    valid=0
    while True:
        f=''
        city=city_name()#Getting city name from user
        df=pd.read_csv(CITY_DATA[city])#loading respective data frame of city using CITY_DATA dictionary
        f_type=get_filter_type()#Calls the get_filter_type funtion to get the filter applied by user.
        if f_type=="month":
            month=get_filters("month")#Passes filter type to get_filters() function
            print(month)
            calculate(city,month,-1,df)  #If filter is month , then setting day argument as -1
            history.append([city,months[month-1],"-","month"])
            
        elif f_type=="day":
            day=get_filters("day")  #Passes filter type to get_filters() function   
            calculate(city,-1,day,df)   #If filter is month , then setting day argument as -1
            history.append([city,"-",day,"day"])
            
        elif f_type=="both":
            month=get_filters("month")
            day=get_filters("day")
            calculate(city,month,day,df)#Passes filter type to get_filters() function..since user gave both the inputs 
            history.append([city,months[month-1],day,"both"])
            
        elif f_type=="none":       #It need not call get_filters() since filter is none
            calculate(city,-1,-1,df) #If filter is none , then both month and day will be set to -1
            history.append([city,"-","-","none"])
                    
        print("Would you like to have a glance on some additional data? Press yes to proceed else press no")
        f=input()#Asks user to have a glance on some user's specific data
        if f=="yes":
            additional_data(df)
        elif f!="no":
            print("Skipping the current operation[Wrong input detected]")
        print("\nIf you want to restart the process press yes else press no ")
        z=input()#Asks user whether to continue the process or stop the process
        if z!="yes" and z!="no":
            while valid<3 and z!="yes" and z!="no":
                print("please give a valid input!")
                z=input()
                valid+=1
        if valid==3 and z!="no" and z!="yes":
            print("We are sorry , you exceeded your number of attempts.Please try after some time other")
            print("\nYOUR SEARCH HISTORY..\n")
            k=0
            for y in history:
                dx.loc[k] =y
                k+=1
            print(dx)
            print("\nThank you !! Have a nice day!")
            break
        elif valid<3 and z=="yes":
            valid=0
        if z=="no":
            print("\nYOUR SEARCH HISTORY..\n")
            k=0
            for y in history:
                dx.loc[k] =y
                k+=1
            print(dx)
            print("\nThank you !! Have a nice day!")
            break

''' Execution starts from here'''
if __name__ == "__main__":
    print("PLEASE ENTER YOUR NAME!!")
    nam=input()
    print("Hello {}, WELCOME TO THE US BIKE SHARE DATA!!".format(nam))
    main()   
