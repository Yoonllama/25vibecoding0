import streamlit as st

# 🌟 기본 설정
st.set_page_config(page_title="🌈MBTI 진로 추천기", page_icon="🧭", layout="centered")

# 🌟 타이틀
st.markdown("""
# 💼✨ MBTI 진로 추천기 🎯  
당신의 **MBTI**를 선택하면,  
🌟 성격에 꼭 맞는 **추천 직업**을 알려드려요!  
""")

# ✅ MBTI 선택
mbti_list = [
    "ISTJ 🧾", "ISFJ 🧸", "INFJ 🔮", "INTJ 🧠",
    "ISTP 🛠️", "ISFP 🎨", "INFP 📖", "INTP 📚",
    "ESTP 🏍️", "ESFP 🎤", "ENFP 🌈", "ENTP 🚀",
    "ESTJ 🏢", "ESFJ 🤝", "ENFJ 🎯", "ENTJ 🦁"
]
mbti = st.selectbox("🧬 당신의 MBTI를 선택해주세요!", mbti_list)

# 💡 직업 데이터와 설명
job_data = {
    "ISTJ 🧾": [("회계사 💼", "정확성과 책임감이 중요한 직업으로, ISTJ의 꼼꼼함이 빛나는 분야입니다."),
               ("공무원 🏛️", "안정적인 환경에서 체계적으로 일할 수 있는 공직 분야가 적합합니다."),
               ("데이터 분석가 📊", "정확한 분석과 논리가 필요한 데이터 직군에서 활약할 수 있어요.")],
    "ISFP 🎨": [("디자이너 🎨", "감각적이고 창의적인 ISFP에게 시각적 표현이 중요한 직업입니다."),
               ("플로리스트 💐", "자연과 아름다움을 사랑하는 ISFP에게 잘 어울리는 직업이에요."),
               ("포토그래퍼 📸", "순간을 담는 예술가로서의 감성이 중요한 분야입니다.")],
    # 나머지 MBTI도 동일한 방식으로 추가 가능
}

if mbti:
    st.markdown(f"## 🎉 {mbti} 유형에게 어울리는 직업은?")
    selected_job = None

    for job, desc in job_data.get(mbti, []):
        if st.button(f"🔍 {job}"):
            selected_job = (job, desc)

    if selected_job:
        st.markdown("---")
        st.markdown(f"### 📌 {selected_job[0]}에 대해 알아볼까요?")
        st.markdown(f"💡 {selected_job[1]}")
        st.success("🎯 이 직업이 당신의 성향과 잘 맞을 수 있어요!")

st.markdown("---")
st.markdown("Made with ❤️ by [GPT온라인](https://gptonline.ai/ko/) – 한국형 AI와 함께하는 진로 탐색")
