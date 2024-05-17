import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open("Used_car_price_prediction2.pki", "rb") as f:
        data = pickle.load(f)
    return data

data = load_model()


regressor  = data["model"]
le_brand = data["le_brand"]
le_fuel_type = data["le_fuel_type"]
le_transmission = data["le_transmission"]
le_accident = data["le_accident"]


def show_predict_page():
    st.title("Welcome to CarSock")

    st.write("""##### Get a fast, fair and free car valuation now""")

    st.write("""CarStock is a used car company dealer that helps you get great prices 
             for your used cars.""")

    
    st.write("""#### Find out what your car is worth""")
    st.write("""###### Please enter your car informations""")

    brand = (
        "BMW",             
        "Ford",             
        "Mercedes-Benz",     
        "Chevrolet",         
        "Toyota",           
        "Audi",              
        "Porsche",          
        "Lexus",             
        "Jeep",              
        "Land",              
        "Nissan",            
        "Cadillac",          
        "RAM",                
        "GMC",                
        "Dodge",              
        "Kia",                
        "Hyundai",            
        "Subaru",             
        "Honda",              
        "Acura",              
        "Mazda",              
        "INFINITI",           
        "Volkswagen",         
        "Lincoln",            
        "Jaguar",             
        "Volvo",              
        "Maserati",           
        "MINI",               
        "Bentley",            
        "Buick",              
        "Lamborghini",        
        "Chrysler",           
        "Mitsubishi",         
        "Genesis",            
        "Alfa",              
        "Hummer",            
        "Pontiac",            
        "Ferrari",           
        "Rolls-Royce",         
        "Aston",               
        "McLaren",             
        "Scion",               
        "Saturn",              
        "FIAT",                
        "Lotus",               
        "Saab",                
        "Mercury",             
        "Bugatti",             
        "Plymouth",            
        "smart",               
        "Maybach",            
        "Suzuki",
    )

    fuel_type = (
        "Gasoline",          
        "Hybrid",             
        "E85 Flex Fuel",      
        "Diesel",             
        "Plug-In Hybrid",     
        "not supported",
    )

    transmission = (
        "A/T",                               
        "8-Speed A/T",                        
        "Transmission w/Dual Shift Mode",     
        "6-Speed A/T",                        
        "6-Speed M/T",                        
        "Automatic",                          
        "7-Speed A/T",                        
        "8-Speed Automatic",                  
        "others",                             
        "10-Speed A/T",                       
        "5-Speed A/T",                         
        "9-Speed A/T",                         
        "6-Speed Automatic",                   
        "4-Speed A/T",                         
        "1-Speed A/T",                         
        "CVT Transmission",                    
        "5-Speed M/T",                         
        "10-Speed Automatic",                  
        "9-Speed Automatic",                   
        "M/T",                                
        "Automatic CVT", 
    )

    accident = (
        "None reported",                            
        "At least 1 accident or damage reported",
    )

    brand = st.selectbox("Car Brand", brand)

    model_year = st.slider("Year Model of the car", 1996, 2024, 2010)

    mileage = st.number_input("Car Mileage", 100, 100000)

    fuel_type = st.selectbox("Fuel Type", fuel_type)

    transmission = st.selectbox("Transmission Type", transmission)

    accident = st.selectbox("Has being involved in an accident", accident)

    

    ok = st.button("Calculate Price")
    if ok:
        x = np.array([[brand, model_year, mileage
                       , fuel_type, transmission, accident]])
        x[:,0] = le_brand.transform(x[:,0])
        x[:,3] = le_fuel_type.transform(x[:,3])
        x[:,4] = le_transmission.transform(x[:,4])
        x[:,5] = le_accident.transform(x[:,5])
        x = x.astype(float) 

        price = regressor.predict(x)
        st.subheader(f"The estimated salary is ${price[0]:,.2f}")
                      