import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="CSV Data Analysis App",
    layout="wide"
)

# Title
st.title("CSV Data Analysis App")
st.write("Upload a CSV file and analyze your data.")

# File uploader (replaces filedialog)
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        # Read CSV
        df = pd.read_csv(uploaded_file)

        st.success("CSV file uploaded successfully!")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

        # Dropdown menu
        option = st.selectbox(
            "Choose an option",
            [
                "Show First 5 Rows",
                "Show Last 5 Rows",
                "Show Column Names",
                "Show Shape",
                "Show Summary"
            ]
        )

        # Run button
        if st.button("Run Option"):

            if option == "Show First 5 Rows":
                st.subheader("First 5 Rows")
                st.dataframe(df.head())

            elif option == "Show Last 5 Rows":
                st.subheader("Last 5 Rows")
                st.dataframe(df.tail())

            elif option == "Show Column Names":
                st.subheader("Column Names")
                st.write(df.columns.tolist())

            elif option == "Show Shape":
                st.subheader("Dataset Shape")
                st.write(f"Rows: {df.shape[0]}")
                st.write(f"Columns: {df.shape[1]}")

            elif option == "Show Summary":
                st.subheader("Summary Statistics")
                st.dataframe(df.describe())

    except Exception as e:
        st.error(f"Could not read file: {e}")

else:
    st.info("Please upload a CSV file first.")