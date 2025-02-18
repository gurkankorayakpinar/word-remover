import os

def remove_first_n_words(filename, n):
    # Dosya ismini "isim" ve "uzantı" olarak ayır.
    name, ext = os.path.splitext(filename)
    
    # İsmi kelimelere ayır.
    words = name.split()
    
    # Eğer kelime sayısı n'den küçükse, hata fırlat
    if len(words) <= n:
        raise ValueError(f'Hata! {n} kelime silinebilmesi için, en az {n+1} kelime olmalıdır: "{filename}"')
    else:
        # İlk n kelimeyi sil ve kalanı birleştir
        new_name = ' '.join(words[n:])
        # Baştaki ve sondaki boşlukları temizle
        new_name = new_name.strip()
        # Uzantıyı ekleyerek yeni dosya ismini oluştur
        new_filename = new_name + ext
        return new_filename

def remove_last_n_words(filename, n):
    # Dosya ismini isim ve uzantı olarak ayır
    name, ext = os.path.splitext(filename)
    
    # İsmi kelimelere ayır
    words = name.split()
    
    # Eğer kelime sayısı n'den küçükse, hata fırlat
    if len(words) <= n:
        raise ValueError(f'Hata! {n} kelime silinebilmesi için, en az {n+1} kelime olmalıdır: "{filename}"')
    else:
        # Sondan n kelimeyi sil ve kalanı birleştir
        new_name = ' '.join(words[:-n])
        # Baştaki ve sondaki boşlukları temizle
        new_name = new_name.strip()
        # Uzantıyı ekleyerek yeni dosya ismini oluştur
        new_filename = new_name + ext
        return new_filename

def rename_files_in_folder(folder_path, n, remove_from_start):
    # Klasördeki tüm dosyaları listele
    for filename in os.listdir(folder_path):
        try:
            # Kullanıcının seçimine göre işlem yap
            if remove_from_start:
                new_filename = remove_first_n_words(filename, n)
            else:
                new_filename = remove_last_n_words(filename, n)
            
            # Eski ve yeni dosya yollarını oluştur
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Dosyayı yeniden adlandır
            os.rename(old_file_path, new_file_path)
            print(f'Değiştirildi: {filename} --→ {new_filename}')
        except ValueError as e:
            # Eğer dosya isminde yeterli kelime yoksa, mesaj göster
            print(e)
        except FileExistsError:
            # Eğer aynı isimde bir dosya zaten varsa, mesaj göster
            print(f'Aynı isimde başka bir dosya var: "{new_filename}" --→ İşlem gerçekleştirilemedi.')
        except Exception as e:
            # Diğer hatalar için genel bir mesaj göster
            print(f'Dosya ismi değiştirilirken bir hata oluştu: "{filename}" - Hata: {e}')

if __name__ == "__main__":
    # Klasör yolu
    folder_path = 'files'
    
    # Kullanıcıdan baştan mı sondan mı silmek istediğini al
    while True:
        remove_from_start = input("Baştan mı yoksa sondan mı silmek istiyorsunuz? (baştan / sondan): ").strip().lower()
        if remove_from_start in ['baştan', 'sondan']:
            break
        else:
            print("Geçersiz seçenek! Lütfen 'baştan' veya 'sondan' yazın.")
    
    # Kullanıcıdan kaç kelime silmek istediğini al
    while True:
        try:
            n = int(input(f"{remove_from_start.capitalize()} kaç kelime silinsin? "))
            if n <= 0:
                print("Lütfen pozitif bir sayı girin.")
            else:
                break
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")
    
    # Dosyaları yeniden adlandır
    rename_files_in_folder(folder_path, n, remove_from_start == 'baştan')
