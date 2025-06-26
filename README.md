🌟 Zena's Amazing Athleisure Catalog

Zena's Amazing Athleisure Catalog is an interactive Streamlit app that connects to a Snowflake database to display stylish sweatsuits. Users can select a color or style and view the associated image, price, available sizes, and an upsell suggestion, all fetched in real time from a Snowflake table.

🚀 Features

Dropdown menu for choosing a product color/style

Fetches product details from a Snowflake database

Displays image, price (formatted), size options, and upsell suggestion

Uses Snowpark and Streamlit for interactivity and secure data access

🚫 Requirements

Python 3.8+

Streamlit

Snowflake Snowpark Python API

Install dependencies:

pip install -r requirements.txt

🧰 How to Run

streamlit run app.py

Make sure the app is running in an environment where get_active_session() is valid (e.g., Snowsight or a Snowflake Native App context).

🔐 Snowflake Table Used

The app connects to the following table:

catalog_for_website (
  color_or_style STRING,
  file_name STRING,
  price NUMBER,
  size_list STRING,
  upsell_product_desc STRING,
  file_url STRING
)

Ensure this table exists and contains the appropriate data.

🤖 Example Output

Pick a sweatsuit color or style: [Navy Blue]

Image: [Navy Blue Sweatsuit]
Price: $65.00
Sizes Available: S, M, L, XL
Also Consider: Matching wristbands!
[Download Image]

💼 Project Structure

.
├── app.py               # Main Streamlit application
├── requirements.txt     # Dependencies list
└── README.md            # This file

🤝 Acknowledgements

This app was developed as part of a Snowflake + Streamlit workshop exercise.
