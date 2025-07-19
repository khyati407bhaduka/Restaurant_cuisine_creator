from langchain_function_helper import genarte_restaurant

if __name__ == "__main__":
    result = genarte_restaurant("Indian")
    print("Restaurant Name:", result["restaurant_name"])
    print("Menu Items:")
    for item in result["restaurant_menu"].split(","):
        print("-", item.strip())
