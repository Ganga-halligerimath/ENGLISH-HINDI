from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

# Load the model from Hugging Face
model_checkpoint = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)

# Save model and tokenizer in a directory
model.save_pretrained("model_directory1")
tokenizer.save_pretrained("model_directory1")