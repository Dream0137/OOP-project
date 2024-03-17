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

def calculate_air_pressure(tire_width, aspect_ratio, rim_diameter):
    # แปลงหน่วยของ rim diameter จาก นิ้ว เป็น เซนติเมตร
    rim_diameter_cm = rim_diameter * 2.54
    # คำนวณค่าลมยาง
    air_pressure_needed = 0.0193 * tire_width + 0.073 * aspect_ratio + 0.118 * rim_diameter_cm - 2.98
    return air_pressure_needed

# UI
st.title("คำนวณการเติมลมยาง")
tire_width = st.number_input("ความกว้างของยาง (มิลลิเมตร)", min_value=1)
aspect_ratio = st.number_input("อัตราส่วนความสูงของแก้มยางต่อความกว้างหน้ายาง", min_value=1)
rim_diameter = st.number_input("เส้นผ่านศูนย์กลางยาง (นิ้ว)", min_value=1)

if st.button("คำนวณ"):
    air_pressure_needed = calculate_air_pressure(tire_size, vehicle_weight)
    st.write(f"ค่าลมยางที่ต้องใช้: {air_pressure_needed} psi")

st.markdown("""
  ### คำแนะนำ
  - เส้นผ่านศูนย์กลางยาง (นิ้ว) ความกว้างของยาง (มิลลิเมตร)
  - อัตราส่วนความสูงของแก้มยางต่อความกว้างหน้ายาง
  - เส้นผ่านศูนย์กลางยาง (นิ้ว)
  - ใช้ได้กับยางรถจักรยานยนต์เท่านั้น
  """)