# Döviz Dönüştürücü API

Bu proje, Python ve Flask kullanılarak geliştirilmiş bir döviz dönüştürücü aracıdır. Kullanıcıların bir para biriminden diğerine dönüştürme yapmalarını sağlayan RESTful bir API sunar. Dönüşüm kurları üçüncü parti bir API'den alınır.

## Özellikler

- Bir para biriminden diğerine istenen miktarda dönüşüm yapabilme.
- Birden fazla para birimini destekler.
- Kolay entegrasyon için REST API sağlar.
- REST API sağlayıcısı fixer.io'dur.

## Gereksinimler

- Python 3.7+ yüklü olmalıdır.
- Flask ve gerekli diğer bağımlılıkları yüklemek için aşağıdaki komutları çalıştırın:
```bash
pip install -r requirements.txt
