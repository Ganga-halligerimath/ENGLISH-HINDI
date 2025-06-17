document.getElementById('translateButton').addEventListener('click', async () => {
    const inputText = document.getElementById('inputText').value;

    // Show loading state or message if needed
    document.getElementById('translatedText').textContent = 'Translating...';
    document.getElementById('translatedTime').textContent = '';
    document.getElementById('bleuscore').textContent = '';

    try {
        const response = await fetch('http://localhost:5000/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const translatedText = data.translated_text;
        const timeTaken = data.time_taken.toFixed(2);  // Format to 2 decimal places
        const bleuScore = data.bleu_score;

        document.getElementById('translatedText').textContent = translatedText;
        document.getElementById('translatedTime').textContent = `${timeTaken} seconds`;
        document.getElementById('bleuscore').textContent = bleuScore ? bleuScore.toFixed(2) : 'N/A';  // Handle undefined score
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('translatedText').textContent = 'Error occurred during translation.';
        document.getElementById('translatedTime').textContent = '';
        document.getElementById('bleuscore').textContent = 'N/A';
    }
});
