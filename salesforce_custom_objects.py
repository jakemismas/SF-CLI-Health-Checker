import sys
import getpass
import csv
import os
from simple_salesforce import Salesforce
from collections import Counter


def process_custom_object(sf, chosen_object):
    # Get the chosen custom object's fields
    object_fields_response = sf.restful(f"sobjects/{chosen_object}/describe")
    object_fields = object_fields_response["fields"]
    field_info = {field["name"]: field["label"] for field in object_fields}

    # SOQL query to grab up to 500 instances of the chosen custom object
    fields_str = ", ".join(field_info.keys())
    query = f"SELECT {fields_str} FROM {chosen_object} ORDER BY CreatedDate DESC LIMIT 500"
    records = sf.query_all(query)["records"]

    # Count instances of each field
    field_counts = Counter()
    for record in records:
        for field, value in record.items():
            if field != 'attributes':
                field_counts[field] += 1 if value is not None else 0

    # Calculate the number of queried objects and percentage
    total_queried_objects = len(records)
    field_stats = [
        {
            'Project Name': chosen_object,
            'Field name': field,
            'Field label': field_info[field],
            'Instances': count,
            'Total Queried Objects': total_queried_objects,
            'Percentage': count / total_queried_objects * 100
        }
        for field, count in field_counts.items()
    ]

    # Sort the rows by lowest to highest percentage
    field_stats.sort(key=lambda x: x['Percentage'])

    # Get the user's Downloads folder path
    downloads_folder = os.path.expanduser('~/Downloads')

    # Write results to a CSV file
    csv_filename = f"{chosen_object}_fields.csv"
    csv_filepath = os.path.join(downloads_folder, csv_filename)
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Project Name', 'Field name', 'Field label',
                      'Instances', 'Total Queried Objects', 'Percentage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for field_stat in field_stats:
            writer.writerow({
                'Project Name': field_stat['Project Name'],
                'Field name': field_stat['Field name'],
                'Field label': field_stat['Field label'],
                'Instances': field_stat['Instances'],
                'Total Queried Objects': field_stat['Total Queried Objects'],
                'Percentage': f"{field_stat['Percentage']:.2f}%"
            })

    print(f"\nResults have been exported to {csv_filepath}")


def main():
    # Prompt for Salesforce credentials
    username = input("Enter your Salesforce username: ")
    password = getpass.getpass("Enter your Salesforce password: ")
    security_token = getpass.getpass("Enter your Salesforce security token: ")

    # Connect to Salesforce
    sf = Salesforce(username=username, password=password,
                    security_token=security_token)
    print("Connected to Salesforce!\n")

    # Retrieve custom objects
    custom_objects = sf.describe()["sobjects"]
    custom_object_names = [obj["name"]
                           for obj in custom_objects if obj["custom"]]

    # Display custom objects
    print("List of custom objects:")
    for obj_name in custom_object_names:
        print(f"- {obj_name}")

    while True:
        # User input for the custom object name
        chosen_object = input(
            "\nEnter the custom object name (or type 'exit' to quit): ")

        # Exit the program if the user enters 'exit'
        if chosen_object.lower() == 'exit':
            break

        # Check if the custom object exists
        if chosen_object not in custom_object_names:
            print(f"{chosen_object} not found.")
            continue

        process_custom_object(sf, chosen_object)


if __name__ == "__main__":
    main()
