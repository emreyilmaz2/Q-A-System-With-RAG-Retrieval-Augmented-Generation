import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset, Dataset

# Tokenizer ve Model'i yükleyin
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
# Tokenizer'ın pad_token'ını eos_token olarak ayarla
tokenizer.pad_token = tokenizer.eos_token

# Dataset'i yükleyin
def load_dataset_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return Dataset.from_dict({"text": [line.strip() for line in lines]})

# Veriyi yükle
dataset = load_dataset_from_file('detailed_logs.txt')

def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=512)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Labels ekleyin
def add_labels(batch):
    batch["labels"] = batch["input_ids"].copy()
    return batch

tokenized_datasets = tokenized_datasets.map(add_labels, batched=True)

# Model eğitim argümanlarını ayarlayın
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="no",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=2,
    weight_decay=0.01,
    logging_dir="./logs",
)

# Trainer oluşturun
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

# Modeli eğitin
trainer.train()

# Modeli kaydedin
model.save_pretrained("trained_gpt2_model")
tokenizer.save_pretrained("trained_gpt2_model")
