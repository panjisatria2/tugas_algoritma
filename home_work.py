print('CALON PILKEDES MINDAKA')
listpendidikan = ['smk','sma','ma','sarjana']
nama = str(input('Masukan Nama : '))
umur = int(input('Masukan Umur : '))
pendidikanterakhir = str(input('Masukan Pendidikan Terakhir [min.sma] : '))
domisili = str(input('Masukan Domisili Anda : '))
kriteria = nama,umur,pendidikanterakhir,domisili

if pendidikanterakhir in listpendidikan and umur >= 35 and domisili == 'mindaka':
    print('Selamat Anda Lolos kriteria Pencalonan')
    print('Ayo Menangkan Pilkades Ini')
else : 
    print('Coba Lagi')

print(kriteria)