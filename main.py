import streamlit as st

# MBTI별 쉬운 설명과 캐릭터 매칭 정보
mbti_data = {
    "ENFP": {
        "description": "새로운 것을 좋아하고 친구들과 노는 걸 정말 좋아해요. 항상 웃으며 재미있는 아이디어가 많아요!",
        "character": "하츄핑 (신나는 리더)"
    },
    "INTJ": {
        "description": "조용하지만 머리가 똑똑하고 계획을 잘 세워요. 혼자 생각하는 걸 좋아하고 문제를 해결하는 걸 잘해요!",
        "character": "시리핑 (생각쟁이 마법사)"
    },
    "ISFJ": {
        "description": "친구들을 잘 도와주고 조용하지만 따뜻한 마음을 가지고 있어요. 약속을 잘 지키는 착한 친구예요!",
        "character": "마리핑 (친절 요정)"
    },
    "ESTP": {
        "description": "활동적인 걸 좋아하고 친구들과 놀면서 인기가 많아요. 용감하고 도전을 좋아해요!",
        "character": "파티핑 (모험가 친구)"
    },
    # 더 많은 MBTI를 추가할 수 있어요!
}

# 제목
st.title("MBTI로 알아보는 나와 어울리는 하츄핑 친구는?")

# 사용자 입력 (MBTI 선택)
selected_mbti = st.selectbox("당신의 MBTI를 골라보세요!", list(mbti_data.keys()))

# 결과 보여주기
if selected_mbti:
    data = mbti_data[selected_mbti]
    st.subheader(f"🧠 {selected_mbti} 성격은 이런 모습이에요!")
    st.write(data["description"])
    
    st.subheader(f"🧚‍♀️ 어울리는 하츄핑 친구: **{data['character']}**")
    
    image_path = f"images/{selected_mbti}.png"  # 이미지 폴더 경로 설정 필요
    st.image(image_path, caption=data["character"], use_column_width=True)
