

import logging


class persist_in_csv:
    """
    A class to persist data in CSV format.
    """

    def __init__(self):
        """
        Initializes the PersistInCsv class.
        """
        self.logger = logging.getLogger(__name__)

    def persist(self, df, file_path):
        """
        Persist the DataFrame to a CSV file.

        Args:
            df (pd.DataFrame): The DataFrame to persist.
            file_path (str): The path to the CSV file where the DataFrame will be saved.
        """
        try:
            df.to_csv(file_path, index=False)
            self.logger.info("Data persisted to CSV at: %s", file_path)
        except Exception as e:
            self.logger.error("Error persisting data to CSV: %s", e)
    