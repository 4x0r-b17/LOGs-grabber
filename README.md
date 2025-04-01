# LOGs-grabber

This repository contains three Python scripts designed for automated scanning of long log files to identify sensitive information, such as credit card details or platform-related data. These scripts are tailored to help identify information related to credit card data, specific platform categories, and login credentials in URL:Login:Password (U:L:P) format. The automation process leverages Python for efficient Bash scripting.

## Scripts Overview

1. **`script-CC.py`**  
   This script scans log files for potential credit card details. It uses regular expressions to detect patterns that resemble credit card numbers in large log files.

2. **`script-LOGs.py`**  
   This script allows the user to specify a category of platforms (e.g., gift card sites or gaming platforms) and searches the provided log files for matching platform-related data.

3. **`script-ULP.py`**  
   This script scans log files formatted in a `U:L:P` (URL:Login:Password) style and looks for potential login credentials associated with specified patterns.

## Features

- **Automated Search:** All scripts automate the search process, saving time compared to manual inspection of log files.
- **Customizable Search:** Users can define platform categories or search for specific patterns (e.g., URLs or credit card formats).
- **Efficient Processing:** The scripts are designed to handle long log files and work seamlessly in Bash scripting for quick operations.

## Requirements

- Python 3.x+
- `re` (Regular Expressions module) – Built-in with Python.
- Python must be installed and available in the system PATH.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/credit-card-and-platform-search.git
   cd credit-card-and-platform-search

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. **`script-CC.py`**:
   ```bash
   python3 script-ULP.py -p <path_to_LOG_file>

2. **`script-LOGs.py`**:
   ```bash
   python3 script-ULP.py -p <path_to_LOG_file>
   
3. **`script-CC.py`**:
   ```bash
   python3 script-ULP.py -p <path_to_LOG_file>

## Contributing

Feel free to fork the repository, submit issues, and create pull requests if you'd like to contribute improvements or bug fixes.
