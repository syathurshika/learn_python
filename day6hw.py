movie=["Inception","Interstellar","The Matrix","Dune","Avatar"]
print("Original_list:",movie)

movie.append("Oppenheimer")
print("After_append:",movie)

movie.remove("Dune")
print("After_remove:",movie)

print("Sorted alphabetically:")
movie.sort()
for i in range(len(movie)):
    print(f"{i+1}. {movie[i]}")