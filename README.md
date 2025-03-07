# Word Remover

- Bu proje, belirli bir klasördeki dosya isimleri üzerinde "kelime silme" işlemi yapan bir uygulamadır.

***

- İşlem yapılacak dosyalar, "files" klasörü içerisinde yer almalıdır.

- Kelime silme işlemi, "files" klasörü içerisindeki tüm dosyalara uygulanır.

- Baştan veya sondan kelime silmek mümkündür.

- Kullanıcıya, (baştan veya sondan) kaç kelime sileceği sorulmaktadır.

- Tek kelime içeren dosyalarda "kelime silme" işleminin engellenmesi için `len(words)` fonksiyonu kullanılmıştır. Kelime silme işleminin yapılabilmesi için, aralarında en az 1 boşluk bulunan en az 2 kelime olması gerekir. Bitişik ya da aralarında "alt çizgi" gibi işaretler barındıran kelimeler, "tek kelime" kabul edilmektedir.

- Kelime silme işleminin akabinde, en sağdaki ve en soldaki boşlukların otomatik olarak temizlenmesi sağlanmıştır.

- Olası hatalar için "Exception Handling" uygulanmıştır.