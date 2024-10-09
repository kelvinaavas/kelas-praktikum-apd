# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku)
# key nya ga boleh sama kalo, sama nanti yang tertampil yang paling bawah

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848" #jika ingin menggakses ini harus menggunakan print([key][key])
#     }
# }

# print(Biodata["KRS"][0:])

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama" : {123 : "informatika"}})
# print(games["Valorant"]['nama'][123])

# Games ={
#     "Game1" : "PUBG Mobile",
#     "Game2" : " Mobile lagens",
#     "Game3" : {
#         "nama" : "coc",
#         "genre" : "strategy"
#     }
# }
# print((Games.get('Game3')).get('genre'))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")

# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

Film = {
    "Avenger Endgame" : "Action",
    "Sherlock Holmes" : "Mystery",
    "The Conjuring" : "Horror"
}
#Sebelum Ditambah
# print(Film)


Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller",
             "rush hour" : "comedy",
             "oblivion" : "science fiction"})

#Setelah Ditambah
# print(Film)

# del Film["Avenger Endgame"]
# print(Film)


# simpan = Film.pop('Hours')
# # Film.clear()
# print(Film)
# # print(simpan)

# Film["Hours"] = simpan
# print(Film)

# print("Jumlah Data = ", len(Film))

# movies = Film.copy()
# print(movies)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")

# #menggunakan setdefault
# print("Nilai Kimia : ", Nilai.setdefault("Kimia", 70))
# print("")

# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for x, y in value.items():
#         print (x, " : ", y)
# print("")

Nilai = {
"Matematika" : 90,
"fisika" : 80,
"biolopgi" : 80,
"kimia" :70
}

for i, j in Nilai.items():
    print(f"Nilai {i} : {j}")

print("nilai rata rata nya adalah : ", Nilai.setdefault("rata rata", 80))
print("Jumlah Data nya adalah = ", len(Nilai))