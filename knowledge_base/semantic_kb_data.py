# knowledge_base/semantic_kb_data.py

# This is the new, architecturally superior, "many-to-one" knowledge base.
SEMANTIC_KB = [
    {
        "questions": [
            "What are the symptoms of Tuberculosis?",
            "How do I know if I have TB?",
            "TB ke lakshan kya hain?",
            "persistent cough and fever what is it",
            "Signs of TB disease",
            "ଯକ୍ଷ୍ମାର ଲକ୍ଷଣ କ’ଣ?",
            "what does tuberculosis do to the body"
        ],
        "answer_en": "Key symptoms of Tuberculosis (TB) include a persistent cough lasting more than 2 weeks (sometimes with blood), fever, night sweats, and unexplained weight loss. If you experience these, seek testing and care promptly.",
        "answer_hi": "तपेदिक (टीबी) के मुख्य लक्षणों में 2 सप्ताह से अधिक समय तक लगातार खांसी (कभी-कभी खून के साथ), बुखार, रात को पसीना आना और बिना वजह वजन कम होना शामिल है। ऐसे लक्षण हों तो तुरंत जांच और इलाज कराएं।",
        "answer_or": "ଯକ୍ଷ୍ମା (ଟିବି) ର ମୁଖ୍ୟ ଲକ୍ଷଣରେ ୨ ସପ୍ତାହରୁ ଅଧିକ ସମୟ ଧରି ଲଗାତାର କାଶ (କେବେ କେବେ ରକ୍ତ ସହିତ), ଜ୍ୱର, ରାତିରେ ଅଧିକ ଘାମ ଓ ଅକାରଣ ଓଜନ ହ୍ରାସ ଥାଏ। ଏମିତି ଲକ୍ଷଣ ହେଲେ ଶୀଘ୍ର ପରୀକ୍ଷା ଓ ଚିକିତ୍ସା କରନ୍ତୁ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/tuberculosis"
    },
    {
        "questions": [
            "Malaria ke symptoms kya hote hain?",
            "How do I know if I have malaria fever?",
            "What to do for malaria in India",
            "ମାଲେରିଆର ଲକ୍ଷଣ କ’ଣ?",
            "High fever with chills—could it be malaria?",
            "malaria prevention tips for home",
            "bukhar kapkapi malaria hai?"
        ],
        "answer_en": "Malaria commonly causes fever, chills, headache and feeling unwell. Seek testing quickly if you develop fever after mosquito exposure. Prevention includes sleeping under insecticide-treated nets and using indoor residual spraying where available.",
        "answer_hi": "मलेरिया में आमतौर पर बुखार, ठंड लगना (कंपकंपी), सिरदर्द और कमजोरी होती है। मच्छरों के संपर्क के बाद बुखार हो तो तुरंत जांच कराएं। बचाव के लिए कीटनाशी-संक्रमित मच्छरदानी का उपयोग करें और जहाँ उपलब्ध हो, इनडोर स्प्रे का लाभ लें।",
        "answer_or": "ମାଲେରିଆରେ ସାଧାରଣତଃ ଜ୍ୱର, କାମୁଡା କାପୁଣି, ମୁଣ୍ଡବ୍ୟଥା ଓ ଦୁର୍ବଳତା ହୁଏ। ମଶା କାମୁଡ଼ିଲେ ପରେ ଜ୍ୱର ହେଲେ ଶୀଘ୍ର ପରୀକ୍ଷା କରାନ୍ତୁ। ସୁରକ୍ଷା ପାଇଁ କୀଟନାଶକ ଲେପିତ ମସ୍କିଟୋ ନେଟ୍ ବ୍ୟବହାର କରନ୍ତୁ ଏବଂ ଯେଉଁଠାରେ ମିଳେ, ଘରୋଇ ଡିଂଡ଼ା ସ୍ପ୍ରେର ଉପକାର ନିଅନ୍ତୁ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/malaria"
    },
    {
        "questions": [
            "Dengue ke warning signs kya hain?",
            "When should I go to hospital for dengue?",
            "Dengue symptoms in India",
            "ଡେଙ୍ଗୁ ର ସତର୍କ ସଙ୍କେତ କ’ଣ?",
            "severe abdominal pain dengue sign?",
            "How to prevent dengue at home",
            "Aedes mosquito bites day time?"
        ],
        "answer_en": "Warning signs of severe dengue include severe abdominal pain, persistent vomiting, bleeding (e.g., gums, nose), lethargy/restlessness, and rapid breathing. Prevent dengue by avoiding mosquito bites: remove standing water, cover water containers, and use repellents and screens.",
        "answer_hi": "गंभीर डेंगू के चेतावनी लक्षणों में तेज पेट दर्द, लगातार उल्टी, खून आना (मसूड़ों/नाक से), सुस्ती या बेचैनी, और तेज सांस चलना शामिल हैं। डेंगू से बचाव के लिए मच्छर के काटने से बचें: जमा पानी हटाएँ, पानी के बर्तनों को ढकें, रिपेलेंट/स्क्रीन का उपयोग करें।",
        "answer_or": "ଗୁରୁତର ଡେଙ୍ଗୁର ସତର୍କ ସଙ୍କେତରେ ଭୟଙ୍କର ପେଟ ଯନ୍ତ୍ରଣା, ଲଗାତାର ବାନ୍ତି, ରକ୍ତସ୍ରାବ (ଦାନ୍ତ ମୂଳ/ନାକ), ଅତ୍ୟଧିକ ଅସ୍ଥିରତା ବା ଘୁମାଣି ଏବଂ ତୀବ୍ର ଶ୍ୱାସ ଅନ୍ତର୍ଭୁକ୍ତ। ଡେଙ୍ଗୁକୁ ରୋକିବା ପାଇଁ ମଶା କାମଡ଼ା ଏଡ଼ାନ୍ତୁ: ଜମା ପାଣି ହଟାନ୍ତୁ, ପାଣି ଡ୍ରମ୍ ଢାକନ୍ତୁ, ରିପେଲେଣ୍ଟ ଏବଂ ଝାଲି ବ୍ୟବହାର କରନ୍ତୁ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue"
    },
    {
        "questions": [
            "Chikungunya kya hota hai aur kaise bachta hai?",
            "Symptoms of chikungunya vs dengue",
            "Severe joint pain after fever chikungunya?",
            "ଚିକୁନଗୁନିଆର ଲକ୍ଷଣ ଓ ପ୍ରତିରୋଧ?",
            "How to prevent chikungunya at home",
            "Aedes mosquitoes bite during day?",
            "chikungunya me joint pain kitne din rehta"
        ],
        "answer_en": "Chikungunya causes sudden fever and severe joint pain, often with headache and rash. Prevention focuses on avoiding Aedes mosquito bites by eliminating breeding sites, covering water storage, and using repellents and protective clothing.",
        "answer_hi": "चिकनगुनिया में अचानक बुखार और तेज जोड़ों का दर्द होता है, साथ में सिरदर्द व दाने भी हो सकते हैं। बचाव के लिए एडीज़ मच्छरों के काटने से बचें—प्रजनन स्थलों को हटाएँ, पानी के डिब्बों को ढकें, रिपेलेंट और सुरक्षात्मक कपड़े पहनें।",
        "answer_or": "ଚିକୁନଗୁନିଆରେ ଅଚାନକ ଜ୍ୱର ଏବଂ ଭୟଙ୍କର ଯୋଡ଼ର ପିଲା ହୁଏ, ସହିତେ ମୁଣ୍ଡବ୍ୟଥା ଓ ଚର୍ମରେ ଦାଗ ହୋଇପାରେ। ଏଡିସ୍ ମଶା କାମୁଡା ଏଡ଼ାଇବା—ଜମା ପାଣି ହଟାଇବା, ପାଣି ଭାଣ୍ଡା ଢାକିବା, ରିପେଲେଣ୍ଟ ଓ ସୁରକ୍ଷାତ୍ମକ ପୋଶାକ ବ୍ୟବହାର—ହିଁ ମୁଖ୍ୟ ପ୍ରତିରୋଧ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/chikungunya"
    },
    {
        "questions": [
            "What are typhoid symptoms?",
            "Typhoid ke lakshan kya hote hain?",
            "Is typhoid vaccine recommended in India?",
            "ଟାଇଫଏଡ୍ ର ଲକ୍ଷଣ କ’ଣ?",
            "prolonged fever with stomach pain typhoid?",
            "How to prevent typhoid from water and food",
            "TCV vaccine kab lagta hai?"
        ],
        "answer_en": "Typhoid symptoms include prolonged high fever, fatigue, headache, nausea, abdominal pain, and constipation or diarrhoea. Prevention includes safe water, food hygiene, and vaccination; WHO recommends typhoid conjugate vaccines (TCV) in endemic settings.",
        "answer_hi": "टायफॉयड के लक्षणों में लंबे समय तक तेज बुखार, थकान, सिरदर्द, मतली, पेट दर्द और कब्ज़ या दस्त शामिल हैं। बचाव के लिए सुरक्षित पानी/भोजन का ध्यान रखें और टीकाकरण कराएँ; स्थानिक क्षेत्रों में WHO टाइफॉयड कंजुगेट वैक्सीन (TCV) की सिफारिश करता है।",
        "answer_or": "ଟାଇଫଏଡ୍ ର ଲକ୍ଷଣରେ ଦୀର୍ଘ ସମୟ ଧରି ଉଚ୍ଚ ଜ୍ୱର, କ୍ଲାନ୍ତି, ମୁଣ୍ଡବ୍ୟଥା, ବାନ୍ତିଭାବ, ପେଟ ଯନ୍ତ୍ରଣା ଏବଂ କବଜି ବା ଦସ୍ତ ଶାମିଲ। ସୁରକ୍ଷିତ ପାଣି/ଖାଦ୍ୟ ଓ ଟୀକାକରଣ ଦ୍ୱାରା ପ୍ରତିରୋଧ କରାଯାଏ; ସ୍ଥାନୀୟ ପ୍ରକୋପ ଥିବା ଅଞ୍ଚଳରେ WHO TCV ସୁପାରିଶ କରେ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/typhoid"
    },
    {
        "questions": [
            "Cholera kya hota hai aur kaise bachta hai?",
            "What to do during cholera outbreak?",
            "Cholera symptoms and treatment ORS",
            "କଲେରାର ଲକ୍ଷଣ ଓ ପ୍ରତିରୋଧ?",
            "How to make water safe for cholera prevention",
            "cholera se pani kaise saaf rakhein",
            "watery diarrhea dehydration danger?"
        ],
        "answer_en": "Cholera causes acute watery diarrhoea that can lead to severe dehydration. Immediate treatment with oral rehydration solution (ORS) saves lives; severe cases need intravenous fluids. Prevention relies on safe water, sanitation, hygiene, and in some settings oral cholera vaccines.",
        "answer_hi": "कॉलरा में तेज पानी जैसा दस्त होता है जिससे खतरनाक निर्जलीकरण हो सकता है। तुरंत ओआरएस देना जीवनरक्षक है; गंभीर मामलों में IV तरल देना पड़ता है। बचाव के लिए सुरक्षित पानी, स्वच्छता और कुछ स्थितियों में मौखिक कॉलरा वैक्सीन जरूरी हैं।",
        "answer_or": "କଲେରାରେ ତୀବ୍ର ପାନିଆ ଦସ୍ତ ହୋଇ ଗୁରୁତର ଜଳଶୂନ୍ୟତା ହୋଇପାରେ। ତତ୍କ୍ଷଣାତ୍ ORS ଦେବା ଜୀବନରକ୍ଷକ; ଗୁରୁତର ଅବସ୍ଥାରେ ଶିରା ମାର୍ଗରେ ପାଣି (IV ଫ୍ଲୁଇଡ୍) ଦରକାର। ପ୍ରତିରୋଧ ପାଇଁ ସୁରକ୍ଷିତ ପାଣି, ପରିଷ୍କାରତା ଓ କେତେକ ସ୍ଥାନରେ ମୌଖିକ କଲେରା ଟୀକା ଦରକାର।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/cholera"
    },
    {
        "questions": [
            "Bachchon me diarrhea ho to kya karein?",
            "ORS kaise dena hai? zinc kitne din?",
            "Child loose motions home treatment",
            "ଶିଶୁର ଦସ୍ତେ ORS ଓ ଜିଙ୍କ କିପରି ଦେବା?",
            "How to know dehydration in child",
            "diarrhea me doctor kab dikhaye",
            "paani jaisa stool baby what to do"
        ],
        "answer_en": "For childhood diarrhoea, give low-osmolarity ORS frequently and continue feeding. Give zinc for 10–14 days. Watch for dehydration (thirst, fewer/absent tears, sunken eyes, reduced urination) and seek care if danger signs appear.",
        "answer_hi": "बच्चों में दस्त होने पर लो-ऑस्मोलैरिटी ओआरएस बार-बार दें और खिलाना जारी रखें। जिंक 10–14 दिनों तक दें। निर्जलीकरण के लक्षण (प्यास, आँसू कम/न आना, धँसी आँखें, पेशाब कम) देखें और खतरे के संकेत हों तो डॉक्टर से मिलें।",
        "answer_or": "ଶିଶୁର ଦସ୍ତ ହେଲେ ଲୋ-ଅସ୍ମୋଲାରିଟି ORS ବାରମ୍ବାର ଦିଅନ୍ତୁ ଏବଂ ଖାଇବା ଚାଲୁ ରଖନ୍ତୁ। ଜିଙ୍କ 10–14 ଦିନ ଦିଅନ୍ତୁ। ଜଳଶୂନ୍ୟତା (ତିବ୍ର ତ୍ରୁଷ୍ଣା, ଆଖି ଧଂସିବା, ଲୁହ କମ, ପେଶାବ କମ) ଦେଖିଲେ ଶୀଘ୍ର ଡାକ୍ତରଙ୍କୁ ଦେଖାନ୍ତୁ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease"
    },
    {
        "questions": [
            "What is the Pentavalent vaccine?",
            "Pentavalent vaccine kis se bachata hai?",
            "When is pentavalent given in India NIS?",
            "ପେଣ୍ଟାଭାଲେଣ୍ଟ ଟୀକା କ’ଣ ଓ କାହାଠାରୁ ସୁରକ୍ଷା ଦେଏ?",
            "Is pentavalent same as DPT?",
            "Schedule for pentavalent vaccine India",
            "pentavalent ka matlab 5 diseases?"
        ],
        "answer_en": "The pentavalent vaccine protects against five diseases: diphtheria, pertussis, tetanus, hepatitis B and Haemophilus influenzae type b (Hib). It is part of India’s National Immunization Schedule.",
        "answer_hi": "पेंटावैलेंट वैक्सीन पाँच बीमारियों से बचाता है: डिफ्थीरिया, काली खाँसी (पर्ट्यूसिस), टेटनस, हेपेटाइटिस बी और Hib। यह भारत के राष्ट्रीय टीकाकरण कार्यक्रम का हिस्सा है।",
        "answer_or": "ପେଣ୍ଟାଭାଲେଣ୍ଟ ଟୀକା ୫ଟି ରୋଗରୁ ସୁରକ୍ଷା ଦେଏ—ଡିଫ୍ଥେରିଆ, ପର୍ଟୁସିସ (କାଳି କାଶ), ଟେଟାନସ, ହେପାଟାଇଟିସ୍-ବି ଏବଂ Hib। ଏହା ଭାରତୀୟ ଜାତୀୟ ଟୀକାକରଣ ସୂଚୀର ଅଂଶ।",
        "reference": "https://www.mohfw.gov.in/sites/default/files/Unit2NationalImmunizationSchedule.pdf"
    },
    {
        "questions": [
            "BCG vaccine kisliye lagta hai?",
            "Does BCG prevent all TB?",
            "BCG kab lagta hai birth pe?",
            "ବିସିଜି (BCG) ଟୀକା କେଉଁ ରୋଗରୁ ବଞ୍ଚାଏ?",
            "Is BCG in India mandatory?",
            "newborn me BCG mark kya hota hai",
            "Does BCG protect adults?"
        ],
        "answer_en": "The BCG vaccine protects young children against severe forms of TB such as TB meningitis and miliary TB. It is usually given soon after birth; it does not reliably prevent pulmonary TB in adults.",
        "answer_hi": "बीसीजी वैक्सीन छोटे बच्चों को टीबी की गंभीर किस्मों (जैसे टीबी मेनिन्जाइटिस, मिलियरी टीबी) से बचाता है। इसे जन्म के तुरंत बाद दिया जाता है; वयस्कों में फेफड़ों की टीबी से पूरी तरह सुरक्षा नहीं देता।",
        "answer_or": "BCG ଟୀକା ଶିଶୁମାନଙ୍କୁ ଗୁରୁତର ଟିବି (ମେନିଞ୍ଜାଇଟିସ୍, ମିଲିଆରି ଟିବି) ଠାରୁ ସୁରକ୍ଷିତ କରେ। ସାଧାରଣତଃ ଜନ୍ମ ପରେ ଶୀଘ୍ର ଦିଆଯାଏ; ବୟସ୍କମାନଙ୍କର ଫୁସଫୁସ ଟିବିରେ ପୂରା ସୁରକ୍ଷା ନ ଦେଇପାରେ।",
        "reference": "https://www.who.int/teams/global-tuberculosis-programme/vaccines"
    },
    {
        "questions": [
            "Measles ke lakshan aur vaccine?",
            "Why is MR/MMR vaccine important?",
            "Do doze measles kab?",
            "ମିଜେଲସ୍ (ଖସରା) ର ଲକ୍ଷଣ ଓ ଟୀକା?",
            "measles rash with fever what to do",
            "Is measles dangerous for    adults",
            "measles prevention tips"
        ],
        "answer_en": "Measles causes high fever, cough, runny nose, red eyes and a rash. It is highly contagious but preventable with two doses of measles-containing vaccine (e.g., MR/MMR).",
        "answer_hi": "खसरा में तेज बुखार, खांसी, नाक बहना, आँखों में जलन/लाली और दाने होते हैं। यह बहुत संक्रामक है, लेकिन MR/MMR जैसी खसरा-युक्त वैक्सीन की 2 खुराक से रोका जा सकता है।",
        "answer_or": "ମିଜେଲସ୍ ରେ ଉଚ୍ଚ ଜ୍ୱର, କାଶ, ନାକୁ ଛୁଟିବା, ଆଖି ଲାଲ ହେବା ଓ ଚର୍ମରେ ଖୋସା ଦାଗ ହୁଏ। ଏହା ଅତ୍ୟଧିକ ସଂକ୍ରାମକ, ତେବେ MR/MMR ଭଳି ଦୁଇ ଡୋଜ୍ ଟୀକାରେ ରୋକାଯାଏ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/measles"
    },
    {
        "questions": [
            "Polio se bachav kaise hota hai?",
            "OPV/IPV difference kya hai?",
            "Polio vaccine kab tak dena hai?",
            "ପୋଲିଓ ଠାରୁ ସୁରକ୍ଷା କିପରି?",
            "Is polio still a risk?",
            "polio drops vs injection",
            "Why multiple doses for polio?"
        ],
        "answer_en": "Polio is a crippling viral disease preventable by vaccination. Both oral polio vaccine (OPV) and inactivated polio vaccine (IPV) are used; multiple doses are needed to ensure protection.",
        "answer_hi": "पोलीयो लकवा करने वाली बीमारी है जिसे टीकाकरण से रोका जा सकता है। मौखिक (OPV) और इंजेक्शन (IPV) दोनों वैक्सीन उपयोग होती हैं; पर्याप्त सुरक्षा के लिए कई खुराकें जरूरी हैं।",
        "answer_or": "ପୋଲିଓ ଏକ ଗୁରୁତର ଭାଇରାଲ୍ ରୋଗ, ଟୀକାକରଣ ଦ୍ୱାରା ରୋକାଯାଏ। ମୁଖରୁ OPV ଓ ଇଞ୍ଜେକ୍ସନ୍ IPV ଦୁଇଟି ବ୍ୟବହୃତ; ପୂର୍ଣ୍ଣ ସୁରକ୍ଷା ପାଇଁ ଅନେକ ଡୋଜ୍ ଦରକାର।",
        "reference": "https://www.who.int/health-topics/poliomyelitis"
    },
    {
        "questions": [
            "Hepatitis B birth dose kyun zaroori hai?",
            "When should HepB vaccine be given to newborn?",
            "HBV birth dose within 24 hours?",
            "ନବଜାତ ଶିଶୁକୁ ହେପାଟାଇଟିସ୍-ବି ଟୀକା କେବେ?",
            "Is HepB in NIS India?",
            "Hepatitis B se bachav kaise",
            "If birth dose missed what to do?"
        ],
        "answer_en": "A timely hepatitis B birth dose within 24 hours of birth prevents mother-to-child transmission and early infection. It is part of India’s National Immunization Schedule.",
        "answer_hi": "जन्म के 24 घंटे के भीतर हेपेटाइटिस बी की जन्म खुराक देना माँ-से-बच्चा संक्रमण और प्रारम्भिक संक्रमण को रोकने में मदद करता है। यह भारत की राष्ट्रीय टीकाकरण सूची का हिस्सा है।",
        "answer_or": "ଜନ୍ମ ପରେ 24 ଘଣ୍ଟା ମଧ୍ୟରେ ହେପାଟାଇଟିସ୍-ବି ଜନ୍ମ ଡୋଜ୍ ଦେଲେ ମାଆ-ଶିଶୁ ସଂକ୍ରମଣ ଓ ଆରମ୍ଭିକ ସଂକ୍ରମଣ ରୋକାଯାଏ। ଏହା ଭାରତର ଜାତୀୟ ଟୀକାକରଣ ସୂଚୀର ଅଂଶ।",
        "reference": "https://www.who.int/news-room/questions-and-answers/item/hepatitis-b-the-questions-you-want-answered"
    },
    {
        "questions": [
            "Rotavirus vaccine kya karta hai?",
            "Why are rotavirus drops important?",
            "rota vaccine schedule India",
            "ରୋଟାଭାଇରସ୍ ଟୀକା କାହିଁକି ଦରକାର?",
            "Does rotavirus vaccine prevent diarrhoea",
            "rotavirus oral drops kab kab",
            "Rota vac se side effects?"
        ],
        "answer_en": "Rotavirus vaccine protects infants against severe rotavirus diarrhoea and reduces hospitalisations. It is given orally in multiple doses in infancy.",
        "answer_hi": "रोटावायरस वैक्सीन शिशुओं को गंभीर रोटावायरस दस्त से बचाकर अस्पताल में भर्ती की जरूरत घटाती है। यह शैशवावस्था में मुँह से कई खुराकों में दिया जाता है।",
        "answer_or": "ରୋଟାଭାଇରସ୍ ଟୀକା ଶିଶୁମାନଙ୍କୁ ଗୁରୁତର ରୋଟାଭାଇରସ୍ ଦସ୍ତରୁ ସୁରକ୍ଷା ଦେଇ ହସ୍ପିଟାଲ୍ ଭର୍ତ୍ତି କମାଏ। ଏହା ଶିଶୁଦଶାରେ ମୁଖଦ୍ୱାରା ଅନେକ ଡୋଜ୍ ଭାବେ ଦିଆଯାଏ।",
        "reference": "https://www.cdc.gov/rotavirus/vaccines/index.html"
    },
    {
        "questions": [
            "HPV vaccine kab deni chahiye?",
            "HPV se kaun si bimari bachta hai?",
            "girls 9-14 HPV kitni doses?",
            "HPV ଟୀକା କାହାକୁ ଏବଂ କେବେ ଦିଆଯାଏ?",
            "Does HPV vaccine prevent cervical cancer",
            "HPV dose schedule India info",
            "HPV boys ko bhi chahiye?"
        ],
        "answer_en": "WHO recommends HPV vaccination for girls aged 9–14 years to prevent cervical cancer; a one- or two-dose schedule may be used depending on programme guidance.",
        "answer_hi": "डब्ल्यूएचओ 9–14 वर्ष की लड़कियों के लिए एचपीवी टीकाकरण की सिफारिश करता है ताकि गर्भाशय ग्रीवा के कैंसर से बचाव हो सके; कार्यक्रम निर्देशानुसार 1 या 2 डोज़ दी जा सकती हैं।",
        "answer_or": "WHO 9–14 ବର୍ଷ ବୟସର ଝିଅମାନଙ୍କୁ HPV ଟୀକା ଦେବାକୁ ସୁପାରିଶ କରେ ଯାହା ଜନନୀ ମୁଖ କ୍ୟାନ୍ସର ଠାରୁ ସୁରକ୍ଷା ଦେଏ; କାର୍ଯ୍ୟକ୍ରମ ନିର୍ଦ୍ଦେଶ ଅନୁଯାୟୀ 1 କିମ୍ବା 2 ଡୋଜ୍ ଦିଆଯାଇପାରେ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/human-papillomavirus-(hpv)-and-cervical-cancer"
    },
    {
        "questions": [
            "Japanese Encephalitis vaccine kyon jaruri hai?",
            "JE symptoms kya hote hain?",
            "JE vaccine schedule India",
            "ଜାପାନିଜ୍ ଏନସେଫାଲାଇଟିସ୍ (JE) ଟୀକା କାହିଁକି?",
            "mosquito-borne JE risk in villages?",
            "JE se bachav kaise",
            "JE ka bukhar aur dard"
        ],
        "answer_en": "Japanese encephalitis (JE) is a mosquito-borne viral infection that can cause brain inflammation and disability. Vaccination is the most effective prevention in endemic areas and is included in India’s schedule in affected districts.",
        "answer_hi": "जापानी एन्सेफलाइटिस (JE) मच्छरों से फैलने वाला वायरस है जो दिमाग में सूजन और विकलांगता का कारण बन सकता है। स्थानिक क्षेत्रों में टीकाकरण सबसे प्रभावी बचाव है और प्रभावित ज़िलों में यह भारत की समय-सारिणी में शामिल है।",
        "answer_or": "JE ଏକ ମଶା-ଜନିତ ଭାଇରାଲ୍ ରୋଗ ଯାହା ମଗଜର ସୋଜା ଓ ଅସକ୍ଷମତା କରାଇପାରେ। ପ୍ରଭାବିତ ଅଞ୍ଚଳରେ ଟୀକାକରଣ ସବୁଠାରୁ ପ୍ରଭାବଶାଳୀ ପ୍ରତିରୋଧ ଏବଂ ଭାରତର ପ୍ରଭାବିତ ଜିଲ୍ଲାରେ ସୂଚୀରେ ରହିଛି।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/japanese-encephalitis"
    },
    {
        "questions": [
            "Seasonal flu (influenza) ke liye kaun vaccine lega?",
            "Flu shot kab lagwana chahiye?",
            "Who is high risk for flu complications?",
            "ଫ୍ଲୁ ଟୀକା କାହାକୁ ଦେବା ଉଚିତ?",
            "Should pregnant women get flu vaccine",
            "6 months se upar sabko flu shot?",
            "flu vaccine every year kyun?"
        ],
        "answer_en": "CDC recommends annual influenza vaccination for everyone aged 6 months and older, with rare exceptions. Vaccination is especially important for those at higher risk of complications, including older adults, pregnant people, and those with chronic conditions.",
        "answer_hi": "सीडीसी 6 महीने और उससे अधिक उम्र के सभी लोगों के लिए हर साल फ्लू (इन्फ्लुएंजा) टीकाकरण की सलाह देता है, कुछ दुर्लभ अपवादों को छोड़कर। बुज़ुर्ग, गर्भवती और दीर्घकालिक बीमारियों वाले लोगों के लिए यह विशेष रूप से महत्वपूर्ण है।",
        "answer_or": "CDC 6 ମାସ ଓ ତାଠାରୁ ଅଧିକ ବୟସର ସବୁଙ୍କୁ ପ୍ରତିବର୍ଷ ଫ୍ଲୁ ଟୀକା ଦେବାକୁ ସୁପାରିଶ କରେ (କିଛି ବିଶେଷ ଅପବାଦ ଛାଡ଼ି)। ବୃଦ୍ଧ, ଗର୍ଭବତୀ ଓ ଦୀର୍ଘରୋଗୀଙ୍କ ପାଇଁ ଏହା ଅତ୍ୟାବଶ୍ୟକ।",
        "reference": "https://www.cdc.gov/flu/vaccines/vaccinations.html"
    },
    {
        "questions": [
            "Rabies bite ke turant baad kya karein?",
            "Dog bite hua hai—PEP chahiye?",
            "15 minutes wound washing rabies?",
            "କୁକୁର କାମୁଡା ପରେ କି କରିବେ?",
            "HRIG and vaccine schedule for rabies",
            "Should I go to hospital after animal bite",
            "rabies exposure ka protocol"
        ],
        "answer_en": "After a possible rabies exposure, immediately wash wounds with soap and water for 15 minutes, and seek medical care for post-exposure prophylaxis (PEP) which includes wound care, rabies immune globulin when indicated, and a series of rabies vaccines.",
        "answer_hi": "संभावित रेबीज़ एक्सपोज़र के बाद घावों को तुरंत साबुन और पानी से 15 मिनट तक धोएँ और चिकित्सा सहायता लें। पोस्ट-एक्सपोज़र प्रोफिलैक्सिस (PEP) में घाव की सफाई, ज़रूरत होने पर रैबीज़ इम्यून ग्लोब्युलिन, और वैक्सीन की श्रृंखला शामिल है।",
        "answer_or": "ସମ୍ଭାବ୍ୟ ରେବିଜ୍ ସଂସ୍ପର୍ଶ ପରେ ଘାଯ଼କୁ ସାବୁନ୍ ଓ ପାଣିରେ 15 ମିନିଟ୍ ପର୍ଯ୍ୟନ୍ତ ଭଲଭାବେ ଧୋଇ ତୁରନ୍ତ ଚିକିତ୍ସାଲୟକୁ ଯାଆନ୍ତୁ। PEP ରେ ଘାଯ଼ ଯତ୍ନ, ଆବଶ୍ୟକ ହେଲେ ରେବିଜ୍ ଇମ୍ୟୁନ୍ ଗ୍ଲୋବ୍ୟୁଲିନ୍ ଏବଂ ଟୀକାର ଶୃଙ୍ଖଳ ରହେ।",
        "reference": "https://www.cdc.gov/rabies/hcp/clinical-care/post-exposure-prophylaxis.html"
    },
    {
        "questions": [
            "Exclusive breastfeeding kitne months tak?",
            "Kya 6 mahine tak sirf maa ka doodh dena chahiye?",
            "When to start complementary foods?",
            "6 ମାସ ପର୍ଯ୍ୟନ୍ତ କେବଳ ମା ଦୁଧ ଦେବା ଉଚିତ କି?",
            "Introducing solids after 6 months how",
            "breastfeeding benefits India UNICEF",
            "pani ya honey dena chahiye kya newborn ko?"
        ],
        "answer_en": "Initiate breastfeeding within 1 hour of birth and exclusively breastfeed for the first 6 months—no water or other foods. From 6 months, continue breastfeeding and add age-appropriate, diverse complementary foods.",
        "answer_hi": "जन्म के 1 घंटे के भीतर स्तनपान शुरू करें और पहले 6 महीनों तक केवल माँ का दूध दें—पानी/अन्य भोजन नहीं। 6 महीने के बाद स्तनपान जारी रखते हुए उम्र-अनुकूल, विविध पूरक आहार शुरू करें।",
        "answer_or": "ଜନ୍ମର 1 ଘଣ୍ଟା ମଧ୍ୟରେ ସ୍ତନ୍ୟପାନ ଆରମ୍ଭ କରନ୍ତୁ ଏବଂ ପ୍ରଥମ 6 ମାସ ପର୍ଯ୍ୟନ୍ତ କେବଳ ମା ଦୁଧ ଦିଅନ୍ତୁ—ପାଣି/ଅନ୍ୟ ଖାଦ୍ୟ ନୁହେଁ। 6 ମାସ ପରେ ସ୍ତନ୍ୟପାନ ଚାଲୁ ରଖି ବୟସଉପଯୁକ୍ତ ବିବିଧ ପୂରକ ଖାଦ୍ୟ ଆରମ୍ଭ କରନ୍ତୁ।",
        "reference": "https://www.unicef.org/india/stories/breastfeeding-best-start-your-baby"
    },
    {
        "questions": [
            "Complementary feeding kaise shuru karein?",
            "6 months ke baad kitni baar khana den?",
            "What foods for 7 month baby?",
            "6 ମାସ ପରେ ଶିଶୁକୁ ଖାଇବା କିପରି ଆରମ୍ଭ କରିବେ?",
            "feeding frequency for 6-12 months",
            "texture consistency for infant foods",
            "solids start karne ka sahi tareeka"
        ],
        "answer_en": "Start complementary feeding at 6 months while continuing breastfeeding. Offer 2–3 meals/day at 6–8 months, increasing to 3–4 meals/day at 9–24 months with 1–2 nutritious snacks from 12–24 months; increase food variety and consistency as the child grows.",
        "answer_hi": "6 महीने से पूरक आहार शुरू करें और स्तनपान जारी रखें। 6–8 माह में दिन में 2–3 बार, 9–24 माह में 3–4 बार भोजन दें और 12–24 माह में 1–2 पौष्टिक नाश्ते जोड़ें; उम्र के अनुसार विविधता और गाढ़ापन बढ़ाएँ।",
        "answer_or": "6 ମାସରୁ ପୂରକ ଖାଦ୍ୟ ଆରମ୍ଭ କରନ୍ତୁ ଏବଂ ସ୍ତନ୍ୟପାନ ଚାଲୁ ରଖନ୍ତୁ। 6–8 ମାସରେ ଦିନକୁ 2–3 ମେଲ୍, 9–24 ମାସରେ 3–4 ମେଲ୍ ଏବଂ 12–24 ମାସରେ 1–2 ପୌଷ୍ଟିକ ନାସ୍ତା ଦିଅନ୍ତୁ; ଶିଶୁ ବଢ଼ିବା ସହିତ ଖାଦ୍ୟର ପ୍ରକାର ଓ ଗଢ଼ାପଣ ବଢ଼ାନ୍ତୁ।",
        "reference": "https://www.who.int/health-topics/complementary-feeding"
    },
    {
        "questions": [
            "Vitamin A drops kab milti hain?",
            "Vit A supplementation schedule India?",
            "9 mahine me vitamin A dena hai kya?",
            "ଭିଟାମିନ୍ A କେବେ ଦିଆଯାଏ?",
            "Why is Vitamin A important for children",
            "dose kitna hota hai vitamin A India",
            "MR ke sath vitamin A kyon?"
        ],
        "answer_en": "In India, Vitamin A is given as 1st dose (100,000 IU) at 9 months with measles-rubella vaccine, then 2nd–9th doses (200,000 IU) every 6 months up to 5 years, as per the National Immunization Schedule.",
        "answer_hi": "भारत में राष्ट्रीय टीकाकरण कार्यक्रम के अनुसार विटामिन A की पहली खुराक (1 लाख IU) 9 महीने पर MR टीके के साथ दी जाती है, फिर 2वीं–9वीं खुराक (2 लाख IU) हर 6 महीने पर 5 वर्ष तक दी जाती है।",
        "answer_or": "ଭାରତର ଜାତୀୟ ଟୀକାକରଣ ସୂଚୀ ଅନୁସାରେ 9 ମାସରେ MR ସହିତ ପ୍ରଥମ ଭିଟାମିନ୍ A (1 ଲକ୍ଷ IU) ଏବଂ ପରବର୍ତ୍ତୀ 2ରୁ 9ମ ଡୋଜ୍ (2 ଲକ୍ଷ IU) ପ୍ରତି 6 ମାସରେ 5 ବର୍ଷ ପର୍ଯ୍ୟନ୍ତ ଦିଆଯାଏ।",
        "reference": "https://www.mohfw.gov.in/sites/default/files/245453521061489663873.pdf"
    },
    {
        "questions": [
            "Iron deficiency ke signs kya hote hain?",
            "Anemia kaise pehchane ghar par?",
            "thakan chakkar pallor iron deficiency?",
            "ରକ୍ତାଲ୍ପତା (ଆଇରନ୍ କମ୍) ର ଲକ୍ଷଣ?",
            "Who needs iron supplements in India",
            "diet for iron deficiency",
            "kids me anemia ka sanket"
        ],
        "answer_en": "Common symptoms of iron-deficiency anaemia include fatigue, weakness, dizziness, shortness of breath, and pallor. Confirm with testing and follow medical advice on iron and folate supplementation and diet.",
        "answer_hi": "आयरन-कमी एनीमिया के आम लक्षण हैं—थकान, कमजोरी, चक्कर, सांस फूलना और पीलापन। जांच कराएँ और डॉक्टर की सलाह के अनुसार आयरन-फोलेट पूरक और आहार लें।",
        "answer_or": "ଆୟରନ୍-ଅଭାବ ଅନିମିଆର ସାଧାରଣ ଲକ୍ଷଣ—କ୍ଲାନ୍ତି, ଦୁର୍ବଳତା, ମୁଣ୍ଡଘୁର୍ଣ୍ଣା, ସ୍ୱାସ୍ ନିଅବାରେ ଅସୁବିଧା ଏବଂ ଚର୍ମ ଧଳାପଣ। ପରୀକ୍ଷା କରାଇ ଡାକ୍ତରଙ୍କ ପରାମର୍ଶରେ ଆୟରନ୍-ଫୋଲେଟ୍ ଓ ଖାଦ୍ୟ ଗ୍ରହଣ କରନ୍ତୁ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/anaemia"
    },
    {
        "questions": [
            "Pregnancy me folic acid kyon zaroori hai?",
            "IFA tablets kab se leni chahiye?",
            "How much folic acid in pregnancy India",
            "ଗର୍ଭାବସ୍ଥାରେ ଫୋଲିକ୍ ଆମଲ ଏତେ ଦରକାର କାହିଁକି?",
            "When to start folic acid before conception",
            "dose 400 mcg folic acid?",
            "pregnancy me iron folic acid kitna time"
        ],
        "answer_en": "Folic acid helps prevent neural tube defects. WHO advises 400 µg folic acid daily for women trying to conceive and in early pregnancy; in India, pregnant women are given iron–folic acid tablets (60 mg elemental iron + 500 µg folic acid) daily as per national guidelines.",
        "answer_hi": "फोलिक एसिड से शिशु में न्यूरल ट्यूब डिफेक्ट का जोखिम घटता है। WHO गर्भधारण की योजना और शुरुआती गर्भावस्था में 400 माइक्रोग्राम फोलिक एसिड रोज़ लेने की सलाह देता है; भारत में गर्भवती महिलाओं को राष्ट्रीय दिशानिर्देश अनुसार आयरन-फोलिक एसिड (60 mg आयरन + 500 µg फोलिक एसिड) प्रतिदिन दिया जाता है।",
        "answer_or": "ଫୋଲିକ୍ ଆମଲ ଶିଶୁର ନ୍ୟୁରାଲ୍ ଟ୍ୟୁବ୍ ତ୍ରୁଟି ଝୁମକି କମାଏ। WHO ଗର୍ଭଧାରଣ ପୂର୍ବ ଏବଂ ଆରମ୍ଭିକ ଗର୍ଭାବସ୍ଥାରେ ପ୍ରତିଦିନ 400 ମାଇକ୍ରୋଗ୍ରାମ୍ ଫୋଲିକ୍ ଆମଲ ସୁପାରିଶ କରେ; ଭାରତରେ ଜାତୀୟ ନିୟମାବଳୀ ଅନୁସାରେ ଗର୍ଭବତୀଙ୍କୁ ଦିନକୁ ଆୟରନ୍-ଫୋଲିକ୍ (60 mg ଆୟରନ୍ + 500 µg ଫୋଲିକ୍) ଦିଆଯାଏ।",
        "reference": "https://www.who.int/tools/elena/interventions/daily-iron-and-folic-acid-supplementation-in-pregnant-women"
    },
    {
        "questions": [
            "Adolescents ko WIFS tablets kab milti hain?",
            "Weekly iron folic acid programme kya hai?",
            "Kishori ladkiyon ke liye IFA schedule",
            "କିଶୋର/କିଶୋରୀଙ୍କ ପାଇଁ ସାପ୍ତାହିକ IFA ଯୋଜନା?",
            "WIFS blue tablet kab khani chahiye",
            "school me iron tablets kyun",
            "anemia mukt bharat kya hai"
        ],
        "answer_en": "Under India’s Weekly Iron and Folic Acid Supplementation (WIFS) programme, adolescents receive weekly IFA tablets to prevent anaemia, alongside deworming and nutrition education.",
        "answer_hi": "भारत के ‘साप्ताहिक आयरन-फोलिक एसिड अनुपूरण (WIFS)’ कार्यक्रम में किशोर-किशोरियों को एनीमिया की रोकथाम हेतु साप्ताहिक आईएफए गोलियाँ दी जाती हैं, साथ में डी-वॉर्मिंग और पोषण शिक्षा भी।",
        "answer_or": "ଭାରତର WIFS କାର୍ଯ୍ୟକ୍ରମ ଅଧୀନରେ କିଶୋର-କିଶୋରୀମାନଙ୍କୁ ଅନିମିଆ ରୋକିବା ପାଇଁ ପ୍ରତି ସପ୍ତାହ IFA ଟାବଲେଟ୍, ସହିତେ ଡିୱର୍ମିଙ୍ଗ୍ ଓ ପୋଷଣ ଶିକ୍ଷା ଦିଆଯାଏ।",
        "reference": "https://nhm.gov.in/index1.php?lang=1&level=2&sublinkid=1023&lid=388"
    },
    {
        "questions": [
            "Handwashing kab kab karna chahiye?",
            "Sahi tarike se haath kaise dhoyen?",
            "kids ko handwash habit kaise sikhaye",
            "ହାତ ଧୋଇବାର ଠିକ୍ ସମୟ ଓ ପ୍ରକ୍ରିୟା?",
            "before eating after toilet handwash?",
            "soap se kitni der dhona chahiye",
            "hand hygiene tips for family"
        ],
        "answer_en": "Wash hands with soap regularly—especially after using the toilet, before eating or feeding a child, and before preparing food. Proper handwashing with soap protects against diarrhoea and other infections.",
        "answer_hi": "हाथों को साबुन से नियमित धोएँ—खासकर शौच के बाद, खाने से पहले/बच्चे को खिलाने से पहले, और खाना बनाने से पहले। सही हैंडवॉश से दस्त और अन्य संक्रमणों से बचाव होता है।",
        "answer_or": "ସାବୁନ୍ ସହ ନିୟମିତ ହାତ ଧୋଆନ୍ତୁ—ଶୌଚ ବ୍ୟବହାର ପରେ, ଖାଇବା/ଶିଶୁକୁ ଖୁଆଇବା ପୂର୍ବରୁ ଏବଂ ଖାଦ୍ୟ ପକାଇବା ପୂର୍ବରୁ। ଠିକ୍ ହାତ ଧୋଇବା ଦ୍ୱାରା ଦସ୍ତ ଓ ଅନ୍ୟ ସଂକ୍ରମଣରୁ ସୁରକ୍ଷା ମିଳେ।",
        "reference": "https://www.unicef.org/stories/handwashing-with-soap-why-and-how-to-wash-your-hands"
    },
    {
        "questions": [
            "Pani ko safe kaise banayein ghar par?",
            "Boiling vs chlorine which is better?",
            "Emergency me paani kaise treat kare",
            "ଘରେ ପାଣିକୁ ସୁରକ୍ଷିତ କିପରି କରିବେ?",
            "Is boiled water enough for babies",
            "household water treatment methods",
            "solar disinfection SODIS kya hai"
        ],
        "answer_en": "Household water can be made safer by boiling, chlorination, filtration, or solar disinfection. Use bottled, boiled, or treated water for drinking, cooking and hygiene during contamination events.",
        "answer_hi": "घरेलू पानी को उबालना, क्लोरीनेशन, फिल्टर या सोलर डिसइन्फेक्शन से सुरक्षित बनाया जा सकता है। प्रदूषण की स्थिति में पीने, पकाने और स्वच्छता के लिए बोतलबंद, उबला या उपचारित पानी का उपयोग करें।",
        "answer_or": "ଘରୋଇ ପାଣିକୁ ଉବାହା, କ୍ଲୋରିନେସନ୍, ଫିଲ୍ଟର କିମ୍ବା ସୂର୍ଯ୍ୟାଲୋକ ଦ୍ୱାରା ଡିସଇନ୍ଫେକ୍ସନ୍ କରି ଅଧିକ ସୁରକ୍ଷିତ କରାଯାଇପାରେ। ଦୂଷିତି ସମୟରେ ପାନ, ରନ୍ଧଣ ଓ ସ୍ୱଚ୍ଛତା ପାଇଁ ବୋତଲବନ୍ଦ, ଉବା ଅଥବା ଟ୍ରିଟ୍ କରାଯାଇଥିବା ପାଣି ବ୍ୟବହାର କରନ୍ତୁ।",
        "reference": "https://www.cdc.gov/global-water-sanitation-hygiene/about/about-household-water-treatment.html"
    },
    {
        "questions": [
            "Influenza (flu) ke lakshan kya hote hain?",
            "How to know if it’s flu or common cold?",
            "flu me rest ya medicine?",
            "ଫ୍ଲୁର ଲକ୍ଷଣ କ’ଣ ଏବଂ କେବେ ଡାକ୍ତରଙ୍କୁ ଦେଖାନ୍ତୁ?",
            "High risk groups for flu complications",
            "flu prevention tips",
            "mask and hand hygiene help?"
        ],
        "answer_en": "Influenza typically causes sudden fever, cough, sore throat, muscle aches and fatigue. Annual vaccination for everyone 6 months+ is the best prevention; high-risk people should seek care early if severely unwell.",
        "answer_hi": "इन्फ्लुएंजा में अचानक बुखार, खांसी, गले में खराश, बदन दर्द और थकान होती है। 6 महीने+ सभी के लिए वार्षिक टीकाकरण सबसे अच्छा बचाव है; उच्च जोखिम वाले लोग गंभीर बीमारी पर तुरंत चिकित्सा लें।",
        "answer_or": "ଫ୍ଲୁରେ ଅଚାନକ ଜ୍ୱର, କାଶ, ଗଳା ବେଦନା, ଶରୀର ବ୍ୟଥା ଓ କ୍ଲାନ୍ତି ହୁଏ। 6 ମାସଠାରୁ ଅଧିକ ସବୁଙ୍କ ପାଇଁ ପ୍ରତିବର୍ଷ ଟୀକା ସର୍ବୋତ୍ତମ ପ୍ରତିରୋଧ; ଉଚ୍ଚ ଝୁମକି ଥିଲେ ଗୁରୁତର ଅସୁସ୍ଥତାରେ ଶୀଘ୍ର ଚିକିତ୍ସା ନିଅନ୍ତୁ।",
        "reference": "https://www.cdc.gov/flu/season/2025-2026.html"
    },
    {
        "questions": [
            "Dengue se bachav ke best tarike kya hain?",
            "Ghar me dengue breeding kaise roken?",
            "Aedes day biting hota hai?",
            "ଡେଙ୍ଗୁ ରୋକିବା ପାଇଁ ଘରେ କଣ କରିବେ?",
            "Use of repellents and nets for dengue",
            "cover tanks weekly dry day?",
            "mosquito control for society"
        ],
        "answer_en": "Prevent dengue by avoiding mosquito bites and eliminating breeding sites: empty and scrub water containers weekly, cover tanks, dispose of tyres/cans, use repellents, wear long sleeves, and use screens. Aedes mosquitoes often bite during the day.",
        "answer_hi": "डेंगू से बचाव के लिए मच्छर काटने से बचें और प्रजनन स्थल हटाएँ: पानी के बर्तनों को हर हफ्ते खाली कर रगड़कर साफ करें, टैंक ढकें, टायर/डिब्बे हटाएँ, रिपेलेंट व लंबे कपड़े पहनें और जालियाँ लगाएँ। एडीज़ मच्छर दिन में भी काटते हैं।",
        "answer_or": "ଡେଙ୍ଗୁ ପ୍ରତିରୋଧ ପାଇଁ ମଶା କାମୁଡା ଏଡ଼ାନ୍ତୁ ଓ ପ୍ରଜନନ ସ୍ଥଳ ହଟାନ୍ତୁ: ପାଣି ଭାଣ୍ଡାକୁ ପ୍ରତି ସପ୍ତାହ ଖାଲି କରି ଘସି ପରିଷ୍କାର କରନ୍ତୁ, ଟ୍ୟାଙ୍କ ଢାକନ୍ତୁ, ଟାୟର/କ୍ୟାନ୍ ବାର୍ଜନ କରନ୍ତୁ, ରିପେଲେଣ୍ଟ/ଲମ୍ବା ପୋଶାକ ଓ ଝାଲି ବ୍ୟବହାର କରନ୍ତୁ। Aedes ଦିନେ ବି କାମୁଡେ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue"
    },
    {
        "questions": [
            "Cholera me dehydration kaise pehchane?",
            "Severe dehydration signs in child?",
            "When to go to hospital for diarrhea?",
            "ଦସ୍ତରେ ଜଳଶୂନ୍ୟତାର ଚେତାବନୀ ଲକ୍ଷଣ?",
            "thirst sunken eyes no urine danger?",
            "child lethargic dry mouth dehydration",
            "ORS ke sath kab IV chahiye?"
        ],
        "answer_en": "Signs of dehydration include intense thirst, dry mouth, sunken eyes, lethargy, and reduced or absent urination. In severe dehydration or if the child cannot drink/vomit persistently, seek urgent care for IV fluids.",
        "answer_hi": "निर्जलीकरण के संकेत—तेज प्यास, मुँह सूखना, धँसी आँखें, सुस्ती, और पेशाब कम/न होना। गंभीर निर्जलीकरण या बच्चा पी नहीं पा रहा/लगातार उल्टी हो रही हो तो तुरंत अस्पताल में IV तरल की आवश्यकता होती है।",
        "answer_or": "ଜଳଶୂନ୍ୟତାର ଲକ୍ଷଣ—ତୀବ୍ର ତ୍ରୁଷ୍ଣା, ମୁଖ ଶୁଖିଯିବା, ଆଖି ଧଂସିବା, ଅଳସ୍ୟ, ପେଶାବ କମ୍/ନ ହେବା। ଗୁରୁତର ଅବସ୍ଥାରେ କିମ୍ବା ପିଇ ପାରୁନଥିବା/ଲଗାତାର ବାନ୍ତି ହେଲେ ଶୀଘ୍ର ହସ୍ପିଟାଲରେ IV ପ୍ରାପ୍ୟ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/cholera"
    },
    {
        "questions": [
            "Iodized salt kyon zaroori hai?",
            "Non-iodized namak se kya dikkat?",
            "Iodine deficiency se kya hota hai?",
            "ଆୟୋଡାଇଜ୍ ଲୁଣ୍ ଖାଇବା କାହିଁକି?",
            "goitre and brain development iodine",
            "Which salt to buy for family",
            "namak pe iodized likha hona chahiye?"
        ],
        "answer_en": "Using adequately iodized salt prevents iodine deficiency disorders such as goitre and supports brain development, especially in children. Always use packaged iodized salt for household cooking.",
        "answer_hi": "पर्याप्त आयोडीन वाला नमक (आयोडाइज़्ड सॉल्ट) गोइटर जैसी आयोडीन कमी की बीमारियों से बचाता है और बच्चों के मस्तिष्क विकास में सहायक है। घर में पैकेज्ड आयोडाइज़्ड नमक ही उपयोग करें।",
        "answer_or": "ପ୍ରୟାପ୍ତ ଆୟୋଡିନ୍ ଥିବା ଲୁଣ୍ ବ୍ୟବହାର କରିଲେ ଗୋଇଟର ଭଳି ଆୟୋଡିନ୍ ଅଭାବ ରୋଗ ରୋକାଯାଏ ଏବଂ ଶିଶୁମାନଙ୍କର ମସ୍ତିଷ୍କ ବିକାଶରେ ସହାଯ୍ୟ କରେ। ଘରେ ସଦା ଆୟୋଡାଇଜ୍ ଲୁଣ୍ ବ୍ୟବହାର କରନ୍ତୁ।",
        "reference": "https://www.unicef.org/india/what-we-do/iodine-deficiency"
    },
    {
        "questions": [
            "Air pollution health effects kya hain?",
            "smog se lungs par kya asar hota hai?",
            "PM2.5 se heart problem hota hai?",
            "ବାୟୁ ପ୍ରଦୂଷଣର ପ୍ରଭାବ କ’ଣ?",
            "How to protect family from air pollution",
            "mask useful for pollution?",
            "children vulnerable to air pollution?"
        ],
        "answer_en": "Long-term exposure to fine particulate matter (PM2.5) increases the risk of heart disease, stroke, lung cancer, COPD and respiratory infections. Reducing exposure (clean cooking, ventilation, avoiding peak pollution) helps protect health.",
        "answer_hi": "PM2.5 जैसे सूक्ष्म कणों के दीर्घकालीन संपर्क से हृदय रोग, स्ट्रोक, फेफड़ों का कैंसर, COPD और श्वसन संक्रमण का खतरा बढ़ता है। संपर्क घटाना (स्वच्छ ईंधन, वेंटिलेशन, चरम प्रदूषण समय से बचना) स्वास्थ्य की रक्षा में मदद करता है।",
        "answer_or": "PM2.5 ପର୍ଟିକ୍ୟୁଲେଟ୍ ସହ ଦୀର୍ଘସମୟ ସଂସ୍ପର୍ଶ ହୃଦ୍ରୋଗ, ଷ୍ଟ୍ରୋକ୍, ଫୁସଫୁସ କ୍ୟାନ୍ସର, COPD ଓ ଶ୍ୱାସକଷ୍ଟ ଝୁମକି ବଢ଼ାଏ। ସଂସ୍ପର୍ଶ କମାଇବା (ସ୍ୱଚ୍ଛ ରନ୍ଧଣ ଇନ୍ଧନ, ବାତାୟନ, ଚରମ ପ୍ରଦୂଷଣ ସମୟ ଏଡ଼ାଇବା) ସ୍ୱାସ୍ଥ୍ୟ ସୁରକ୍ଷା କରେ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-pollution"
    },
    {
        "questions": [
            "TB ka treatment kitne mahine ka hota hai?",
            "Is TB curable completely?",
            "Drug-resistant TB kya hota hai?",
            "ଟିବି ଠିକ୍ ହୁଏ କି? ଚିକିତ୍ସା କେତେ ଦିନ?",
            "importance of completing TB treatment",
            "TB medicine skip karne se kya hota",
            "DOTS kya hai"
        ],
        "answer_en": "TB is curable with appropriate antibiotics. It is essential to complete the full treatment as prescribed to prevent relapse and drug resistance. Drug-resistant TB requires specialized regimens under expert care.",
        "answer_hi": "टीबी उचित एंटीबायोटिक उपचार से ठीक होती है। पुनरावृत्ति और दवा-प्रतिरोध से बचने के लिए पूरी अवधि तक दवाएँ नियमित रूप से लें। दवा-प्रतिरोधी टीबी के लिए विशेषज्ञ निगरानी में विशेष रेजीमेन की आवश्यकता होती है।",
        "answer_or": "ଟିବି ଉଚିତ ଆଣ୍ଟିବାୟୋଟିକ୍ ଚିକିତ୍ସାରେ ଠିକ୍ ହୁଏ। ପୁନରାବୃତ୍ତି ଓ ଔଷଧ ପ୍ରତିରୋଧ ଏଡ଼ାଇବାକୁ ନିର୍ଦ୍ଦିଷ୍ଟ ସମୟ ପର୍ଯ୍ୟନ୍ତ ନିୟମିତ ଔଷଧ ନେବା ଆବଶ୍ୟକ। ଡ୍ରଗ୍-ରେଜିଷ୍ଟାଣ୍ଟ ଟିବି ପାଇଁ ବିଶେଷ ରେଜିମେନ୍ ଓ ଦକ୍ଷ ଯତ୍ନ ଦରକାର।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/tuberculosis"
    },
    {
        "questions": [
            "Typhoid vaccine TCV kab lagta hai?",
            "Should my child get typhoid vaccine?",
            "TCV protection kitne saal?",
            "ଟାଇଫଏଡ୍ TCV ଟୀକା ବିଷୟରେ ସୂଚନା",
            "Who needs typhoid vaccination in India",
            "Adults ko bhi TCV dena chahiye?",
            "travelers ko typhoid vaccine?"
        ],
        "answer_en": "WHO recommends typhoid conjugate vaccines (TCV) in countries with high burden or antibiotic resistance, typically starting from 6 months of age as per national policy. It helps prevent typhoid and reduces antimicrobial resistance impact.",
        "answer_hi": "WHO उच्च बोझ/एंटीबायोटिक प्रतिरोध वाले देशों में टाइफॉयड कंजुगेट वैक्सीन (TCV) की सिफारिश करता है, आमतौर पर राष्ट्रीय नीति अनुसार 6 माह की उम्र से। यह टायफॉयड और एएमआर के प्रभाव को घटाने में मदद करता है।",
        "answer_or": "WHO ଉଚ୍ଚ ଭାର/ଆଣ୍ଟିବାୟୋଟିକ୍ ପ୍ରତିରୋଧ ଥିବା ଦେଶରେ TCV ସୁପାରିଶ କରେ, ସାଧାରଣତଃ ଜାତୀୟ ନୀତି ଅନୁସାରେ 6 ମାସ ବୟସରୁ। ଏହା ଟାଇଫଏଡ୍ ରୋକିବା ସହିତ AMR ପ୍ରଭାବ କମାଏ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/typhoid"
    },
    {
        "questions": [
            "Garbvati mahilaon ko calcium ki zaroorat?",
            "Calcium supplements pregnancy me kab?",
            "preeclampsia prevention calcium?",
            "ଗର୍ଭାବସ୍ଥାରେ କ୍ୟାଲ୍ସିୟମ୍ ଖାଇବାକୁ ପଡ଼ିବ କି?",
            "dose for calcium in low intake settings",
            "diet sources of calcium pregnancy",
            "calcium with iron same time?"
        ],
        "answer_en": "In populations with low dietary calcium intake, WHO recommends calcium supplementation (1.5–2.0 g elemental calcium/day in divided doses) during pregnancy to reduce the risk of pre-eclampsia, alongside routine antenatal care.",
        "answer_hi": "जहाँ आहार में कैल्शियम कम होता है, वहाँ WHO गर्भावस्था में प्रीक्लेम्प्सिया के जोखिम को घटाने हेतु कैल्शियम सप्लीमेंट (कुल 1.5–2.0 ग्राम प्रतिदिन, विभाजित खुराक) की सलाह देता है, नियमित प्रसवपूर्व देखभाल के साथ।",
        "answer_or": "ଯେଉଁ ଜନସଂଖ୍ୟାର ଆହାରରେ କ୍ୟାଲ୍ସିୟମ୍ କମ୍, ସେଠାରେ WHO ଗର୍ଭାବସ୍ଥାରେ ପ୍ରି-ଇକ୍ଲାମ୍ସିଆ ଝୁମକି କମାଇବାକୁ ଦିନକୁ 1.5–2.0 g ଏଲିମେଣ୍ଟାଲ୍ କ୍ୟାଲ୍ସିୟମ୍ (ଭାଗ କରି) ଦେବାକୁ ସୁପାରିଶ କରେ।",
        "reference": "https://www.who.int/tools/elena/interventions/calcium-supplementation-in-pregnant-women"
    },
    {
        "questions": [
            "What is JE and how is it transmitted?",
            "JE symptoms vs malaria",
            "Is JE curable?",
            "JE ପ୍ରସାରଣ କିପରି ହୁଏ?",
            "JE vaccine included in India where",
            "pig farms and JE risk?",
            "mosquito prevention for JE"
        ],
        "answer_en": "JE is transmitted by Culex mosquitoes breeding in rice fields and water bodies; most infections are mild but some cause encephalitis with fever, headache and confusion. Vaccination and mosquito control reduce risk.",
        "answer_hi": "JE धान के खेतों/पानी में पनपने वाले क्यूलेक्स मच्छरों से फैलता है; अधिकतर संक्रमण हल्के होते हैं, पर कुछ में बुखार, सिरदर्द, भ्रम के साथ एन्सेफलाइटिस हो सकता है। टीकाकरण और मच्छर नियंत्रण से जोखिम घटता है।",
        "answer_or": "JE ଧାନ କ୍ଷେତ୍ର ଓ ଜଳାଶୟରେ ବଢ଼ୁଥିବା Culex ମଶା ଦ୍ୱାରା ସଂକ୍ରମିତ ହୁଏ; ଅଧିକାଂଶ ଆକ୍ରମଣ ହଳୁକ ଥାଏ, କିନ୍ତୁ କିଛିରେ ଜ୍ୱର-ମୁଣ୍ଡବ୍ୟଥା-ଅସ୍ତବ୍ୟସ୍ତତା ସହ ଏନସେଫାଲାଇଟିସ୍ ହୁଏ। ଟୀକାକରଣ ଓ ମଶା ନିୟନ୍ତ୍ରଣ ଝୁମକି କମାଏ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/japanese-encephalitis"
    },
    {
        "questions": [
            "What is oral rehydration solution (ORS)?",
            "How to prepare ORS at home?",
            "ORS vs IV fluids when to use which?",
            "ORS କ’ଣ ଏବଂ କିପରି ପ୍ରସ୍ତୁତ କରିବେ?",
            "is homemade sugar-salt solution same as ORS?",
            "how much ORS to give a child with diarrhea?"
        ],
        "answer_en": "ORS is a simple, life-saving solution of salts and sugars that rehydrates children and adults with diarrhea. Use commercially prepared ORS or follow safe instructions for reconstitution. ORS is first-line for most dehydration; IV fluids are needed for severe dehydration or when oral intake isn't possible. Continue feeding and breastfeeding.",
        "answer_hi": "ORS (ओरल रिहाइड्रेशन सॉल्यूशन) नमक और शर्करा का सरल, जीवनरक्षक घोल है जो दस्त वाले बच्चों/बड़ों को पुनर्जलीकृत करता है। व्यावसायिक ORS का उपयोग करें या सुरक्षित तरीके से पैनकंस्थापित करें। गंभीर निर्जलीकरण में IV फ्लूइड की आवश्यकता हो सकती है।",
        "answer_or": "ORS ହେଉଛି ଲବଣ ଓ ସୁଗାରର ସମାଧାନ ଯାହା ଦସ୍ତ ଥିବା ବେଳେ ପୁନର୍ଜଲୀକରଣ କରିଥାଏ। ଗୁରୁତର ନିର୍ଜଳୀକରଣ ଘଟଣାରେ IV ଦ୍ରବ ଆବଶ୍ୟକ ହୁଏ।",
        "reference": "https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease"
    }
]