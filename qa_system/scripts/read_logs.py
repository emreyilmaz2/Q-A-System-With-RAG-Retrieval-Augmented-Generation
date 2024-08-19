# read_logs.py

import re
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
import numpy as np

# Modeli yükle
model = SentenceTransformer('all-MiniLM-L6-v2')

def process_query(query_text):
    def create_vectorizer(parsed_logs):
        paths = [log['path'] for log in parsed_logs]
        vectorizer = TfidfVectorizer()
        vectorizer.fit(paths)
        return vectorizer

    def encode_text(text, vectorizer):
        return vectorizer.transform([text]).toarray()

    def read_log_file(filename):
        with open(filename, "r") as file:
            log_lines = file.readlines()
        return log_lines

    def parse_log_line(log_line):
        log_pattern = re.compile(
            r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\w+) (?P<path>[^\s]+) HTTP/1.1" (?P<status>\d+) (?P<size>\d+)'
        )
        match = log_pattern.match(log_line)
        if match:
            return match.groupdict()
        return None

    def parse_log_file(filename):
        log_lines = read_log_file(filename)
        parsed_logs = [parse_log_line(line) for line in log_lines if parse_log_line(line)]
        return parsed_logs

    # Log dosyasını okuyup verileri ayıklama
    # parsed_logs = parse_log_file("/data/market_logs.txt")
    parsed_logs = parse_log_file("/app/data/market_logs.txt")
    vectorizer = create_vectorizer(parsed_logs)

    def vectorize_paths(parsed_logs):
        paths = [log['path'] for log in parsed_logs]
        vectorizer = TfidfVectorizer()
        path_vectors = vectorizer.fit_transform(paths)
        return path_vectors

    # Vektörleştirilmiş verileri elde etme
    path_vectors = vectorize_paths(parsed_logs)

    def load_vectors_to_faiss(path_vectors):
        dimension = path_vectors.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(path_vectors.toarray())
        return index

    # FAISS indeksi oluşturma ve vektörleri yükleme
    index = load_vectors_to_faiss(path_vectors)

    def search_similar_paths(index, query_vector, k=25):
        distances, indices = index.search(query_vector, k)
        return distances, indices

    query_vector = encode_text(query_text, vectorizer)
    distances, indices = search_similar_paths(index, query_vector, k=25)

    def generate_response(logs):
        combined_text = "\n".join([f"Log path: {log['path']}, Timestamp: {log['timestamp']}" for log in logs])
        return combined_text

    retrieved_logs = [parsed_logs[idx] for idx in indices[0]]
    response = generate_response(retrieved_logs)
    
    return response

















# import re
# import faiss
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sentence_transformers import SentenceTransformer
# import numpy as np
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import torch

# # # Model ve tokenizer'ı yükleyin
# # model_name = "gpt2"
# # tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# # model = GPT2LMHeadModel.from_pretrained(model_name)

# # Modeli yükle
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # TfidfVectorizer'ı oluşturma ve fit etme
# def create_vectorizer(parsed_logs):
#     paths = [log['path'] for log in parsed_logs]
#     vectorizer = TfidfVectorizer()
#     vectorizer.fit(paths)
#     return vectorizer

# # Metni vektöre dönüştür
# def encode_text(text, vectorizer):
#     return vectorizer.transform([text]).toarray()

# # Log dosyasını okuma
# def read_log_file(filename):
#     with open(filename, "r") as file:
#         log_lines = file.readlines()
#     return log_lines

# # Log verilerinden IP adresi, erişilen sayfa, zaman damgası, durum kodu ve boyut ayıklama
# def parse_log_line(log_line):
#     log_pattern = re.compile(
#         r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\w+) (?P<path>[^\s]+) HTTP/1.1" (?P<status>\d+) (?P<size>\d+)'
#     )
#     match = log_pattern.match(log_line)
#     if match:
#         return match.groupdict()
#     return None

# # Log dosyasını okuma ve gerekli verileri ayıklama
# def parse_log_file(filename):
#     log_lines = read_log_file(filename)
#     parsed_logs = [parse_log_line(line) for line in log_lines if parse_log_line(line)]
#     return parsed_logs

# # Örnek: Log dosyasını okuyup verileri ayıklama
# parsed_logs = parse_log_file("market_logs.txt")
# print(parsed_logs[:5])  # İlk 5 log kaydını yazdırma
# vectorizer = create_vectorizer(parsed_logs)


# # Path bilgisini vektörleştirme
# def vectorize_paths(parsed_logs):
#     paths = [log['path'] for log in parsed_logs]
#     vectorizer = TfidfVectorizer()
#     path_vectors = vectorizer.fit_transform(paths)
#     return path_vectors

# # Vektörleştirilmiş verileri elde etme
# path_vectors = vectorize_paths(parsed_logs)
# print("Vectors shape: " , path_vectors.shape)  # Vektörlerin boyutunu yazdırma





# # FAISS kullanarak vektörleri veri tabanına yükleme
# def load_vectors_to_faiss(path_vectors):
#     dimension = path_vectors.shape[1]
#     index = faiss.IndexFlatL2(dimension)  # L2 mesafesine göre bir FAISS indeksi oluşturma
#     index.add(path_vectors.toarray())  # Vektörleri FAISS indeksine ekleme
#     return index

# # FAISS indeksi oluşturma ve vektörleri yükleme
# index = load_vectors_to_faiss(path_vectors)

# # Bir sorgu vektörüyle en yakın komşuları arama
# def search_similar_paths(index, query_vector, k=5):
#     # Vektör boyutunu kontrol edin ve uygun şekilde yeniden şekillendirin
#     distances, indices = index.search(query_vector, k)
#     return distances, indices

# # Sorgu metnini vektörleştirme
# # query_text = "orange POST 200 241.155.108.94"
# query_text = "What types of products do customers search mostly"
# query_vector = encode_text(query_text, vectorizer)
# distances, indices = search_similar_paths(index, query_vector, k=300)

# print("Bulunan en yakın path'ler (indeksler):", indices)

# print("\nEn Yakın Log Kayıtları:")
# for i, idx in enumerate(indices[0]):
#     print(f"En Yakın {i+1}:")
#     print(parsed_logs[idx])
#     print(f"Mesafe: {distances[0][i]}")
#     print()

# # FAISS'ten çekilen logları birleştirme
# # def combine_logs_for_generation(logs):
# #     combined_text = "\n".join([f"Log path: {log['path']}, Timestamp: {log['timestamp']}" for log in logs])
# #     return combined_text

# # Kullanıcıya yanıt oluşturma
# # def generate_response(logs):
# #     combined_text = combine_logs_for_generation(logs)
# #     inputs = tokenizer.encode(combined_text, return_tensors="pt", max_length=1024, truncation=True)
# #     attention_mask = torch.ones(inputs.shape, dtype=torch.long)
# #     outputs = model.generate(inputs, attention_mask=attention_mask, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
# #     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# #     return response

# def generate_response(logs):
#     combined_text = "\n".join([f"Log path: {log['path']}, Timestamp: {log['timestamp']}" for log in logs])
#     # GPT2 Modeli ile kurulum yapilamadigindan dolayi sadece sentence transformer
#     return combined_text

# retrieved_logs = [parsed_logs[idx] for idx in indices[0]]
# # # Generatif model ile yanıt oluşturma
# response = generate_response(retrieved_logs)
# print("Yanıt:", response)