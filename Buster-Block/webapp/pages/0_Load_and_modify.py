import requests
import streamlit as st
from pages.uils_pages.utils_load_n_modify import show_response

if "get_data_insights" not in st.session_state:
    st.session_state["get_data_insights"] = False
if "press_button_to_post" not in st.session_state:
    st.session_state["press_button_to_post"] = False
if "save_base_changes" not in st.session_state:
    st.session_state["save_base_changes"] = False
if "show_apply_changes" not in st.session_state:
    st.session_state["show_apply_changes"] = False

# Show file uploader
st.markdown("# Buster-block ")
st.markdown("####  Upload your files :open_file_folder:")
uploaded_file = st.file_uploader(
                                " ",
                                accept_multiple_files=False,
                                type=["csv"],
                                key="file_uploader"
                                )


if uploaded_file:
    go = st.button("Send file to preview", key="send_file")

    if go:
        st.session_state["press_button_to_post"] = True

        response = requests.post(
                                'http://127.0.0.1:8000/load_data',
                                data={"type": "multipart/form-data"},
                                files={"upload_file": uploaded_file}
                                )

        # log(f"Response: {response.status_code}")

        if response.status_code != 200:
            st.session_state["get_data_insights"] = False
            st.error("Could not connect to server")
        else:
            st.session_state["get_data_insights"] = response

if st.session_state["get_data_insights"]:
    show_response(st.session_state["get_data_insights"])
