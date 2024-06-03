import streamlit as st
import pandas as pd
import numpy as np
import time
import os

# Inject custom CSS for the bot (if required, you can add the bot script here too)
bot_css = """
<style type='text/css'>
    .embeddedServiceHelpButton .helpButton .uiButton {
        background-color: #005290;
        font-family: "Arial", sans-serif;
    }
    .embeddedServiceHelpButton .helpButton .uiButton:focus {
        outline: 1px solid #005290;
    }
</style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(bot_css, unsafe_allow_html=True)

# Title of the app
st.title('Intern Performance Dashboard')

# Admin authentication
admin_password = "admin123"
password = st.text_input("Enter admin password:", type="password")
is_admin = password == admin_password

if is_admin:
    st.success("Admin access granted")

    # Input fields for intern details
    intern_name = st.text_input('Enter intern name:', 'Type here...', key='intern_name_input')
    date = st.date_input('Date:', key='date_input')
    in_time = st.time_input('In Time:', key='in_time_input')
    out_time = st.time_input('Out Time:', key='out_time_input')
    performance = st.slider('Performance (1 to 10):', 1, 10, 5, key='performance_slider')
    remarks = st.text_input('Remarks:', 'Type here...', key='remarks_input')

    # Button to submit data
    if st.button('Submit'):
        # Append the new record to a CSV file
        record = {
            'Name': intern_name,
            'Date': str(date),
            'In Time': str(in_time),
            'Out Time': str(out_time),
            'Performance': performance,
            'Remarks': remarks
        }
        record_df = pd.DataFrame([record])
        if os.path.exists('intern_records.csv'):
            record_df.to_csv('intern_records.csv', mode='a', header=False, index=False)
        else:
            record_df.to_csv('intern_records.csv', mode='w', header=True, index=False)
        st.success('Record added successfully!')

    # Display existing records with edit options
    st.write('### Intern Records')
    try:
        records_df = pd.read_csv('intern_records.csv')
        edited_df = st.data_editor(records_df, num_rows="dynamic")

        # Save the edited dataframe back to the CSV
        if st.button('Save Changes'):
            edited_df.to_csv('intern_records.csv', index=False)
            st.success('Changes saved successfully!')
    except FileNotFoundError:
        st.write('No records found. Please add some records.')

else:
    if password:
        st.error("Invalid admin password")
    # Display records in read-only mode
    st.write('### Intern Records')
    try:
        records_df = pd.read_csv('intern_records.csv')
        st.write(records_df)
    except FileNotFoundError:
        st.write('No records found. Please add some records.')

# Additional info
st.write("""
This is a simple interactive Streamlit app to manage and track intern records, including in-time, out-time, performance, and remarks on a daily basis.
""")

