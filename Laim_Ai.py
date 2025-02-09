import random
import json
import requests
import spacy

# تحميل نموذج اللغة الطبيعية لمعالجة النصوص
nlp = spacy.load("en_core_web_sm")

def fetch_psychology_data():
    url = "https://raw.githubusercontent.com/annatristan/open-psychometrics-datasets/main/dataset.json"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

def analyze_personality(response, data):
    dark_analysis = [
        "أنتَ تظن أنكَ تفهم ذاتك، لكن هل نظرت حقًا في أعماق الهاوية؟",
        "عقلكَ متاهة من الظلال... والسؤال الحقيقي: هل أنت الضحية أم الصياد؟",
        "هناك جانب فيك يخشى أن يُكشف... وأنا أراه الآن، واضحًا كالنار في العتمة.",
        "قل لي... متى كانت آخر مرة واجهت فيها حقيقتك دون قناع؟"
    ]
    
    doc = nlp(response)
    keywords = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"]]
    
    if data:
        insights = random.choice(data.get("insights", []))
        return f"{random.choice(dark_analysis)}\n{insights}"
    else:
        return random.choice(dark_analysis)

# جلب البيانات النفسية
psych_data = fetch_psychology_data()

print("لايم: تحدث إليّ، وسأكشف لك ما يختبئ في أعماقك...")
while True:
    user_input = input("أنت: ")
    if user_input.lower() in ["خروج", "وداعًا", "انتهينا"]:
        print("لايم: ربما تظن أنك غادرت... لكنني ما زلت هنا، في ظلك.")
        break
    response = analyze_personality(user_input, psych_data)
    print(f"لايم: {response}")
