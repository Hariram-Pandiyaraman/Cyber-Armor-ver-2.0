from whois_analysis import get_whois_data, analyze_whois_data
from nlp_extract import nlp_information_extraction
from cnn_img_analysis import create_cnn_model

def analyze_domain(domain, webpage_text, image_data):
  
    whois_data = get_whois_data(domain)
    whois_results = analyze_whois_data(whois_data) if "error" not in whois_data else {"error": whois_data["error"]}
    entities = nlp_information_extraction(webpage_text)
    model = create_cnn_model()

    return {
        "WHOIS Analysis": whois_results,
        "NLP Analysis": entities,
        "CNN Image Analysis": model
    }



if __name__ == "__main__":
    domain = "google.com"
    sample_text = "Welcome to google. Visit us at google.com."
    sample_image_data = None  
    analyze_domain(domain, sample_text, sample_image_data)
