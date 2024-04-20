from pandasAi import pandasAi
import streamlit as st
import os
class Home:
    def __init__(self):
        self.pd = pandasAi()
        st.title("Upload CSV file and ask query.")
    def render(self):
        st.sidebar.markdown(f"""{open('components/about.html').read()}""", unsafe_allow_html=True)
        data = st.file_uploader("Upload CSV File", type=["csv"])
        query = st.text_area("Type query")
        if st.button("Submit Query", type="primary"):
            with st.spinner('Loading...'):
                try:
                    self.pd.createAgent(data)
                    response = self.pd.query(query+'.')
                    if type(response) == str and '.png' in response:
                        st.markdown(
                            '''<h4>Result:</h4>''',
                            unsafe_allow_html=True)
                        st.image(response)
                        file_path = 'exports/charts/temp_chart.png'
                        if os.path.exists(file_path):
                            os.remove(file_path)

                    elif type(response) == str and 'Unfortunately, I was not able to answer your question, because of the following error:' in response:
                        st.markdown(
                            '''<div style="border-radius: .5rem;background: #ff00001a;padding: 1rem;color: rgb(55, 59, 55);font-size: 24px;"><span>⚠️ Some error occurred! Please recheck the query and try again.</span></div>''',
                            unsafe_allow_html=True)
                    else:
                        st.markdown(
                            '''<h4>Result:</h4>''',
                            unsafe_allow_html=True)
                        st.write(response)
                except Exception as e:
                    st.markdown(
                        '''<div style="border-radius: .5rem;background: #ff00001a;padding: 1rem;color: rgb(55, 59, 55);font-size: 24px;"><span>⚠️ Some error occurred! Please recheck the query and try again.</span></div>''',
                        unsafe_allow_html=True)


if __name__ == '__main__':
    home = Home()
    home.render()
