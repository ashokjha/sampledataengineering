# Sample Data Engineering

* **Create and activate virtual environment:**
  ```bash
  python -m venv .deenv
  .deenv\bin\activate.ps1  # Windows PowerShell
  source .deenv/bin/activate #MAC OS
  pip install dotenv pandas matplotlib seaborn mplfinance
  pip install -e .
  pip freeze > requirements.txt
  #deactivate environment if required
  deactivate
  ```
* **Install dependencies:**
  ```bash
  pip install dotenv pandas matplotlib seaborn
  ```
* Freeze Requirement
  ```bash
  pip freeze > requirements.txt
  ```
* Install  Requirement
  ```bash
  pip install -r requirements.txt
  ```
* Execute
  ```bash
  <Project Root>/python src/sample_de/dodo.py
  ```
* Example
  - <p align="center">
    <img src="./charts/sales_visualizations_category_en.png" width="100%" alt="Sales category performance">

  </p>
  - <p align="center">
    <img src="./charts/sales_visualizations_en.png" width="100%" alt="Sales subcategory performance">
  </p>
  - <p align="center">
    <img src="./charts/candle_chart_en.png" width="800" alt="Stock Performance Candlestick">
  </p>
  - <p align="center">
    <img src="./charts/advanced_candle_chart_en.png" width="800" alt="Stock Performance Candlestick">
  </p>
