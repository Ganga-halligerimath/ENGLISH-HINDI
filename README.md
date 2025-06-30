**"ENGLISH TO HINDI TRANSLATION"**

GOAL IS TO Fine-tune a pre-trained English-to-Hindi translation model using Hugging Face Transformers with TensorFlow backend.
Model used is 
"Helsinki-NLP/opus-mt-en-hi" → This model is already trained for English ➝ Hindi translation.

OBJECTIVE
-Fine-tune a pre-trained model on a custom English-Hindi parallel dataset.
- Tokenize, truncate, and pad the text data for training a Seq2Seq model.
- Train the model with tuned hyperparameters (learning rate, batch size, epochs).
- Evaluate performance using **BLEU score** and **inference time**.
- Save and reuse the model for real-time English-to-Hindi translation.

 Features
 Tokenization and truncation using Hugging Face Tokenizer  
-  Fine-tuning using "TFAutoModelForSeq2SeqLM"  
- Training for **50 epochs**, **batch size 16**  
-  BLEU score evaluation  
-  Real-time translation inference  
-  Translation time measurement  
-  Save and reload model for future use

DATASET
- Parallel English-Hindi sentence pairs
