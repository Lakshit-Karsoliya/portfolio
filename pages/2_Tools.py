import streamlit as st 

st.set_page_config(page_title='I M GR8')
css_file = "styles/style.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
st.title("Tools and Projects")
items = [#image,description,link
    [
        "Reverse image search(car)", 
        "https://www.competethemes.com/wp-content/uploads/2022/01/reverse-image-search-seo-tools.png",
        "This is a reverse image search tool it search the top similar image from the database that resembles the uploaded image streamlit provide wheels to this project.",
        "https://github.com/Lakshit-Karsoliya/carReverseImageSearch"
    ],
    [
        'python file transfer',
        'https://www.aetechgroup.com/wp-content/uploads/2015/03/best-options-to-transfer-files-from-one-computer-to-another.jpg',
        'It,s a file transfer tool used to transfer files from one pc to another pc in a LAN connected via wifi or ethrnet this program is written in python uses socket,tqdm and click-shell module. It is a CLI version. If you dont have python installed on your system just install .exe file by click on "get" button.',
        'https://github.com/Lakshit-Karsoliya/python-file-transfer'
    ],
    [
        'GUI image classifier',
        'https://miro.medium.com/max/1000/0*j961qCylc0GLW51h.png',
        "It's a GUI image classifier User can capture two types of classes and nural network figures out the input class in a interactive tkinter GUI",
        'https://github.com/Lakshit-Karsoliya/image_classifier_gui'
    ],
    [
        'Movie recommendation system',
        "https://149695847.v2.pressablecdn.com/wp-content/uploads/2020/08/stars-movies-1200x670-1.jpg",
        "It's a Movie recommendation system basend on Content based recommendation systems this project use streamlit as to show power of transferred learning",
        "https://github.com/Lakshit-Karsoliya/recommendation_system/tree/main/Movie%20Recommendation%20System"
    ],
    [
        'Song recommendation system',
        "https://repository-images.githubusercontent.com/481851510/24e876a4-5f85-4c10-8b12-7638b49d6179",
        "It's a Movie recommendation system basend on Content based recommendation systems this project use streamlit as to show power of transferred learning",
        "https://github.com/Lakshit-Karsoliya/recommendation_system/tree/main/songRecommendationSystem"
    ],
    [
        'Django Blog project',
        "https://images.ctfassets.net/23aumh6u8s0i/6ubUHRD1qfolOVHxiBfjZ7/4e704f48dc5b0104d0c380fec1fe9b9e/django",
        "It is a django blog project it's aim to show CRUD operation in database ",
        "https://github.com/Lakshit-Karsoliya/django-Blog_project"
    ]

]
st.write(f"Currently we have {len(items)} tools and projects")
st.write('---')
for item in items:
    col1,col2 = st.columns(2)
    with col1:
        st.write(f'***{item[0]}***')
        st.image(item[1],width=250)
    with col2:
        st.write(item[2])
        st.markdown(f'<a href="{item[3]}">Get👇</a>', unsafe_allow_html=True)
    st.write('---')
