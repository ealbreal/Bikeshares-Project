
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': r'C:\Users\Eva\Documents\Udacity\Bikeshares Project\chicago.csv',
              'new york city': r'C:\Users\Eva\Documents\Udacity\Bikeshares Project\new_york_city.csv',
              'washington': r'C:\Users\Eva\Documents\Udacity\Bikeshares Project\washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while True:
        city = input("\nWhich city would you like to analyze?\n")
        if city.strip() == 'chicago' or city.strip() == 'Chicago':
            city = ('chicago')
            break
        elif city.strip() == 'washington' or city.strip() == 'Washington':
            city = ('washington')
            break
        elif city.strip() == 'new york city' or city.strip() == 'New York City':
            city = ('new york city')
            break
        else:
            print('Please pick a valid city: New York City, Chicago or Washington')
        
    month = ''
    while True:
        month = input("\nWhich month would you like to analyze?Input \"all\" to apply no month filter.\n")
        if month.lower() not in('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):
            print('\nThat input isn\'t valid.Please try again.\n')
            continue
        else:
            month = month.lower()
            break
            
    day = ''
    while True:
        day = str(input("\nFor which day would you like to see the data? Input \"all\" to apply no day filter.\n"))
        if day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print ('\nThat input isn\'t valid.Please try again.\n')
            continue
        else:
            day = day.lower()
            break
             
           
    print('-'*40)
    return city, month, day
city, month, day = get_filters()



# In[2]:


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
        months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df= df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


# In[ ]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start Month:', popular_month)

    # display the most common day of week
    
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    print('Most Popular Start Day:', popular_day)

    # display the most common start hour
   
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


# In[ ]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    popular_start = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end)

    # display most frequent combination of start station and end station trip
    popular_station = df.groupby('Start Station')['End Station'].apply(pd.Series).mode()[0]

    print('Most Popular Station:', popular_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_time) 

    # display mean travel time
    mean_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('User Type:', user_types)

    # Display counts of gender
    user_gender = df['Gender'].value_counts()

    print('Gender:', user_gender)

    # Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    recent_year = df['Birth Year'].max()
    most_year = df['Birth Year'].mode()[0]
    
    print ('The earliest Year of birth:', earliest_year)
    print ('The most recent Year of birth:', recent_year)
    print ('The most common Year of birth:', most_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

