import streamlit as st
import plotly.express as px
import pandas as pd

# Load & transform sample Data
university = pd.read_csv('university_student_dashboard_data.csv')
university_long = pd.melt(
    university, 
    id_vars=['Year', 'Term', 'Applications', 'Admitted', 'Enrolled', 
             'Retention Rate (%)', 'Student Satisfaction (%)'],
    var_name="Department", 
    value_name="Enrolled Students"
)
university_long['Department'] = df_long['Department'].str.replace(" Enrolled", "")

# Streamlit App Title
st.title("📊 Applications, admission and enrollments in University")

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select Year:", int(university_long["Year"].min()), int(university_long["Year"].max()), int(university_long["Year"].min()))

# Filter data based on the selected year
filtered_df = university_long[university_long.Year == selected_year]

# Create four different plots

fig1 = px.line(university, x="Year", y="Applications", title="Number of applications with time")

fig2 = px.line(university, x="Year", y="Admitted", title="Number of admissions with time")

fig3 = px.line(university, x="Year", y="Enrolled", title="Number of enrollments with time")

fig4=px.bar(
    filtered_df, 
    x="Department", 
    y="Enrolled Students", 
    color="Term",
    text="Enrolled Students",
    title="Number of Enrolled Students by Department in 2015",
    color_discrete_map=color_map,  # Custom colors
    barmode="group"  # Grouped bars
)



# Arrange the plots in a grid layout
col1, col2, col3 = st.columns(3)  # Create 3 columns

with col1:
    st.plotly_chart(fig1, use_container_width=True)  # First plot in first column

with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Second plot in second column
with col3:
    st.plotly_chart(fig3, use_container_width=True)  # Third plot in third column

# Add the fourth plot in a full-width row below
st.plotly_chart(fig4, use_container_width=True)
