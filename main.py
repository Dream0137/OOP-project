import streamlit as st
from PIL import Image
import base64

bg_image_path = "R1.jpg"
with open(bg_image_path, "rb") as img_file:
    bg_image = img_file.read()
bg_image_base64 = base64.b64encode(bg_image).decode()
page_bg_img = f'''
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_image_base64}");
            background-size: cover;
        }}
    </style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def calculate_tire_size(W, S, d):
    D = (W * (S/100 * 2)) + d
    return D

# UI
st.title("คำนวณขนาดยาง")
W = st.number_input("ความกว้างของยาง (มิลลิเมตร)", min_value=1)
S = st.number_input("ซีรี่ยาง", min_value=1)
d = st.number_input("เส้นผ่าศูนย์กลางของล้อ (มิลลิเมตร)", min_value=1)

if st.button("คำนวณ"):
    tire_size = calculate_tire_size(W, S, d)
    st.write(f"ขนาดยางที่ได้: {tire_size:.2f} มิลลิเมตร")

st.markdown("""
  ### คำแนะนำ
  - ความกว้างของยาง (มิลลิเมตร)
  - ซีรี่ยาง
  - เส้นผ่าศูนย์กลางของล้อ (มิลลิเมตร)
  - ตัวอย่างข้อมูล195/55/15
  """)