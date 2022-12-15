import requests
import streamlit as st
import pandas as pd
import json
from pages.uils_pages.utils_load_n_modify import show_response

if "get_data_insights" not in st.session_state:
    st.session_state["get_data_insights"] = False
if "file_name" not in st.session_state:
    st.session_state["file_name"] = False
if "save_base_changes" not in st.session_state:
    st.session_state["save_base_changes"] = False
if "show_apply_changes" not in st.session_state:
    st.session_state["show_apply_changes"] = False
if "post_transform" not in st.session_state:
    st.session_state["post_transform"] = False
if "Save_data_db" not in st.session_state:
    st.session_state["Save_data_db"] = False
if "status_final_response" not in st.session_state:
    st.session_state["status_final_response"] = False


# Show file uploader
st.markdown("# Buster-block ")
st.markdown("####  Modify your files! :open_file_folder:")
uploaded_file = st.file_uploader(
                                " ",
                                accept_multiple_files=False,
                                type=["csv"],
                                key="file_uploader"
                                )


if uploaded_file:
    go = st.button("Send file to preview", key="send_file")

    if go:
        st.session_state["file_name"] = uploaded_file.name

        response = requests.post(
                                'http://127.0.0.1:8000/info_data',
                                data={"type": "multipart/form-data"},
                                files={"upload_file": uploaded_file}
                                )

        # log(f"Response: {response.status_code}")

        if response.status_code != 200:
            st.session_state["get_data_insights"] = False
            st.error("Could not connect to server")
        else:
            st.session_state["get_data_insights"] = response
else:
    st.session_state["get_data_insights"] = False

if st.session_state["get_data_insights"]:
    show_response(st.session_state["get_data_insights"])

if uploaded_file and st.session_state["post_transform"]:

    #print("")

    settings = str(st.session_state["show_apply_changes"])

    response = dats = requests.post(
                        url='http://127.0.0.1:8000/transform_and_save',
                        data={
                            "settings": settings,
                            "save_file":st.session_state["Save_data_db"]
                        }
                    )
    if response.status_code !=200:
        st.error("Could not connect to server")
    else:
        st.session_state["status_final_response"] = response #response.status_code
        st.session_state["post_transform"] = False

if st.session_state["status_final_response"] != False:

    st.session_state["post_transform"] = False
    response = st.session_state["status_final_response"]

    st.markdown("---")
    st.markdown("#  Data preview:")
    data = json.loads(response.content.decode('utf-8'))
    df = pd.DataFrame(data)
    st.dataframe(df)

    new_name_csv = st.text_input("Name of the new csv file", "my_file")
    
    downl = st.download_button(
                        label="Download data as CSV",
                        data=df.to_csv().encode('utf-8'),
                        file_name=f'{new_name_csv}.csv',
                        mime='text/csv',
                    )
    if downl:
        st.success("Thanks :tada:")
