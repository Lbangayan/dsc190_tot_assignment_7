import marimo

__generated_with = "0.4.0"
app = marimo.App()

@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    return pd, plt

@app.cell
def _(pd):
    # Load the final features dataset
    df = pd.read_csv("data/features/events.csv")
    return df,

@app.cell
def _(df, plt):
    # Produce the histogram of duration_minutes
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df["duration_minutes"], bins=40, color="skyblue", edgecolor="black")
    
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (Minutes)")
    ax.set_ylabel("Frequency")
    
    # Output the figure to render it in Marimo
    fig
    return ax, fig

if __name__ == "__main__":
    app.run()
