import streamlit as st
from groq import Groq
from openai import OpenAI

# --- API YAPILANDIRMASI ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client_groq = Groq(api_key=GROQ_API_KEY)
client_openai = OpenAI(api_key=OPENAI_API_KEY)

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TechDoc Translator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS İLE GÖRSELLEŞTİRME ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTextArea textarea {
        font-size: 16px;
        color: #ffffff;
    }
    .header-style {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .success-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1c2e4a;
        border-left: 6px solid #3498db;
        margin-bottom: 20px;
    }
    .info-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1e3a2f;
        border-left: 6px solid #2ecc71;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- YAN MENÜ (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=80)
    st.title("Proje Hakkında")
    st.info("""
    Bu uygulama, teknik dokümantasyonları anlamayı kolaylaştırmak için **iki farklı yapay zeka** yaklaşımını birleştirir.
    """)
    st.markdown("---")
    st.markdown("**Geliştirici:**")
    st.markdown("👨‍💻 Onur YERLİKAYA")
    st.markdown("🎓 Yazılım Müh. Öğrencisi")
    st.markdown("---")
    st.caption("Final Projesi 2026")

# --- ANA BAŞLIK ---
st.title("🧠 Çift Modelli Teknik Doküman Asistanı")
st.markdown("""
Dokümantasyonları hem **uzman** hem de **yeni başlayan** gözüyle analiz edin.
""")

# --- GİRİŞ ALANI ---
col_input, col_btn = st.columns([4, 1])

with col_btn:
    # Hızlı test için örnek metin butonu
    if st.button("📝 Örnek Metin Yükle"):
        st.session_state['text_input'] = "Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files."
    else:
        if 'text_input' not in st.session_state:
            st.session_state['text_input'] = ""

text = st.text_area(
    "Analiz edilecek İngilizce teknik metni buraya yapıştırın:",
    value=st.session_state['text_input'],
    height=150,
    placeholder="Örn: Kubernetes pods are the smallest deployable units..."
)

analyze_btn = st.button("🚀 Analizi Başlat", type="primary", use_container_width=True)

# --- FONKSİYONLAR ---
def get_technical_translation(input_text):
    """Sol Panel: Meta Llama 3.3"""
    try:
        completion = client_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Sen kıdemli bir yazılım mühendisisin. Verilen metni Türkçeye çevir. Teknik terimleri (Deploy, Pod, Container, Thread vb.) asla Türkçeleştirme, orijinal bırak. Resmi ve akademik bir dil kullan."},
                {"role": "user", "content": input_text}
            ],
            temperature=0.1
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Hata: {e}"

def get_eli5_summary(input_text):
    """Sağ Panel: OpenAI GPT-4o"""
    try:
        response = client_openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen harika bir öğretmensin. Verilen teknik metni 5 yaşındaki bir çocuğun anlayacağı dilde, günlük hayattan metaforlar (lego, trafik, yemek vb.) kullanarak Türkçe özetle. Teknik terim kullanmaktan kaçın."},
                {"role": "user", "content": input_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Hata: {e}"

# --- SONUÇ EKRANI ---
if analyze_btn and text:
    if len(text) < 5:
        st.warning("⚠️ Lütfen analiz için daha uzun bir metin girin.")
    else:
        st.markdown("---")
        with st.spinner('Yapay zeka modelleri metni işliyor...'):
            
            col1, col2 = st.columns(2)

            # SOL PANEL: META LLAMA (TEKNİK)
            with col1:
                st.markdown('<div class="header-style">🛠️ Teknik Çeviri (Meta Llama 3.3)</div>', unsafe_allow_html=True)
                technical_res = get_technical_translation(text)
                st.markdown(f'<div class="success-box">{technical_res}</div>', unsafe_allow_html=True)
                st.caption("ℹ️ Teknik terimler korunarak, mühendislik jargonuyla çevrildi.")

            # SAĞ PANEL: OPENAI GPT (BASİT)
            with col2:
                st.markdown('<div class="header-style">🧸 Basit Özet (OpenAI GPT-4o)</div>', unsafe_allow_html=True)
                simple_res = get_eli5_summary(text)
                st.markdown(f'<div class="info-box">{simple_res}</div>', unsafe_allow_html=True)
                st.caption("ℹ️ Metaforlar kullanılarak, herkesin anlayacağı dilde özetlendi.")

elif analyze_btn and not text:
    st.error("Lütfen önce bir metin girin veya örnek metin butonunu kullanın.")