import streamlit as st
import pandas as pd
import numpy as np
import time

# Title of the app
st.title('Simple Interactive Dashboard')

# Text input widget
name = st.text_input('Enter your name:', 'Type here...', key='name_input')
st.write(f'Hello, {name}!')

# Slider widget
age = st.slider('Select your age:', 0, 100, 25, key='age_slider')
st.write(f'You are {age} years old.')

# Select box widget
options = ['Python', 'Java', 'C++', 'JavaScript']
language = st.selectbox('What is your favorite programming language?', options, key='language_select')
st.write(f'You selected: {language}')

# Checkbox widget
if st.checkbox('Show line chart', key='show_chart_checkbox'):
    # Generate some data for the line chart
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

# Progress bar widget
st.write('Progress Bar Example')
progress_bar = st.progress(0)
for i in range(101):
    time.sleep(0.01)
    progress_bar.progress(i)

# Expander widget
with st.expander('See explanation'):
    st.write("""
        This is a simple interactive Streamlit app to demonstrate various widgets.
        You can enter your name, select your age, choose your favorite programming language,
        and see a line chart if you select the checkbox.
    """)

# Sidebar widgets
st.sidebar.header('Sidebar Controls')
sidebar_name = st.sidebar.text_input('Enter your name:', 'Type here...', key='sidebar_name_input')
st.sidebar.write(f'Hello, {sidebar_name} from the sidebar!')

sidebar_age = st.sidebar.slider('Select your age:', 0, 100, 25, key='sidebar_age_slider')
st.sidebar.write(f'You are {sidebar_age} years old.')

sidebar_language = st.sidebar.selectbox('What is your favorite programming language?', options, key='sidebar_language_select')
st.sidebar.write(f'You selected: {sidebar_language}')

# Displaying dataframe
st.write('Random Dataframe')
data = pd.DataFrame({
    'first column': np.random.randn(10),
    'second column': np.random.randn(10)
})
st.write(data)

