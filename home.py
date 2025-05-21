import streamlit as st
from datetime import date

st.title("主頁：選擇日期區間")

# 初始化 session_state
if 'start_date' not in st.session_state:
    st.session_state['start_date'] = date(2024, 1, 1)
if 'end_date' not in st.session_state:
    st.session_state['end_date'] = date.today()

# 日期選擇器
start_date = st.date_input("選擇起始日期", st.session_state['start_date'])
end_date = st.date_input("選擇結束日期", st.session_state['end_date'])

# 儲存使用者選擇
st.session_state['start_date'] = start_date
st.session_state['end_date'] = end_date

st.success(f"目前選擇的日期區間為：{start_date} 到 {end_date}")

