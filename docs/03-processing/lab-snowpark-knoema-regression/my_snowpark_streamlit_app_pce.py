# Import required libraries
# Snowpark
from snowflake.snowpark.session import Session
from snowflake.snowpark.types import IntegerType
from snowflake.snowpark.functions import avg, sum, col, call_udf, lit, call_builtin, year
# Pandas
import pandas as pd
#Streamlit
import streamlit as st

#Set page context
st.set_page_config(
     page_title="Economical Data Atlas",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://developers.snowflake.com',
         'About': "This is an *extremely* cool app powered by Snowpark for Python, Streamlit, and Snowflake Marketplace"
     }
 )

# Create Session object
def create_session_object():
    connection_parameters = {
   "account": "<account_identifier",
   "user": "<username",
   "password": "<password>",
   "warehouse": "compute_wh",
   "role": "accountadmin",
   "database": "SUMMIT_HOL",
   "schema": "PUBLIC"
   }
    session = Session.builder.configs(connection_parameters).create()
    print(session.sql('select current_warehouse(), current_database(), current_schema()').collect())
    return session
  
# Create Snowpark DataFrames that loads data from Knoema: Economical Data Atlas
def load_data(session): 
    #US Inflation, Personal consumption expenditures (PCE) per year
    #Prepare data frame, set query parameters
    snow_df_pce = (session.table("ECONOMY_DATA_ATLAS.ECONOMY.BEANIPA") 
                            .filter(col('Table Name') == 'Price Indexes For Personal Consumption Expenditures By Major Type Of Product') 
                            .filter(col('Indicator Name') == 'Personal consumption expenditures (PCE)')
                            .filter(col('"Frequency"') == 'A')
                            .filter(col('"Date"') >= '1972-01-01'))
    #Select columns, substract 100 from value column to reference baseline
    snow_df_pce_year = snow_df_pce.select(year(col('"Date"')).alias('"Year"'), (col('"Value"')-100).alias('PCE')).sort('"Year"', ascending=False)
    #convert to pandas dataframe 
    pd_df_pce_year = snow_df_pce_year.to_pandas()
    #round the PCE series
    pd_df_pce_year["PCE"] = pd_df_pce_year["PCE"].round(2)
  
    #create metrics
    latest_pce_year = pd_df_pce_year.loc[0]["Year"].astype('int')
    latest_pce_value = pd_df_pce_year.loc[0]["PCE"]
    delta_pce_value = latest_pce_value - pd_df_pce_year.loc[1]["PCE"]

    #Use Snowflake UDF for Model Inference
    snow_df_predict_years = session.create_dataframe([[int(latest_pce_year+1)], [int(latest_pce_year+2)],[int(latest_pce_year+3)]], schema=["Year"])
    pd_df_pce_predictions = snow_df_predict_years.select(col("year"), call_udf("predict_pce_udf", col("year")).as_("pce")).sort(col("year")).to_pandas()
    pd_df_pce_predictions.rename(columns={"YEAR": "Year"}, inplace=True)
    #round the PCE prediction series
    pd_df_pce_predictions["PCE"] = pd_df_pce_predictions["PCE"].round(2).astype(float)-100
    
    #Combine actual and predictions dataframes
    pd_df_pce_all = (
        pd_df_pce_year.set_index('Year').sort_index().rename(columns={"PCE": "Actual"})
        .append(pd_df_pce_predictions.set_index('Year').sort_index().rename(columns={"PCE": "Prediction"}))
    )
   
    #Data per quarter
    snow_df_pce_q = (session.table("ECONOMY_DATA_ATLAS.ECONOMY.BEANIPA") 
                            .filter(col('Table Name') == 'Price Indexes For Personal Consumption Expenditures By Major Type Of Product') 
                            .filter(col('Indicator Name') == 'Personal consumption expenditures (PCE)')
                            .filter(col('"Frequency"') == 'Q')
                            .select(year(col('"Date"')).alias('Year'),
                                    call_builtin("date_part", 'quarter', col('"Date"')).alias('"Quarter"') ,
                                    (col('"Value"')-100).alias('PCE'))
                            .sort('Year', ascending=False))
    
    # by Major Type Of Product
    snow_df_pce_all = (session.table("ECONOMY_DATA_ATLAS.ECONOMY.BEANIPA")
                        .filter(col('"Table Name"') == 'Price Indexes For Personal Consumption Expenditures By Major Type Of Product')
                        .filter(col('"Indicator Name"') != 'Personal consumption expenditures (PCE)')
                        .filter(col('"Frequency"') == 'A')
                        .filter(col('"Date"') >= '1972-01-01')
                        .select('"Indicator Name"', year(col('"Date"')).alias('Year'), (col('"Value"')-100).alias('PCE') ))
    
    # Add header and a subheader
    st.title("Knoema: Economical Data Atlas")
    st.header("Powered by Snowpark for Python and Snowflake Marketplace | Made with Streamlit")
    st.subheader("Personal consumption expenditures (PCE) over the last 25 years, baseline is 2012")
    with st.expander("What is the Personal Consumption Expenditures Price Index?"):
        st.write("""
         The prices you pay for goods and services change all the time – moving at different rates and even in different directions. Some prices may drop while others are going up. A price index is a way of looking beyond individual price tags to measure overall inflation (or deflation) for a group of goods and services over time.
         
         The Personal Consumption Expenditures Price Index is a measure of the prices that people living in the United States, or those buying on their behalf, pay for goods and services.The PCE price index is known for capturing inflation (or deflation) across a wide range of consumer expenses and reflecting changes in consumer behavior.
        """)
    # Use columns to display metrics for global value and predictions
    col11, col12, col13 = st.columns(3)
    with st.container():
        with col11:
            st.metric("PCE in " + str(latest_pce_year), round(latest_pce_value), round(delta_pce_value), delta_color=("inverse"))
        with col12:
            st.metric("Predicted PCE for " + str(int(pd_df_pce_predictions.loc[0]["Year"])), round(pd_df_pce_predictions.loc[0]["PCE"]), 
                round((pd_df_pce_predictions.loc[0]["PCE"] - latest_pce_value)), delta_color=("inverse"))
        with col13:
            st.metric("Predicted PCE for " + str(int(pd_df_pce_predictions.loc[1]["Year"])), round(pd_df_pce_predictions.loc[1]["PCE"]), 
                round((pd_df_pce_predictions.loc[1]["PCE"] - latest_pce_value)), delta_color=("inverse"))

    # Barchart with actual and predicted PCE
    st.bar_chart(data=pd_df_pce_all.tail(25), width=0, height=0, use_container_width=True)

    # Display interactive chart to visualize PCE Emissions by Top 10 Countries, by selecting the year  
    with st.container():
        
        year_selection = st.selectbox('Select year', pd_df_pce_year['Year'].head(25),index=0 )
        pd_df_pce_q = snow_df_pce_q.filter(col('Year') == year_selection).sort(col('"Quarter"')).to_pandas().set_index('Quarter')
        with st.expander("Price Indexes For Personal Consumption Expenditures per Quarter"):
             st.bar_chart(data=pd_df_pce_q['PCE'], width=0, height=500, use_container_width=True)
        pd_df_pce_all = snow_df_pce_all.filter(col('Year') == year_selection).sort(col('"Indicator Name"')).to_pandas().set_index('Indicator Name')
        st.write("Price Indexes For Personal Consumption Expenditures By Major Type Of Product")
        st.bar_chart(data=pd_df_pce_all['PCE'], width=0, height=500, use_container_width=True)
    

if __name__ == "__main__":
    session = create_session_object()
    load_data(session)
