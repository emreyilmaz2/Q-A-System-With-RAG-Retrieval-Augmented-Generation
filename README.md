# Proje: Web Trafik Loglarına Dayalı Yapay Zeka Destekli Soru-Cevap Sistemi

Bu proje, web trafik loglarını kullanarak yapay zeka destekli bir soru-cevap (Q&A) sistemi geliştirmeyi amaçlamaktadır. Kullanıcılar, bu sistem üzerinden doğal dilde sorular sorabilir ve sistem, log verilerini analiz ederek en uygun yanıtları oluşturur. Projenin temelinde Retrieval-Augmented Generation (RAG) modeli yer almaktadır.

## Docker ile Derleme ve Çalıştırma

Projeyi Docker kullanarak çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

bash
Copy code
docker-compose up --build
Bu komut, Docker container'ını derleyip çalıştıracak ve proje, Docker ortamında başlatılacaktır.
## Not
Sistem bu uyarı mesajı gelene kadar müsait olmuyor: '/usr/local/lib/python3.10/site-packages/transformers/tokenization_utils_base.py:1601: FutureWarning: `clean_up_tokenization_spaces`'. Docker ile çalıştıktan sonra bu uyarı mesajı geldikten sonra kullanıma hazır oluyor.

## Projeden Görüntüler
<img width="988" alt="Screenshot 2024-08-19 at 21 02 17" src="https://github.com/user-attachments/assets/5809999d-b0e5-4481-8d1d-8df12397d0e5">
<img width="919" alt="Screenshot 2024-08-19 at 21 03 09" src="https://github.com/user-attachments/assets/4fcd3c1b-91ba-45b5-ba75-db7952934897">
