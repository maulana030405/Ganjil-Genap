# Tugas Program Ganjil Genap MAULANA
# Semoga bisa bermanfaat dalam Pembelajaran Informatika :)

# while True digunakan untuk mengulang (looping) program sampai memilih [4] Berhenti
while True:

    # Tampilan Program
    batas = ('====================')
    print (batas)
    print ('Program Ganjil Genap')
    print (batas)
    print ('[1] Bilangan Ganjil')
    print ('[2] Bilangan Genap')
    print ('[3] Periksa Bilangan Genap/Ganjil')
    print ('[4] Berhenti')
    print (batas)

# while True digunakan untuk mengulang (looping) dalam memilih nomor program
    while True:

        # Pemilihan Nomor Program
        pilihan = input('Pilih nomor program (1/2/3/4) = ')
        print (batas)
        
        if pilihan in ('1', '2', '3', '4'):

            # Berlaku hanya untuk program [1] Bilangan Ganjil dan [2] Bilangan Genap
            if pilihan in ('1', '2'):
                print ('Masukkan bilangan awal dan akhir sebagai range')
                bil_awal = int(input('Masukkan bilangan awal = '))
                bil_akhir = int(input('Masukkan bilangan akhir = '))
                print (batas)

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
                    print ('\n'* 2)
                    break
                
                
                # Program [2] Bilangan Genap
                elif pilihan == '2':
                    print ('Bilangan Genap = {}'.format(', '.join([str(bil) for bil in bil_genap])))
                    print ('\n'* 2)
                    break
            
            # Program [3] Periksa Bilangan Genap/Ganjil
            elif pilihan == '3':
                periksa_bil = int(input('Masukkan angka = '))
                print (batas)
                print (periksa_bil, 'adalah bilangan', 'genap' if (periksa_bil % 2 == 0) else 'ganjil')
                print ('\n'* 2)
                break

            # Program [4] Berhenti
            elif pilihan == '4':
                raise SystemExit

        # Pilihan lain
        else:
            print ('Input salah')
            print ('\n'* 2)
            break
        
# Demikian Program Saya :) 
