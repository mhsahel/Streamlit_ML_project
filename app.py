
import streamlit as st
from PIL import Image
from api_calling import note_generator as nt , quize_generator as qz
st.title("sahel's vision........")
st.title("Note Summary and quize Generator")
st.write("Upload upto 3 images to generate Note summary and quizes")
st.divider()
with st.sidebar:
    images = st.file_uploader("upload your images: ", type = ['jpg','jpeg','png'], accept_multiple_files= True)
    pil_image = []
    for img in images:
        pil_img = Image.open(img)
        pil_image.append(pil_img)
    if images :
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("uploaded images")
            col= st.columns(len(images))
            for i , img in enumerate(images):
                with col[i]:
                    st.image(img)
                        
        
    select = st.selectbox("Enter the difficulty of Quize", ("Easy","Medium","Hard") ,  index = None)  
        
    press = st.button("Click the button to initiate AI", type = "primary") 
    

if press:
    if not images:
        st.error("upload atleast 1 image")
    if not select:
        st.error("you must select atleast 1 options")    

    if images and select :
        with st.container(border = True):
            st.subheader("YOUR NOTE")
            
            with st.spinner("AI is writing notes for you.."):
                 
                 notes = nt(pil_image)
                 st.text(notes)
                
        
            
        # with st.container(border = True):
        #     st.subheader("AUDIO TRANSCRIPTION")
        #     st.text("audio transcription will be upload here soon")           
        with st.container(border = True):
            st.subheader(f"Quize {select} level difficulty show below")
            with st.spinner("Quizzes are making..."):
                quizes = qz(pil_image,select)
                st.text(quizes)
            
                 