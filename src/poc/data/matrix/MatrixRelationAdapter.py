import pandas as pd
import numpy as np


class MatrixRelationAdapter:

    # 1. HeatMap
    @staticmethod
    def heatMapData() -> pd.DataFrame:
        """
        Heatmap data

        Returns:
            pd.DataFrame: _description_
        """
        np.random.seed(42)
        # Create a correlation-like matrix dataset
        data = np.random.rand(5, 5)
        cols = ["Feature A", "Feature B", "Feature C", "Feature D", "Feature E"]
        df_matrix = pd.DataFrame(data, columns=cols, index=cols)
        return df_matrix

    # 2. hierarchical clustering
    @staticmethod
    def clusterData() -> pd.DataFrame:
        """hierarchical clustering
        Returns:
            pd.DataFrame: _description_
        """
        # Create a sample 10x10 matrix with patterns
        np.random.seed(42)
        clusterdata = np.random.rand(10, 10)
        clusterdata[:5, :5] += 2  # Create a distinct visual cluster

        clusterdf = pd.DataFrame(
            clusterdata,
            columns=[f"Col_{i}" for i in range(10)],
            index=[f"Row_{i}" for i in range(10)],
        )
        return clusterdf

    # 3. sankey
    @staticmethod
    def sankeyFlowData() -> pd.DataFrame:
        """Sankey Data to Visualizes flows and volumes

        Returns:
             pd.DataFrame: _description_
        """
        # Long-form data for flow/relationship visualizations
        df_flow = pd.DataFrame(
            {
                "Source": ["A", "A", "B", "B", "C"],
                "Target": ["X", "Y", "X", "Z", "Y"],
                "Value": [10, 20, 15, 5, 25],
            }
        )
        return df_flow

    # 4. Chord Diagram
    @staticmethod
    def chordData() -> pd.DataFrame:
        """hierarchical clustering
        Returns:
            pd.DataFrame: _description_
        """
        departments = [
            "Engineering",
            "Product",
            "Design",
            "Data Science",
            "Marketing",
            "Sales",
            "Customer Success",
            "HR",
            "Finance",
            "Legal",
        ]
        n = len(departments)

        np.random.seed(42)
        matrix = np.random.randint(5, 25, size=(n, n))

        matrix[0, 1] = matrix[1, 0] = 114
        matrix[1, 2] = matrix[2, 1] = 77
        matrix[0, 2] = matrix[2, 0] = 71
        matrix[4, 5] = matrix[5, 4] = 102
        matrix[5, 6] = matrix[6, 5] = 84
        np.fill_diagonal(matrix, 0)
        chord_matrix = pd.DataFrame(matrix, columns=departments, index=departments)
        return chord_matrix


if __name__ == "__main__":
    print(MatrixRelationAdapter.heatMapData())
