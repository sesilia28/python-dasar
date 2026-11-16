# break menghentikan loop, continue melewati satu iterasi
for i in range(1, 8):
    if i == 4:
        continue # lewati angka 4
    if i == 6:
        break # hentikan loop saat i == 6
    print(i)
