import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page title
st.title("Health Data Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("people_data.csv")

df = load_data()

st.sidebar.header("Customize View")

# Show data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Dataset")
    st.write(df)

# Show basic statistics
if st.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(df.describe())

# User input for filtering
st.sidebar.subheader("Filter Data")
min_age, max_age = st.sidebar.slider("Select Age Range", int(df.Age.min()), int(df.Age.max()), (20, 60))
filtered_df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]

# Dropdown for selecting X and Y axes
st.sidebar.subheader("Plot Settings")
x_axis = st.sidebar.selectbox("X-axis", df.columns.drop(['ID', 'DiseaseOutcome']))
y_axis = st.sidebar.selectbox("Y-axis", df.columns.drop(['ID', 'DiseaseOutcome']))

# Choose graph type
plot_type = st.sidebar.radio("Select Plot Type", ["Scatter Plot", "Box Plot", "Histogram"])

# Create plots
st.subheader("Graph")
plt.figure(figsize=(8, 5))
if plot_type == "Scatter Plot":
    sns.scatterplot(data=filtered_df, x=x_axis, y=y_axis, hue="DiseaseOutcome")
elif plot_type == "Box Plot":
    sns.boxplot(data=filtered_df, x="DiseaseOutcome", y=y_axis)
elif plot_type == "Histogram":
    sns.histplot(data=filtered_df, x=x_axis, hue="DiseaseOutcome", kde=True)
st.pyplot(plt.gcf())

# User input section for prediction-like interaction
st.subheader("User Input: Check Risk")
age_input = st.slider("Age", 20, 80, 30)
sbp_input = st.slider("Systolic BP", 90, 180, 120)
dbp_input = st.slider("Diastolic BP", 60, 120, 80)
temp_input = st.slider("Temperature (°F)", 95.0, 105.0, 98.6)

risk = 1 if (sbp_input > 130 or dbp_input > 85 or temp_input > 99.5) else 0

st.write("### Predicted Disease Outcome:", "High Risk (1)" if risk == 1 else "Low Risk (0)")
