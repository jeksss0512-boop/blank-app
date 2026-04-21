import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", page_icon="👤", layout="centered")

# 헤더
st.title("👤 자기소개")
st.divider()

# 프로필 섹션
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    st.image("https://via.placeholder.com/200", use_column_width=True)

with col2:
    st.subheader("이름: 정은경")
    st.write("**하는 일:** 대학원생")
    st.write("**관심분야:** Problem Solving, digital tools, chatbot")

st.divider()

# 자기소개
st.subheader("📝 소개")
st.write("""
안녕하세요! 저는 수학강사로 일하고 있고 수학교육전공을 하고 있는 대학원생입니다. 
""")

st.divider()

# 스킬
st.subheader("🛠️ 기술 스택")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**언어**")
    st.write("• Python\n• JavaScript\n• SQL")

with col2:
    st.write("**라이브러리**")
    st.write("• Streamlit\n• Pandas\n• NumPy")

with col3:
    st.write("**기타**")
    st.write("• Git\n• Docker\n• APIs")

st.divider()

# 연락처
st.subheader("📧 연락처")
st.write("📧 Email: jeksss@korea.ac.kr")
st.write("🔗 GitHub: https://gdp-dashboard-tf2akjg7tmp.streamlit.app/")
st.write("💼 LinkedIn: linkedin.com/in/yourprofile")
