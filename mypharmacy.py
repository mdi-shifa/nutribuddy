import pandas as pd

def search_medicine_skincare(medicine_name):
    """
    Returns a DataFrame containing product name suggestions and
    direct purchase/search links from 1mg, Netmeds, and Amazon
    for the given medicine or skincare product.
    """
    
    # Sanitize the input
    med = medicine_name.strip().replace(" ", "+")
    
    # Create links for search
    links_data = [
        {
            "Product Name": f"{medicine_name} on 1mg",
            "Price": "Visit site for price",
            "Link": f"https://www.1mg.com/search/all?name={med}"
        },
        {
            "Product Name": f"{medicine_name} on Netmeds",
            "Price": "Visit site for price",
            "Link": f"https://www.netmeds.com/catalogsearch/result?q={med}"
        },
        {
            "Product Name": f"{medicine_name} on Amazon",
            "Price": "Visit site for price",
            "Link": f"https://www.amazon.in/s?k={med}"
        },
    ]
    
    return pd.DataFrame(links_data)
