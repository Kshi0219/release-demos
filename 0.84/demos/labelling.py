import os
import random

import streamlit as st


def show():
    st.write(
        """
        ## 🐾 Data Labelling
        
        This is one for all machine learning fans: Label some images and all of your 
        annotations are preserved in `st.session_state`!
        """
    )

    script_path = os.path.dirname(__file__)
    st.write(script_path)
    rel_path = "images"
    abs_file_path = script_path + "/" + rel_path
    files = os.listdir(abs_file_path)
    st.write(files)

    if "annotations" not in st.session_state:
        st.session_state.annotations = {}
        st.session_state.files = files
        st.session_state.current_image = "cat.1.jpg"

    def annotate(label):
        st.session_state.annotations[st.session_state.current_image] = label
        if st.session_state.files:
            st.session_state.current_image = random.choice(st.session_state.files)
            st.session_state.files.remove(st.session_state.current_image)

    image_path = abs_file_path + "/" + st.session_state.current_image

    st.write("")
    col1, col2 = st.beta_columns(2)
    st.write(image_path)
    col1.image(image_path, width=300)
    with col2:
        if st.session_state.files:
            st.write(
                "Annotated:",
                len(st.session_state.annotations),
                "– Remaining:",
                len(st.session_state.files),
            )
            st.button("This is a dog! 🐶", on_click=annotate, args=("dog",))
            st.button("This is a cat! 🐱", on_click=annotate, args=("cat",))
        else:
            st.success(
                f"🎈 Done! All {len(st.session_state.annotations)} images annotated."
            )
        st.write("### Annotations")
        st.write(st.session_state.annotations)

    st.write(st.session_state.files)


if __name__ == "__main__":
    show()