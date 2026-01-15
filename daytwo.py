# Max Farnham (vsx8ws)

# %%
# Open the Codespace in your local VS Code

# /workspaces/daytwostuff

# %%
# Create a virtual environment

# You should not include the environment in your repo
# The file path is still /workspaces/daytwostuff, but there is a (.venv) in the front the line in the terminal, showing that the virtual environment is running.
# %%
# Viewing Data

import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/MMiDS-textbook/MMiDS-textbook.github.io/refs/heads/main/utils/datasets/penguins-measurements.csv')
# %%
# Extension Management 

# In the extensions tab, Data Wrangler is under Codespaces, which mean I'll have to reinstall it for each new Codespace I make.
# Data Wrangler is helpful with data viewing, data cleaning, and data preparation for tabular datasets.
# %%
# Package Managing

# We use a requirements.txt file to record a project’s Python dependencies and their versions so the environment can be recreated consistently across different machines.