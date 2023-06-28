# USB Belleğe Dosya Kopyalama

Bu Python betiği, belirtilen dosya yollarındaki dosyaları bir USB belleğe kopyalar.


## Gereksimler
- pip install os
- pip install shutil



## Kullanım

1. Bir metin düzenleyici açın ve verilen Python kodunu yapıştırın.

2. `file_paths` listesine kopyalanacak dosya yollarını ekleyin. Örnek olarak:

    ```python
    file_paths = [
        "C:/Users/Kullanici/Desktop/dosya1.txt",
        "C:/Users/Kullanici/Documents/dosya2.jpg"
    ]
    ```

3. `usb_path` değişkenine USB bellek yolunu ekleyin. Örneğin:

    ```python
    usb_path = "E:/USB"
    ```

4. Kaydedin ve dosyayı `.py` uzantısı ile kaydedin, örneğin `usb_kopyalama.py`.

5. Script dosyasını çalıştırmak için Python yüklediğinizden emin olun.

6. Script dosyasını çalıştırmak için bir terminal açın ve aşağıdaki komutu çalıştırın:

    ```shell
    python usb_kopyalama.py
    ```

7. Script, belirtilen dosya yollarındaki dosyaları USB belleğe kopyalar ve işlem sonunda başarı veya hata mesajlarını görüntüler.

## Lisans

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.
