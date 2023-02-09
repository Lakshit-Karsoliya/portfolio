import streamlit as st 

st.set_page_config(page_title='I M GR8',layout='wide')
css_file = "styles/style.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

with st.container():
    st.title('')
    st.markdown("<p class='tagLineMinor'>I am here to create meaningful and lasting relationship with you.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:50px' class='tagLineMinor'>Let's build something amazing togather</p>", unsafe_allow_html=True)
    
    # st.title("Let's build something amazing togather")
    # st.header("LAKSHIT KARSOLIY")
    st.write('''#''')
    st.write('''#''')
    st.write('''#''')
    st.subheader('As an independent developer My aim is to provide some very useful tools and programs that make daily hustle bit easy')
    st.subheader('I make programs , cli tools that are simple beautyful and easy to use.')
    st.markdown('<button class="button"><a href="/Tools" target="_self"><span>Explore</span></a></button>', unsafe_allow_html=True)



