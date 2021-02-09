import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import time
from datetime import datetime
import math
import statistics
import base64

def get_table_download_link(dafr):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = dafr.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="Results.csv">Download Result (CSV)</a>'

def app():
    st.title('Hourly Water Resource Index')

    st.write("Please upload the timeseries hourly rainfall data. Once you upload the csv file, the application will start to compute the Water Resource Index (WRI).")
    st.write("After WRI is calculated, the results will be available for download.")
    st.write("The WRI for 24, 48, 72, and 96 hours will be computed by this application.")
    st.write("The three columns in the csv file should be named as 'date', 'hour', and 'rain'.")
    st.write("Please ensure there are no missing values in the dataset.")

    wri_uploaded_file = st.file_uploader("Choose a file")
    if wri_uploaded_file is not None:
        df = pd.read_csv(wri_uploaded_file)

        df['wri_24'] = 0.0
        df['wri_48'] = 0.0
        df['wri_72'] = 0.0
        df['wri_96'] = 0.0

        st.sidebar.write("Calculating 24 Hour WRI....")

        antecedent_period = 24
        wri = 0
        itr = 0
        last_itr = 0

        weight = 0
        for x in range (1, antecedent_period + 1, 1):
            weight = weight + 1/x

        new_weight = weight

        for i in range(antecedent_period - 1, len(df.index), 1):
            df["wri_24"][i] = 0
            for j in range(i, i - antecedent_period, -1):
                if(itr == 0):
                    wri = wri + df['rain'][j]
                else:
                    new_weight = new_weight - 1/itr
                    wri = wri + ((df['rain'][j] * new_weight) / weight)
                    
                itr = itr + 1
            df['wri_24'][i] = round(wri, 3)
            wri = 0
            itr = 0
            new_weight = weight

        st.sidebar.write("Calculating 48 Hour WRI....")

        antecedent_period = 48
        wri = 0
        itr = 0
        last_itr = 0

        weight = 0
        for x in range (1, antecedent_period + 1, 1):
            weight = weight + 1/x

        new_weight = weight

        for i in range(antecedent_period - 1, len(df.index), 1):
            df["wri_48"][i] = 0
            for j in range(i, i - antecedent_period, -1):
                if(itr == 0):
                    wri = wri + df['rain'][j]
                else:
                    new_weight = new_weight - 1/itr
                    wri = wri + ((df['rain'][j] * new_weight) / weight)
                    
                itr = itr + 1
            df['wri_48'][i] = round(wri, 3)
            wri = 0
            itr = 0
            new_weight = weight

        st.sidebar.write("Calculating 72 Hour WRI....")

        antecedent_period = 72
        wri = 0
        itr = 0
        last_itr = 0

        weight = 0
        for x in range (1, antecedent_period + 1, 1):
            weight = weight + 1/x

        new_weight = weight

        for i in range(antecedent_period - 1, len(df.index), 1):
            df["wri_72"][i] = 0
            for j in range(i, i - antecedent_period, -1):
                if(itr == 0):
                    wri = wri + df['rain'][j]
                else:
                    new_weight = new_weight - 1/itr
                    wri = wri + ((df['rain'][j] * new_weight) / weight)
                    
                itr = itr + 1
            df['wri_72'][i] = round(wri, 3)
            wri = 0
            itr = 0
            new_weight = weight

        st.sidebar.write("Calculating 96 Hour WRI....")

        antecedent_period = 96
        wri = 0
        itr = 0
        last_itr = 0

        weight = 0
        for x in range (1, antecedent_period + 1, 1):
            weight = weight + 1/x

        new_weight = weight

        for i in range(antecedent_period - 1, len(df.index), 1):
            df["wri_96"][i] = 0
            for j in range(i, i - antecedent_period, -1):
                if(itr == 0):
                    wri = wri + df['rain'][j]
                else:
                    new_weight = new_weight - 1/itr
                    wri = wri + ((df['rain'][j] * new_weight) / weight)
                    
                itr = itr + 1
            df['wri_96'][i] = round(wri, 3)
            wri = 0
            itr = 0
            new_weight = weight

        st.write("Computations Completed")
        st.write(df)
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)