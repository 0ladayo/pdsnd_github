import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=(input('Enter a city from chicago, new york city, washington: ')).lower()
        if city not in CITY_DATA:
            print('Enter a valid city name')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=(input('Enter a month from january to june or enter "all": ')).lower()
        month_list=['january','february','march','april','may','june']
        if month !="all" and month not in month_list:
            print('Enter a valid month or type "all"')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=(input('Enter a day of the week or type "all": ')).lower()
        day_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if day !="all" and day not in day_list:
            print('Enter a valid day or type "all"')
        else:
            break
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   #Create dataframe for each city based on the city entry
    df=pd.read_csv(CITY_DATA[city])
    #Create a new column named month in the dataframe which extract month information from the pandas datetime format in start time column            
    df['month']=pd.to_datetime(df['Start Time']).dt.month_name()
    #Create a new column named week_day in the data frame which extract day name information from the pandas datetime format in start time column              
    df['week_day']=pd.to_datetime(df['Start Time']).dt.day_name()
    
    #Filter month column containing month name by the month entry. The title method ensures the first letter of the day entry is upper case.
    if month != 'all':
        df=df[df['month']==month.title()]
           
    #Filter week_day column containing day name by the day entry. The title method ensures the first letter of the day entry is upper case.
    if day !='all':
        df=df[df['week_day']==day.title()]
                       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month=df['month'].mode()[0]
    print('most common month is: {}'.format(month))

    # TO DO: display the most common day of week
    day=df['week_day'].mode()[0]
    print('Most common day is: {}'.format(day))

    # TO DO: display the most common start hour
    #creates a new column in the dataframe named hour which extract hour information from the pandas datetime format in start time column 
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    common_hour=df['hour'].mode()[0]   
    print('Most common hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('Most common start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('Most common end station is: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_trip=df['Start Station'] + ' '+'to'+' ' + df['End Station']
    common_trip=common_trip.mode()[0]
    print('Most frequent combination of start station and end station trip is: {}'.format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
   
                  
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time is: {} seconds'.format(total_travel_time))
   

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time is: {} seconds'.format(mean_travel_time))
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("the city entered doesn't have users gender information in its data")
            
 
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('earliest birth year is: {}'.format(int(df['Birth Year'].min())))
        print('most recent birth year is: {}'.format(int(df['Birth Year'].max())))  
        print('common birth year is: {}'.format(int(df['Birth Year'].mode()[0])))
    else:
        print("the city entered doesn't have users birth year information in its data")

def individual_trip_data(df):
    while True:
        view_individual_data = (input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')).lower()
        a_list=['yes','no']
        if view_individual_data not in a_list:
            print('Enter yes or no')
        else:
            start_row_index=0
            while (view_individual_data=='yes'):
                print(df.iloc[start_row_index:(start_row_index+5)])
                start_row_index += 5
                view_individual_data=(input('Do you wish to continue?: ')).lower()
                b_list=['yes','no']
                if view_individual_data not in b_list:
                    print('Enter yes or no')
                    view_individual_data=(input('Do you wish to continue?: ')).lower()
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#References  
#Helpful resources https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column
#https://www.geeksforgeeks.org/python-pandas-series-dt-day_name/
#https://www.studytonight.com/python-howtos/how-to-get-month-name-from-month-number-in-python
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
