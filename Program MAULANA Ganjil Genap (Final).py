# Tugas Program Ganjil Genap MAULANA
# Semoga bisa bermanfaat dalam Pembelajaran Informatika :)

# while True digunakan untuk mengulang (looping) program sampai memilih [4] Berhenti
while True:

    # Tampilan Program
    print ('Program Ganjil Genap')
    print ('====================')
    print ('[1] Bilangan Ganjil')
    print ('[2] Bilangan Genap')
    print ('[3] Periksa Bilangan Genap/Ganjil')
    print ('[4] Berhenti')
    print ('====================')

# while True digunakan untuk mengulang (looping) dalam memilih nomor program
    while True:

        # Pemilihan Nomor Program
        pilihan = input('Pilih nomor program (1/2/3/4) = ')
        
        if pilihan in ('1', '2', '3', '4'):

            # Berlaku hanya untuk program [1] Bilangan Ganjil dan [2] Bilangan Genap
            if pilihan in ('1', '2'):
                print ('Masukkan bilangan awal dan akhir sebagai range')
                bil_awal = int(input('Masukkan bilangan awal = '))
                bil_akhir = int(input('Masukkan bilangan akhir = '))

                # Membuat tipe data list sebagai set kumpulan anggota angka ganjil & genap
                list_bil = [i for i in range(bil_awal, bil_akhir +1)]
                bil_ganjil = []
                bil_genap = []

                # Membedakan anggota angka yang ganjil & genap
                for bil in list_bil:
                        if bil % 2 == 0:
                            bil_genap.append(bil)
                        else:
                            bil_ganjil.append(bil)
                            
                # Program [1] Bilangan Ganjil
                if pilihan == '1':
                    print ('Bilangan Ganjil = {}'.format(', '.join([str(bil) for bil in bil_ganjil])))
                    print ('====================')
                    break
                
                # Program [2] Bilangan Genap
                elif pilihan == '2':
                    print ('Bilangan Genap = {}'.format(', '.join([str(bil) for bil in bil_genap])))
                    print ('====================')
                    break

            # Program [3] Periksa Bilangan Genap/Ganjil
            elif pilihan == '3':
                periksa_bil = int(input('Masukkan angka = '))
                print (periksa_bil, 'adalah bilangan', 'genap' if (periksa_bil % 2 == 0) else 'ganjil')
                print ('====================')
                break

            # Program [4] Berhenti
            elif pilihan == '4':
                raise SystemExit

        # Pilihan lain
        else:
            print ('Nomor masukan salah')
            print ('====================')
            break
        
# Demikian Program Saya :) 
