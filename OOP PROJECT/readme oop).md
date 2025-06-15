# Health Data Dashboard

This project is a **Streamlit-based interactive dashboard** that visualizes and analyzes health-related data, including blood pressure, temperature, heart rate, and more. The dashboard also allows basic risk checking based on user input.

---

## Features

- **Interactive Graphs:** Scatter plots, box plots, and histograms with customizable axes
- **Data Summary:** View raw dataset and descriptive statistics
- **User Controls:** Sliders, dropdowns, and checkboxes for filtering and customizing plots
- **Basic Risk Estimation:** Enter your vitals to see potential risk outcome (based on simple rule-based logic)

---

##  Dataset

The dataset used contains 64 rows of synthetic health data with features such as:

- Age, Weight, Height
- SystolicBP, DiastolicBP
- Heart Rate, Temperature
- DiseaseOutcome (0 = Low Risk, 1 = High Risk)

You can download the dataset here: [people\_data.csv](people_data.csv)

---

## How to Run

1. Make sure you have Streamlit and required libraries installed:

```bash
pip install streamlit pandas seaborn matplotlib
```

2. Run the dashboard:

```bash
streamlit run health_dashboard.py
```

---

## File Structure

```
├── health_dashboard.py     # Streamlit app
├── people_data.csv # Dataset
├── README.md               # Project overview
```

---

## Notes

- The "DiseaseOutcome" is generated based on rules involving high blood pressure and temperature.
- This dashboard is for demonstration/educational purposes only and not for clinical diagnosis.

---


