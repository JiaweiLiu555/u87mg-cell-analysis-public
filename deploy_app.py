"""Polished, conservative public entrypoint for U87MG microscopy review."""
import csv
import io
import sys
from pathlib import Path

import streamlit as st
from PIL import Image, ImageStat, UnidentifiedImageError

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from mgmt_cell_ai.input_qc import assess_image

GENERATED_DIR = ROOT / "demo_outputs" / "generated"

st.set_page_config(
    page_title="U87MG Microscopy Analysis",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    :root { --navy:#17324d; --slate:#536777; --teal:#2a7d7b; --mist:#f4f7f8; --line:#dfe7e9; }
    .stApp { background:#fbfcfc; color:var(--navy); }
    .block-container { max-width:1180px; padding:3.3rem 3rem 4rem; }
    html, body, [class*="css"] { font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }
    h1,h2,h3 { color:var(--navy); letter-spacing:-.025em; }
    h1 { font-family:Georgia,"Times New Roman",serif; font-size:clamp(2.25rem,4vw,3.5rem)!important; font-weight:500!important; margin-bottom:.25rem!important; }
    h2,h3 { font-weight:600!important; }
    .eyebrow { color:var(--teal); font-size:.76rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; margin-bottom:.55rem; }
    .subtitle { color:var(--slate); font-size:1.08rem; margin-bottom:.9rem; }
    .status { display:inline-block; color:#286a68; background:#e9f4f2; border:1px solid #cde6e2; border-radius:999px; padding:.35rem .7rem; font-size:.78rem; font-weight:600; }
    .section-label { color:var(--slate); font-size:.77rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; margin:1.8rem 0 .55rem; }
    .mode-help { color:var(--slate); font-size:.91rem; margin:-.25rem 0 .8rem; }
    .upload-note { color:var(--slate); font-size:.88rem; text-align:center; margin-top:-.35rem; }
    .metric-card { background:white; border:1px solid var(--line); border-radius:12px; padding:1rem 1.1rem; min-height:6.1rem; box-shadow:0 5px 18px rgba(23,50,77,.045); }
    .metric-label { color:var(--slate); font-size:.78rem; font-weight:600; }
    .metric-value { color:var(--navy); font-size:1.72rem; font-weight:700; line-height:1.25; margin-top:.35rem; }
    .about { border-top:1px solid var(--line); margin-top:3.5rem; padding-top:1.4rem; color:var(--slate); font-size:.9rem; line-height:1.6; }
    div.stButton > button[kind="primary"] { background:var(--navy); border-color:var(--navy); border-radius:8px; padding:.55rem 1.4rem; font-weight:600; }
    div.stButton > button[kind="primary"]:hover { background:var(--teal); border-color:var(--teal); }
    [data-testid="stFileUploader"] { background:white; border:1px dashed #a9c2c4; border-radius:12px; padding:.35rem; }
    [data-testid="stMetric"] { background:white; border:1px solid var(--line); border-radius:12px; padding:.7rem 1rem; }
    [data-testid="stSidebar"] { display:none; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">Microscopy quantification</div>', unsafe_allow_html=True)
st.title("U87MG Microscopy Analysis")
st.markdown('<div class="subtitle">Automated Cell Quantification Research Prototype</div>', unsafe_allow_html=True)
st.markdown('<span class="status">Research prototype • validation in progress</span>', unsafe_allow_html=True)

st.markdown('<div class="section-label">Step 1 · Select analysis mode</div>', unsafe_allow_html=True)
mode = st.radio(
    "Analysis mode",
    ["Live Phase Contrast", "Crystal Violet", "Neurosphere"],
    horizontal=True,
    label_visibility="collapsed",
)
mode_help = {
    "Live Phase Contrast": "Experimental morphology review; not a live/dead assay.",
    "Crystal Violet": "Attached stained-cell candidate quantification; manual verification recommended.",
    "Neurosphere": "Aggregate candidate regions and pixel-based morphology; individual-cell counts are not inferred.",
}
st.markdown(f'<div class="mode-help">{mode_help[mode]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-label">Step 2 · Upload microscopy image</div>', unsafe_allow_html=True)
uploaded = st.file_uploader(
    "Upload microscopy image",
    type=["png", "jpg", "jpeg", "tif", "tiff", "bmp"],
    label_visibility="collapsed",
)
st.markdown('<div class="upload-note">PNG, JPEG, TIFF, or BMP · or select a demonstration below</div>', unsafe_allow_html=True)

demo = st.selectbox(
    "Try a demo image",
    ["No demo selected", "Crystal Violet demonstration", "Neurosphere demonstration"],
    label_visibility="collapsed",
)
demo_data = {
    "Crystal Violet demonstration": {
        "source": "rotich_figure23_crystal_violet.png",
        "stem": "rotich_crystal_violet",
        "mode": "Crystal Violet",
        "label": "Automated candidate count",
        "count": 110,
    },
    "Neurosphere demonstration": {
        "source": "kyi_figure26_neurosphere_reference.tif",
        "stem": "kyi_neurosphere_reference",
        "mode": "Neurosphere",
        "label": "Aggregate candidates",
        "count": 129,
    },
}

st.markdown('<div class="section-label">Step 3 · Analyze</div>', unsafe_allow_html=True)
analyze = st.button("Analyze image", type="primary")

if analyze:
    if demo in demo_data:
        result = demo_data[demo]
        st.markdown('<div class="section-label">Results</div>', unsafe_allow_html=True)
        st.caption("Historical thesis figure — demonstration only, not validation data.")
        left, right = st.columns([1.15, 1], gap="large")
        with left:
            st.markdown("#### Annotated microscopy view")
            preview_path = GENERATED_DIR / f"{result['stem']}_annotated.png"
            if preview_path.exists():
                st.image(str(preview_path), use_container_width=True)
            else:
                st.warning("Annotated output is unavailable in this runtime.")
        with right:
            st.markdown("#### Summary")
            st.markdown(
                f'<div class="metric-card"><div class="metric-label">{result["label"]}</div><div class="metric-value">{result["count"]}</div></div>',
                unsafe_allow_html=True,
            )
            st.write("")
            st.markdown(
                '<div class="metric-card"><div class="metric-label">Review status</div><div class="metric-value" style="font-size:1.05rem">Manual verification recommended</div></div>',
                unsafe_allow_html=True,
            )
            st.write("")
            st.info("The overlay shows the regions included in this software demonstration. It does not establish biological accuracy.")
        rows = [{
            "mode": result["mode"],
            "candidate_regions": result["count"],
            "review_status": "Manual verification recommended",
        }]
        st.markdown("#### Results table")
        st.dataframe(rows, use_container_width=True, hide_index=True)
        csv_text = f"mode,candidate_regions,review_status\n{result['mode']},{result['count']},Manual verification recommended\n"
        st.download_button("Download CSV", csv_text, f"{result['stem']}_summary.csv", "text/csv")
    elif uploaded is not None:
        try:
            image = Image.open(io.BytesIO(uploaded.getvalue())).convert("RGB")
        except (UnidentifiedImageError, OSError, ValueError):
            st.error("This file could not be read as an image. No measurements were generated.")
        else:
            assessment = assess_image(image)
            st.markdown('<div class="section-label">Results</div>', unsafe_allow_html=True)
            if not assessment.accepted_for_review:
                st.error("I cannot reliably analyze this image.")
                st.warning("Manual review recommended. This image is outside the current supported analysis conditions.")
                st.write("Reason: " + "; ".join(assessment.reasons) + ".")
            else:
                st.info("Image accepted for software review. The public release does not claim biological classification for uploaded images.")
            left, right = st.columns([1.15, 1], gap="large")
            with left:
                st.markdown("#### Uploaded microscopy view")
                st.image(image, caption="Uploaded image", use_container_width=True)
            with right:
                st.markdown("#### Image review")
                st.metric("QC status", assessment.status)
                st.metric("Dimensions", f"{assessment.width} × {assessment.height} px")
                st.metric("Mean grayscale", f"{assessment.mean_gray:.1f}")
                st.metric("Grayscale variation", f"{assessment.gray_std:.1f}")
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow(["image", "width_px", "height_px", "mean_gray", "gray_std", "qc_status", "reasons"])
            writer.writerow([uploaded.name, assessment.width, assessment.height, assessment.mean_gray, assessment.gray_std, assessment.status, "; ".join(assessment.reasons)])
            st.markdown("#### Results table")
            st.dataframe([{
                "image": uploaded.name,
                "width_px": assessment.width,
                "height_px": assessment.height,
                "mean_gray": assessment.mean_gray,
                "gray_std": assessment.gray_std,
                "qc_status": assessment.status,
            }], use_container_width=True, hide_index=True)
            st.download_button("Download CSV", output.getvalue(), "upload_qc.csv", "text/csv")
    else:
        st.warning("Choose a demonstration or upload an image before analyzing.")

st.markdown(
    '<div class="about"><strong>About this prototype</strong><br>This prototype is being developed to automate U87MG microscopy quantification. Current software functionality has been tested, while biological performance still requires validation using independent raw microscopy images and trusted reference measurements.<br><br>Uploaded images are processed for analysis and are not intentionally retained by the application.</div>',
    unsafe_allow_html=True,
)

