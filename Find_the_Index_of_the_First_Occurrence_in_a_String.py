def cari_substring(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        cocok = "Benar"
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                cocok = "Salah"
                break
        if cocok == "Benar":
            return i
    return -1

# Panggil fungsi
hasil = cari_substring("halhaloo", "hal")
print(hasil)