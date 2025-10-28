
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Medals Visualization",
                   layout="wide")
st.title("Medals Visualization")
#Dropdown menu
medal = st.selectbox("Medal type", ["gold",'silver','bronze'])

#Checkboxes
show_bar = st.checkbox("Show Bar Chart", value = True)
show_pie = st.checkbox("Show Pie Chart", value = True)

#two-col structure
col1,col2 = st.columns(2)

#load the mdeal wide dataset
df = px.data.medals_wide()

#plot the bar chart

if show_bar:
  fig_bar = px.bar(df, x = "nation", y = f"{medal}", title = f"Medals Count ({medal})")
  fig_bar.update_layout(title = 0.5, xaxis_title = "Nation", yaxis_title = "Count", width = 300, height = 400)
  col1.plotly_chart(fig_bar, use_container_width = True)

#plot the pie chart
if show_pie:
  fig_pie = px.pie(df, values = f"{medal}", names = "nation", title = f"Medals Count ({medal})")
  fig_pie.update_layout(title = 0.5, width = 300, height = 400)
  col2.plotly_chart(fig_pie, use_container_width = True)
