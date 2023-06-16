import os

# Download the latest Miniconda installer for Windows
os.system('curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe')

# Install Miniconda
os.system('start /wait "" Miniconda3-latest-Windows-x86_64.exe /S /D=C:\\Miniconda3')

# Create a new virtual environment named "qgis_env" with Python 3.7
os.system('conda create --name qgis_env python=3.7')

# Activate the virtual environment
os.system('conda activate qgis_env')

# Install QGIS in the virtual environment using the conda-forge channel
os.system('conda install -c conda-forge qgis')

# Deactivate the virtual environment
os.system('conda deactivate')