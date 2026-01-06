import streamlit as st
import yfinance as yf
import datetime

st.title("stock price analyzer")
st.subheader("analyze and visualize stockprice over time")

company=st.text_input()

ticker = yf.Ticker("MSFT")
sd = st.date_input("start date", datetime.date(2024, 10, 1))
ed = st.date_input("end date", datetime.date(2024, 12, 31))

ticker_data=ticker.history(end=ed,start=sd)

st.subheader("Here is raw day wise stock price")
st.dataframe(ticker_data.head())

st.subheader("Price movement over time")
st.line_chart(ticker_data['Close'])

st.subheader("Bar Chart")
st.bar_chart(ticker_data['Close'])
