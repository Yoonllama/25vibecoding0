import streamlit as st

# 16가지 MBTI에 대한 쉬운 설명과 어울리는 하츄핑 캐릭터 매칭
mbti_data = {
    "ENFP": {
        "description": "새로운 것을 좋아하고 친구들과 노는 걸 정말 좋아해요. 항상 웃으며 재미있는 아이디어가 많아요!",
        "character": "하츄핑 (신나는 리더)"
    },
    "ENFJ": {
        "description": "친구들을 잘 도와주고 모두가 행복하길 바라는 마음이 커요. 따뜻하고 리더십이 있어요!",
        "character": "피치핑 (따뜻한 친구)"
    },
    "ENTP": {
        "description": "궁금한 게 많고 말도 잘해요. 새로운 생각을 자주 하고 친구들을 웃게 해줘요!",
        "character": "코지핑 (아이디어 천재)"
    },
    "ENTJ": {
        "description": "계획을 잘 세우고 친구들을 이끄는 걸 좋아해요. 똑똑하고 씩씩한 친구예요!",
        "character": "마카핑 (꼼꼼 대장)"
    },
    "INFP": {
        "description": "상상력이 풍부하고 마음이 따뜻해요. 혼자서 조용히 그림 그리거나 생각하는 걸 좋아해요.",
        "character": "미니핑 (꿈꾸는 요정)"
    },
    "INFJ": {
        "description": "친구들이 힘들면 먼저 도와주고, 조용하지만 깊은 생각을 해요. 마음이 착한 친구예요.",
        "character": "로미핑 (마음 읽는 요정)"
    },
    "INTP": {
        "description": "왜 그런지 궁금해하고 스스로 답을 찾는 걸 좋아해요. 똑똑하고 조용한 생각쟁이예요.",
        "character": "테크핑 (호기심 박사)"
    },
    "INTJ": {
        "description": "조용하지만 머리가 똑똑하고 계획을 잘 세워요. 혼자 생각하는 걸 좋아하고 문제를 해결하는 걸 잘해요!",
        "character": "시리핑 (생각쟁이 마법사)"
    },
    "ESFP": {
        "description": "친구들과 놀 때 가장 신나요! 춤추고 노래하는 걸 좋아하고 모두를 즐겁게 해줘요.",
        "character": "멜로핑 (무대의 스타)"
    },
    "ESFJ": {
        "description": "친구를 잘 챙기고, 모두가 함께 놀 수 있게 도와줘요. 아주 친절하고 밝은 친구예요!",
        "character": "핑크핑 (친구 챙김왕)"
    },
    "ESTP": {
        "description": "모험을 좋아하고 용감해요! 운동도 잘하고 친구들과 노는 걸 정말 좋아해요.",
        "character": "파티핑 (모험가 친구)"
    },
    "ESTJ": {
        "description": "규칙을 잘 지키고 계획을 세워서 친구들을 이끌어요. 책임감이 강한 친구예요.",
        "character": "바움핑 (책임감 대장)"
    },
    "ISFP": {
        "description": "조용하고 다정해요. 혼자서 그림을 그리거나 노래 듣는 걸 좋아하는 예쁜 마음을 가진 친구예요.",
        "character": "벨핑 (감성 요정)"
    },
    "ISFJ": {
        "description": "친구들을 잘 도와주고 조용하지만 따뜻한 마음을 가지고 있어요. 약속을 잘 지키는 착한 친구예요!",
        "character": "마리핑 (친절 요정)"
    },
    "ISTP": {
        "description": "손으로 만드는 걸 좋아하고 똑똑해요. 조용하지만 뭐든지 스스로 해보는 걸 좋아해요!",
        "character": "스피디핑 (만들기 천재)"
    },
    "ISTJ": {
        "description": "약속을 잘 지키고 정리를 잘해요. 책임감이 있고 항상 바른 행동을 하려고 해요!",
        "character": "루루핑 (꼼꼼 요정)"
    },
}

# Streamlit 앱 제목
st.title("🧠 MBTI로 알아보는 나와 어울리는 하츄핑 친구는?")

# 사용자 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 골라보세요!", list(mbti_data.keys()))

# 선택 후 결과 출력
if selected_mbti:
    data = mbti_data[selected_mbti]
    
    st.subheader(f"🌟 {selected_mbti} 친구는 이런 성격이에요!")
    st.write(data["description"])

    st.subheader(f"🧚‍♀️ 어울리는 하츄핑 친구: **{data['character']}**")
    
    # 이미지 출력 부분
    image_path = f"images/{selected_mbti}.png"
    st.image(image_path, caption=data["character"], use_container_width=True)
