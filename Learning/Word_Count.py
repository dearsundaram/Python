song_orig=""" Kodi kodi kodi parakka
Thada thadathu
Pari pari pari thudikka
Kadum manathil
Veri veri veri pirakka
Adukalathil
Pori pori pori parakka
Ethirigalai
Vaalodu velodu ..hoi
Poradu poradu ..hoi
Pada pada pulikodi
Vanam yerattum
Puvinilam puvinilam
Sozham agattum"""

song=song_orig.lower()

###### Convert the string to a list #######
song_in_list=song.split()

print(song_in_list)

###### Create an empty dictionary ##########
song_in_dict={}

for word in song_in_list:
    if word in song_in_dict:
        ####### Convert the List to a Dictionary by adding the values #######
        song_in_dict[word]+=1
    else:
        song_in_dict[word]=1
print(song_in_dict)