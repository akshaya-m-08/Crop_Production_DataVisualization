import streamlit as st
import base64
import plotly.io as pio
from streamlit_option_menu import option_menu
import numpy as np
from r3_fetchsql import data
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import json



# Set page configuration as the first Streamlit command
st.set_page_config(
    page_title="Crop Production India",
    page_icon="asset/crop.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for the sidebar and main content
custom_css = """
<style>
.image-container img {
    height: 30%;
    width: 100%; 
}
.side-image-container img {
    height: 100px;
    width: 100px;  
}
[data-testid="stSidebar"] {
    background-color: #0A5933; 
    text-align: center;
}
[data-testid="stMetric"] 
{
    background-color: #099F57; 
    text-align: center;
    padding: 5px 0;
    font-weight: bold;
    border-radius: 15px;
    color: white; 
    width: auto;
}
[data-testid="stMetricValue"] {
    font-size: 30px;
}

[data-testid="stTable"] {
    width: auto;
    height: 500px;
    overflow-y: auto;
    background-color: #099F57;
    border-radius: 8px;  
    font-size: 19px;
    color: white;
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 
}
[data-testid="stTable"] thead th {
    font-size: 20px;
    text-align: center !important; 
    font-weight: bold;
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 
}

[data-testid="stTable"] tbody td {
    text-align: left !important; 
    font-size: 20px;
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 
}

[data-testid="stTable"] table tbody td{
    color: white;
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 
}
[data-testid="stTable"] table th,
[data-testid="stTable"] table tbody td:first-child {
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 
    color: white; 
}
[data-testid="stTable"] table tbody td:nth-child(odd) {
    text-align: right !important;
    color: #0A5933; !important;
    font-weight: bold !important;
    font-size: 22px !important;
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 

}
[data-testid="stTable"] table tbody td:first-child {
    text-align: left !important;
    color: white!important;
    font-weight: italic !important;
    font-size: 22px !important;
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 
}
[data-testid="stTable"] tbody tr:nth-child(even),
[data-testid="stTable"] tbody tr:nth-child(odd) {
    background-color: #099F57; 
    border-right: none; 
    border-left: none; 
    border-top: none; 
    border-bottom: none; 
}
</style>
"""

# Embed custom CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Function to get the base64 encoded string of the image
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Sidebar content
with st.sidebar:
    logo_path = "asset/crop.svg"
    logo_base64 = get_image_base64(logo_path)
    st.markdown(f'<div class="side-image-container"><img src="data:image/svg+xml;base64,{logo_base64}" alt="Company Logo" /></div>', unsafe_allow_html=True)   
    # Toggle button for India/State
    is_state_selected = st.sidebar.checkbox("Select State", False)

    if is_state_selected:
        # Dropdown for selecting state
        selected_state = st.sidebar.selectbox("## Select State",options=sorted(data["State_Name"].unique()))
        view=selected_state
    else:
        view="India"

    # Default tab selection

    st.write("")
    st.write("")
    selected = option_menu(
        menu_title=f"{view}",
        options=["Home","Cropscape Overview", "Harvest Chronicles",  "Climate Harvest", "Cropfolio Insights", "Growth Nexus"],
        icons=["house-heart", "flower1","calendar3", "sun-fill","minecart-loaded","graph-up-arrow"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"background-color": "#13472E"},
            "icon": {"color": "white", "font-size": "16px"},
            "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#099F57"},
            "nav-link-selected": {"background-color": "#099F57"},
        }
    )
    
if selected == "Home":    
    # Base64 encode the image for the main content
    image_path = "asset/dashboard1.svg"
    image_base64 = get_image_base64(image_path)
    st.markdown(f'<div class="image-container"><img src="data:image/svg+xml;base64,{image_base64}" /></div>', unsafe_allow_html=True)    
    if view == "India":
        st.write("# Welcome to the Agriculture Dashboard!")
        st.write("India is one of the world's leading agricultural producers, known for its diverse range of crops and fertile agricultural land.")
        st.write("Here, you can explore insights into crop production and agriculture across different states of India.")
        st.write("Select a tab from the sidebar to dive into specific analyses.")

        # Add more content about agriculture in India and its states
        st.write("### Agriculture in India")
        st.write("India is an agricultural powerhouse, with a rich agricultural heritage and a wide variety of crops grown throughout the country.")
        st.write("From the fertile plains of Punjab to the rice paddies of West Bengal, each region contributes to India's vibrant agricultural landscape.")

        # Display key statistics about agriculture in India
        st.write("### Key Statistics")
        st.write("- India is the world's largest producer of various crops, including rice, wheat, and pulses.")
        st.write("- Agriculture employs over half of India's workforce and is a significant contributor to the country's economy.")
        st.write("- With its diverse climate and soil conditions, India can grow a wide range of crops, from tropical fruits in the south to temperate crops in the north.")

        # Provide links or buttons for users to explore further
        st.write("### Explore Further")
        st.write("To begin exploring, select a tab from the sidebar to analyze specific aspects of agriculture in India and its states.")

    # Dictionary containing agricultural information for each state/UT
    agricultural_info = {
        "Arunachal Pradesh": {
            "Description": "Arunachal Pradesh, in the northeastern region of India, is characterized by its hilly terrain and diverse climatic conditions, which support a wide range of agricultural activities.",
            "Key Crops": "Rice, maize, millet, pulses, and horticultural crops like oranges and apples.",
            "Notable Agricultural Practices": "Terrace farming is commonly practiced due to the hilly landscape. The state also focuses on organic farming",
            "Interesting Fact": "Arunachal Pradesh is known for its organic farming practices and sustainable agriculture, promoting eco-friendly farming techniques"
        },
        "Andhra Pradesh": {
            "Description": "Andhra Pradesh, located in southeastern India, has a diverse agricultural landscape driven by its varied climatic zones and extensive irrigation network.",
            "Key Crops": "Paddy (rice), maize, groundnut, sugarcane, cotton, tobacco, and chillies.",
            "Notable Agricultural Practices": "Extensive use of irrigation projects, adoption of high-yield variety seeds, and a focus on horticulture and organic farming.",
            "Interesting Fact": "Andhra Pradesh is renowned for its high-quality mangoes and chillies, significantly contributing to both domestic consumption and exports."
        },        
        "Assam": {
            "Description" : "Assam, situated in the northeastern part of India, is renowned for its tea plantations and rich agricultural heritage. The Brahmaputra River and its tributaries provide ample water for irrigation.",
            "Key Crops": "TTea, rice, jute, sugarcane, and mustard.",
            "Notable Agricultural Practices": "The state is famous for its traditional organic farming methods and extensive tea gardens.",
            "Interesting Fact": "Assam is the largest tea-producing state in India, contributing significantly to the global tea market."
        },
        "Bihar": {
            "Description" : "Bihar, located in the eastern part of India, is an agriculturally rich state with fertile soil and abundant water resources. Agriculture is the backbone of the state's economy.",
            "Key Crops": "Rice, wheat, maize, pulses, and oilseeds.",
            "Notable Agricultural Practices": "Bihar has a high cropping intensity and practices multiple cropping systems, with a focus on improving productivity through modern techniques.",
            "Interesting Fact": "The state is known for its high yield of crops due to the fertile Gangetic plains, and it is a major producer of fruits like mango, litchi, and guava."
        },
        "Chhattisgarh": {
            "Description" : "Chhattisgarh, in central India, is known as the ""Rice Bowl of India"" due to its extensive rice production. The state's agriculture is supported by its abundant natural resources and favorable climate.",
            "Key Crops": "Rice, maize, pulses, oilseeds, and vegetables.",
            "Notable Agricultural Practices": "The state focuses on sustainable agriculture and has a high adoption rate of organic farming, with an emphasis on traditional practices.",
            "Interesting Fact": "Chhattisgarh produces a significant portion of India's total rice output, making it a crucial state for the country's food security."
        },
        "Goa": {
            "Description" : "Goa, on the western coast of India, is known for its unique agricultural practices and diverse crop production. The state's agriculture is influenced by its coastal location and tropical climate.",
            "Key Crops": "Rice, coconut, cashew, spices, and fruits like mango and pineapple.",
            "Notable Agricultural Practices": "Goa utilizes traditional farming methods and promotes organic farming, focusing on sustainable practices.",
            "Interesting Fact": "Cashew cultivation is a major agricultural activity in Goa, and the state is famous for its high-quality cashew nuts and feni, a local alcoholic beverage made from cashew apples."
        },
        "Gujarat": {
            "Description" : "Gujarat, in western India, is known for its diverse agricultural landscape and high agricultural productivity. The state has a robust agricultural infrastructure and advanced farming techniques.",
            "Key Crops": "Cotton, groundnut, tobacco, sugarcane, and cereals like wheat and bajra.",
            "Notable Agricultural Practices": "Gujarat focuses on modern irrigation systems like drip irrigation and efficient water management practices to overcome its semi-arid climate.",
            "Interesting Fact": "The state is a leading producer of cotton and groundnuts in India and has a significant dairy industry, contributing to the White Revolution."
        },
        "Haryana": {
            "Description" : "Haryana, in northern India, is an agriculturally advanced state with a strong emphasis on modern farming practices and high-yield crop varieties. The state has a well-developed agricultural infrastructure.",
            "Key Crops": "Wheat, rice, sugarcane, cotton, and barley.",
            "Notable Agricultural Practices": "Haryana utilizes advanced agricultural technologies and mechanization to enhance productivity, along with efficient water management.",
            "Interesting Fact": "The state is known for its high productivity of wheat and rice, contributing significantly to India's food grain production through the Green Revolution."
        },
        "Himachal Pradesh": {
            "Description" : "Himachal Pradesh, in the northern part of India, is characterized by its hilly terrain and diverse climatic conditions, which support a variety of agricultural activities.",
            "Key Crops": "Apples, barley, maize, rice, and vegetables like peas and beans.",
            "Notable Agricultural Practices": "The state practices terrace farming and promotes organic farming, with a focus on horticulture and floriculture.",
            "Interesting Fact": "Himachal Pradesh is famous for its apple orchards and is a leading producer of apples in India, contributing significantly to the horticulture sector."
        },
        "Jharkhand": {
            "Description" : "Jharkhand, located in eastern India, is known for its rich natural resources and diverse agricultural activities. The state's agriculture is supported by its fertile soil and favorable climate.",
            "Key Crops": "Rice, maize, pulses, oilseeds, and vegetables like tomato and cauliflower.",
            "Notable Agricultural Practices": "Jharkhand focuses on sustainable agriculture and promotes organic farming, with an emphasis on traditional and tribal farming practices.",
            "Interesting Fact": "The state has a diverse agricultural landscape, with both traditional and modern farming practices, and is known for its minor millets and tuber crops."
        },
        "Karnataka": {
            "Description" : "Karnataka, in southern India, is a major agricultural state with a diverse range of crops and advanced farming techniques. The state's agriculture is supported by its varied climatic conditions and rich soil.",
            "Key Crops": "Rice, sugarcane, cotton, coffee, ragi (finger millet), and horticultural crops like mango, banana, and coconut.",
            "Notable Agricultural Practices": "Karnataka focuses on modern irrigation systems, efficient water management practices, and organic farming.",
            "Interesting Fact": "The state is a leading producer of coffee and silk in India and has a significant floriculture industry."
        },
        "Kerala": {
            "Description" : "Kerala, on the southwestern coast of India, is known for its diverse agricultural landscape and rich natural resources. The state's agriculture is influenced by its tropical climate and abundant rainfall.",
            "Key Crops": "Rice, coconut, rubber, spices like black pepper and cardamom, and fruits like banana and jackfruit.",
            "Notable Agricultural Practices": "Kerala utilizes traditional farming methods and promotes organic farming, with a focus on sustainable practices and integrated farming systems.",
            "Interesting Fact": "The state is famous for its spice plantations and is a major producer of spices in India, contributing significantly to the export market."
        },
        "Madhya Pradesh": {
            "Description" : "Madhya Pradesh, in central India, is known for its vast agricultural land and diverse crop production. The state's agriculture is supported by its fertile soil and favorable climate.",
            "Key Crops": "Wheat, rice, pulses (especially chickpeas), soybeans, and oilseeds.",
            "Notable Agricultural Practices": "Madhya Pradesh focuses on modern farming techniques, efficient water management practices, and organic farming.",
            "Interesting Fact": "The state is a leading producer of pulses and soybeans in India, contributing significantly to the country's agricultural output."
        },
        "Maharashtra": {
            "Description":"Maharashtra, in western India, is a major agricultural state with a diverse range of crops and advanced farming techniques. The state's agriculture is supported by its varied climatic conditions and rich soil.",
            "Key Crops": "Sugarcane, cotton, rice, soybeans, and horticultural crops like grapes, oranges, and bananas.",
            "Notable Agricultural Practices": "Maharashtra focuses on modern irrigation systems like drip irrigation, efficient water management practices, and organic farming.",
            "Interesting Fact": "The state is a leading producer of sugarcane and cotton in India and has a significant wine industry, with Nashik being known as the Wine Capital of India."
        },
        "Manipur": {
            "Description" : "Manipur, in northeastern India, is characterized by its hilly terrain and diverse climatic conditions, which support a variety of agricultural activities.",
            "Key Crops": "Rice, maize, pulses, oilseeds, and horticultural crops like pineapple and oranges.",
            "Notable Agricultural Practices": "The state practices terrace farming and promotes organic farming, with a focus on sustainable practices.",
            "Interesting Fact": "Manipur is known for its organic farming practices and sustainable agriculture, promoting eco-friendly farming techniques."
        },
        "Meghalaya": {
            "Description" : "Meghalaya, located in northeastern India, is known for its rich natural resources and diverse agricultural activities. The state's agriculture is supported by its fertile soil and favorable climate.",
            "Key Crops": "Rice, maize, potatoes, spices, and fruits like oranges and pineapples.",
            "Notable Agricultural Practices": "Meghalaya focuses on sustainable agriculture and promotes organic farming, with an emphasis on traditional practices.",
            "Interesting Fact": "The state is known for its high-quality turmeric and ginger production, contributing significantly to the spice market."
        },
        "Mizoram": {
            "Description" : "Mizoram, in northeastern India, is characterized by its hilly terrain and diverse climatic conditions, which support a wide range of agricultural activities.",
            "Key Crops": "Rice, maize, pulses, oilseeds, and horticultural crops like banana and passion fruit.",
            "Notable Agricultural Practices": "Terrace farming is commonly practiced due to the hilly landscape, along with jhum (shifting) cultivation in some areas.",
            "Interesting Fact": "Mizoram is known for its organic farming practices and sustainable agriculture, promoting eco-friendly farming techniques."
        },
        "Nagaland": {
            "Description" : "Nagaland, located in northeastern India, is known for its rich natural resources and diverse agricultural activities. The state's agriculture is supported by its fertile soil and favorable climate.",
            "Key Crops": "Rice, maize, millet, pulses, and horticultural crops like pineapple and orange.",
            "Notable Agricultural Practices": "The state focuses on sustainable agriculture and promotes organic farming, with traditional practices like jhum cultivation.",
            "Interesting Fact": "Nagaland is known for its traditional farming methods and high-quality organic produce, especially fruits and vegetables."
        },
        "Odisha": {
            "Description" : "Odisha, located on the eastern coast of India, is known for its diverse agricultural landscape and rich natural resources. The state's agriculture is influenced by its varied climatic conditions and fertile soil.",
            "Key Crops": "Rice, maize, pulses, oilseeds, and vegetables like tomato and brinjal.",
            "Notable Agricultural Practices": "Odisha focuses on modern farming techniques, efficient water management practices, and integrated farming systems.",
            "Interesting Fact": "The state is a leading producer of rice in India and has significant production of high-quality turmeric and ginger."
        },
        "Punjab": {
            "Description" : "Punjab, in northern India, is known as the ""Granary of India"" due to its extensive wheat and rice production. The state's agriculture is supported by its fertile soil and advanced farming techniques.",
            "Key Crops": "Wheat, rice, maize, sugarcane, and cotton",
            "Notable Agricultural Practices": "Punjab utilizes advanced irrigation systems and modern agricultural techniques to enhance productivity, with a focus on mechanization and high-yield varieties.",
            "Interesting Fact": "The state is a major contributor to India's food grain production, playing a crucial role in the Green Revolution."
        },
        "Rajasthan": {
            "Description" : "Rajasthan, located in northwestern India, is characterized by its arid and semi-arid climate, which influences its agricultural activities. The state has a rich cultural heritage and diverse agricultural practices.",
            "Key Crops": "Bajra (pearl millet), wheat, maize, pulses, and oilseeds like mustard.",
            "Notable Agricultural Practices": "Rajasthan focuses on dryland farming techniques, efficient water management practices like drip irrigation, and conservation agriculture.",
            "Interesting Fact": "The state is known for its hardy crops and livestock, with significant production of spices like coriander and cumin."
        },
        "Sikkim": {
            "Description" : "Sikkim, in northeastern India, is known for its organic farming and diverse agricultural activities. The state's agriculture is supported by its hilly terrain and favorable climate.",
            "Key Crops": "Rice, maize, millet, pulses, and horticultural crops like cardamom and ginger.",
            "Notable Agricultural Practices": "Sikkim is the first fully organic state in India, promoting sustainable and eco-friendly farming practices.",
            "Interesting Fact": "The state is renowned for its high-quality organic produce, especially large cardamom, which is a major export."
        },
        "Tamil Nadu": {
            "Description" : "Tamil Nadu, in southern India, is a major agricultural state with a diverse range of crops and advanced farming techniques. The state's agriculture is supported by its varied climatic conditions and rich soil.",
            "Key Crops": "Rice, sugarcane, cotton, groundnut, and horticultural crops like banana, mango, and coconut.",
            "Notable Agricultural Practices": "Tamil Nadu focuses on modern irrigation systems like drip irrigation, efficient water management practices, and integrated farming systems.",
            "Interesting Fact": "The state is a leading producer of rice and bananas in India, with significant contributions to the floriculture sector."
        },
        "Telangana": {
            "Description" : "Telangana, located in southern India, is known for its diverse agricultural landscape and rich natural resources. The state's agriculture is supported by its varied climatic conditions and fertile soil.",
            "Key Crops": "Rice, maize, pulses, cotton, and oilseeds like sunflower.",
            "Notable Agricultural Practices": "Telangana focuses on modern farming techniques, efficient water management practices, and integrated farming systems.",
            "Interesting Fact": "The state is known for its high yield of rice and cotton, contributing significantly to the agricultural sector."
        },
        "Tripura": {
            "Description" : "Tripura, in northeastern India, is characterized by its hilly terrain and diverse climatic conditions, which support a variety of agricultural activities.",
            "Key Crops": "Rice, maize, pulses, oilseeds, and horticultural crops like pineapple and orange.",
            "Notable Agricultural Practices": "The state practices terrace farming and promotes organic farming, with a focus on sustainable practices.",
            "Interesting Fact": "Tripura is known for its high-quality organic produce, especially pineapples and rubber plantations."
        },
        "Uttar Pradesh": {
            "Description" : "Uttar Pradesh, in northern India, is one of the largest agricultural states in the country, with a diverse range of crops and advanced farming techniques. The state's agriculture is supported by its fertile soil and favorable climate.",
            "Key Crops": "Wheat, rice, sugarcane, pulses, and oilseeds.",
            "Notable Agricultural Practices": "Uttar Pradesh focuses on modern farming techniques, efficient water management practices, and integrated farming systems.",
            "Interesting Fact": "The state is a leading producer of sugarcane and wheat in India, contributing significantly to the country's food security."
        },
        "Uttarakhand": {
            "Description" : "Uttarakhand, located in northern India, is characterized by its hilly terrain and diverse climatic conditions, which support a variety of agricultural activities.",
            "Key Crops": "Rice, wheat, maize, pulses, and horticultural crops like apple and peach.",
            "Notable Agricultural Practices": "The state practices terrace farming and promotes organic farming, with a focus on horticulture and floriculture.",
            "Interesting Fact": "Uttarakhand is known for its high-quality apples and other temperate fruits, contributing significantly to the horticulture sector."
        },
        "West Bengal": {
            "Description" : "West Bengal, located in eastern India, is known for its diverse agricultural landscape and rich natural resources. The state's agriculture is influenced by its varied climatic conditions and fertile soil.",
            "Key Crops": "Rice, jute, tea, sugarcane, and horticultural crops like mango and litchi.",
            "Notable Agricultural Practices": "West Bengal focuses on modern farming techniques, efficient water management practices, and integrated farming systems.",
            "Interesting Fact": "The state is a leading producer of rice and jute in India, with significant contributions to the tea industry, especially in Darjeeling."
        },
        "Andaman and Nicobar Islands": {
            "Description" : "The Andaman and Nicobar Islands, located in the Bay of Bengal, have a unique agricultural landscape influenced by their tropical climate and insular geography.",
            "Key Crops": "Coconut, rice, arecanut, banana, and spices like black pepper and cloves.",
            "Notable Agricultural Practices": "The islands utilize traditional farming methods and promote organic farming, with a focus on horticulture and plantation crops.",
            "Interesting Fact": "KThe region is known for its diverse flora and fauna, and agriculture is mainly practiced in small pockets of cultivable land."
        },
        "Chandigarh": {
            "Description" : "Chandigarh, a Union Territory and the capital of both Punjab and Haryana, has limited agricultural activities due to its urban nature.",
            "Key Crops": "Wheat, rice, maize, and vegetables grown in peri-urban areas.",
            "Notable Agricultural Practices": "Urban and peri-urban agriculture, with a focus on vegetable farming and floriculture.",
            "Interesting Fact": "Chandigarh's agricultural activities are primarily concentrated in the outskirts, supporting the city's demand for fresh produce."
        },
        "Dadra and Nagar Haveli and Daman and Diu": {
            "Description" : "These Union Territories, located on the western coast of India, have a tropical climate conducive to diverse agricultural activities.",
            "Key Crops": "Rice, ragi (finger millet), pulses, and horticultural crops like mango, banana, and sapota (chikoo).",
            "Notable Agricultural Practices": "The region focuses on traditional farming methods and promotes horticulture and plantation crops.",
            "Interesting Fact": "The territories are known for their high-quality sapota and other tropical fruits."
        },
        "Lakshadweep": {
            "Description" : "Lakshadweep, an archipelago in the Arabian Sea, has a unique agricultural landscape influenced by its tropical maritime climate.",
            "Key Crops": "Coconut, banana, and limited vegetable cultivation.",
            "Notable Agricultural Practices": "Agriculture is primarily based on coconut plantations, with a focus on traditional methods and organic farming.",
            "Interesting Fact": "The region's economy is heavily dependent on coconut and coconut-based products, including copra and coconut oil."
        },
        "Delhi": {
            "Description" : "Delhi, the capital territory of India, has limited agricultural activities due to its highly urbanized environment.",
            "Key Crops": "Vegetables, fruits, and flowers grown in peri-urban areas.",
            "Notable Agricultural Practices": "Urban agriculture, vertical farming, and rooftop gardening are increasingly being adopted to meet the city's demand for fresh produce.",
            "Interesting Fact": "Delhi's agricultural activities are concentrated in the rural fringes and peri-urban areas, contributing to the local food supply."
        },
        "Puducherry": {
            "Description" : "Puducherry, located on the southeastern coast of India, has a diverse agricultural landscape influenced by its tropical climate.",
            "Key Crops": "Rice, pulses, sugarcane, and horticultural crops like coconut and cashew.",
            "Notable Agricultural Practices": "The region focuses on traditional farming methods, organic farming, and integrated farming systems.",
            "Interesting Fact": "Puducherry is known for its high-quality cashew nuts and organic produce, with significant emphasis on sustainable agriculture."
        },
        "Jammu and Kashmir": {
            "Description" : "Jammu and Kashmir, located in northern India, has a diverse agricultural landscape influenced by its varied climatic conditions.",
            "Key Crops": "Rice, maize, wheat, barley, and horticultural crops like apples, saffron, and almonds.",
            "Notable Agricultural Practices": "The region practices traditional farming methods, with a focus on horticulture and organic farming.",
            "Interesting Fact": "Jammu and Kashmir are renowned for their high-quality apples, saffron, and dry fruits, contributing significantly to the horticulture sector."
        },
        "Ladakh": {
            "Description" : "Ladakh, located in the northernmost part of India, has a unique agricultural landscape characterized by its high-altitude desert climate.",
            "Key Crops": "Barley, wheat, buckwheat, peas, and vegetables.",
            "Notable Agricultural Practices": "The region practices high-altitude farming, with a focus on organic methods and traditional Ladakhi farming techniques.",
            "Interesting Fact": "Ladakh's agriculture is largely dependent on glacial meltwater for irrigation, and the region is known for its unique varieties of barley and buckwheat."
        }
    }

    selected_state = view
    if selected_state != "India":
        if selected_state:
            info = agricultural_info[selected_state]
            st.header(selected_state)
            st.write(info["Description"])
            st.subheader("Key Crops")
            st.write(info["Key Crops"])
            st.subheader("Notable Agricultural Practices")
            st.write(info["Notable Agricultural Practices"])
            st.subheader("Interesting Fact")
            st.write(info["Interesting Fact"])
        else:
            st.write("No data available for the selected state.")
        
def format_crop_quantity(quantity):
    if quantity >= 1e6:
        quantity_in_million = round(quantity / 1e6)
        return f"{quantity_in_million} M Tons"
    elif quantity >= 1e3:
        quantity_in_thousands = round(quantity / 1e3)
        return f"{quantity_in_thousands} K Tons"
    else:
        return f"{round(quantity)} Kg"

def format_crop_area(area):
    if area >= 1e6:
        area_in_square_km = round(area / 1e6)
        return f"{area_in_square_km} Sq.KM"
    elif area >= 1e4:
        area_in_hectares = round(area / 1e4)    
        return f"{area_in_hectares} Hect"
    else:
        return f"{round(area)} Sq.M"

if selected == "Cropscape Overview":
    # Base64 encode the image for the main content
    image_path = "asset/dashboard1.svg"
    image_base64 = get_image_base64(image_path)
    st.markdown(f'<div class="image-container"><img src="data:image/svg+xml;base64,{image_base64}" /></div>', unsafe_allow_html=True)
    st.write(f'# {view}')
    if view == "India":
        col1, col2, col3,col4,col5 = st.columns((2,2,2,2,2),gap="large")
        with col1:
            # Total Production
            total_production = data["Production"].sum()
            total_production = format_crop_quantity(total_production)
            st.metric("Total Production 1997-2015", value=total_production)
        with col2:
            # Total Area
            total_area = data["Area"].sum()
            total_area = format_crop_area(total_area)
            st.metric("Total Area 1997-2015", value=total_area)
        with col3:
            # Highest Production Season
            highest_season = data.groupby("Season").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_season = highest_season.head(1)
            highest_production_season = highest_season["Season"].values[0]
            st.metric("Highest Production Season", value=highest_production_season)    
        with col4:
            # Highest Production Year
            highest_year= data.groupby("Crop_Year").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_year = highest_year.head(1)
            highest_production_year = highest_year["Crop_Year"].values[0]
            st.metric("Highest Production Year", value=highest_production_year)   
        with col5:
            # Highest Production State
            highest_state = data.groupby("State_Name").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_state = highest_state.head(1)
            highest_production_state = highest_state["State_Name"].values[0]
            st.metric("Highest Production State", value=highest_production_state)
        col1, col2 = st.columns((3,3),gap="large")
        with col1:
            #Top 10 Crop production history
            st.write("## Top 10 Crops with production details")
            crop_list = data.groupby("Crop").sum().reset_index().sort_values(by="Production",ascending=False)
            crop_list_display = crop_list[["Crop","Production"]].head(10)
            crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
            crop_list_display.reset_index(drop=True, inplace=True)
            crop_list_display.index += 1
            st.table(crop_list_display)   
        with col2:
            #Area and production list for all states
            st.write("## Area and production list for all States")
            crop_list = data.groupby("State_Name").sum().reset_index().sort_values(by="Production",ascending=False)
            All_states_history = data.groupby("State_Name")[["Production","Area"]].sum().reset_index()
            All_states_history = crop_list[["State_Name","Production","Area"]]
            All_states_history["Production"]=All_states_history["Production"].apply(format_crop_quantity)
            All_states_history["Area"]=All_states_history["Area"].apply(format_crop_area)
            All_states_history.reset_index(drop=True, inplace=True)
            All_states_history.index += 1
            st.table(All_states_history)    
        col1, col2 = st.columns((2,5),gap="large")
        with col1:
            #Season wise Crop List
            st.write("## Season wise Crop List")
            seasons = st.selectbox("## Select Season",options=sorted(data["Season"].unique()))
            selected_season =data[(data["Season"] == seasons)]
            crop_list = selected_season.groupby("Crop").sum().reset_index().sort_values(by="Production",ascending=False)
            if crop_list.empty:
                st.write("No cultivation in this season")
            else:
                crop_list_display = crop_list['Crop']
                crop_list_display.reset_index(drop=True, inplace=True)
                crop_list_display.index += 1
                st.table(crop_list_display)      
        with col2:
            #Production Comparison by Season
            st.write("## Production Comparison by Season")
            st.write("")
            st.write("")
            allseasons = data.groupby("Season").sum().reset_index()
            fig = px.bar(allseasons, x="Season", y="Production", color="Season",height=500,
                        title="Production Comparison by Season")            
            st.plotly_chart(fig, use_container_width=True)    
        col4,col5 = st.columns((2,3),gap="large")
        with col4:
            #Top 10 States production history
            st.write("## Top 10 States with production details")
            crop_list = data.groupby("State_Name").sum().reset_index().sort_values(by="Production",ascending=False)
            crop_list_display = crop_list[["State_Name","Production"]].head(10)
            crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
            crop_list_display.reset_index(drop=True, inplace=True)
            crop_list_display.index += 1
            st.table(crop_list_display)  
        with col5:
            #All States Productions
            st.write("## All States Productions Comparison")
            all_states = data.groupby("State_Name").sum().reset_index()

            fig = px.bar(all_states, x="State_Name", y="Production", labels={'State_Name': 'State Name', 'Production': 'Production'},
                        title=f"All States Productions Comparison",color="Production",height=600)
            st.plotly_chart(fig, use_container_width=True)            
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:        
            #heatmap    
            st.title("Heatmap of Crop Production Across States and Seasons")

            heatmap_data = data.pivot_table(index='State_Name', columns='Season', values='Production', aggfunc='sum')
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
            ax.set_title('Heatmap of Crop Production by State and Season')
            st.pyplot(fig)                
    else:
        selected_state =data[(data["State_Name"] == view)]
        col1, col2, col3,col4,col5 = st.columns((2,2,2,2,2),gap="large")
        with col1:
            # Total Production
            total_production = selected_state["Production"].sum()
            total_production = format_crop_quantity(total_production)
            st.metric("Total Production 1997-2015", value=total_production)
        with col2:
            # Total Area
            total_area = selected_state["Area"].sum()
            total_area = format_crop_area(total_area)
            st.metric("Total Area 1997-2015", value=total_area)
        with col3:
            # Highest Production Season
            highest_season = selected_state.groupby("Season").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_season = highest_season.head(1)
            highest_production_season = highest_season["Season"].values[0]
            st.metric("Highest Production Season", value=highest_production_season) 
        with col4:
            # Highest Production Year
            highest_year= selected_state.groupby("Crop_Year").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_year = highest_year.head(1)
            highest_production_year = highest_year["Crop_Year"].values[0]
            st.metric("Highest Production Year", value=highest_production_year) 
        with col5:                
            # Highest Production District
            highest_state = selected_state.groupby("District_Name").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_state = highest_state.head(1)
            highest_production_district = highest_state["District_Name"].values[0]
            st.metric("Highest Production District", value=highest_production_district)
        col1, col2 = st.columns((3,3),gap="large")
        with col1:
            #Top 10 Crop production history
            st.write("## Top 10 Crops with production details")
            crop_list = selected_state.groupby("Crop").sum().reset_index().sort_values(by="Production",ascending=False)
            crop_list_display = crop_list[["Crop","Production"]].head(10)
            crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
            crop_list_display.reset_index(drop=True, inplace=True)
            crop_list_display.index += 1
            st.table(crop_list_display)         
        with col2:
            #Area and production list for all districts
            st.write("## Area and production list for all districts")
            All_districts_history = selected_state.groupby("District_Name")[["Production","Area"]].sum().reset_index()
            crop_list = selected_state.groupby("District_Name").sum().reset_index().sort_values(by="Production",ascending=False)
            All_districts_history = crop_list[["District_Name","Production","Area"]]
            All_districts_history["Production"]=All_districts_history["Production"].apply(format_crop_quantity)
            All_districts_history["Area"]=All_districts_history["Area"].apply(format_crop_area)
            All_districts_history.reset_index(drop=True, inplace=True)
            All_districts_history.index += 1
            st.table(All_districts_history)
            
        col1, col2 = st.columns((2,5),gap="large")
        with col1:
            #Season wise Crop List
            st.write("## Season wise Crop List")
            seasons = st.selectbox("## Select Season",options=sorted(data["Season"].unique()), index=4)
            selected_season =data[(data["State_Name"] == view) & (data["Season"] == seasons)]
            crop_list = selected_season.groupby("Crop").sum().reset_index().sort_values(by="Production",ascending=False)
            if crop_list.empty:
                st.write("No cultivation in this season")
            else:
                crop_list_display = crop_list['Crop']
                crop_list_display.reset_index(drop=True, inplace=True)
                crop_list_display.index += 1
                st.table(crop_list_display)     
        with col2:
            #Production Comparison by Season
            st.write("## Production Comparison by Season")
            st.write("")
            st.write("")
            allseasons = selected_state.groupby("Season").sum().reset_index()
            fig = px.bar(allseasons, x="Season", y="Production", color="Season",height=500,
                        title="Production Comparison by Season")    
            st.plotly_chart(fig, use_container_width=True)
            
        col4,col5 = st.columns((2,3),gap="large")
        with col4:
            #Top 10 Districts production history
            st.write("## Top 10 Districts with production details")
            crop_list = selected_state.groupby("District_Name").sum().reset_index().sort_values(by="Production",ascending=False)
            crop_list_display = crop_list[["District_Name","Production"]].head(10)
            crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
            crop_list_display.reset_index(drop=True, inplace=True)
            crop_list_display.index += 1
            st.table(crop_list_display)
        with col5:
            #All districts Productions
            st.write("## All districts Productions Comparison")
            st.write("")
            st.write("")
            st.write("")            
            all_districts = selected_state.groupby("District_Name").sum().reset_index()
            fig = px.bar(all_districts, x="District_Name", y="Production", labels={'District_Name': 'District Name', 'Production': 'Production'},
                        title=f"All districts Productions Comparison",color="Production",height=600)
            st.plotly_chart(fig, use_container_width=True)
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            #Heatmap
            st.title("Heatmap of Crop Production Across Districts and Seasons")

            heatmap_data = selected_state.pivot_table(index='District_Name', columns='Season', values='Production', aggfunc='sum')
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
            ax.set_title('Heatmap of Crop Production by Districts and Season')
            st.pyplot(fig)


if selected == "Harvest Chronicles":
    # Base64 encode the image for the main content
    image_path = "asset/dashboard1.svg"
    image_base64 = get_image_base64(image_path)
    st.markdown(f'<div class="image-container"><img src="data:image/svg+xml;base64,{image_base64}" /></div>', unsafe_allow_html=True)    
    st.write("Harvest Chronicles")
    if view == "India":
        col1, col2, col3 = st.columns([1, 5, 5])
        with col1:
            selected_year = st.selectbox("## Select Year",sorted(data["Crop_Year"].unique()))
            selected_data = data[ data["Crop_Year"]==selected_year]
        col1, col2, col3,col4 = st.columns((2,2,2,2),gap="small")
        with col1:
            # Total Production
            total_production = selected_data["Production"].sum()
            total_production = format_crop_quantity(total_production)
            st.metric(f"Total Production {selected_year}", value=total_production)
        with col2:
            # Total Area
            total_area = selected_data["Area"].sum()
            total_area = format_crop_area(total_area)
            st.metric(f"Total Area {selected_year}", value=total_area)
        with col3:
            # Highest Production Season
            highest_season = selected_data.groupby("Season").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_season = highest_season.head(1)
            highest_production_season = highest_season["Season"].values[0]
            st.metric(f"Highest Production Season {selected_year}", value=highest_production_season)    
        with col4: 
            # Highest Production State
            highest_state = selected_data.groupby("State_Name").sum().reset_index().sort_values(by="Production", ascending=False)
            highest_state = highest_state.head(1)
            highest_production_state = highest_state["State_Name"].values[0]
            st.metric(f"Highest Production State {selected_year}", value=highest_production_state)
        col1, col2 = st.columns((3,3),gap="large")
        with col1:
            #Top 10 Crop production history
            st.write(f"## Top 10 Crops with production details - {selected_year}")
            crop_list = selected_data.groupby("Crop").sum().reset_index().sort_values(by="Production",ascending=False)
            crop_list_display = crop_list[["Crop","Production"]].head(10)
            crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
            crop_list_display.reset_index(drop=True, inplace=True)
            crop_list_display.index += 1
            st.table(crop_list_display)   
        with col2:
             #Area and production list for all states
            st.write(f"## Area and production list for all States - {selected_year}")
            crop_list = selected_data.groupby("State_Name").sum().reset_index().sort_values(by="Production",ascending=False)
            All_states_history = selected_data.groupby("State_Name")[["Production","Area"]].sum().reset_index()
            All_states_history = crop_list[["State_Name","Production","Area"]]
            All_states_history["Production"]=All_states_history["Production"].apply(format_crop_quantity)
            All_states_history["Area"]=All_states_history["Area"].apply(format_crop_area)
            All_states_history.reset_index(drop=True, inplace=True)
            All_states_history.index += 1
            st.table(All_states_history)       
        
        col1, col2 = st.columns((2,5),gap="large")
        with col1:
        #Season wise Crop List
            st.write(f"## Season wise Crop List - {selected_year}")
            seasons = st.selectbox("## Select Season",options=sorted(data["Season"].unique()))
            selected_season =selected_data[(selected_data["Season"] == seasons)]
            # Group by Crop and sum up Production and Area
            crop_list = selected_season.groupby("Crop").agg({
                "Production": "sum",
                "Area": "sum"
            }).reset_index().sort_values(by="Production", ascending=False)
            if crop_list.empty:
                st.write("No cultivation in this season")
            else:
                
                crop_list["Production"]=crop_list["Production"].apply(format_crop_quantity)
                crop_list["Area"]=crop_list["Area"].apply(format_crop_area)
                # Reset index to start from 1 for display purposes
                crop_list.reset_index(drop=True, inplace=True)
                crop_list.index += 1
                # Display the table with Crop, Production, and Area
                st.table(crop_list)     
        with col2:
            #Production Comparison by Season
            st.write("## Production Comparison by Season")
            st.write("")
            st.write("")
            allseasons = selected_data.groupby("Season").sum().reset_index()
            fig = px.bar(allseasons, x="Season", y="Production", color="Season",height=500,
                        title=f"Production Comparison by Season - {selected_year}")            
            st.plotly_chart(fig, use_container_width=True)         
            
        col4,col5 = st.columns((2,3),gap="large")
        with col4:
            #Top 10 States production history
            st.write(f"## Top 10 States with production details - {selected_year}")
            crop_list = selected_data.groupby("State_Name").sum().reset_index().sort_values(by="Production",ascending=False)
            crop_list_display = crop_list[["State_Name","Production"]].head(10)
            crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
            crop_list_display.reset_index(drop=True, inplace=True)
            crop_list_display.index += 1
            st.table(crop_list_display)  
        with col5:
            #All States Productions
            st.write(f"## All States Productions Comparison - {selected_year}")
            all_states = selected_data.groupby("State_Name").sum().reset_index()

            fig = px.bar(all_states, x="State_Name", y="Production", labels={'State_Name': 'State Name', 'Production': 'Production'},
                        title=f"All States Productions Comparison",color="Production",height=600)
            st.plotly_chart(fig, use_container_width=True)  
            
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:            
            #heatmap    
            st.title(f"Heatmap of Crop Production Across States and Seasons - {selected_year}")

            heatmap_data = selected_data.pivot_table(index='State_Name', columns='Season', values='Production', aggfunc='sum')
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
            ax.set_title(f'Heatmap of Crop Production by State and Season - {selected_year}')
            st.pyplot(fig)                

        
    else:
        col1, col2, col3 = st.columns([1, 5, 5])
        with col1:
            selected_year = st.selectbox("Select Year",sorted(data["Crop_Year"].unique()), index=3)
            selected_state =data[(data["State_Name"] == view) & (data["Crop_Year"]==selected_year)]
        selected_year = np.int64(selected_year)
        # Convert selected_year to string and strip whitespace
        selected_year_str = str(selected_year).strip()
        if selected_year_str in ["1997", "1998", "1999","2015"]:
            st.write("# No Data")
        else:
            col1, col2, col3,col4 = st.columns((2,2,2,2),gap="small")
            with col1:
                # Total Production
                total_production = selected_state["Production"].sum()
                total_production = format_crop_quantity(total_production)
                st.metric(f"Total Production {selected_year}", value=total_production)
            with col2:
                # Total Area
                total_area = selected_state["Area"].sum()
                total_area = format_crop_area(total_area)
                st.metric(f"Total Area {selected_year}", value=total_area)
            with col3:
                # Highest Production Season
                highest_season = selected_state.groupby("Season").sum().reset_index().sort_values(by="Production", ascending=False)
                highest_season = highest_season.head(1)
                highest_production_season = highest_season["Season"].values[0]
                st.metric(f"Highest Production Season {selected_year}", value=highest_production_season)
            with col4:            
                # Highest Production District
                highest_state = selected_state.groupby("District_Name").sum().reset_index().sort_values(by="Production", ascending=False)
                highest_state = highest_state.head(1)
                highest_production_district = highest_state["District_Name"].values[0]
                st.metric(f"Highest Production District - {selected_year}", value=highest_production_district)
            col1, col2 = st.columns((3,3),gap="large")
            with col1:
                #Top 10 Crop production history
                st.write(f"## Top 10 Crops with production details - {selected_year}")
                crop_list = selected_state.groupby("Crop").sum().reset_index().sort_values(by="Production",ascending=False)
                crop_list_display = crop_list[["Crop","Production"]].head(10)
                crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
                crop_list_display.reset_index(drop=True, inplace=True)
                crop_list_display.index += 1
                st.table(crop_list_display)   
            with col2:
                #Area and production list for all districts
                st.write(f"## Area and production list for all districts - {selected_year}")
                crop_list = selected_state.groupby("District_Name").sum().reset_index().sort_values(by="Production",ascending=False)
                All_districts_history = selected_state.groupby("District_Name")[["Production","Area"]].sum().reset_index()
                All_districts_history = crop_list[["District_Name","Production","Area"]]
                All_districts_history["Production"]=All_districts_history["Production"].apply(format_crop_quantity)
                All_districts_history["Area"]=All_districts_history["Area"].apply(format_crop_area)
                All_districts_history.reset_index(drop=True, inplace=True)
                All_districts_history.index += 1
                st.table(All_districts_history)
            
            col1, col2 = st.columns((3,5),gap="large")
            with col1:                
                #Season wise Crop List
                st.write(f"## Season wise Crop List - {selected_year}")
                seasons = st.selectbox("## Select Season",options=sorted(data["Season"].unique()))
                selected_season =selected_state[(selected_state["Season"] == seasons)]
                # Group by Crop and sum up Production and Area
                crop_list = selected_season.groupby("Crop").agg({
                    "Production": "sum",
                    "Area": "sum"
                }).reset_index().sort_values(by="Production", ascending=False)
                if crop_list.empty:
                    st.write("No cultivation in this season")
                else:
                    # Reset index to start from 1 for display purposes
                    crop_list["Production"]=crop_list["Production"].apply(format_crop_quantity)
                    crop_list["Area"]=crop_list["Area"].apply(format_crop_area)
                    crop_list.reset_index(drop=True, inplace=True)
                    crop_list.index += 1
                    
                    # Display the table with Crop, Production, and Area
                    st.table(crop_list)       
            with col2: 
                #Production Comparison by Season
                st.write("## Production Comparison by Season")
                st.write("")
                st.write("")
                allseasons = selected_state.groupby("Season").sum().reset_index()
                fig = px.bar(allseasons, x="Season", y="Production", color="Season",height=500,
                            title=f"Production Comparison by Season - {selected_year}")    
                st.plotly_chart(fig, use_container_width=True)
            
            col4,col5 = st.columns((2,3),gap="large")
            with col4:    
                #Top 10 Districts production history
                st.write(f"## Top 10 Districts with production details - {selected_year}")
                crop_list = selected_state.groupby("District_Name").sum().reset_index().sort_values(by="Production",ascending=False)
                crop_list_display = crop_list[["District_Name","Production"]].head(10)
                crop_list_display["Production"]=crop_list_display["Production"].apply(format_crop_quantity)
                crop_list_display.reset_index(drop=True, inplace=True)
                crop_list_display.index += 1
                st.table(crop_list_display)
            with col5:
                #All districts Productions
                st.write(f"## All districts Productions Comparison - {selected_year}")
                all_districts = selected_state.groupby("District_Name").sum().reset_index()
                fig = px.bar(all_districts, x="District_Name", y="Production", labels={'District_Name': 'District Name', 'Production': 'Production'},
                            title=f"All districts Productions Comparison",color="Production",height=600)
                st.plotly_chart(fig, use_container_width=True)
                
            
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:                
                #Heatmap
                st.title(f"Heatmap of Crop Production Across Districts and Seasons - {selected_year}")

                heatmap_data = selected_state.pivot_table(index='District_Name', columns='Season', values='Production', aggfunc='sum')
                fig, ax = plt.subplots(figsize=(12, 8))
                sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax)
                ax.set_title('Heatmap of Crop Production by Districts and Season')
                st.pyplot(fig)   

                      
if selected == "Climate Harvest":
    # Base64 encode the image for the main content
    image_path = "asset/dashboard1.svg"
    image_base64 = get_image_base64(image_path)
    st.markdown(f'<div class="image-container"><img src="data:image/svg+xml;base64,{image_base64}" /></div>', unsafe_allow_html=True)    
    if view == "India":
        st.title("State-wise Production for Each Season")
        col1,col2,col3 = st.columns((2,2,5),gap="large")
        with col1:
            seasons = st.selectbox("Select Season", data["Season"].unique())
        with col2:
            years = st.selectbox("Select Year", sorted(data["Crop_Year"].unique()))
        col1, col2= st.columns([5,2])
        with col1:
            filtered_data = data[(data["Season"] == seasons) & (data["Crop_Year"] == years) ]
            with open('json/states_india.geojson') as f:
                india_states_geojson = json.load(f)
            st.subheader(f"{seasons} Production Map - {years}")

            fig = px.choropleth(
                        filtered_data,
                        geojson=india_states_geojson,
                        featureidkey='properties.st_nm',
                        locations='State_Name',
                        projection="mercator",
                        hover_data=['Crop_Year','Season','Production'],
                        color='State_Name',
                        color_discrete_sequence=px.colors.sequential.Viridis,
                        range_color=(filtered_data['Production'].min(), filtered_data['Production'].max())
                        )
            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(
                width=1200,  
                height=1000, 
                margin={"r":0,"t":0,"l":0,"b":0},
                geo=dict(bgcolor='rgba(0,0,0,0)')

            )
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.subheader(f"Top 10 Producing States in {seasons}")
            state_production = filtered_data.groupby("State_Name")["Production"].sum().reset_index().sort_values(by="Production",ascending=False)
            state_production['Serial'] = range(1, len(state_production) + 1)
            state_production = state_production.head(10)
            state_production['Production'] = state_production['Production'].apply(format_crop_quantity)
            state_production_display = pd.DataFrame(state_production[['Serial', "State_Name", "Production"]])
            state_production_display.set_index('Serial', inplace=True)
            state_production_display.columns = ['States', 'Production']
            st.table(state_production_display)
            
            
        st.subheader(f"Production Distribution Across States -  {seasons}")
        state_production = filtered_data.groupby("State_Name")["Production"].sum().reset_index()
        fig = px.bar(state_production, x="State_Name", y="Production", color="State_Name",
                    title=f"Production Distribution Across States -  {seasons}",
                    labels={'State_Name': 'State Name', 'Production': 'Production'})
        st.plotly_chart(fig, use_container_width=True)
        


    else:
        col1,col2,col3 = st.columns((2,2,5),gap="large")
        selected_state =data[(data["State_Name"] == view)]
        st.title("Distric-wise Production for Each Season")
        with col1:
            seasons = st.selectbox("Select Season", selected_state["Season"].unique())
        with col2:
            years = st.selectbox("Select Year", sorted(selected_state["Crop_Year"].unique()))
        col1, col2= st.columns([5,2])
 
        with col1:
            filtered_data = selected_state[(selected_state["Season"] == seasons) & (selected_state["Crop_Year"] == years) ]
            filtered_data1 = selected_state[(selected_state["Season"] == seasons) & (selected_state["Crop_Year"] == years) ]
            formatted_state_name = view.replace(' ', '').lower()
            filtered_data1['District_Name'] = [district.title() for district in filtered_data1['District_Name']]
            if formatted_state_name == "andaman&nicobarislands":
                formatted_state_name='andamanandnicobarislands'
            if formatted_state_name == "dadra&nagarhaveli&daman&diu":
                formatted_state_name='dadranagarhaveli'
            if formatted_state_name == "jammu&kashmir":
                formatted_state_name='jammuandkashmir'                      
            geojson_file_path = f'json/state-geojson-master/{formatted_state_name}.json'
            with open(geojson_file_path) as f:
                state_geojson = json.load(f)
            st.subheader(f"{seasons} Production Map - {years}")
            fig = px.choropleth(
                        filtered_data1,
                        geojson=state_geojson,
                        featureidkey='properties.district',
                        locations='District_Name',
                        projection="mercator",
                        hover_data=['Crop_Year','Season','Production'],
                        color='District_Name',
                        color_discrete_sequence=px.colors.sequential.Viridis,
                        range_color=(filtered_data1['Production'].min(), filtered_data1['Production'].max())
                        )
            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(
                width=1200,  
                height=800, 
                margin={"r":0,"t":0,"l":0,"b":0},
                geo=dict(bgcolor='rgba(0,0,0,0)')

            )
            st.plotly_chart(fig, use_container_width=True)
            
        with col2: 
            st.subheader(f"Top 10 Producing Districts in {seasons}")
            district_production = filtered_data.groupby("District_Name")["Production"].sum().reset_index().sort_values(by="Production",ascending=False)
            district_production['Serial'] = range(1, len(district_production) + 1)
            district_production = district_production.head(10)
            district_production['Production'] = district_production['Production'].apply(format_crop_quantity)
            district_production_display = pd.DataFrame(district_production[['Serial', "District_Name", "Production"]])
            district_production_display.set_index('Serial', inplace=True)
            district_production_display.columns = ['Districts', 'Production']
            st.table(district_production_display)
            
                    
        st.subheader(f"Production Distribution Across Districts -  {seasons}")
        district_production = filtered_data.groupby("District_Name")["Production"].sum().reset_index()
        fig = px.bar(district_production, x="District_Name", y="Production", color="District_Name",height=600,
                    title=f"Production Distribution Across Districts -  {seasons}",
                    labels={'District_Name': 'District Name', 'Production': 'Production'})
        st.plotly_chart(fig, use_container_width=True)
       
        
        
if selected == "Cropfolio Insights":
    # Base64 encode the image for the main content
    image_path = "asset/dashboard1.svg"
    image_base64 = get_image_base64(image_path)
    st.markdown(f'<div class="image-container"><img src="data:image/svg+xml;base64,{image_base64}" /></div>', unsafe_allow_html=True)    
    if view == "India":
        st.title("Crop-specific Production Insights")
        col1,col2,col3 = st.columns((2,2,5),gap="large")
        with col1:
            crop = st.selectbox("Select Crop", data["Crop"].unique())
        filtered_data = data[data["Crop"] == crop]


        st.subheader(f"Seasonal Production of {crop}")
        filtered_data1 = filtered_data.groupby(["Crop_Year","Season"]).sum().reset_index().sort_values(by="Production",ascending=False)
        fig = px.bar(filtered_data1, x="Crop_Year", y="Production", color="Season",height=800,
                    title=f"Seasonal Production of {crop}")
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )        
        fig.update_traces(marker_color='mediumseagreen')
        st.plotly_chart(fig, use_container_width=True)

        st.subheader(f"Production Trend of {crop} Over the Years")
        fig = px.line(filtered_data, x="Crop_Year", y="Production", color="State_Name",height=800,
                    title=f"Production Trend of {crop} Over the Years")
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )        
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        selected_state =data[(data["State_Name"] == view)]
        st.title("Crop-specific Production Insights")
        col1,col2,col3 = st.columns((2,2,5),gap="large")
        with col1:
            crop = st.selectbox("Select Crop", selected_state["Crop"].unique())

        filtered_data_district = selected_state[selected_state["Crop"] == crop]

        filtered_data_district1 = filtered_data_district.groupby(["Crop_Year","Season"]).sum().reset_index().sort_values(by="Production",ascending=False)
        st.subheader(f"Seasonal Production of {crop}")
        fig = px.bar(filtered_data_district1, x="Crop_Year", y="Production", color="Season",height=800,
                    title=f"Seasonal Production of {crop}")
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )       
        fig.update_traces(marker_color='mediumseagreen') 
        st.plotly_chart(fig, use_container_width=True)

        st.subheader(f"Production Trend of {crop} Over the Years")
        fig = px.line(filtered_data_district, x="Crop_Year", y="Production", color="District_Name",height=800,
                    title=f"Production Trend of {crop} Over the Years")
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )        
        st.plotly_chart(fig, use_container_width=True)    
        
        
if selected == "Growth Nexus":
    # Base64 encode the image for the main content
    image_path = "asset/dashboard1.svg"
    image_base64 = get_image_base64(image_path)
    st.markdown(f'<div class="image-container"><img src="data:image/svg+xml;base64,{image_base64}" /></div>', unsafe_allow_html=True)    
    if view == "India":
        st.markdown("# Year-over-Year Production Growth")
        growth = data.groupby("Crop_Year")["Production"].sum()
        fig = px.line(growth, x=growth.index, y=growth.values, labels={'x': 'Year', 'y': 'Year-over-Year Growth'},
                    title="Year-over-Year Production Growth",height=600)
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )
        st.plotly_chart(fig, use_container_width=True)
        
        
        st.title("Trend Analysis")
        state = st.selectbox("# Select State", data["State_Name"].unique())
        filtered_data = data[data["State_Name"] == state]
        filtered_data = filtered_data.groupby("Crop_Year")["Production"].sum().reset_index()
        # Plot production trend over years
        fig = px.bar(filtered_data, x="Crop_Year", y="Production", 
                     title=f"Production Trend in {state}",
                     labels={"Crop_Year": "Year", "Production": "Production (kg)"},
                     width=800, height=600)
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )
        # Customize layout and styling
        fig.update_traces(marker_color='mediumseagreen')

        # Plot
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        selected_state =data[(data["State_Name"] == view)]
        st.markdown("### Year-over-Year Production Growth")
        growth = selected_state.groupby("Crop_Year")["Production"].sum()
        fig = px.line(growth, x=growth.index, y=growth.values, labels={'x': 'Year', 'y': 'Year-over-Year Growth'},
                    title="Year-over-Year Production Growth",height=600)
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )
        st.plotly_chart(fig, use_container_width=True)
        
        
        st.title("Trend Analysis")
        district = st.selectbox("Select District", selected_state["District_Name"].unique())
        
        filtered_data = selected_state[selected_state["District_Name"] == district]
        filtered_data = filtered_data.groupby("Crop_Year")["Production"].sum().reset_index()
        # Plot production trend over years
        fig = px.bar(filtered_data, x="Crop_Year", y="Production", 
                     title=f"Production Trend in {district}",
                     labels={"Crop_Year": "Year", "Production": "Production (kg)"},
                     width=800,  height=600)
        fig.update_layout(
                xaxis=dict(
                tickmode='array',
                tickvals=list(range(1997, 2016)),
                ticktext=list(range(1997, 2016))
            )
        )
        # Customize layout and styling
        fig.update_traces(marker_color='mediumseagreen')

        # Plot
        st.plotly_chart(fig, use_container_width=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.markdown("***")
st.write("Created by **Akshaya Muralidharan** www.linkedin.com/in/akshayam08")
