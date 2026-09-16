import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

st.set_page_config(
    page_title="AI画像生成アプリ",
    page_icon="☁",
    layout="centered"
)

# Custom Header HTML
st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-size: 2.5rem; margin-bottom: 0;">AI画像生成アプリ</h1>
        <div style="font-size: 2rem; margin-top: 5px;">☁ 🌲🏡🌲 🌱🌊🌱</div>
    </div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32 if device=="cpu" else torch.float16)
    pipe = pipe.to(device)
    return pipe

prompt = st.text_area("プロンプト（英語で入力してください）", "A peaceful landscape with mountains and lake, highly detailed")

if st.button("画像を生成"):
    if prompt:
        with st.spinner("画像を生成中..."):
            pipe = load_model()
            image = pipe(prompt).images[0]
            st.image(image, caption="生成された画像", use_column_width=True)
    else:
        st.warning("プロンプトを入力してください。")
