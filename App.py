
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

    dashboard_image2 = "DistributionDashboard.png"
    st.image(dashboard_image2, caption='Dashboard of Distribution', use_column_width=True)
    
 


