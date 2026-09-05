import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 Data Analysis Toolkit")


# -------------------------
# CSV Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)


if uploaded_file:

    try:

        df = pd.read_csv(uploaded_file)

        st.success("CSV loaded successfully!")


        # -------------------------
        # Sidebar Filter
        # -------------------------

        st.sidebar.header("Data Filter")

        filter_column = st.sidebar.selectbox(
            "Choose a column",
            df.columns
        )

        filter_values = st.sidebar.multiselect(
            "Choose values",
            df[filter_column].dropna().unique()
        )

        if filter_values:

            df = df[
                df[filter_column].isin(filter_values)
            ]


        # -------------------------
        # Dataset Information
        # -------------------------

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        with col3:
            st.metric(
                "Missing Values",
                df.isnull().sum().sum()
            )


        # -------------------------
        # Data Preview
        # -------------------------

        st.subheader("Data Preview")

        rows = st.slider(
            "Number of rows to display",
            min_value=5,
            max_value=50,
            value=10
        )

        st.dataframe(df.head(rows))


        # -------------------------
        # Statistics
        # -------------------------

        st.subheader("Statistics")

        st.dataframe(df.describe())


        # -------------------------
        # Chart Section
        # -------------------------

        st.subheader("📈 Create a Chart")

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()


        if len(numeric_columns) == 0:

            st.warning(
                "No numeric columns are available for charting."
            )

        else:

            chart_type = st.selectbox(
                "Choose a chart",
                [
                    "Bar Chart",
                    "Line Chart",
                    "Scatter Chart",
                    "Histogram"
                ]
            )


            # Histogram only needs one numeric column

            if chart_type == "Histogram":

                x_column = st.selectbox(
                    "Choose column",
                    numeric_columns
                )

                fig = px.histogram(
                    df,
                    x=x_column
                )


            # Other charts need at least two numeric columns

            elif len(numeric_columns) >= 2:

                x_column = st.selectbox(
                    "Choose X-axis",
                    numeric_columns
                )

                y_column = st.selectbox(
                    "Choose Y-axis",
                    numeric_columns
                )


                if chart_type == "Bar Chart":

                    fig = px.bar(
                        df,
                        x=x_column,
                        y=y_column
                    )

                elif chart_type == "Line Chart":

                    fig = px.line(
                        df,
                        x=x_column,
                        y=y_column
                    )

                else:

                    fig = px.scatter(
                        df,
                        x=x_column,
                        y=y_column
                    )


            else:

                fig = None

                st.warning(
                    "Bar, Line, and Scatter charts require "
                    "at least two numeric columns."
                )


            # Display chart

            if fig is not None:

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


        # -------------------------
        # Download Processed CSV
        # -------------------------

        st.subheader("💾 Download Data")

        processed_csv = df.to_csv(
            index=False
        )

        st.download_button(
            label="⬇️ Download Processed CSV",
            data=processed_csv,
            file_name="processed_data.csv",
            mime="text/csv"
        )


    except Exception as e:

        st.error(
            f"Could not read the CSV: {e}"
        )