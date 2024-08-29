# stock_app.py

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pandas.plotting import scatter_matrix
import streamlit as st

# Load the data from CSV files
tesla = pd.read_csv('tesla_stock.csv', parse_dates=['Date'], index_col='Date')
ford = pd.read_csv('ford_stock.csv', parse_dates=['Date'], index_col='Date')
gm = pd.read_csv('GM_stock.csv', parse_dates=['Date'], index_col='Date')

# Add Total Traded column
tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
ford['Total Traded'] = ford['Open'] * ford['Volume']
gm['Total Traded'] = gm['Open'] * gm['Volume']

# Streamlit app title
st.title("Interactive Stock Data Visualization")

# Sidebar options
data_type = st.sidebar.selectbox(
    "Select Data Type to Plot",
    ['Open', 'Volume', 'Total Traded', 'Scatter Matrix']
)

# Function to plot data based on selection
def plot_data(data_type='Open'):
    """
    Plots the selected data type ('Open', 'Volume', 'Total Traded', or 'Scatter Matrix') for Tesla, GM, and Ford.

    Parameters:
    data_type (str): The type of data to plot.
    """
    if data_type in ['Open', 'Volume', 'Total Traded']:
        plt.figure(figsize=(16, 8))
        if data_type == 'Open':
            tesla['Open'].plot(label='Tesla', title='Open Price')
            gm['Open'].plot(label='GM')
            ford['Open'].plot(label='Ford')
            plt.ylabel('Open Price')
        elif data_type == 'Volume':
            tesla['Volume'].plot(label='Tesla', title='Volume Traded')
            gm['Volume'].plot(label='GM')
            ford['Volume'].plot(label='Ford')
            plt.ylabel('Volume')
        elif data_type == 'Total Traded':
            tesla['Total Traded'].plot(label='Tesla', title='Total Traded')
            gm['Total Traded'].plot(label='GM')
            ford['Total Traded'].plot(label='Ford')
            plt.ylabel('Total Traded')
        plt.legend()
        plt.xlabel('Date')
        st.pyplot(plt)  # Display plot with Streamlit

    elif data_type == 'Scatter Matrix':
        car_comp = pd.concat([tesla['Open'], gm['Open'], ford['Open']], axis=1)
        car_comp.columns = ['Tesla Open', 'GM Open', 'Ford Open']
        scatter_matrix(car_comp, figsize=(8, 8), alpha=0.2, hist_kwds={'bins': 50})
        st.pyplot(plt)  # Display scatter matrix with Streamlit

    else:
        st.error("Invalid data type selected.")

# Call the function with the selected data type
plot_data(data_type)
