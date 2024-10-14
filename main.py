meme_dict = {"cringe": "garip ya da utandırıcı şey","meem": "internet şakası", "troll": "alay durumlarında kullanılır", "sus": "şüpheli"}
word = input("anlamayı istediğin kelimeyi gir")
if word in meme_dict.keys():
    print("aradığın kelimenin anlamı:", meme_dict[word])
else:
    print("aradığınız kelime sözlükte yok! ")
