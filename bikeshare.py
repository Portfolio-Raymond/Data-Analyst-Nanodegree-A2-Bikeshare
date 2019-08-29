# 
# Raymond Atherley
# Bikeshare Project

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
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York, or Washington?\n')
    city = city.lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print('Invalid choice, please try again')	
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n')
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month? all or january, february, march, april, may or june?\n')
    month = month.lower()
    while month not in ('all', 'january', 'february', 'march', 'april', 'may',  'june'):
        print('Invalid choice, please try again')	
        month = input('Which month? all or january, february, march, april, may or june?\n')
        month = month.lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day? all or monday, tuesday, wednesday, thursday, friday, saturday, sunday?\n')
    day = day.lower()
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print('Invalid choice, please try again')
        day = input('Which day? all or monday, tuesday, wednesday, thursday, friday, saturday, sunday?\n')
        day = day.lower()
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
     
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        monthlist = ['january', 'february', 'march', 'april', 'may', 'june']
        month = monthlist.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is {}'.format(popular_day))
    # TO DO: display the most common start hour
    print('The most common start hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    start_end = df['Start Station'] + " AND " + df['End Station']
    popular_start_and_end = start_end.mode()[0]
    print('The most frequent combination of start station and end station trip is {}'.format(popular_start_and_end))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    if CITY_DATA[city] == 'new_york_city.csv' or CITY_DATA[city] == 'Chicago':
        df['Trip Duration'] = float(df['Trip Duration']) / 60.00
    elif CITY_DATA[city] == 'washington.csv':
        df['Trip Duration'] = df['Trip Duration'] / 60.00
    
          
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_duration = df['Trip Duration'].sum()
    mean_duration = df['Trip Duration'].mean()
    # TO DO: display total travel time
    print('Total Travel Time: {}'.format(total_duration))

    # TO DO: display mean travel time
    print('Mean Travel Time: {}'.format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    usertypes = df['User Type'].value_counts()
    print('\nUser Types\n {}'.format(usertypes))
    
    if city == 'new york city' or city == 'chicago':
	
        # TO DO: Display counts of gender
        gendercount = df['Gender'].value_counts()
        print('\nGender Counts\n {}'.format(gendercount))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = np.nanmin(df['Birth Year'])
        mostrecent_yob = np.nanmax(df['Birth Year'])
        most_yob = df['Birth Year'].mode()[0]
        
        print('\nThe earliest year of birth is {}'.format(earliest_yob))
        print('The most recent year of birth is {}'.format(mostrecent_yob))
        print('The most common year of birth is {}'.format(most_yob))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

	
def display_data(df):
    '''
        Displays five lines of data if the user specifies that they would like to.
        After displaying five lines, ask the user if they would like to see five more,
        continuing asking until they say stop.

        Args:
            none.
        Returns:
        TODO: fill out return type and description (see get_city for an example)'''
    
    
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    display = display.lower()
    i = 0
    j = 5
	
    while j < df.shape[0]:
        if display == 'yes':
            print(df[i:j])
            i+=5
            j+=5
            display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
            display = display.lower()
            if display == 'no':
                break
    
    # TODO: handle raw input and complete function


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df, city)
        user_stats(df, city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()