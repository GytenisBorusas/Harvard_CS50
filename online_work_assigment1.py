"""
Prompt
Write code to execute the following and provide a detailed explanation of your code: Given a dataframe 
with column = date, starting from 1 Jan 2017 to 30 Jun 2017, create a new column = monitoring period, 
grouping each Monday to Sunday as a new group. For example: 1 jan 2017 which is a Sunday, so the 
monitoring period value = p0, then for 2 jan 2017 to 8 jan 2017 , the monitoring period value = p1,
then 9 jan 2017 to 15 jan 2017, the monitoring period value = p2, then continue to do until 30 jun 2017.
"""




import pandas as pd

def create_date_list(start_date, end_date):
    # date_rng creates range. 
    # "start=" is start date of the range
    # "end=" is the end of the range
    return pd.date_range(start=start_date, end=end_date)

def initialize_dataframe(dates_list):
    #this line creates an 'excel' like table for the range of dates we have created above.
    return pd.DataFrame(dates_list, columns=['date'])

def check_if_sunday(date_series):
    #this line returns true/false collumn to check if the day is Sunday
    return date_series.dt.dayofweek == 6

def calculate_periods(is_sunday_series):
    return is_sunday_series.cumsum()

def format_periods(period_series):
    return 'p' + period_series.astype(str)

def main():
    # Defining start and end dates
    start_date = '1/1/2017'
    end_date = '30/6/2017'
    list_of_dates = create_date_list(start_date, end_date)
    
    # Starts the data frames
    df = initialize_dataframe(list_of_dates)
    
    # Find the Sundays
    is_sunday = check_if_sunday(df['date'])
    
    # Calculates and reformats the tables
    periods = calculate_periods(is_sunday)
    df['monitoring_period'] = format_periods(periods)
    
    # prints out the tables
    print(df)

if __name__ == "__main__":
    main()
