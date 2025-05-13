import streamlit as st

# 🎨 웹페이지 기본 설정
st.set_page_config(page_title="🌟MBTI 진로 추천기🌈", page_icon="🧭", layout="centered")

# 🌈 타이틀과 설명
st.markdown("""
# 💼✨ MBTI 진로 추천기 🎯  
당신의 **MBTI**를 선택하면,  
🌟성격에 딱 맞는 **꿈의 직업**을 추천해드릴게요!  

> 🎓 진로 교육에 딱! 이모지 가득 귀여운 스타일 웹앱 💖
""")

# 🧬 MBTI 리스트
mbti_list = [
    "ISTJ 🧾", "ISFJ 🧸", "INFJ 🔮", "INTJ 🧠",
    "ISTP 🛠️", "ISFP 🎨", "INFP 📖", "INTP 📚",
    "ESTP 🏍️", "ESFP 🎤", "ENFP 🌈", "ENTP 🚀",
    "ESTJ 🏢", "ESFJ 🤝", "ENFJ 🎯", "ENTJ 🦁"
]

mbti = st.selectbox("🧬 당신의 MBTI를 선택해주세요!", mbti_list)

# 💼 직업 추천 데이터
job_dict = {
    "ISTJ 🧾": ["회계사 💼", "공무원 🏛️", "데이터 분석가 📊"],
    "ISFJ 🧸": ["간호사 🏥", "교사 👩‍🏫", "사회복지사 🤝"],
    "INFJ 🔮": ["심리상담가 🧘", "작가 ✍️", "인권운동가 🌍"],
    "INTJ 🧠": ["전략기획가 📈", "과학자 🔬", "AI 엔지니어 🤖"],
    "ISTP 🛠️": ["엔지니어 ⚙️", "파일럿 ✈️", "정비사 🔧"],
    "ISFP 🎨": ["디자이너 🎨", "플로리스트 💐", "포토그래퍼 📸"],
    "INFP 📖": ["작가 ✍️", "번역가 🌐", "예술가 🎭"],
    "INTP 📚": ["개발자 💻", "이론 물리학자 ⚛️", "교수 👨‍🏫"],
    "ESTP 🏍️": ["기업가 💼", "세일즈 매니저 📢", "소방관 🚒"],
    "ESFP 🎤": ["연예인 🎬", "이벤트 플래너 🎉", "운동선수 🏅"],
    "ENFP 🌈": ["마케팅 전문가 📢", "작가 ✍️", "창업가 🚀"],
    "ENTP 🚀": ["기획자 🗂️", "벤처 CEO 👨‍💼", "방송인 🎙️"],
    "ESTJ 🏢": ["경영자 📊", "군인 🪖", "행정관리자 📋"],
    "ESFJ 🤝": ["교사 👩‍🏫", "간호사 🏥", "HR 매니저 👥"],
    "ENFJ 🎯": ["리더십 코치 🧑‍🏫", "사회 운동가 🕊️", "홍보 담당자 📣"],
    "ENTJ 🦁": ["CEO 🏆", "전략가 📈", "투자 전문가 💸"]
}

# 💡 추천 직업 출력
if mbti:
    st.markdown(f"""
    ## 🎉 당신에게 어울리는 직업은?
    """)
    for job in job_dict.get(mbti, []):
        st.markdown(f"- {job}")
    st.balloons()

# 🖼️ 하단 푸터
st.markdown("---")
st.markdown("Made with ❤️ by [GPT온라인](https://gptonline.ai/ko/) – 한국형 AI와 함께하는 진로 탐색")
