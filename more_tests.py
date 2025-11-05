import ast

a = [1, 2, 3] #list
b = (1, 2, 3) #tuple -> dapat dimodifikasi setelah tuple dibuat

c = ("english word", "indonesian word") #contoh tuple untuk flashcard

d = [[1,2], [1.2], [5, 5, 4]] #list di dalam list

another_list = [("a", "b"), ("c", "d"), ("e", "f")] #list di dalam list kosong

print(another_list[0])
print(another_list[0][0]) #mengakses elemen pertama dari elemen pertama di dalam list

result = str(another_list)
print(result)

number_list = "[4, 5, 6]" #string yang berisi list
print(ast.literal_eval(number_list)) #mengubah string menjadi list

print(number_list[0]) #mengakses elemen pertama dari string, bukan dari list

print(ast.literal_eval(number_list)[0]) #mengubah string menjadi list