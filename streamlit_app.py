import streamlit as st
from snowflake.snowpark.context import get_active_session
import pandas as pd

st.title("Zena's Amazing Athleisure Catalog")

session = get_active_session()

# Get a list of colors for a drop list selection
table_colors = session.sql("SELECT color_or_style FROM catalog_for_website")
pd_colors = table_colors.to_pandas()

# Put the list of colors into a drop list selector
option = st.selectbox('Pick a sweatsuit color or style:', pd_colors)

# Build the image caption
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

# Use the color selected to query product details safely
query = """
    SELECT file_name, price, size_list, upsell_product_desc, file_url
    FROM catalog_for_website
    WHERE color_or_style = ?
"""
table_prod_data = session.sql(query, params=[option])
pd_prod_data = table_prod_data.to_pandas()

# Extract data fields from query result
price = '${:.2f}'.format(pd_prod_data['PRICE'].iloc[0])
file_name = pd_prod_data['FILE_NAME'].iloc[0]
size_list = pd_prod_data['SIZE_LIST'].iloc[0]
upsell = pd_prod_data['UPSELL_PRODUCT_DESC'].iloc[0]
url = pd_prod_data['FILE_URL'].iloc[0]

# Display product info
st.image(image=url, width=400, caption=product_caption)
st.markdown('**Price:** ' + price)
st.markdown('**Sizes Available:** ' + size_list)
st.markdown('**Also Consider:** ' + upsell)
st.markdown(f"[Download Image]({url})")
