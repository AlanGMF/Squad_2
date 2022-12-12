
import streamlit as st
import pandas as pd
import json


def show_response(response):

    # Deserialize JSON document to a Python object.
    response_dict = json.loads(response.text)

    # Show info
    tabs = st.tabs(["Information", "Describe"])
    with tabs[1]:
        st.dataframe(pd.DataFrame(response_dict["describe"]))

    with tabs[0]:
        table_nulls = pd.Series(response_dict["nulls"])
        st.table(table_nulls)

    # The dictionary of transformations is displayed
    transf = st.checkbox("Transform", key="transform_file")
    if transf:

        # Dict to save the settings to do
        settings_form = {}

        selected_columns = st.multiselect(
                                "Columns to use",
                                response_dict["columns"],
                                key="selected_columns_",
                                help="Remove unselected columns"
                                )
        null_values_action = st.selectbox(
                        "What do we do with null values?",
                        ["Nothing", "Delete rows"],
                        key="null_values_action",
                        help=r"""
                            Method to use for filling holes
                            in reindexed Series ffill: propagate last
                            valid observation forward to next valid bfill:
                            use next valid observation to fill gap."""
                        )
        sort_column = st.selectbox(
                                "Sort by column",
                                selected_columns,
                                key="sort_column",
                                help="Sorts rows based on selected column"
                                )
        if sort_column:
            order = st.radio("Order", ["ASC", "DESC"], key="order")

        # show more options based on selected columns
        if len(selected_columns) > 0:

            # Check if addfilter exist
            # the api can return None as a value
            if response_dict["addfilter"]:

                # transforms the dictionary that
                #  brings the api to a dataframe
                df_numeric_columns = pd.DataFrame(response_dict["addfilter"])

                # Scrolls through each column and displays a checkbox
                for column in list(df_numeric_columns.index):

                    # ignore the column if it is not selected
                    if column not in selected_columns:
                        continue
                    else:
                        change_col = st.checkbox(
                                                f"add filter: {column}",
                                                key=f"add_f_{column}"
                                                )

                        if change_col:

                            # get the minimum and maximum
                            #  values to create the slider
                            max_value = float(
                                            df_numeric_columns.loc[column, "0"]
                                            )
                            min_value = float(
                                            df_numeric_columns.loc[column, "1"]
                                            )

                            slide_column = st.slider(
                                                    "Select range",
                                                    value=(
                                                        max_value,
                                                        min_value
                                                        )
                                                    )

                            settings_form[f"slide_{column}"] = slide_column

            else:
                st.write("There are no numerical columns!")

            # Save changes made
            save_settings = st.button("Save!", key="columns_setting")

            if save_settings:
                # print("")

                st.success("Save changes made!")
                settings_form["selec_columns"] = selected_columns
                settings_form["nulls_action"] = null_values_action
                settings_form["sort_column"] = sort_column
                settings_form["order"] = order
                st.session_state["show_apply_changes"] = settings_form

            # Change status succes to warning and show
            # delete changes button
            elif st.session_state["show_apply_changes"]:
                st.warning("There are changes saved")
                delete_changes = st.button(
                                        "Delete changes saved",
                                        key="delete_changes"
                                    )

                if delete_changes:

                    # print("")
                    st.session_state["show_apply_changes"] = False
                    # Rerun streamlit (Bug: checkboxes and
                    # selectbox are not reset)
                    st.experimental_rerun()

            if st.session_state["show_apply_changes"]:
                st.markdown("---")
                save_core_settings = st.button("Apply changes")
                st.write(st.session_state["show_apply_changes"])
                if save_core_settings:
                    # print("")
                    st.write("Done")
