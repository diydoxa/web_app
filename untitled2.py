import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Data Analysis App", layout="wide")

st.title("CSV Data Analysis App")
st.markdown("Upload a CSV file and analyze it easily.")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("CSV file uploaded successfully.")
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

        # Dropdown options
        option = st.selectbox(
            "Choose an option",
            [
                "Show First 5 Rows",
                "Show Last 5 Rows",
                "Show Column Names",
                "Show Shape",
                "Show Summary",
                "Plot First Two Columns"
            ]
        )

        if st.button("Run Option"):
            if option == "Show First 5 Rows":
                st.dataframe(df.head())

            elif option == "Show Last 5 Rows":
                st.dataframe(df.tail())

            elif option == "Show Column Names":
                st.write(list(df.columns))

            elif option == "Show Shape":
                st.write(f"Rows: {df.shape[0]}")
                st.write(f"Columns: {df.shape[1]}")

            elif option == "Show Summary":
                st.dataframe(df.describe())

            elif option == "Plot First Two Columns":
                if df.shape[1] < 2:
                    st.warning("Need at least 2 columns to plot.")
                else:
                    fig, ax = plt.subplots(figsize=(6, 4))
                    ax.plot(df.iloc[:, 0], df.iloc[:, 1])
                    ax.set_title("Simple Plot")
                    ax.set_xlabel(df.columns[0])
                    ax.set_ylabel(df.columns[1])
                    st.pyplot(fig)

    except Exception as e:
        st.error(f"Could not read file: {e}")
else:
    st.info("Please upload a CSV file to begin.")
