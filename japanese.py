japanese=["KA", "ZU", "Mi", "TE", "KU", "LU", "Ji", "Ri", "Ki", "ZU", "ME", "TA ", "RiN", "TO", "MO", "NO", "KE", "SHi", "ARi", "CHi", "DO", "RU", "MEi", "NA", "FU", "Z"]
name=input('Enter your Name : ')
name=name.upper()
result=[i if i==' ' else japanese[ord(i)-65] for i in name]
print('Your name in Japanese is ',''.join(result))