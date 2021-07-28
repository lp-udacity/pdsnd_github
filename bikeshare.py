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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs and list what city the user selected. 
    city = ''
    while city not in CITY_DATA:
        city = input("please enter city name (chicago, new york city, or washington) in all lowercase:\n").lower()
    print(f'You entered {city}')#print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    month = ''
    while month not in MONTH_DATA:
       month = input("please enter a month (all, january, february, march, april, may, or june) in all lowercase:\n").lower()
    print(f'You entered {month}')#print(city)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    day = ''
    while day not in DAY_DATA:
       day = input("please enter a day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) in all lowercase:\n").lower()
    print(f'You entered {day}')#print(city)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month of traveling:', most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of traveling:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour (24 hr time) :', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station:", most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]
    print('Most frequent combination of start and end stations:', start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types:', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Gender count: ', gender)
    except KeyError:
        print("Gender data not available for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest year of birth: ', earliest_birth_year)
        most_recent = df['Birth Year'].max()
        print('The most recent year of birth: ', most_recent)
        most_common = df['Birth Year'].mode()[0]
        print('Most common year of birth: ', most_common)
    except KeyError:
        print("Birth year data not available for Washington")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""
Raw data is displayed upon request by the user in this manner: Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.
"""
def raw_data(df):
    raw_data = input('Would ypu like to see the bike share raw data? (yes or no)\n').lower()
    i = 0
    while raw_data.lower() == 'yes':
        print(df.iloc[i:i+5])
        i += 5
        raw_data = input('Would you like to see 5 more rows? (yes or no)\n').lower()
        if raw_data.lower() != 'yes':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
