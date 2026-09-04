import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Little Beats",
    page_icon="❤️",
    layout="wide",
)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

# ---------------------------------------------------------
# Page state
# ---------------------------------------------------------
if "selected_subject" not in st.session_state:
    st.session_state.selected_subject = None

# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(112, 216, 255, 0.18), transparent 40%),
        radial-gradient(circle at 85% 0%, rgba(255, 182, 217, 0.18), transparent 40%),
        linear-gradient(180deg, #F5F9FC 0%, #EFF6FA 100%);
    background-attachment: fixed;
}

.block-container {
    max-width: 1300px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

#MainMenu, header[data-testid="stHeader"], footer {
    visibility: hidden;
}

/* ---------------- HEADER ---------------- */
.lb-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.6);
    box-shadow: 0 8px 30px rgba(18, 59, 82, 0.08);
    padding: 16px 30px;
    border-radius: 18px;
    margin-bottom: 26px;
    position: sticky;
    top: 10px;
    z-index: 999;
}

.lb-logo {
    font-family: 'Poppins', sans-serif;
    font-size: 24px;
    font-weight: 800;
    background: linear-gradient(120deg, #FF6FA5, #7C4DFF, #17B8D6);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: flex;
    align-items: center;
    gap: 8px;
    animation: shimmer 6s linear infinite;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}

.lb-badge {
    font-size: 11.5px;
    font-weight: 700;
    color: #12658F;
    background: linear-gradient(120deg, #E6F7FC, #EEF3FF);
    border: 1px solid #CFE9F2;
    padding: 6px 14px;
    border-radius: 100px;
    letter-spacing: .4px;
}

/* ---------------- HERO ---------------- */
.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(125deg, #1B2A4A 0%, #2E3F73 35%, #7C4DFF 75%, #FF6FA5 130%);
    border-radius: 24px;
    padding: 54px 50px;
    margin-bottom: 34px;
    box-shadow: 0 20px 45px rgba(72, 46, 140, 0.28);
}

.hero::before {
    content: "";
    position: absolute;
    width: 340px;
    height: 340px;
    background: radial-gradient(circle, rgba(255,255,255,0.18), transparent 70%);
    top: -120px;
    right: -80px;
    border-radius: 50%;
}

.hero::after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    background: radial-gradient(circle, rgba(255,255,255,0.12), transparent 70%);
    bottom: -100px;
    left: -60px;
    border-radius: 50%;
}

.hero h1 {
    font-family: 'Poppins', sans-serif;
    color: #FFFFFF;
    font-size: 44px;
    font-weight: 800;
    margin: 0 0 12px;
    position: relative;
    z-index: 2;
}

.hero p {
    color: rgba(255,255,255,0.85);
    font-size: 16.5px;
    max-width: 700px;
    line-height: 1.7;
    position: relative;
    z-index: 2;
    margin: 0;
}

.hero-pill {
    display: inline-block;
    margin-bottom: 18px;
    padding: 6px 16px;
    border-radius: 100px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .5px;
    text-transform: uppercase;
    position: relative;
    z-index: 2;
}

/* ---------------- SECTION TITLES ---------------- */
.subject-title {
    font-family: 'Poppins', sans-serif;
    color: #123B52;
    font-size: 26px;
    font-weight: 800;
    margin-bottom: 4px;
}

.subject-subtitle {
    color: #71818C;
    margin-bottom: 22px;
    font-size: 14.5px;
}

/* ---------------- SUBJECT CARDS ---------------- */
.subject-card {
    position: relative;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(220, 232, 237, 0.9);
    border-radius: 18px;
    padding: 26px 20px 20px;
    text-align: center;
    box-shadow: 0 10px 24px rgba(18, 59, 82, 0.06);
    margin-bottom: 10px;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color .25s ease;
    overflow: hidden;
}

.subject-card::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #17B8D6, #7C4DFF, #FF6FA5);
    opacity: 0;
    transition: opacity .25s ease;
}

.subject-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 34px rgba(18, 59, 82, 0.14);
    border-color: rgba(124, 77, 255, 0.35);
}

.subject-card:hover::before {
    opacity: 1;
}

.subject-number {
    width: 62px;
    height: 62px;
    line-height: 62px;
    margin: auto;
    border-radius: 50%;
    background: linear-gradient(135deg, #17B8D6, #7C4DFF);
    color: #fff;
    font-family: 'Poppins', sans-serif;
    font-size: 22px;
    font-weight: 800;
    box-shadow: 0 8px 18px rgba(124, 77, 255, 0.35);
}

.subject-card h3 {
    font-family: 'Poppins', sans-serif;
    color: #123B52;
    font-size: 18px;
    font-weight: 700;
    margin: 15px 0 4px;
}

.subject-card p {
    color: #7A8A94;
    font-size: 13px;
    margin: 0;
    line-height: 1.5;
}

.status-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #35C97C;
    margin-right: 6px;
    box-shadow: 0 0 0 3px rgba(53, 201, 124, 0.18);
}

/* ---------------- GRAPH HEADER (detail view) ---------------- */
.graph-header {
    position: relative;
    overflow: hidden;
    background: linear-gradient(120deg, #16223F, #2E3F73 60%, #6C4CD8);
    border-radius: 20px;
    padding: 30px 34px;
    margin-bottom: 26px;
    box-shadow: 0 14px 32px rgba(46, 63, 115, 0.25);
}

.graph-header .small {
    color: #9FE3F5;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.4px;
}

.graph-header h1 {
    font-family: 'Poppins', sans-serif;
    color: #fff;
    margin: 6px 0 4px;
    font-size: 30px;
    font-weight: 800;
}

.graph-header p {
    color: rgba(255,255,255,0.75);
    margin: 0;
    font-size: 14.5px;
}

.graph-title {
    font-family: 'Poppins', sans-serif;
    color: #123B52;
    font-size: 19px;
    font-weight: 800;
    margin: 26px 0 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.graph-title::before {
    content: "";
    width: 6px;
    height: 20px;
    border-radius: 4px;
    background: linear-gradient(180deg, #17B8D6, #7C4DFF);
    display: inline-block;
}

.graph-box {
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid #E1EBF0;
    border-radius: 18px;
    padding: 16px;
    box-shadow: 0 10px 26px rgba(18, 59, 82, 0.07);
    transition: box-shadow .25s ease;
}

.graph-box:hover {
    box-shadow: 0 16px 34px rgba(18, 59, 82, 0.12);
}

/* ---------------- BUTTONS ---------------- */
div.stButton > button {
    border-radius: 10px;
    border: none;
    background: linear-gradient(120deg, #17B8D6, #7C4DFF);
    color: #fff;
    font-weight: 700;
    min-height: 42px;
    box-shadow: 0 8px 18px rgba(124, 77, 255, 0.25);
    transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    filter: brightness(1.06);
    box-shadow: 0 12px 24px rgba(124, 77, 255, 0.35);
    color: #fff;
}

div.stButton > button:active {
    transform: translateY(0px);
}

/* Back button gets a lighter, secondary style */
div.stButton > button:has(p:contains("Back")) {
    background: white;
}

/* ---------------- FOOTER ---------------- */
.footer {
    text-align: center;
    color: #8998A0;
    border-top: 1px solid #DCE8ED;
    margin-top: 50px;
    padding: 22px;
    font-size: 12.5px;
}

.footer span {
    color: #7C4DFF;
    font-weight: 700;
}

/* ---------------- RESPONSIVE ---------------- */
@media (max-width: 900px) {
    .hero { padding: 34px 26px; }
    .hero h1 { font-size: 30px; }
    .hero p { font-size: 14.5px; }
    .lb-header { padding: 14px 18px; }
    .lb-badge { display: none; }
    .graph-header { padding: 22px 20px; }
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Function: open selected subject
# ---------------------------------------------------------
def open_subject(number):
    st.session_state.selected_subject = number
    st.rerun()


def back_to_subjects():
    st.session_state.selected_subject = None
    st.rerun()


# ---------------------------------------------------------
# Shared header
# ---------------------------------------------------------
st.markdown("""
<div class="lb-header">
    <div class="lb-logo">♥ Little Beats</div>
    <div class="lb-badge">FETAL MONITORING SUITE</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# SUBJECT LIST
# =========================================================
if st.session_state.selected_subject is None:

    st.markdown("""
    <div class="hero">
        <div class="hero-pill">Dashboard</div>
        <h1>Fetal Monitoring Dashboard</h1>
        <p>
            Select a monitoring subject below to view recorded fetal and
            maternal physiological signal graphs — heart rate, sensor
            signals, and analysis summaries, all in one place.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="subject-title">Monitoring Subjects</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subject-subtitle">'
        'Click a subject to open its monitoring graphs.'
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # Six subject widgets/buttons — responsive grid
    # -----------------------------------------------------
    for row in range(0, 6, 3):

        cols = st.columns(3)

        for i, col in enumerate(cols):

            subject_number = row + i + 1

            with col:

                st.markdown(
                    f"""
                    <div class="subject-card">
                        <div class="subject-number">
                            {subject_number}
                        </div>
                        <h3>Subject {subject_number}</h3>
                        <p>
                            <span class="status-dot"></span>Fetal monitoring<br>
                            Signal graphs available
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"Open Subject {subject_number} →",
                    key=f"subject_button_{subject_number}",
                    use_container_width=True
                ):
                    open_subject(subject_number)

        st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# SELECTED SUBJECT — SHOW PNG GRAPHS
# =========================================================
else:

    number = st.session_state.selected_subject
    subject_folder = DATA_DIR / f"subject_{number:02d}"

    if st.button("← Back to Subjects"):
        back_to_subjects()

    st.markdown(
        f"""
        <div class="graph-header">
            <div class="small">Little Beats · Fetal Monitoring</div>
            <h1>Subject {number}</h1>
            <p>
                Recorded physiological monitoring graphs
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # GRAPH CONFIGURATION — 5 GRAPHS
    # =====================================================

    graphs = [
        ("Fetal Beats", "fetal_beats.png"),
        ("Abdominal Composite ECG Signal", "abdominal_composite_ecg_signal.png"),
        ("Extracted MECG", "extracted_mecg.png"),
        ("Filtered Abdominal ECG", "filtered_abdominal_ecg.png"),
        ("Labeled Fetal Movements", "labeled_fetal_movements.png"),
    ]

    # =====================================================
    # RESPONSIVE GRAPH GRID
    # =====================================================

    graph_cols = st.columns(2)

    for idx, (title, filename) in enumerate(graphs):

        image_path = subject_folder / filename
        target_col = graph_cols[idx % 2]

        with target_col:

            # Graph title
            st.markdown(
                f"""
                <div class="graph-title">
                    {title}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Graph container
            if image_path.exists():

                st.markdown(
                    '<div class="graph-box">',
                    unsafe_allow_html=True
                )

                st.image(
                    str(image_path),
                    use_container_width=True
                )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="graph-missing">
                        <strong>Graph not found</strong><br>
                        {filename}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown(
        """
        <div class="footer">
            Little Beats · Fetal Monitoring &amp; Research Dashboard —
            crafted with <span>care</span> for maternal &amp; fetal health research
        </div>
        """,
        unsafe_allow_html=True
    )