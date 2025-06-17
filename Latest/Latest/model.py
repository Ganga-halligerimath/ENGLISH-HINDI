from flask import Flask, request, jsonify
import time
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
from flask_cors import CORS
import sacrebleu


# Load the model and tokenizer using from_pretrained
model_directory1 = "model_directory1"  # Update this to your model directory path
tokenizer = AutoTokenizer.from_pretrained(model_directory1)
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_directory1)

app = Flask(__name__)
CORS(app, resources={r"/translate": {"origins": "http://localhost:5501"}})


# Read the reference translations from the file using UTF-8 encoding
reference_translations = {}
with open('eng-hindi.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():
            # Check if the line contains a period to split on
            if '.' in line:
                eng_sentence, hindi_translation = line.strip().split('.', 1)
                eng_sentence = eng_sentence.strip()  # Clean up leading/trailing spaces
                hindi_translation = hindi_translation.strip()  # Clean up leading/trailing spaces
                reference_translations[eng_sentence] = hindi_translation
            else:
                print(f"Skipping line (no period found): {line}")

# Translation endpoint
@app.route('/translate', methods=['POST'])
def translate():
    # Record the start time
    start_time = time.time()

    data = request.get_json()
    text = data.get('text', '')

    # Tokenize and translate
    inputs = tokenizer.encode(text, return_tensors="tf")
    outputs = model.generate(inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Calculate BLEU score
    bleu_score = None
    reference = reference_translations.get(text, None)  # Get reference translation if available

    if reference:
        # Use sacrebleu for sentence-level BLEU score
        bleu = sacrebleu.sentence_bleu(translated_text, [reference])
        bleu_score = bleu.score
    else:
        print(f"Text not found in reference translations: {text}")

    return jsonify({
        'translated_text': translated_text,
        'time_taken': elapsed_time,
        'bleu_score': bleu_score
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)