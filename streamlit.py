import streamlit as st
import numpy as np
import pandas as pd
import datetime
import plotly.express as px
import refinitiv_access as refin

st.title('ETF Premium Tracker')

ticker = st.selectbox(
    'Select your ETF for premium / discount calculation:',
    ('VOO', '3033.HK', '226490.KS'))

startD = st.date_input("Start Date:", datetime.date(2023, 1, 1))
endD = st.date_input("Start Date:", datetime.date(2023, 11, 1))

df = refin.etf_prem(ticker, str(startD), str(endD))

fig = px.line(df, x='Date', y='Premium', title='Premium / Discount for %s' % ticker) #log_y=True
fig.update_layout(showlegend=False, xaxis_title='Date', yaxis_title='Premium / Discount (%)')
st.plotly_chart(fig, use_container_width=True)
