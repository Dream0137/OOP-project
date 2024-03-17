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

def calculate_air_pressure(tire_size, vehicle_weight):
    air_pressure_needed = tire_size / vehicle_weight * 10  
    return air_pressure_needed

# UI
st.title("คำนวณการเติมลมยาง")
cols = st.columns(2)
with cols[0]:
    tire_size = st.number_input("ขนาดยาง (หน่วย: นิ้ว)", min_value=1.0, step=0.1)

with cols[1]:
    vehicle_weight = st.number_input("น้ำหนักของรถ (หน่วย: กิโลกรัม)", min_value=1.0, step=0.1)

if st.button("คำนวณ"):
    air_pressure_needed = calculate_air_pressure(tire_size, vehicle_weight)
    st.write(f"ค่าลมยางที่ต้องใช้: {air_pressure_needed} psi")
