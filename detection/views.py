from django.shortcuts import render
import joblib
import os
from django.conf import settings
from .forms import EmailForm

# Define paths to model and vectorizer
model_path = os.path.join(settings.BASE_DIR, "detection", "models", "spam_model.pkl")
vectorizer_path = os.path.join(settings.BASE_DIR, "detection", "models", "tfidf_vectorizer.pkl")

# Load model and vectorizer with error handling
model, vectorizer = None, None

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("Model and vectorizer loaded successfully!")  # Debugging
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except Exception as e:
    print(f"Error loading model/vectorizer: {e}")

def detect_spam(request):
    result = None
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["email"]
            if model is None or vectorizer is None:
                result = "Error: Model or vectorizer not loaded!"
            else:
                text_vectorized = vectorizer.transform([text])
                prediction = model.predict(text_vectorized)[0]
                result = "Spam" if prediction == 1 else "Ham"
    else:
        form = EmailForm()
    
    return render(request, "detection/index.html", {"form": form, "result": result})
