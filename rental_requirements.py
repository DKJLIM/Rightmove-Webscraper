##Rental requirement details

location = "London Bridge"



##rental requirements
search_radius = str(0.5)
price_range_min = str(100)
price_range_max = str(2000)
bedrooms_min = str(1)
bedrooms_max = str(2)
property_type = "flats"


dictionary = {
    'search_radius': ['radius',search_radius],
    'price_range_min': ['minPrice',price_range_min],
    'price_range_max': ['maxPrice',price_range_max],
    'bedrooms_min': ['minBedrooms', bedrooms_min],
    'bedrooms_max': ['maxBedrooms', bedrooms_max],
    'property_type': ['displayPropertyType', property_type],
}
