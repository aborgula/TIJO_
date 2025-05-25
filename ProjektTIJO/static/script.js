// Zaznaczanie analizy
let selectedAnalysis = '';

const analysisPrompts = {
  'SOLID': 'Przeanalizuj poniższy kod pod kątem przestrzegania zasad SOLID i wskaż ewentualne naruszenia.',
  'OOP': 'Sprawdź, czy poniższy kod wykorzystuje dobre praktyki programowania obiektowego i zaproponuj ulepszenia.',
  'DRY': 'Zidentyfikuj powtórzenia w kodzie i zaproponuj jak zastosować zasadę DRY (Don’t Repeat Yourself).',
  'KISS': 'Czy kod jest prosty i zrozumiały? Oceń zgodność z zasadą KISS i zaproponuj uproszczenia.',
  'Prawo Demeter': 'Sprawdź, czy kod nie narusza prawa Demeter (zasady najmniejszej wiedzy) i uzasadnij odpowiedź.',
  'Code smell': 'Zidentyfikuj potencjalne „code smells” w tym kodzie i zaproponuj ich refaktoryzację.',
  'Wygeneruj testy': 'Wygeneruj testy jednostkowe (unit tests) dla poniższego kodu w odpowiednim frameworku.',
  'Przypadki testowe': 'Na podstawie logiki poniższego kodu zaproponuj zestaw przypadków testowych (test cases).',
  'Analiza pokrycia': 'Przeanalizuj pokrycie kodu testami i zasugeruj dodatkowe przypadki, które warto przetestować.',
  'Udokumentuj kod': 'Wygeneruj dokumentację techniczną dla poniższego kodu, z opisem funkcji, klas i parametrów.'
};



document.querySelectorAll('.analysis-btn').forEach(button => {
  button.addEventListener('click', () => {
    selectedAnalysis = button.innerText;
    document.querySelectorAll('.analysis-btn').forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');

    // Ustaw domyślny prompt
    document.getElementById('customPrompt').value = analysisPrompts[selectedAnalysis] || '';
  });
});


// Wczytaj kod z pliku
document.getElementById('fileInput').addEventListener('change', event => {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = e => {
    document.getElementById('codeInput').value = e.target.result;
  };
  reader.readAsText(file);
});

// Pobierz odpowiedź jako plik
document.getElementById('downloadBtn').addEventListener('click', () => {
  const text = document.getElementById('responseOutput').value;
  const blob = new Blob([text], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'odpowiedz_gemini.txt';
  a.click();
  URL.revokeObjectURL(url);
});

// Odpowiedź
document.getElementById('sendBtn').addEventListener('click', () => {
  const code = document.getElementById('codeInput').value;
  const prompt = document.getElementById('customPrompt').value;
  const sendBtn = document.getElementById('sendBtn');


  if (!code.trim()) {
    alert('Wklej lub wczytaj kod!');
    return;
  }

    // Zablokuj przycisk na czas analizy
  sendBtn.disabled = true;
  sendBtn.innerText = 'Analizuję...';

 fetch('/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      code,
      prompt,
      analysis: selectedAnalysis || 'Ogólna analiza'
    })
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        document.getElementById('responseOutput').value = '❌ Błąd: ' + data.error;
      } else {
        document.getElementById('responseOutput').value = data.response;
      }
    })
    .catch(err => {
      document.getElementById('responseOutput').value = '❌ Błąd połączenia: ' + err;
    })
    .finally(() => {
      // Odblokuj przycisk po analizie (sukces lub błąd)
      sendBtn.disabled = false;
      sendBtn.innerText = 'Wyślij do Gemini';
    });
});
