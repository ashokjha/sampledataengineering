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

    @staticmethod
    def test2():
        import numpy as np

        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        surface = np.sin(np.sqrt(X**2 + Y**2))
        data = {
            "X": X.flatten(),
            "Y": Y.flatten(),
            "surface": surface.flatten(),
        }
        df = pd.DataFrame(data)
        print(df["X"])


if __name__ == "__main__":
    Test.test2()
