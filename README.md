# Salesforce CLI Health Tool

This Python script helps you analyze the fields of custom objects in your Salesforce environment. Given a custom object name, it retrieves up to 500 instances of the object, calculates the usage percentage of each field, and exports the results to a CSV file.

## 🌟 Features

- Connects to your Salesforce environment using the simple-salesforce library
- Retrieves a list of all custom objects in the environment
- Allows users to enter a custom object name to be analyzed
- Queries up to 500 instances of the selected custom object
- Calculates field usage statistics and exports them to a CSV file
- CSV file includes project name, field name, field label, instance count, total queried objects, and usage percentage

## 🛠️ Requirements

- Python 3.6 or later 🐍
- simple-salesforce library

## 💻 Installation (Using the command line)

1. Clone the repository:
git clone https://github.com/yourusername/salesforce-custom-objects-field-analyzer.git
2. Navigate to the project directory:
cd salesforce-custom-objects-field-analyzer
3. Install the required libraries:
pip install -r requirements.txt


## 🚀 Usage
1. Run the script:
python salesforce_custom_objects.py
2. Enter your Salesforce credentials (username, password, and [security token](https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm&type=5)) when prompted.
3. The script will display a list of custom objects in your Salesforce environment.
4. Enter the custom object name you want to analyze. The script will query up to 500 instances of the custom object, calculate field usage statistics, and export the results to a CSV file in your Downloads folder.
5. You can analyze multiple custom objects by entering their names one by one. To exit the program, type 'exit' when prompted for a custom object name.

## 🤝 Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 👏 Acknowledgments
- [simple-salesforce](https://github.com/simple-salesforce/simple-salesforce) for providing an easy-to-use Salesforce API client



