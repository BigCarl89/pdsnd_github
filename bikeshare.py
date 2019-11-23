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
        try:
            city = str(input('Data available for Chicago, New York City and Washington. \n'
                             'What city do you want to analyze? \n')).lower()
        except ValueError:
            print('Not a valid city, try something else')
        if city not in CITY_DATA.keys():
            print('Not a valid city, try something else')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Data available from January to June. \n'
                              'Which month do you want to analyze? Type \'all\' to analyze the entire time period. \n')).lower()
        except ValueError:
            print('Not a valid month, try something else')
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Not a valid month, try something else')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Which day of the week? Type \'all\' to analyze the entire week. \n')).lower()
        except ValueError:
            print('Not a valid day, try something else')
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('Not a valid day, try something else')
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

    df = pd.read_csv(CITY_DATA[city])

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name()
    c_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['day'] = df['Start Time'].dt.weekday_name
    c_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour
    c_hour = df['hour'].mode()[0]

    print('The most common month of travel is {}, the most common day of travel is {} and the most common hour of travel is {}.'.format(c_month, c_day, c_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    s_st = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(s_st))

    # TO DO: display most commonly used end station
    e_st = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(e_st))

    # TO DO: display most frequent combination of start station and end station trip
    df['combined trip'] = df['Start Station'] + ' - ' + df['End Station']
    trip = df['combined trip'].mode()[0]
    print('The most common trip is {}'.format(trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_trip = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()

    print('Total travel time is {} seconds and the mean travel time is {} seconds.'.format(tot_trip,mean_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()
    print('The user types for this city are: \n{}'.format(users))

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('Gender data is unavailable for this city')
    else:
        g_count = df['Gender'].value_counts()
        print('Gender count for this city is: \n{}'.format(g_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth Year data is unavailable for this city')
    else:
        older = int(df['Birth Year'].min())
        younger = int(df['Birth Year'].max())
        c_year = int(df['Birth Year'].mode()[0])
        print('The oldest user is born in {}, the youngest in {} and the most common year of birth is {}'.format(older, younger, c_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays 5 lines of raw data"""
    #defining the firist 5 lines of data
    first = 0
    last = 5
    while True:
        r_lines = input('\nWould you like to view 5 lines of the selected data? Enter yes or no.\n').lower()
        if r_lines != 'yes':
            break
        else:
            print(df[df.columns[0:]].iloc[first:last])
            first += 5
            last += 5
    return

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
