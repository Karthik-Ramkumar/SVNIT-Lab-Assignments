import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Part I: Frequency Analysis
    print("Part I: Frequency Analysis ")
    
    # Load the Titanic dataset
    df = pd.read_csv('titanic.csv')
    
    # Generate a frequency table for the passenger class
    # Calculate absolute frequency
    absolute_freq = df['pclass'].value_counts().sort_index()
    
    # Calculate relative frequency (%)
    relative_freq = df['pclass'].value_counts(normalize=True).sort_index() * 100
    
    # Calculate cumulative frequency
    cumulative_freq = absolute_freq.cumsum()
    
    freq_table = pd.DataFrame({
        'Absolute Frequency': absolute_freq,
        'Relative Frequency (%)': relative_freq,
        'Cumulative Frequency': cumulative_freq
    })
    print("\nFrequency Table for Passenger Class:")
    print(freq_table)

    # Part II: Probability Analysis
    print("\n Part II: Probability Analysis ")
    
    # Create a contingency table between Sex and Survived using pd.crosstab()
    contingency_table = pd.crosstab(df['sex'], df['survived'], margins=True, margins_name="Total")
    print("\nContingency Table (Sex vs Survived):")
    print(contingency_table)
    
    # Calculate joint probability
    joint_prob = pd.crosstab(df['sex'], df['survived'], normalize='all')
    print("\nJoint Probabilities:")
    print(joint_prob)
    
    # Calculate marginal probabilities
    marginal_prob_sex = df['sex'].value_counts(normalize=True)
    marginal_prob_survived = df['survived'].value_counts(normalize=True)
    print("\nMarginal Probabilities (Sex):")
    print(marginal_prob_sex)
    print("\nMarginal Probabilities (Survived):")
    print(marginal_prob_survived)
    
    # Calculate conditional probabilities
    cond_prob = pd.crosstab(df['sex'], df['survived'], normalize='index')
    print("\nConditional Probabilities P(Survived | Sex):")
    print(cond_prob)

    # Part III: Correlation Analysis
    print("\n Part III: Correlation Analysis")
    
    # Select the Age and Fare columns
    age_fare_df = df[['age', 'fare']].copy()
    
    # Handle missing values (dropping rows with missing Age or Fare)
    age_fare_df = age_fare_df.dropna()
    print(f"\nHandled missing values. Remaining rows: {len(age_fare_df)}")
    
    # Compute Pearson correlation
    pearson_corr = age_fare_df.corr(method='pearson')
    print("\nPearson Correlation (Age vs Fare):")
    print(pearson_corr)
    
    # Visualize the correlation using a heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(pearson_corr, annot=True, cmap='Greens', fmt=".2f", vmin=-1, vmax=1)
    plt.title('Pearson Correlation Heatmap (Age vs Fare)')
    plt.tight_layout()
    heatmap_filename = 'correlation_heatmap.png'
    plt.savefig(heatmap_filename)
    print(f"Saved heatmap to {heatmap_filename}")
    plt.close()
    
    # Plot a scatter plot for Age vs Fare
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=age_fare_df, x='age', y='fare', alpha=0.6)
    plt.title('Scatter Plot of Age vs Fare')
    plt.tight_layout()
    scatter_filename = 'scatter_age_fare.png'
    plt.savefig(scatter_filename)
    print(f"Saved scatter plot to {scatter_filename}")
    plt.close()

if __name__ == "__main__":
    main()
