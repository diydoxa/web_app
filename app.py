import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="CSV Data Analysis App",
    layout="wide"
)

# Title
st.title("CSV Data Analysis App")
st.write("Upload a CSV file and analyze your dataset.")

# Upload CSV
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        # Read file
        df = pd.read_csv(uploaded_file)

        st.success("CSV file uploaded successfully!")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

        # Menu options
        option = st.selectbox(
            "Select an option",
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

            elif option == "Plot First Two Columns":
                st.subheader("Plot")

                if df.shape[1] < 2:
                    st.warning("Need at least 2 columns to plot.")
                else:
                    plot_df = df.iloc[:, :2].copy()

                    # Rename columns
                    plot_df.columns = ["X", "Y"]

                    # Convert second column to numeric
                    plot_df["Y"] = pd.to_numeric(
                        plot_df["Y"],
                        errors="coerce"
                    )

                    # Remove invalid rows
                    plot_df = plot_df.dropna()

                    if plot_df.empty:
                        st.warning("Second column must contain numeric values.")
                    else:
                        st.line_chart(
                            data=plot_df,
                            x="X",
                            y="Y"
                        )

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("Please upload a CSV file to begin.")