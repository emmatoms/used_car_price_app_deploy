import streamlit as st


def show_explore_page():
    st.title("Explore With CarSock")
    st.subheader("Factors Affects Cars Prices")

    st.write(
    """
    ### Mileage
    As a general rule of thumb, the more miles a car has travelled, the lower the value of the car. This is largely because high-mileage cars usually need more repairs and maintenance, which can be an expensive running cost.
    
    ### Fuel
    The type of fuel that a car consumes is another factor that can affect its value because of the price of the fuel itself and any additional costs connected to its use, such as ULEZ and CAZ charges.
    
    ### Condition
    Wear and tear caused by accident can lower the value slightly, but more major issues can have a big impact on a valuation. The cheapest and easiest way to retain value in your car, however, is by maintaining it and preventing accident that can reduce its value. A clean car suggests to a buyer you’ve cared for it.

    ### Make and model
    Let’s be honest: some cars are just more desirable than others. The more desirable a car is on the second-hand market, the more valuable it is.

    ### Modifications
    By the same token, any modifications made to your car by you or any other owners over the years could have an impact on the overall value. Most modifications mean a reduction in value, as buyers tend to prefer unmodified cars. 

    
    ##### Follow us on all social platforms.

    ##### Get a fast, fair and free car valuation now with CarSock
    """
    )