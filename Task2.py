import pandas as pd

# Step 1: Load the CSV file into a Pandas DataFrame
df = pd.read_csv('01.Data Cleaning and Preprocessing.csv') 

# Step 2: View the first few rows of the DataFrame
print(df.head())

# Step 3: Filtering data based on conditions
# Example: Filter rows where a certain column meets a condition
filtered_df = df[df['ChipRate'] > 10]

# Step 4: Handling missing values
# Check for missing values
print(df.isnull().sum())

# Fill missing values with a specific value
df_filled = df.fillna(0)  # Replace NaNs with 0

# Drop rows with missing values
df_dropped = df.dropna()

# Step 5: Calculating summary statistics
mean_value = df['ChipRate'].mean()
median_value = df['ChipRate'].median()
min_value = df['ChipRate'].min()
max_value = df['ChipRate'].max()

# Step 6: View summary statistics for the DataFrame
print(df.describe())
