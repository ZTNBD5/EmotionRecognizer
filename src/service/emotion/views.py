import numpy as np
from django.shortcuts import redirect, render
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import Sequential

from .forms.DocumentForm import DocumentForm


def predict_by_model(X, weights_path):
    model = Sequential()
    model.add(LSTM(80, input_dim=40))
    model.add(Dense(1, activation='sigmoid'))
    model.load_weights(weights_path)
    return float(model.predict(X)[0, 0])


def predict(request):
    # X.shape = (8064, 40)
    X = np.loadtxt(request.FILES['docfile'], delimiter=",")
    # X.shape = (1, 8064, 40)
    X = np.expand_dims(X, axis=0)

    return [
        predict_by_model(X, 'emotion/keras_models/weights_0.h5'),
        predict_by_model(X, 'emotion/keras_models/weights_1.h5'),
        predict_by_model(X, 'emotion/keras_models/weights_3.h5'),
    ]


def index(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['emotion'] = predict(request)

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Render list page with the documents and the form
    context = {'form': form, 'message': message, 'emotion': request.session.get('emotion', None)}
    return render(request, 'list.html', context)
