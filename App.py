import streamlit as st
import openai
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from io import BytesIO
import base64

def generate_comment(image_description):
    api_key = "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" 
    openai.api_key = api_key
    prompt_text = f"This is an image of {image_description}. Can you describe it?"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

st.title('Real Estate Prediction')


uploaded_file = st.file_uploader("Upload File.CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Loaded File.csv:")
    st.write(data.head())
    st.sidebar.header('Lựa chọn mô hình ML')

    model_choice = st.sidebar.selectbox("Chọn mô hình ML", ['XGBoost'])

    st.header('Dashboard')

    dashboard_image = "DashboardRealEstateTotalDetails.png"  
    st.image(dashboard_image, caption='Dashboard Real Estate Total Details', use_column_width=True)
    

    if st.button("Generate Dashboard Total Details Comment"):
        img1_info = "Hình ảnh cho thấy sự phân bổ các loại hình bất động sản, tỷ lệ giữa các loại hình bất động sản của 5 thành phố"
        generated_comment = generate_comment(img1_info)
        st.write("Comment from chat gpt:", generated_comment)
        print("Comment", generate_comment(img1_info))
    dashboard_image2 = "DistributionDashboard.png"
    st.image(dashboard_image2, caption='Dashboard of Distribution', use_column_width=True)
    
    if st.button("Generate Dashboard of Distribution"):
        img2_info ="Hình ảnh cho thấy sự phân bổ số lượng phòng ngủ, phòng tắm, diện tích và giá cả"
        generated_comment = generate_comment(img2_info)
        st.write("Comment from chat gpt:", generated_comment)
        print("Comment", generate_comment(img2_info))



