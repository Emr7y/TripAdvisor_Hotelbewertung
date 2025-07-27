# 🏨 TripAdvisor Hotel Reviews – Sentimentanalyse

&#x20;&#x20;

Dieses Projekt beschäftigt sich mit der Klassifikation von Hotelbewertungen auf TripAdvisor als **positiv oder negativ**. Ziel ist eine einfache, robuste Sentimentanalyse mit klassischen Machine-Learning-Methoden und **TF-IDF-Vektorisierung**.

---

## 🔍 Projektbeschreibung

Mit Hilfe von echten Hotelbewertungen lernte ein Modell automatisch, wie „positive“ und „negative“ Texte typischerweise aussehen. Dieses Modell kann dann auf neue Bewertungen angewendet werden – z. B. in einer **interaktiven Web-App**, die auf Hugging Face läuft.

---

## 🧠 Modell

* **Modelltyp**: Logistic Regression
* **Vektorisierung**: TF-IDF
* **Genauigkeit**: ca. 88,5 %
* **Zielvariable**: `Sentiment` (0 = negativ, 1 = positiv)

Modell und Vektorisierer sind in `.pkl`-Dateien gespeichert und in der App integriert.

---

## 📁 Projektstruktur

```bash
├── app.py                     # Streamlit-App für Sentimentanalyse
├── model.pkl                  # Gespeichertes Modell
├── tfidf_vectorizer.pkl       # TF-IDF-Vektorisierer
├── submission_demo.csv        # Beispielhafte Submission (mit echten Labels)
├── requirements.txt           # Python-Abhängigkeiten
├── README.md                  # Projektbeschreibung
└── data/
    └── tripadvisor_reviews.csv  # Optional: Originaldatensatz
```

---

## 🖥️ Web-App (lokal starten)

```bash
pip install -r requirements.txt
streamlit run app.py
```

➡ Du gibst einen Hotel-Bewertungstext ein – das Modell klassifiziert ihn als **positiv** oder **negativ** 🟢🔴

---

## 🌐 Web-App (online nutzen)

Das Projekt ist auch **live auf Hugging Face** verfügbar:

🔗 [**Zur App auf Hugging Face**](https://huggingface.co/spaces/emr7y/Tripadvisor_Hotel_Bewertungen)

---

## ⚙️ Installation (lokal)

```bash
git clone https://github.com/DeinGitHubName/tripadvisor-sentiment.git
cd tripadvisor-sentiment
pip install -r requirements.txt
```

---

## 📊 Beispiel-Output

Die Datei `submission_demo.csv` zeigt einen typischen Modelloutput mit:

* Bewertungstext
* Vorhergesagtem Sentiment
* Wahrem Label (falls verfügbar)

---

## 👨‍💼 Autor

Made with ❤️ by [**Emr7y**](https://github.com/Emr7y)

---

## 📄 Lizenz

Dieses Projekt steht unter der **MIT License** – frei zur Nutzung & Erweiterung!

---
