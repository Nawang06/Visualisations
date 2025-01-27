import streamlit as st
from visualizations import *

st.set_option('deprecation.showPyplotGlobalUse', False)

# Paths to your JSON files
path_with_santiago = 'compiled_with_santiago_january_2024.json'
path_without_santiago = 'compiled_without_santiago_january_2024.json'

# Load JSON data
data_with_santiago = load_json_data(path_with_santiago)
data_without_santiago = load_json_data(path_without_santiago)

# Define the Streamlit UI components
st.title('Crop Elements Analysis')

# Selection for Santiago
with_santiago = st.radio('Select Data Type', ('With Santiago', 'Without Santiago'))

# Assuming you have a function to get a list of available crops and elements from your dataset
available_crops = ["Limón", "Café", "Maiz", "Naranja", "Uva", "Nogal"]  # This should be dynamically generated from your data
selected_crop = get_crop_id(st.selectbox('Select Crops', available_crops))

# Define macro and micro elements
macro_elements = ['N [%]', 'P [%]', 'K [%]', 'Ca [%]', 'Mg [%]']
micro_elements = ['Fe [mg/kg]', 'Cu [mg/kg]', 'Zn [mg/kg]', 'Mn [mg/kg]', 'B [mg/kg]']
all_elements = macro_elements + micro_elements

# Nutrient type selection
nutrient_type = st.radio("Select Nutrient Type", ['All', 'Macro Nutrients', 'Micro Nutrients'])

# Filter elements based on selection
if nutrient_type == 'Macro Nutrients':
    elements_to_display = macro_elements
elif nutrient_type == 'Micro Nutrients':
    elements_to_display = micro_elements
else:
    elements_to_display = all_elements

# Elements selection based on nutrient type
elements = st.multiselect('Select Elements', elements_to_display, default=elements_to_display)

available_metrics = ['$R^2 Score$', 'MAE', 'MAPE']
selected_metrics = st.radio('Select Metric', available_metrics)
metric_index = available_metrics.index(selected_metrics)

# Selecting between base model and crop model
model_type = st.radio('Model Type', ('Base Model', 'Crop Model'))

# Assuming you have a separate function to filter data based on selected options
# This is a placeholder for whatever data filtering logic you need
crop, crop_data = filter_data(data_with_santiago, data_without_santiago, selected_crop, elements, metric_index,
                            True if model_type=='Base Model' else False, with_santiago)  # Filter your data based on selected options



# Placeholder for your plotting function, adjust as necessary
if st.button('Plot Data'):
    if nutrient_type == "All":
        st.pyplot(plot_all_nutrients(crop,crop_data,selected_metrics))
    else:
       st.pyplot(plot_data(crop,crop_data, selected_metrics))
