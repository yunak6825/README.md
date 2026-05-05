import streamlit as st
import google.generativeai as genai

# 1. AI 설정 (AI Studio에서 만든 설정 그대로)
genai.configure(api_key="AIzaSyDFjkNKawokylB-XHwDUYFM1vi-4otR288")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 2. 웹 화면 꾸미기
st.set_page_config(page_title="R&D 과제 신청 가이드", page_icon="🤖")
st.title("🤖 R&D 신규과제 신청 응대 챗봇")
st.caption("교수님, 신규 과제 신청 관련 궁금한 점을 물어보세요.")

# 3. 채팅 세션 관리 (대화 내용 기억)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. 화면에 대화 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. 교수님 질문 입력 및 답변 생성
if prompt := st.chat_input("질문을 입력하세요 (예: 3책 5공 예외가 뭔가요?)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # 여기에 윤아님이 AI Studio에서 짠 시스템 명령어를 녹여냅니다
        full_prompt = f"너는 R&D 행정 전문가야. 다음 질문에 정확히 답해줘: {prompt}"
        response = model.generate_content(full_prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
