from django.shortcuts import render

# Create your views here.
import joblib
from django.shortcuts import render
from .forms import EmailForm

# Load the trained model and vectorizer
model = joblib.load(
    r"C:\Users\DELL\Documents\DATA SCIENCE\Spam Detection\spam_model.pkl"
)  # Change to actual path
vectorizer = joblib.load(
    r"C:\Users\DELL\Documents\DATA SCIENCE\Spam Detection\tfidf_vectorizer.pkl"
)


def detect_spam(request):
    result = None
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["content"]
            text_vectorized = vectorizer.transform([text])
            prediction = model.predict(text_vectorized)[0]
            result = "Spam" if prediction == 1 else "Ham"
    else:
        form = EmailForm()
    return render(request, "detection/index.html", {"form": form, "result": result})
