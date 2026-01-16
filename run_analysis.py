import pandas as pd
import matplotlib.pyplot as plt
from helpers import add_revenue

    df = pd.read_csv('sales.csv')
    print("File loaded successfully.")

    df = add_revenue(df)

    df.to_csv('sales_with_revenue.csv', index=False)
    print("Saved updated data to sales_with_revenue.csv")

  
    plt.figure(figsize=(10, 6))
    plt.bar(df['product'], df['total_revenue'], color='skyblue')
    plt.xlabel('Product')
    plt.ylabel('Total Revenue')
    plt.title('Product vs Total Revenue')

    plt.savefig('revenue_plot.png')
    print("Plot saved as revenue_plot.png")
    
    plt.show()

except FileNotFoundError:
    print("Error: 'sales.csv' not found. Please ensure the file exists.")
