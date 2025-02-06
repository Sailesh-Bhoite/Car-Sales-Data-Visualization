import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar Elements
st.sidebar.markdown('<h1 style="color:violet"><u>Car Sales Data Visualization</u></h1>', unsafe_allow_html=True)
with st.sidebar.expander("Basic Car Information"):
    st.write("You can Select a car from the list given to see its available models. This section helps you explore the different models offered by each car manufacturer, making it easier to find the one that fits your needs.")
with st.sidebar.expander("Brand Sales"):
    st.write("This bar graph showcases the sales performance of various car brands. By analyzing the sales data, you can identify the most popular brands and make informed decisions based on market trends.")
with st.sidebar.expander("Price V/S Age"):
    st.write("This scatter plot illustrates the relationship between car prices and their age. Use this visualization to analyze how the age of a car influences its resale value, helping you make informed buying or selling decisions.")
with st.sidebar.expander("Customer Data"):
    st.write("The pie chart below displays the distribution of car ownership among first, second, and third owners. Understand the ownership history of the cars in the dataset, providing insights into their usage and potential value.")
with st.sidebar.expander("City Sales"):
    st.write("Explore the distribution of car sales across different cities with this horizontal bar graph. Understand the regional demand and preferences for different car models by examining city-wise sales data.")
with st.sidebar.expander("Fuel Type Data"):
    st.write("A pie chart that below displays the distribution of fuel type of vehicles. Understand the fuel consumed history of the cars.")
with st.sidebar.expander("Kilometer V/S Price"):
    st.write("A scatter plot that illustrates the relationship between car prices and their total kilometers covered. This visualization is to analyze how the distance covered by the cars influences its resale value.")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Basic Information", "Brand Sales", "Price v/s Age", "Customer Data", "City Sales", "Fuel Type Data", "Km v/s Price"])

with tab1:
    data = pd.read_csv("Pre-Owned-Car-Resale.csv")
    brands = data.maker.unique()
    brand = st.selectbox("Select Car Brands", brands)
    st.subheader(f"Available {brand} Models")
    model_names_d = data[data["maker"] == brand]["model_name"].unique().tolist()
    model_names = list(set([x.split()[0] for x in model_names_d]))
    with st.container(border=True):
        st.text("\n".join(model_names))


with tab2:
    st.markdown("<h1 style='color:#00ff00'>Car Brand Sales</h1>", unsafe_allow_html=True)
    maker_data = data["maker"].value_counts()
    st.bar_chart(maker_data, x_label="Brand", y_label="Number of Units Sold", color='#00ff00')


with tab3:
    st.markdown("<h1 style='color:yellow'>Price V/S Age of Cars</h1>", unsafe_allow_html=True)
    data_copy = data.copy()
    data_copy['Age'] = 2025-data_copy['model_year']
    # Set Age as the index
    data_copy.set_index('Age', inplace=True)
    # Plot the line chart
    st.scatter_chart(data_copy['price'], x_label="Age", y_label="Price", color='#fff01f')


with tab4:
    st.markdown("<h1 style='color:#4cc9f0'>Customer Data</h1>", unsafe_allow_html=True)
    customer_data = data["pre_owner"].value_counts()
    labels = customer_data.index.tolist()
    pie_fig, ax = plt.subplots(facecolor='#0E1117')
    ax.pie(customer_data, labels=labels, textprops={'color': 'white'}, radius=0.8)
    st.pyplot(fig=pie_fig)


with tab5:
    st.markdown("<h1 style='color:#ff5f1f'>City-wise Car Sales</h1>", unsafe_allow_html=True)
    city_data = data["city"].value_counts()
    st.bar_chart(city_data, horizontal=True, x_label="Number of Units Sold", y_label="City", color='#ff5f1f')


with tab6:
    st.markdown("<h1 style='color:#a9a9a9'>Fuel Type Data</h1>", unsafe_allow_html=True)
    fuel_data = data["fuel_type"].value_counts()
    labels = fuel_data.index.tolist()
    pie_fig, ax = plt.subplots(facecolor='#0E1117')
    ax.pie(fuel_data, labels=labels, textprops={'color': 'white'}, radius=0.8, colors=["#3e3636", "#5d5555", "#716868"])
    st.pyplot(fig=pie_fig)


with tab7:
    st.write("<h1 style='color:#fc6a03'>Kilometers V/S Price</h1>", unsafe_allow_html=True)
    km_data = data.copy()
    km_data.set_index('distance_covered (km)', inplace=True)
    st.scatter_chart(km_data["price"], x_label="Kilometers", y_label="Price", color='#fc6a03')
