# Code for Bikeshare Project in Udacity Learning, from Helmut Weidenauer
import os
import pandas as pd
from datetime import date

# definition of filenames
data = ['chicago.csv','new_york_city.csv', 'washington.csv'];

# definition of valid user enrty
Available_Data = ['Chicago', 'New York City', 'Washington']
Valid_Month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC',
                    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
Valid_Day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', 'Monday',
                    'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
Valid_City_Input = ['0', '1', '2', '3']
Valid_Accept_Input = ['y', 'yes', 'Y', 'YES', 'Yes']

def cls():
    # found in stackoverflow.com
    os.system('cls' if os.name=='nt' else 'clear')
    
def color(color):# change text color
    if color == 'white':
        print('\033[1;37;40m')# set color to white
    elif color == 'green':
        print('\033[1;32;40m') # set color to green
    elif color == 'red':
        print('\033[1;31;40m') # set color to red
    elif color == 'yellow':
        print('\033[1;33;40m') # set color to yellow
  
def print_time_heading(c_choice):    # print header for time input
    cls()
    color('green')
    print('-----------------------------------------------------------------------------\n')
    print('Welcome to Bikshare Data Analysis of\033[1;37;40m', Available_Data[c_choice],'\033[1;32;40m\n')
    print('-----------------------------------------------------------------------------\n')
    print('Would you like to focus on a special month or day ?')
    print('Use \033[1;37;40mJAN - DEC\033[1;32;40m for month or \033[1;37;40mMON - SUN\033[1;32;40m for days, for no limitation press \033[1;37;40mENTER\033[1;32;40m\n')
  
def time_filter(c_choice): # user input if time
    i=''
    while True:
        time_filter = input(i+'Please enter your choice:  \033[1;33;40m')
        time_filter =  time_filter.upper()                                      # convert input to upper case
        if time_filter in Valid_Month or time_filter in Valid_Day:   # check if in put is a valid 
            t_coice = time_filter
            color('green')
            break
        elif time_filter == '':                                                         # user choose no limitation
            time_filter = 'no time limitation'
            color('green')
            break
        else:                                                                                   # invalid input handling
            print_time_heading(c_choice)
            color('red')
            i='Invalid entry - '
    return time_filter
    
def time_filter_to_text(time_filter): # convert month number to test
    Text = time_filter
    if time_filter in Valid_Month:
        Text = Valid_Month[Valid_Month.index(time_filter) + 12] # shift index of month 
    elif time_filter in Valid_Day:
        Text = Valid_Day[Valid_Day.index(time_filter) + 7] # shift index of day
    return Text
  
  
def print_city_heading():  #print header for city input
    cls()
    color('green')
    print('-----------------------------------------------------------------------------\n')
    print('Welcome to Bikshare Data Analysis\n')
    print('-----------------------------------------------------------------------------\n')
    print('What data would you like to analyze :\n')
    print(' \033[1;37;40m1\033[1;32;40m - Chicago')
    print(' \033[1;37;40m2\033[1;32;40m - New York City')
    print(' \033[1;37;40m3\033[1;32;40m - Washington?\n')
    print(' \033[1;37;40m0\033[1;32;40m - quit analysis\n')
    
def city_filter(): # user input if city
    i=''
    while True:
        city_filter = input(i+'Please enter your choice ?  \033[1;33;40m')
        if city_filter in Valid_City_Input:     # check if input is valid
            city = int(city_filter)-1                 # name if city file
            color('green')
            break
        else:                                                   # invalid entry handling
            print_city_heading()
            color('red')
            i='Invalid entry - '
    return city
 
 
def data_import(city_choice, time_choice): # import csv file and add columns
    month = ''
    day= ''
    # ---- Load and Create additional collumns ----
    city_data = pd.read_csv(data[city_choice])                                                              # Load Data File
    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])                           # Create 'Start Time' Column
    city_data['hour'] = city_data['Start Time'].dt.hour                                                 # Create 'hour' Column
    city_data['month'] = city_data['Start Time'].dt.month                                              # Create 'month' Column
    city_data['day'] = city_data['Start Time'].dt.weekday                                              # Create 'day' Column
    city_data['trip'] = city_data['Start Station'] + ' to ' + city_data['End Station']   # Create 'trip' Column
    
    # ---- Filter Data according time_choice ----
    if time_choice in Valid_Month:
        month = Valid_Month.index(time_choice) + 1
        if 'month' in city_data:
            city_data = city_data[city_data['month'] == month]
    elif time_choice in Valid_Day:
        day = Valid_Day.index(time_choice)
        if 'day' in city_data:
            city_data = city_data[city_data['day'] == day]    
    return city_data


def print_result_heading(c_choice, t_choice): # print header for result display
    cls()
    print('\033[1;32;40m-----------------------------------------------------------------------------\n')
    print('\033[1;32;40mBikeshare Analysis Result for\033[1;37;40m', Available_Data[c_choice], '+', time_filter_to_text(t_choice),'\n')
    print('\033[1;32;40m-----------------------------------------------------------------------------')

def print_rawdata_heading(c_choice, t_choice): # printheader for raw data display
    cls()
    print('\033[1;32;40m-----------------------------------------------------------------------------\n')
    print('\033[1;32;40mBikeshare RAW Data for\033[1;37;40m', Available_Data[c_choice], '+', time_filter_to_text(t_choice),'\n')
    print('\033[1;32;40m-----------------------------------------------------------------------------')

def min_max_time(data): # check time period if filtered data
    min_time = data['Start Time'].min()
    max_time = data['Start Time'].max()
    print('\033[1;32;40m\nData found from \033[1;37;40m', min_time.date(),
            '\033[1;32;40m\n             to \033[1;37;40m', max_time.date())

def rental_count(data): # analyse and display rentalcount
    user_types =[]
    user_gender=[]
    count = data['hour'].count()
    user_types = data['User Type'].value_counts()
    print('\033[1;32;40m\nTotal No of Rentals  : \033[1;37;40m', count,
            '\033[1;32;40m\nRentals by User Type : Subscribers\033[1;37;40m',user_types['Subscriber'],
            '\033[1;32;40m\n                       Customers  \033[1;37;40m',user_types['Customer'])
    if 'Gender' in data:
        user_gender = data['Gender'].value_counts()       
        print('\033[1;32;40m\nRentals by User Gender Male       \033[1;37;40m',user_gender['Male'],
                '\033[1;32;40m\n                       Female     \033[1;37;40m',user_gender['Female'])
       
def trip_length(data): # calulate trip lenght
    mean = round(data['Trip Duration'].mean())
    min_length = round(data['Trip Duration'].min()/ 60)
    max_length = round(data['Trip Duration'].max()/ 60)
    print('\033[1;32;40m\nTrip Duration [hours]: Average    \033[1;37;40m', mean, 
            '\033[1;32;40m\n                       min        \033[1;37;40m',min_length,
            '\033[1;32;40m\n                       max        \033[1;37;40m',max_length)
    
def most_popular_time(data): # calulate most popular rental time
    most_month = data['month'].mode()[0]
    most_day = data['day'].mode()[0]
    most_hour = data['hour'].mode()[0]
    print('\033[1;32;40m\nMost popular time    : Month      \033[1;37;40m', Valid_Month[most_month + 11],
            '\033[1;32;40m\n                       Day        \033[1;37;40m', Valid_Day[most_day + 7],
            '\033[1;32;40m\n                       Hour       \033[1;37;40m', most_hour)

def most_popular_station(data): # calulate most popular station
    most_start = data['Start Station'].mode()[0]
    no_on_start = data['Start Station'].value_counts()
    most_end = data['End Station'].mode()[0]
    no_on_end = data['End Station'].value_counts()
    trip = data['trip'].mode()[0]
    print('\033[1;32;40m\nMost popular station : Start      \033[1;37;40m', most_start,' - ', no_on_start[most_start],
            '\033[1;32;40m\n                       End        \033[1;37;40m', most_start, ' - ',no_on_end[most_end],
            '\033[1;32;40m\n\nMost popular trip    : \033[1;37;40m', trip)
  
def customer_age(data): # get customer birthyear and age 
    today =date.today()
    act_year = int(today.strftime("%Y"))
    most_year = int(data['Birth Year'].mode()[0])
    max_year = int(data['Birth Year'].max())
    min_year = int(data['Birth Year'].min())
    print('\033[1;32;40m\nCustomer Age Overview: Most are Born in \033[1;37;40m', most_year, '\033[1;32;40m Age: \033[1;37;40m', act_year - most_year, 
            '\033[1;32;40m\n                       Youngest Born in \033[1;37;40m', max_year,   '\033[1;32;40m Age: \033[1;37;40m', act_year - max_year,
            '\033[1;32;40m\n                       Oldest   Born in \033[1;37;40m', min_year,   '\033[1;32;40m Age: \033[1;37;40m', act_year - min_year,)
 
def display_raw_data(data,c_choice, t_choice): # diaplay raw data table
    start = 0 # starting row
    end = 6    # end row
    count = data['hour'].count() # total number of rows
    while True:
        print_rawdata_heading(c_choice, t_choice)
        print('\033[1;37;40m', data.iloc[start:end])
        print('\033[1;32;40mPlease press\033[1;33;40m 1 \033[1;32;40mfor \033[1;33;40mup\033[1;37;40m')
        print('\033[1;32;40mPlease press\033[1;33;40m 2 \033[1;32;40mfor \033[1;33;40mdown\033[1;37;40m')
        next_step = input('\033[1;32;40mPlease press\033[1;33;40m 0 \033[1;32;40mto \033[1;33;40m EXIT \033[1;37;40m')        
        if next_step == '1' and start > 0: # skip 5 rows down
            start -= 5
            end -= 5
        elif next_step == '2' and start < count: # skip 5 rows up
            start += 5
            end += 5
        elif next_step == '0':
            break
    return
 
#---------------------- MAIN --------------------------------------------------------------    
def main():
    while True:
        print_city_heading()
        c_choice = city_filter()
        if c_choice < 0:
            break        
        print_time_heading(c_choice)
        t_choice = time_filter(c_choice)
        data = data_import(c_choice, t_choice)   
        print_result_heading(c_choice, t_choice)
        if data.empty:
            print('\nSorry, No data avaliable for this time period')
        else:
            min_max_time(data)
            rental_count(data)
            trip_length(data)
            most_popular_time(data)
            most_popular_station(data)
            if 'Birth Year' in data:
                customer_age(data)    
            next_step = input('\n\033[1;32;40mDo you want to see raw data y/n ?  \033[1;33;40m')
            if  next_step == 'y':
                display_raw_data(data,c_choice,t_choice)                                
    print('\nThank you for using Bikeshare Analysis')
    color('white')
       
       
if __name__ == "__main__":
	main()
    
    
 
   
    
    
    
    

    
    