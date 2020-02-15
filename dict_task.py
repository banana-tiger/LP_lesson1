cities_temp = {"city": "Москва", "temperature": "20"}
print(cities_temp["city"])
cities_temp["temperature"] = int(cities_temp["temperature"]) - 5
print(cities_temp)

#Task 2

print("country" in cities_temp)

cities_temp["country"] = "Россия"

cities_temp["date"] = "27.05.2019"

print(len(cities_temp))

#a = cities_temp["example"]
#print(a)
#a1 = cities_temp.get("example")
#print(a1)

print(cities_temp)
