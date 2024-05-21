programming_dictionary = {
    "Bug": "An error in a program that prevents the program form running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a List in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log["France"]["total_visits"])