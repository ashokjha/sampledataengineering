import json
import matplotlib.pyplot as plt
import pandas as pd


class Test:
    @staticmethod
    def test1():
        import matplotlib.pyplot as plt
        import pandas as pd
        from pandas.plotting import parallel_coordinates
        import seaborn as sns

        # Load sample dataset
        df = sns.load_dataset("iris")

        # Create the static parallel coordinates plot
        plt.figure(figsize=(10, 6))
        parallel_coordinates(df, class_column="species", colormap="Set2", linewidth=1.5)

        # Styling and showing the plot
        plt.title("Static Parallel Coordinates Plot (Iris Dataset)", fontsize=14)
        plt.xlabel("Features")
        plt.ylabel("Values")
        plt.grid(True, alpha=0.3)
        plt.show()


if __name__ == "__main__":
    Test.test1()
