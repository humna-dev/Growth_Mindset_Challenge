<<<<<<< HEAD

import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📁File Converter & Cleaner", layout="wide")
st.title("📁File Converter & Cleaner")
st.write("**Upload Your CSV and Excel Files to Convert and Clean Data🚀**")
files = st.file_uploader("**Upload CSV or Excel Files**", type=["csv", "xlsx"], accept_multiple_files=True)
if files:
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())
        if st.checkbox(f"Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.write("**🎉 Missing Values Filled Successfully!**")
            st.dataframe(df.head())
        selected_columns = st.multiselect(f"**Select Columns - {file.name}**", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())
        st.write("**🎉 Data Cleaning Completed Successfully!**")

        if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        format_choice = st.radio(f"**💱 Convert {file.name} to:**", ["CSV", "Excel"], key=file.name)
        if st.button(f"📥 Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace("xlsx", "csv")
            else:
                df.to_excel(output, index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace("csv", "xlsx")
            output.seek(0)
            st.download_button(f"📩 Click Here to Download", file_name=new_name, data=output, mime=mime)
        st.success(f"🎉 Processed Successfully!")
=======

import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📁File Converter & Cleaner", layout="wide")
st.title("📁File Converter & Cleaner")
st.write("**Upload Your CSV and Excel Files to Convert and Clean Data🚀**")
files = st.file_uploader("**Upload CSV or Excel Files**", type=["csv", "xlsx"], accept_multiple_files=True)
if files:
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())
        if st.checkbox(f"Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.write("**🎉 Missing Values Filled Successfully!**")
            st.dataframe(df.head())
        selected_columns = st.multiselect(f"**Select Columns - {file.name}**", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())
        st.write("**🎉 Data Cleaning Completed Successfully!**")

        if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        format_choice = st.radio(f"**💱 Convert {file.name} to:**", ["CSV", "Excel"], key=file.name)
        if st.button(f"📥 Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace("xlsx", "csv")
            else:
                df.to_excel(output, index=False)
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace("csv", "xlsx")
            output.seek(0)
            st.download_button(f"📩 Click Here to Download", file_name=new_name, data=output, mime=mime)
        st.success(f"🎉 Processed Successfully!")
>>>>>>> e8356b63e81851f6d70a298d88a8bae93b9c4fd7
