import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Face Mask Detection",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = load_model("facemask_VGG16.h5")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #eef2ff 0%,
        #f8fafc 50%,
        #f1f5f9 100%
    );
}

.block-container {
    max-width: 1350px;
    padding-top: 1.2rem;
    padding-bottom: 1rem;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(18px);
    border-right: 1px solid rgba(255,255,255,0.5);
}

/* =========================================================
TITLE SECTION
========================================================= */

.hero-card {
    background: rgba(255,255,255,0.65);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.6);
    border-radius: 30px;
    padding: 45px;
    margin-bottom: 28px;
    box-shadow: 0 8px 30px rgba(15,23,42,0.08);
}

.hero-title {
    font-size: 78px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 12px;

    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed,
        #c026d3
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 24px;
    color: #475569;
    line-height: 1.7;
}

.tag-container {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 28px;
}

.tag {
    background: rgba(255,255,255,0.8);
    padding: 12px 20px;
    border-radius: 14px;
    font-weight: 600;
    color: #334155;
    box-shadow: 0 4px 12px rgba(15,23,42,0.05);
}

/* =========================================================
MAIN CARDS
========================================================= */

.main-card {

    background: rgba(255,255,255,0.72);

    backdrop-filter: blur(18px);

    border-radius: 28px;

    padding: 28px;

    border: 1px solid rgba(255,255,255,0.7);

    box-shadow: 0 8px 25px rgba(15,23,42,0.08);

    height: fit-content;
}
/* =========================================================
UPLOAD BOX
========================================================= */

.upload-box {
    background: #f8fafc;
    border: 2px dashed #cbd5e1;
    border-radius: 20px;
    padding: 14px;
}

/* =========================================================
RESULT BOX
========================================================= */

.result-box {
    background: linear-gradient(
        135deg,
        #ffffff,
        #f8fafc
    );

    border-radius: 24px;

    padding: 28px;

    margin-top: 18px;

    text-align: center;

    border: 1px solid #e2e8f0;
}

.result-icon {
    font-size: 82px;
}

.result-title {
    font-size: 42px;
    font-weight: 800;
    margin-top: 10px;
}

.result-sub {
    font-size: 20px;
    color: #475569;
    margin-top: 10px;
}

/* =========================================================
INFO CARDS
========================================================= */

.info-card {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(18px);
    border-radius: 24px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.7);
    box-shadow: 0 8px 25px rgba(15,23,42,0.07);
}

.info-title {
    font-size: 28px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 15px;
}

.info-text {
    color: #475569;
    line-height: 1.9;
    font-size: 17px;
}

/* =========================================================
FILE UPLOADER
========================================================= */

div[data-testid="stFileUploader"] {
    background: #ffffff;
    border-radius: 18px;
    padding: 10px;
    border: 1px dashed #cbd5e1;
}

/* =========================================================
PROGRESS BAR
========================================================= */

.stProgress > div > div > div > div {
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("# 🤖 AI Dashboard")

st.sidebar.markdown("---")

st.sidebar.markdown("## 👨‍💻 Developer")
st.sidebar.success("Sujal Chavan")

st.sidebar.markdown("## 🧠 Model")

st.sidebar.info("""
VGG16 Transfer Learning

CNN Architecture

95% Accuracy
""")

st.sidebar.markdown("## ⚡ Technologies")

st.sidebar.write("""
- Python
- TensorFlow
- Keras
- Streamlit
- Deep Learning
- Computer Vision
""")

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero-card">

<div class="hero-title">
🛡️ AI Face Mask Detection
</div>

<div class="hero-subtitle">
Modern Deep Learning based Face Mask Detection System using
VGG16 Transfer Learning & Computer Vision.
</div>

<div class="tag-container">

<div class="tag">
🚀 VGG16 Transfer Learning
</div>

<div class="tag">
⚡ 95% Accuracy
</div>

<div class="tag">
🧠 CNN Architecture
</div>

<div class="tag">
📷 Computer Vision
</div>

</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# MAIN SECTION
# =========================================================

left, right = st.columns([1,1])

# =========================================================
# LEFT CARD
# =========================================================

with left:

    st.markdown("""
    <div class="main-card">

    <div class="card-title">
    📤 Upload Face Image
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg","jpeg","png"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            use_container_width=True
        )

    else:

        st.markdown("""
        <div style="
        text-align:center;
        padding-top:60px;
        padding-bottom:50px;
        ">

        <img src="https://cdn-icons-png.flaticon.com/512/1048/1048941.png"
        width="140">

        <h2 style="
        margin-top:20px;
        color:#334155;
        ">
        Upload Face Image
        </h2>

        <p style="
        color:#64748b;
        font-size:18px;
        line-height:1.8;
        ">

        Upload JPG, JPEG or PNG image<br>
        to detect whether mask is present or not.

        </p>

        <div style="
        margin-top:20px;
        display:flex;
        justify-content:center;
        gap:12px;
        flex-wrap:wrap;
        ">

        <div style="
        background:#eff6ff;
        color:#2563eb;
        padding:10px 16px;
        border-radius:12px;
        font-weight:600;
        ">
        📷 Image Detection
        </div>

        <div style="
        background:#f5f3ff;
        color:#7c3aed;
        padding:10px 16px;
        border-radius:12px;
        font-weight:600;
        ">
        🧠 CNN Model
        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
# =========================================================
# RIGHT CARD
# =========================================================

with right:

    st.markdown("""
    <div class="main-card">

    <div class="card-title">
    🧠 Detection Analytics
    </div>
    """, unsafe_allow_html=True)

    if uploaded_file is not None:

        # =========================================================
        # PREPROCESSING
        # =========================================================

        img = image.resize((200,200))

        img = np.array(img)

        img = img[:,:,::-1]

        img = img / 255.0

        img = np.expand_dims(img, axis=0)

        # =========================================================
        # PREDICTION
        # =========================================================

        prediction = model.predict(img)

        class_names = ["No Mask", "Mask"]

        predicted_class = np.argmax(prediction)

        confidence = np.max(prediction) * 100

        # =========================================================
        # RESULT
        # =========================================================

        if class_names[predicted_class] == "Mask":

            result_icon = "✅"
            result_title = "MASK DETECTED"
            result_color = "#16a34a"

        else:

            result_icon = "❌"
            result_title = "NO MASK DETECTED"
            result_color = "#dc2626"

        st.markdown(f"""

        <div class="result-box">

        <div class="result-icon">
        {result_icon}
        </div>

        <div class="result-title"
        style="color:{result_color};">
        {result_title}
        </div>

        <div class="result-sub">
        Confidence Score: {confidence:.2f}%
        </div>

        </div>

        """, unsafe_allow_html=True)

        st.progress(int(confidence))

        st.markdown("""
        <div class="info-card" style="margin-top:20px;">

        <div class="info-title">
        🧠 AI Interpretation
        </div>

        <div class="info-text">

        The VGG16 CNN model analyzed facial regions,
        extracted deep visual features,
        and classified the uploaded image
        using Transfer Learning architecture.

        </div>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
        text-align:center;
        padding-top:70px;
        padding-bottom:50px;
        ">

        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png"
        width="150">

        <h2 style="
        margin-top:20px;
        color:#334155;
        ">
        AI Detection Results
        </h2>

        <p style="
        color:#64748b;
        font-size:18px;
        line-height:1.8;
        ">

        AI prediction analytics and confidence<br>
        scores will appear here after upload.

        </p>

        <div style="
        margin-top:28px;
        background:#f8fafc;
        border-radius:18px;
        padding:20px;
        border:1px solid #e2e8f0;
        ">

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:10px;
        ">

        <span style="font-weight:600;color:#334155;">
        Prediction Accuracy
        </span>

        <span style="color:#2563eb;font-weight:700;">
        95%
        </span>

        </div>

        <div style="
        height:10px;
        background:#dbeafe;
        border-radius:10px;
        overflow:hidden;
        ">

        <div style="
        width:95%;
        height:100%;
        background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
        );
        ">
        </div>

        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
# =========================================================
# BOTTOM INFO SECTION
# =========================================================

st.write("")
st.write("")

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="info-card">

    <div class="info-title">
    🏗️ Architecture
    </div>

    <div class="info-text">

    • VGG16 Pre-trained CNN Model<br>
    • Transfer Learning Approach<br>
    • Deep Feature Extraction<br>
    • Binary Classification<br>
    • High Accuracy Prediction

    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="info-card">

    <div class="info-title">
    ⚡ Key Features
    </div>

    <div class="info-text">

    • Real-Time Detection<br>
    • Deep Learning Based<br>
    • Fast Image Processing<br>
    • Computer Vision Powered<br>
    • Streamlit Deployment

    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.write("")

st.markdown("""
<div style="
text-align:center;
padding-top:20px;
padding-bottom:10px;
">

<hr style="margin-bottom:20px;">

<h2 style="
color:#334155;
">
👨‍💻 Developed by Sujal Chavan
</h2>

<p style="
font-size:18px;
color:#64748b;
">
Artificial Intelligence • Deep Learning • Computer Vision
</p>

</div>
""", unsafe_allow_html=True)
