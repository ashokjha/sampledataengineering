
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np


class Distribution:
    """ <b>Statistical & Distribution Charts:</b>
        Best libraries: <b>Seaborn</b> or <b>Matplotlib</b>
        <ul> <b>Histogram:</b> Visualizes the distribution of a single continuous variable.</ul>
        <ul> <b>Box Plot:</b> Displays the median, quartiles, and outliers of a dataset.</ul>
        <ul> <b>Violin Plot:</b> Combines a box plot with a kernel density plot to show data shape.</ul>        
        <ul> <b>Density Plot (KDE):</b> Shows the probability density function of the data.</ul>
        <ul> <b>Strip / Swarm Plot:</b> Plots every individual data point to show exact distribution.</ul>
        <ul> <b>Error Bar Chart: </b> Shows error or uncertainty along with the main data points.</ul>
    """

    # Generate fake data for demonstration
    def get_sample_data(self):
        np.random.seed(42)
        data = {
            'Value': np.random.normal(loc=50, scale=10, size=500),
            'Category': np.random.choice(['Group A', 'Group B', 'Group C'], size=500)
        }
        return pd.DataFrame(data)

    def render_histogram(self, df, column):
        """Generates both a static and interactive Histogram."""
        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(data=df, x=column, kde=True, ax=ax, color='#1f77b4')
        ax.set_title(f"Static Histogram of {column}")
        
        # 2. Interactive (Plotly)
        fig_interactive = px.histogram(
            df, x=column, marginal="rug", 
            title=f"Interactive Histogram of {column}",
            color_discrete_sequence=['#1f77b4']
        )
        
        return fig_static, fig_interactive

    def render_boxplot(self, df, x_col, y_col):
        """Generates both a static and interactive Box Plot."""
        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x=x_col, y=y_col, ax=ax, palette="Set2")
        ax.set_title(f"Static Box Plot: {y_col} by {x_col}")
        
        # 2. Interactive (Plotly)
        fig_interactive = px.box(
            df, x=x_col, y=y_col, color=x_col,
            title=f"Interactive Box Plot: {y_col} by {x_col}",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        
        return fig_static, fig_interactive

    def render_violinplot(self, df, x_col, y_col):
        """Generates both a static and interactive Violin Plot."""
        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.violinplot(data=df, x=x_col, y=y_col, ax=ax, palette="Pastel1")
        ax.set_title(f"Static Violin Plot: {y_col} by {x_col}")
        
        # 2. Interactive (Plotly)
        fig_interactive = px.violin(
            df, x=x_col, y=y_col, color=x_col, box=True, points="all",
            title=f"Interactive Violin Plot: {y_col} by {x_col}",
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )
        
        return fig_static, fig_interactive
    

    def render_density_plot(self, df, column):
        """Generates both a static and interactive Density Plot (KDE)."""
        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.kdeplot(data=df, x=column, fill=True, color='#2ca02c', alpha=0.5, ax=ax)
        ax.set_title(f"Static Density Plot (KDE) of {column}")
        
        # 2. Interactive (Plotly)
        # Plotly doesn't have a native continuous KDE line, so we use a histogram with probability density
        fig_interactive = px.histogram(
            df, x=column, histnorm='probability density', 
            title=f"Interactive Density Plot of {column}",
            color_discrete_sequence=['#2ca02c']
        )
        
        return fig_static, fig_interactive

    def render_swarm_plot(self, df, x_col, y_col):
        """Generates both a static and interactive Strip/Swarm Plot."""
        # 1. Static (Seaborn Strip Plot - cleaner for larger data than pure Swarm)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.stripplot(data=df, x=x_col, y=y_col, jitter=True, size=5, ax=ax, palette="Dark2", hue=x_col, legend=False)
        ax.set_title(f"Static Strip Plot: {y_col} by {x_col}")
        
        # 2. Interactive (Plotly Strip)
        fig_interactive = px.strip(
            df, x=x_col, y=y_col, color=x_col,
            title=f"Interactive Strip Plot: {y_col} by {x_col}",
            color_discrete_sequence=px.colors.qualitative.Dark2
        )
        
        return fig_static, fig_interactive

    def render_error_bar_chart(self, df, x_col, y_col):
        """Generates an Error Bar Chart showing averages and standard deviations."""
        # Calculate group aggregates for error calculation
        summary = df.groupby(x_col)[y_col].agg(['mean', 'std']).reset_index()
        
        # 1. Static (Matplotlib / Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        ax.errorbar(
            x=summary[x_col], y=summary['mean'], yerr=summary['std'], 
            fmt='o', color='#d62728', ecolor='black', elinewidth=2, capsize=5, ms=8
        )
        ax.set_title(f"Static Error Bar Chart (Mean ± SD) of {y_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(f"Mean {y_col}")
        
        # 2. Interactive (Plotly)
        fig_interactive = px.scatter(
            summary, x=x_col, y='mean', error_y='std',
            title=f"Interactive Error Bar Chart (Mean ± SD) of {y_col}",
            color_discrete_sequence=['#d62728']
        )
        fig_interactive.update_traces(marker=dict(size=10))
        
        return fig_static, fig_interactive
        