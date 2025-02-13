import streamlit as st

import pandas as pd
st.title('IM Calculator')
st.divider()
st.subheader('Current Position:')         
data = pd.read_csv('POSITION - 20250103.csv')
st.dataframe(data)
st.subheader('Add new trades:')
new_trades = pd.DataFrame(columns=data.columns)
edited = st.data_editor(new_trades,num_rows='dynamic')

st.write('new version - here is where the calcs would appear but not pasting my code here')