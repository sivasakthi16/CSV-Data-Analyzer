import streamlit as st
st.sidebar.markdown(f"""{open('components/about.html').read()}""", unsafe_allow_html=True)
st.title("How to use?")
with st.container(border=None):
    st.markdown('''
        <h2 style="color:rgb(55 59 55);font-size:24px;">➡️Selecting CSV file</h2>''', unsafe_allow_html=True)
    st.markdown('''<p><span style="color:black;font-weight: bolder;">Query: </span>Click Browse files button and select a csv file.</p>''', unsafe_allow_html=True)
    with st.container(border=True):
        with st.spinner('Loading Image...'):
            st.image('pages/images/browse.png')

with st.container(border=None):
    st.markdown('''
        <h2 style="color:rgb(55 59 55);font-size:24px;">➡️Performing statistical analysis on the data</h2>'''
                , unsafe_allow_html=True)
    st.markdown('''<p><span style="color:black;font-weight: bolder;">Query: </span>Calculate mean of price</p>''', unsafe_allow_html=True)
    with st.container(border=True):
        with st.spinner('Loading Image...'):
            st.image('pages/images/mean.png')
    st.markdown('''<p><span style="color:black;font-weight: bolder;">Query: </span>Calculate median, mode and standard deviation of price</p>''', unsafe_allow_html=True)
    with st.container(border=True):
        with st.spinner('Loading Image...'):
            st.image('pages/images/describe.png')

with st.container(border=None):
    st.markdown('''
        <h2 style="color:rgb(55 59 55);font-size:24px;">➡️Plotting Graph</h2>'''
                , unsafe_allow_html=True)
    st.markdown('''<p><span style="color:black;font-weight: bolder;">Query: </span>Plot a bar graph for houses bedrooms</p>''', unsafe_allow_html=True)
    with st.container(border=True):
        with st.spinner('Loading Image...'):
            st.image('pages/images/bar.png')
    st.markdown('''<p><span style="color:black;font-weight: bolder;">Query: </span>Plot a histogram for house prices.</p>''', unsafe_allow_html=True)
    with st.container(border=True):
        with st.spinner('Loading Image...'):
            st.image('pages/images/hist.png')

with st.container(border=None):
    st.markdown('''
        <h2 style="color:rgb(55 59 55);font-size:24px;">➡️Filtering data</h2>'''
                , unsafe_allow_html=True)
    st.markdown('''<p><span style="color:black;font-weight: bolder;">Query: </span>Show me top 5 houses with highest price</p>''', unsafe_allow_html=True)
    with st.container(border=True):
        with st.spinner('Loading Image...'):
            st.image('pages/images/filter.png')