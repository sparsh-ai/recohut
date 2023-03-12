# Imports
import sqlalchemy
import pandas    as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid

# Initial Configs
st.set_page_config(layout='wide')
st.title('Star Jeans : A Data Engineering Project') 
st.markdown('Welcome, here you will find H&M scraped and cleaned data. Feel free to use the filters by clicking on the three stripes next to each column. ') 

# Functions
@st.cache(allow_output_mutation=True)
def connect_engine(conn_url):
    engine = sqlalchemy.create_engine(conn_url)
    return engine

st.cache(hash_funcs={sqlalchemy.engine.base.Engine: id})
def get_data(engine):
    query = """
    SELECT * FROM hm;
    """
    data = pd.read_sql(query, con=engine)
    return data

def show_data(data):
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) # Paging
    gb.configure_selection('multiple', groupSelectsChildren="Group checkbox select children") 
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=True,
        enable_enterprise_modules=True,
        height=600, 
        width='100%',
        reload_data=True
    )
    return grid_response

def show_cols_definitions():
    if st.checkbox('Show Columns Definitions'):
        st.markdown("""
        | **Column**          | **Definition** |
        |:--------------------:|----------------|
        |      product_id     | A 10-digit number uniquely assigned to each product, composed of style_id and color_id |
        |      style_id       | A 7-digit number uniquely assigned to each product style| 
        |      color_id       | A 3-digit number assigned to each product color|
        |      product_name   | Product's name |
        |      product_type   | Product's type |
        |      product_color  | Product's color |
        |      product_fit    | Product's fit - if it's slim, skinny, loose, etc |
        |      cotton         | Percentage of cotton in the product's composition |
        |      spandex        | Percentage of spandex in the product's composition |
        |      polyester      | Percentage of polyester in the product's composition |
        |    elastomultiester | Percentage of elastomultiester in the product's composition |
        |       lyocell       | Percentage of lyocell in the product's composition |
        |       rayon         | Percentage of rayon in the product's composition |
        |       product_price | Product's unit price |
        |  scraping_datetime  | The Date of which the data scraping was performed |
        """)
        return None

if __name__ == "__main__":
    # Parameters and Connection
    conn_url = "postgresql://brunodifranco:ExoCs9IRXJ6u@ep-soft-disk-362766.us-east-2.aws.neon.tech:5432/neondb" # obs.: this would ideally be hidden
    engine = connect_engine(conn_url)

    # Get Data
    data = get_data(engine) # Job 05

    # Display Data
    show_data(data) # Job 06

    # Display Columns Definitions
    show_cols_definitions()
