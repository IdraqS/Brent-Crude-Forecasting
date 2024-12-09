import pandas as pd
import matplotlib.pyplot as plt

def main():
    # load data onto pandas dataframe
    df = pd.read_excel('RBRTEd.xls', sheet_name = 'Data 1', skiprows = 2)
    df = df.rename(columns = {'Sourcekey': 'Date','Europe Brent Spot Price FOB (Dollars per Barrel)': 'Price'})

    # convert all values to numerical
    df['Date'] = pd.to_datetime(df['Date'])
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # print to check
    print(df)
    print(df.columns)

    # calc yearly avg
    df['Year'] = df['Date'].dt.year
    yearly_avg = df.groupby('Year')['Price'].mean()

    # aaaaaand plot
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_avg.index, yearly_avg.values, marker='o', linestyle='-', color='b')
    plt.title('Average Yearly Europe Brent Spot Price (1987 - Present)')
    plt.xlabel('Year')
    plt.ylabel('Average Price (Dollars per Barrel) / $')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
