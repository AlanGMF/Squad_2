import streamlit as st
import time
import pandas as pd
import requests
import os

DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/frontend')

if "response" not in st.session_state:
    st.session_state["response"] = False

st.markdown("# Store " )
st.markdown("#### Upload files to transform them! :open_file_folder:" )

# NUEVO000
if st.button('get the data'):

    res = requests.get(url="http://127.0.0.1:8000/getdata")

    if res.status_code != 200:
        st.error("Could not connect to server")
    else:
        st.session_state["response"] = res.json()

if st.session_state["response"]:
    res = st.session_state["response"]

    file_names = []
    for name in res:
        if "/" in name:
            file_names.append(name.split("/")[-1])
        if "\\" in name:
            file_names.append(name.split("\\")[-1])

    st.markdown("---")

    # Generate tabs
    tabs = st.tabs(file_names)
    count = 0

    for tab in tabs:
        with tab:
            st.write(file_names[count])
            
            st.dataframe(pd.read_csv(str(res[count])))

            st.download_button(
                label="Download data as CSV",
                data=str(res[count]),
                file_name=file_names[count],
                mime='text/csv',
            )
        count += 1
    # NUEVOOOOO
# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
    
#     client_file = pd.DataFrame(uploaded_file)
#     #/home/manu/desktop2/proyect/data/data_client/df.csv'
#     client_file.to_csv('Buster-Block/data_client/df.csv')

# st.session_state.df = pd.read_csv("Buster-Block/data_client/df.csv")

# st.subheader("Add Record")

# num_new_rows = st.sidebar.number_input("Add Rows",1,50)
# ncol = st.session_state.df.shape[1] 
# rw = -1

# with st.form(key="add form", clear_on_submit= True):
#     cols = st.columns(ncol)
#     rwdta = []

#     for i in range(ncol):
#         rwdta.append(cols[i].text_input(st.session_state.df.columns[i]))

#     if st.form_submit_button("Add"):
#         if st.session_state.df.shape[0] == num_new_rows:
#             st.error("Add row limit reached. Cant add any more records..")
#         else:
#             rw = st.session_state.df.shape[0] + 1
#             st.info(f"Row: {rw} / {num_new_rows} added")
#             st.session_state.df.loc[rw] = rwdta

#             if st.session_state.df.shape[0] == num_new_rows:
#                 st.error("Add row limit reached...")

# st.dataframe(st.session_state.df)

# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')

# csv = convert_df(st.session_state.df)

# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name='large_df.csv',
#     mime='text/csv',
# )