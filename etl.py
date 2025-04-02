# from sqlalchemy import create_engine

# # Define your PostgreSQL connection parameters
# DATABASE_TYPE = "postgresql"
# USERNAME = "postgres"
# PASSWORD = "incorrect22"
# HOST = "localhost"  # Change if your database is hosted elsewhere
# PORT = "5432"
# DATABASE_NAME = "Customer_data_integration Database"

# # Create the connection string
# connection_string = f"{DATABASE_TYPE}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
# engine = create_engine(connection_string)

# # # Test the connection
# # try:
# #     with engine.connect() as connection:
# #         print("✅ Connected to PostgreSQL database successfully!")
# # except Exception as e:
# #     print(f"❌ Failed to connect: {e}")

# import pandas as pd

# # Function to read CSV file
# def extract_csv(file_path):
#     return pd.read_csv(file_path)

# # File path
# csv_file = "user_data_23_4.csv"

# # Extracting data
# csv_data = extract_csv(csv_file)

# # Display first few rows
# print(csv_data.head()) 
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.max_rows', None)  # Show all rows
# pd.set_option('display.width', None)  # Remove width restrictions
# pd.set_option('display.max_colwidth', None)  # Show full content in each column
# print(csv_data)


# import pandas as pd

# # Load CSV into a DataFrame
# csv_file = "user_data_23_4.csv"
# df = pd.read_csv(csv_file)  # 'df' is now a DataFrame

# # Show DataFrame
# print(df)


# import pandas as pd

# # Function to read JSON file
# def extract_json(file_path):
#     return pd.read_json(file_path)

# # File path
# json_file = "user_data_23_4.json"

# # Extracting data
# df_json = extract_json(json_file)

# # Show DataFrame
# print(df_json)

# import pandas as pd

# # Function to read JSON file
# def extract_json(file_path):
#     return pd.read_json(file_path)

# # File path
# json_file = "user_data_23_4.json"

# # Extracting data
# df_json = extract_json(json_file)

# # Show DataFrame
# print(df_json)


# import pandas as pd

# # Ensure all rows and columns are fully visible
# pd.set_option("display.max_rows", None)  
# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", None)
# pd.set_option("display.max_colwidth", None)

# # Load JSON with better structure handling
# df_json = pd.read_json("user_data_23_4.json", orient="records")

# # Print clearly formatted DataFrame
# print(df_json.to_string())  # Ensures table-like format

# import pandas as pd

# # Ensure full DataFrame visibility
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", None)
# pd.set_option("display.max_colwidth", None)

# # Load JSON data
# df_json = pd.read_json("user_data_23_4.json", orient="records")

# # Reset index to start from 1 and rename it to "S/N"
# df_json.index = range(1, len(df_json) + 1)
# df_json.index.name = "S/N"

# # Display the DataFrame
# print(df_json.to_string())

# import pandas as pd

# # Ensure full DataFrame visibility
# pd.set_option("display.max_rows", None)       # Show all rows
# pd.set_option("display.max_columns", None)    # Show all columns
# pd.set_option("display.width", None)          # Expand display width
# pd.set_option("display.max_colwidth", None)   # Prevent truncation of long text

# # Load JSON data
# df_json = pd.read_json("user_data_23_4.json")

# # Reset index and create a Serial Number (S/N) column
# df_json.reset_index(drop=True, inplace=True)
# df_json.index += 1  # Start index from 1 instead of 0
# df_json.insert(0, "S/N", df_json.index)  # Insert S/N as the first column

# # Display the DataFrame properly
# print(df_json)

# import pandas as pd
# from tabulate import tabulate  # Install using: pip install tabulate

# # Load JSON data
# df_json = pd.read_json("user_data_23_4.json")

# # Reset index and add Serial Number (S/N)
# df_json.reset_index(drop=True, inplace=True)
# df_json.index += 1  # Start from 1
# # df_json.insert(0, "S/N", df_json.index)
# # Display as a table
# print(tabulate(df_json, headers="keys", tablefmt="fancy_grid"))

# import pandas as pd

# # Load your dataset
# df = pd.read_json("user_data_23_4.json")

# # Display all rows and columns properly
# pd.set_option("display.max_rows", None)  # Show all rows
# pd.set_option("display.max_columns", None)  # Show all columns
# pd.set_option("display.width", None)  # Adjust width to fit terminal
# pd.set_option("display.colheader_justify", "center")  # Center column headers
# # Print as a table
# print(df.to_string(index=False))  # Remove index for better readability

import pandas as pd
import json
import xml.etree.ElementTree as ET

# File paths
csv_file = "user_data_23_4.csv"
json_file = "user_data_23_4.json"
xml_file = "user_data_23_4.xml"
txt_file = "user_data_23_4.txt"

# # 📌 Step 1: Extract Data

# # 1️⃣ Read CSV
# def extract_csv(file_path):
#     return pd.read_csv(file_path)

# # 2️⃣ Read JSON
# def extract_json(file_path):
#     return pd.read_json(file_path)

# # 3️⃣ Read XML
# def extract_xml(file_path):
#     tree = ET.parse(file_path)
#     root = tree.getroot()

#     data = []
#     for item in root.findall("record"):  # Change "record" based on your XML structure
#         entry = {child.tag: child.text for child in item}
#         data.append(entry)

#     return pd.DataFrame(data)

# # 4️⃣ Read TXT
# def extract_txt(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         lines = file.readlines()
#     return pd.DataFrame([line.strip().split(",") for line in lines])

# # Load Data
# csv_data = extract_csv(csv_file)
# json_data = extract_json(json_file)
# xml_data = extract_xml(xml_file)
# txt_data = extract_txt(txt_file)

# # Print Sample Outputs
# print("✅ CSV Data:\n", csv_data.head())
# print("✅ JSON Data:\n", json_data.head())
# print("✅ XML Data:\n", xml_data.head())
# print("✅ TXT Data:\n", txt_data.head())

# import pandas as pd

# # Read XML file
# df = pd.read_xml("user_data_23_4.xml")
# # Display dataframe
# print(df)
 
#  print('Hello World!')
# print('Hello World!')



y='Hello World'
print(y)