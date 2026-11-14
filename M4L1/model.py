from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


def get_class(model_path, labels_path, image_path):
    np.set_printoptions(suppress=True)
    model = load_model(model_path, compile=False)
    with open(labels_path, "r", encoding="utf-8") as labels_file:
        class_names = [line.strip() for line in labels_file if line.strip()]
    if not class_names:
        raise ValueError("O arquivo de rótulos está vazio.")

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data, verbose=0)
    index = np.argmax(prediction)
    if index >= len(class_names):
        raise ValueError("A quantidade de rótulos não corresponde às classes do modelo.")

    class_name = class_names[index].split(maxsplit=1)
    label = class_name[-1] if len(class_name) > 1 else class_name[0]
    confidence_score = float(prediction[0][index])

    return label, confidence_score