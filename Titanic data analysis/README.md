 # Titanic data analysis

This repository contains my Titanic data analysis project using the classic Titanic dataset from Seaborn. The aim of this project was to clean, organize, and visually explore the data to uncover patterns and relationships — especially those that influenced survival outcomes.

## Project outcomes

- Load and explore the Titanic dataset
- Clean the data by removing or transforming missing and irrelevant values
- Create visual representations to better understand the relationships between variables
- Add features and draw meaningful insights through exploratory data analysis (EDA)

## Description

- **Cleaned tables** with added categorical columns for age, fare, and class
- **Visualizations** like histograms, bar charts, count plots, and heatmaps to analyze patterns
- **Feature engineering**, such as the creation of a `family_size` column
- A development file (`ex.1`) used for learning, notes, and step-by-step exploration

## Tools used 

- **Jupyter Notebook** -  combining code and commentary
- **Pandas** -  data manipulation
- **Seaborn** - data visualisation
- **Matplotlib** - plotting and customising graphs

## Key tasks & Highlights

### Dataset Overview
- Loaded the Titanic dataset via `sns.load_dataset('titanic')`
- Viewed the structure with `df.head()` and described numerical data with `df.describe()`
- Counted rows and columns to understand data shape: `891 rows × 15 columns`

### Data Cleaning
- Dropped rows with missing values
- Created new categorial columns:
  - `Age_Category` (Child, Young Adult, Adult, Senior)
  - `Fare_Category` (Low, Medium, High)
  - Cleaned `class` based on `pclass`
- Dropped irrelevant columsn such as 'deck','who','embark_town'

### Visualisation & Analysis
- **Age Distribution Histogram**  
  Showed most passengers were between 18–32 years old

- **Survivors by Gender Bar Plot**  
  Revealed that **more women survived** than men, nearly 2:1

- **Survivors by Passenger Class Count Plot**  
  Indicated that **first-class passengers had the highest survival rate**

- **Correlation Heatmap**  
  Showed:
  - Older passengers paid higher fares

### Feature Engineering

- Created a new column `family_size` = `sibsp + parch + 1`  
  This represented the total number of family members onboard (including the person themselves)

## File Structure

- `Titanic.ex` – Cleaned dataset and final analysis/visuals
- `ex.1` – Development notes and experimental analysis
- Images and plots were generated using matplotlib & seaborn

## License

MIT © 2023 Khan1021
