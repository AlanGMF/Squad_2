import streamlit as st
import pandas as pd
import requests


def change_null_values(action: str, df: pd.DataFrame):
    pass


def drop_columns(s_columns: list, df: pd.DataFrame):
    """Return df with selected columns

    :param s_columns: Selected columns
    :type s_columns: list
    :param df: Dataframe to filter
    :type df: pd.DataFrame
    :return: filtered dataframe
    :rtype: pd.DataFrame
    """
    columns_to_drop = [column for column in df.columns]

    for column in df.columns:
        if column in s_columns:
            columns_to_drop.remove(column)
    return df.drop(columns=columns_to_drop)


def apply_changes(cfgs: dict, dfs: dict):

    sc = "selected_columns"
    # Apply change in each df

    # null_df = pd.DataFrame(
    #     {
    #         'animal': ['alligator', 'bee', 'falcon',
    #  'lion','monkey', 'parrot', 'shark', 'whale', 'zebra']
    #     })
    new_dfs = {}
    for df_name, cfgs_df in cfgs.items():

        # FIXME this code catch te error -> "name csv file" : NULL
        # if cfgs[df_name]  == None:
        #    st.markdown("# Entra al none")
        #    new_dfs[df_name]=null_df
        # else:
        filtered_df = drop_columns(cfgs[df_name][sc], dfs[df_name])

        # if cfgs[df_name][n] != "Nothing":
        #    filtered_df = change_null_values(cfgs[df_name][n],dfs[df_name])

        new_dfs[df_name] = filtered_df

    return new_dfs

    # filter_columns(df: Dataframe,columns: list)
    # alter_null_values(df: Dataframe, how: str) # FIXME check variable name
    # order_by_column(df: Dataframe,column: str)


def show_settings_for_selected_columns(df_name):

    # Select sort column
    sort_column = st.selectbox(
            "Sort by column",
            st.session_state[f"dynamic_cfg_{df_name}"],
            key=f"sort_column{df_name}",
            help="Sorts rows based on selected column"
    )

    if sort_column:
        pass
        # order = st.radio("Order", ["ASC", "DESC"], key=f"order_{df_name}")

    # FIXME
    # add_filter = st.checkbox(
    #         "Add filter to a specific column",
    #         #st.session_state[f"dynamic_cfg_{df_name}"],
    #         key= f"filter_to_column{df_name}",
    #         help= "Despliega un"
    # )
    # if add_filter:
    #     for select

    return "configuracion"


def show_settings_df(dataframe, df_name):
    """Show configuration options

    :param dataframe: Dataframe target
    :type dataframe: pd.Dataframe
    :param df_name: dataframe name
    :type df_name: str
    """
    # Init sess_st
    if f"dynamic_cfg_{df_name}" not in st.session_state:
        st.session_state[f"dynamic_cfg_{df_name}"] = []

    # Show dataframe
    st.write("Data:")
    st.dataframe(dataframe, height=180)

    # Get columns to select
    col = []
    for column in dataframe.columns:
        col.append(str(column))

    # Select Columns to filter
    selected_columns = st.multiselect(
                                    "Columns to use",
                                    col,
                                    key=f"selected_columns_{df_name}",
                                    help="Remove unselected columns"
                                    )
    if len(selected_columns) != 0:
        # FIXME can be improved using only a dictionary
        st.session_state[f"dynamic_cfg_{df_name}"] = selected_columns

    save_cols = st.form_submit_button(
        "Save columns",
        type="secondary",
        help=r"""
            saves the chosen columns
            and displays more options
            based on those columns
            """
        )

    # More cfgs
    more_cfg = {}
    null_values_action = "Nothing"
    if save_cols and len(selected_columns) != 0:

        # Select what to do with null data
        null_values_action = st.selectbox(
                            "What do we do with null values?",
                            ["Nothing", "Delete rows", ],
                            key=f"null_values_action_{df_name}",
                            help=r"""
                                Method to use for filling holes
                                in reindexed Series ffill: propagate last
                                valid observation forward to next valid bfill:
                                use next valid observation to fill gap."""
                            )
        # FIXMEreturn a json with the cfgs
        more_cfg = show_settings_for_selected_columns(df_name)
    elif save_cols and len(selected_columns) == 0:
        # FIXME add st.empty with 5 sec ttl
        st.error("No column selected")
    if len(selected_columns) == 0:
        return False
    cfg = {
        "null_values": null_values_action,
        "selected_columns": selected_columns,
        "more_setting": more_cfg,
        }

    return cfg


def get_company_data():
    
    res = requests.post(url="http://0.0.0.0:8000/getdata")
    st.write(res.text.split(","))
    data1, data2, data3, data4, data5 = res.text.split(",")

    dataframe1 = pd.read_csv(data1.replace('"', '').strip())
    st.dataframe(dataframe1)

    dataframe2 = pd.read_csv(data2.replace('"', '').strip())
    st.dataframe(dataframe2)

    dataframe3 = pd.read_csv(data3.replace('"', '').strip())
    st.dataframe(dataframe3)

    dataframe4 = pd.read_csv(data4.replace('"', '').strip())
    st.dataframe(dataframe4)

    dataframe5 = pd.read_csv(data5.replace('"', '').strip())
    st.dataframe(dataframe5)


st.markdown("# Buster-block ")
st.markdown("####  Download company files :open_file_folder:")

if "Show_company_data" not in st.session_state():
    st.session_state["Show_company_data"] = False

download_company_files = st.button(
    "Download",
    disabled=st.session_state["Show_company_data"]
)

if (download_company_files):
    st.session_state["Show_company_data"] = True
    data = get_company_data()
    # display_download_buttons(data) # FIXME


st.markdown("####  Upload your files :open_file_folder:")
uploaded_files = st.file_uploader(
                                " ",
                                accept_multiple_files=True,
                                type=["csv"],
                                key="file_uploader"
                                )

dfs = {}


@st.experimental_memo(
    ttl=60, max_entries=5
)
def get_dataframe(files):
    """get dataframes from files

    :param files: list of files
    :type files: list[UploadedFile]
    :return: dictionary with dataframes and names
    :rtype: dict
    """
    for file in files:
        dfs[file.name] = pd.read_csv(file)
    return dfs


if "data_preview" not in st.session_state:
    st.session_state["data_preview"] = False


def show_dict(dfs: dict, dowload: bool):
    for df_name, df in dfs.items():

        s1 = st.expander(f"{df_name}")
        with s1:
            st.dataframe(df)
        if dowload:
            csv = convert_df(df)
            st.download_button(
                            label="Download data as CSV",
                            data=csv,
                            file_name=f'{df_name}',
                            mime='text/csv',
                            )


@st.experimental_memo(
    ttl=60, max_entries=5
)
def show_preview(dfs: dict):
    show_dict(dfs, True)


@st.cache
def convert_df(df: pd.DataFrame):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


def page_show():
    st.markdown("### Dataframes")
    show_dict(dfs, dowload=False)


def page_transform():

    if "Show_apply_changes" not in st.session_state:
        st.session_state["Show_apply_changes"] = False
    if "Changes" not in st.session_state:
        st.session_state["Changes"] = {}
    st.markdown("### Transforms")

    # Shows the transformations of each df
    for df_name, df in dfs.items():
        # Initializes the variable that determines whether or
        # not the settings are applied
        if f"apply_cfg_{df_name}" not in st.session_state:
            st.session_state[f"apply_cfg_{df_name}"] = False
        # Display settings form
        transform_df = st.expander(f"{df_name}")
        with transform_df:
            form_ = st.form(key=f"form_df{df_name}")
            with form_:

                disable = True
                cfg_df = show_settings_df(df, df_name)
                if cfg_df:
                    disable = False

                submitted = st.form_submit_button(
                                                "Save",
                                                type="primary",
                                                disabled=disable
                                                )
                if submitted:
                    # Save the transformation state of df
                    st.session_state[f"apply_cfg_{df_name}"] = submitted
        # Show state success
        if st.session_state[f"apply_cfg_{df_name}"]:
            # Show success
            st.success(f"Changes saved: {df_name}")
            st.session_state["Show_apply_changes"] = True
            st.session_state["Changes"][f"{df_name}"] = cfg_df
    # Show Show_apply_changes
    if st.session_state["Show_apply_changes"]:

        apply = st.button("Apply changes", key="apply-changes", disabled=False)
        if apply:
            if "save_predata" not in st.session_state:
                st.session_state["save_predata"] = {}
            # FIXME
            new_dfs_dict = apply_changes(st.session_state["Changes"], dfs)
            st.session_state["save_predata"] = new_dfs_dict
            st.session_state["data_preview"] = True


if (uploaded_files):

    # --- Save dfs in cache ---
    dfs = get_dataframe(uploaded_files)

    pages = {
        "Show": page_show,
        "Transform": page_transform,
    }

    selec_page = st.selectbox(
        " ",
        pages.keys(),
        key="pages_sb",
        help="Choose page to display"
    )
    pages[selec_page]()

if st.session_state["data_preview"] and st.session_state["save_predata"]:
    st.markdown("## Data preview!")
    show_dict(st.session_state["save_predata"], dowload=True)
