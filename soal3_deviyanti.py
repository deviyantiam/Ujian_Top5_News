try:
    print('\nSelamat datang, mau tahu berita apa hari ini?\n[1] Berita seputar teknologi\n[2] Berita seputar bisnis\n[3] Berita seputar olahraga\n[4] Berita seputar kesehatan\n[5] Berita seputar science')
    inp=int(input('Ketik pilihan Anda [1/2/3/4/5]: '))
    apikey='81a9bbd082eb438b87b9f930529e9fbf'  
    bidang={1:'technology',
            2:'business',
            3:'sports',
            4:'health',
            5:'science'}
    import requests
    url='https://newsapi.org/v2/top-headlines?country=id&category='+bidang[inp]+'&apiKey='+apikey
    data=requests.get(url)
    isi=data.json()
    print('\nBerikut adalah top 5 berita Indonesia bidang '+bidang[inp]+' :')
    for i in range(5): #top5 aja
        print(str(i+1)+' - '+isi['articles'][i]['title'])
    print('\n')
except:
        print('Maaf, Anda salah input')