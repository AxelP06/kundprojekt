# Lägg till i katalogen

# Härlig Kärlekssoffa
lovely_loveseat_description = "Härlig Kärlekssoffa. Tuftad polyesterblandning av trä. 81 cm hög x 102 cm bred x 76 cm djup. Röd eller vit."
lovely_loveseat_price = 250.00

# Stilfull Bänksoffa
stylish_settee_description = "Stilfull Bänksoffa. Konstläder på björk. 75 cm hög x 139 cm bred x 71 cm djup. Svart."
stylish_settee_price = 180.00

# Lyxig Lampa
luxurious_lamp_description = "Lyxig Lampa. gjort av Glas och järn. 91 cm hög. Brun med cremefärgad skärm."
luxurious_lamp_price = 52.00

# Försäljningsskatt
sales_tax = 0.088  # 8,8%

# Vår första kund

# Initiala variabler
customer_one_total = 0
customer_one_itemization = ""

# Köp Härliga Kärlekssoffan
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description + "\n"

# Köp Lyxiga Lampan
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description + "\n"

# Beräkna försäljningsskatt
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Skriv ut kvitto
print("Rekomendation till kunden:")
print(customer_one_itemization)
print("Totalt pris för kunden:")
print(customer_one_total)
