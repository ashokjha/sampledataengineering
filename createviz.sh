#!/bin/bash

python src/sample_de/utils/UpdateReadme.py

python src/poc/utils/json_merge.py config/master_report_config.json report_data_fetcher.json

streamlit run src/poc/main.py