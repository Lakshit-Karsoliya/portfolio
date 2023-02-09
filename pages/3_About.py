import streamlit as st 

st.set_page_config(page_title='I M GR8',layout='wide')
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css" integrity="sha512-SzlrxWUlpfuzQ+pcUCosxcglQRNAq/DZjVsC0lE40xsADsfeQoEypE+enwcOiGjk/bSuGGKHEyjSoQ1zVisanQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />',unsafe_allow_html=True)
css_file = "styles/style.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
st.title("About")
st.write('---')
col1,col2 = st.columns([1,2])
with col1:
    st.image('assets/profile-pic.png',width=200)
    st.markdown("<p class='sign'>LakshitKarsoliya</p>",unsafe_allow_html=True)
with col2:
    st.write('''
    #### Hey I'am Lakshit Karsoliya
    #### Intrigued by design , Photography , Art , Music , Food and even better Conversations

    #### Seeking to be Inspired , to envision the unlikely , to work hard for things that are worth it and to be surrounded by those who bring out the best in me.

    Mail : lakshitkumar220@gmail.com
    ''')
st.markdown('<button class="button"><a href="https://github.com/Lakshit-Karsoliya"><span><i class="fa-brands fa-github"></i></span></a></button><button class="button"><a href="https://www.linkedin.com/in/lakshit-karsoliya-b371751b8"><span><i class="fa-brands fa-linkedin-in"></i></span></a></button>', unsafe_allow_html=True)
st.write('')
st.write('---')
# st.write('''

#     Hey! \n
#     hope you find this program useful \n
#     Download exe file from 
#     -    🧾 https://github.com/Lakshit-Karsoliya/python-file-transfer \n
#     Download 👇 source code from 
#     -    🧾 https://github.com/Lakshit-Karsoliya/python-file-transfer \n

#     Connect With Me
#     -    🐈‍⬛ https://github.com/Lakshit-Karsoliya 
#     -    📧 lakshitkumar220@outlook.com 
# ''')
