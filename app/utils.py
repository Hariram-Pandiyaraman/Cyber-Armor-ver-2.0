import re
import cv2
def validate_domain(domain):
   
    pattern = r'^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$'
    return re.match(pattern, domain) is not None

def clean_text(text):
    
    cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    return cleaned_text.lower()

def resize_image(image, target_size=(64, 64)):
   
    
    resized_image = cv2.resize(image, target_size)
    return resized_image



