import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def query_ai(prompt):
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "system", "content": "You are an educational AI assistant. You ONLY answer questions related to education, academics, learning, and study topics. If asked about anything unrelated to education (like entertainment, jokes, personal advice, etc.), politely decline and remind the user you're here for educational purposes only."},
                    {"role": "user", "content": prompt}
                ]
            }
        )
        result = response.json()
        if 'error' in result:
            return f"⚠️ API Error: {result['error'].get('message', 'Unknown error')}"
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content'].strip()
        return f"⚠️ Unexpected response"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem;}
    .stApp {background: transparent;}
    .hero {background: white; border-radius: 20px; padding: 3rem; text-align: center; box-shadow: 0 10px 40px rgba(0,0,0,0.3); margin-bottom: 2rem;}
    .hero h1 {color: #667eea; font-size: 3.5rem; margin-bottom: 1rem;}
    .hero p {color: #666; font-size: 1.3rem;}
    .feature-box {background: white; border-radius: 15px; padding: 2rem; margin: 1rem; box-shadow: 0 5px 20px rgba(0,0,0,0.2); text-align: center; transition: transform 0.3s;}
    .feature-box:hover {transform: translateY(-5px);}
    .chat-container {background: white; border-radius: 20px; padding: 2rem; box-shadow: 0 10px 40px rgba(0,0,0,0.2); margin-bottom: 2rem;}
    .content-box {background: #f8f9fa; border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border-left: 4px solid #667eea;}
    .action-buttons {display: flex; gap: 10px; margin-top: 1rem;}
    .stButton>button {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 0.75rem 2rem; border-radius: 25px; font-weight: bold;}
    .stDownloadButton>button {background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; border: none; padding: 0.5rem 1.5rem; border-radius: 20px;}
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = None
if 'topic_data' not in st.session_state:
    st.session_state.topic_data = {}

with st.sidebar:
    st.markdown("### 🎯 Navigation")
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    if st.button("💬 Study Buddy Chat", use_container_width=True):
        st.session_state.page = 'chat'
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Your Progress")
    st.metric("Topics Studied", len(st.session_state.topic_data))
    
    if st.session_state.topic_data:
        st.markdown("### 📚 Recent Topics")
        for topic in list(st.session_state.topic_data.keys())[-3:]:
            if st.button(f"📖 {topic[:20]}...", use_container_width=True, key=f"recent_{topic}"):
                st.session_state.current_topic = topic
                st.session_state.page = 'chat'
                st.rerun()

if st.session_state.page == 'home':
    st.markdown("""
    <div class="hero">
        <h1>📚 AI Study Buddy</h1>
        <p>Your Personal AI-Powered Learning Companion</p>
        <p style="font-size: 1.1rem; color: #888; margin-top: 1rem;">Learn, Quiz, Revise - All in One Place!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="feature-box">
            <h2>💬 Smart Chat Interface</h2>
            <p>Ask about any topic and get instant explanations</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-box">
            <h2>🎴 Instant Flashcards</h2>
            <p>Generate flashcards with one click from your topic</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <h2>📝 Quick Quizzes</h2>
            <p>Test your knowledge instantly on any topic</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-box">
            <h2>📄 Smart Summaries</h2>
            <p>Get concise summaries for quick revision</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_start = st.columns([1, 2, 1])
    with col_start[1]:
        if st.button("🚀 Start Learning Now", use_container_width=True, type="primary"):
            st.session_state.page = 'chat'
            st.rerun()

elif st.session_state.page == 'chat':
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown("## 💬 Study Buddy Chat")
    st.markdown("Enter a topic and I'll help you learn it completely!")
    
    topic = st.text_input("📚 What do you want to learn today?", 
                          value=st.session_state.current_topic if st.session_state.current_topic else "",
                          placeholder="e.g., Photosynthesis, Pythagorean Theorem, World War II")
    
    if st.button("🎯 Learn This Topic", use_container_width=True, type="primary"):
        if topic:
            st.session_state.current_topic = topic
            if topic not in st.session_state.topic_data:
                with st.spinner("🤔 Learning about this topic..."):
                    prompt = f"You are an expert teacher. Explain '{topic}' clearly for students with examples and step-by-step breakdown."
                    explanation = query_ai(prompt)
                    st.session_state.topic_data[topic] = {
                        "explanation": explanation,
                        "quiz": None,
                        "flashcards": None,
                        "summary": None,
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
            st.rerun()
    
    if st.session_state.current_topic and st.session_state.current_topic in st.session_state.topic_data:
        topic_info = st.session_state.topic_data[st.session_state.current_topic]
        
        st.markdown(f"### 📚 Topic: {st.session_state.current_topic}")
        st.markdown(f"*Started: {topic_info['time']}*")
        
        # Explanation Section
        st.markdown("#### 🎓 Explanation")
        st.markdown(f'<div class="content-box">{topic_info["explanation"]}</div>', unsafe_allow_html=True)
        st.download_button(
            "📥 Download Explanation",
            data=f"Topic: {st.session_state.current_topic}\n\n{topic_info['explanation']}",
            file_name=f"{st.session_state.current_topic.replace(' ', '_')}_explanation.txt",
            key="download_exp"
        )
        
        st.markdown("---")
        
        # Quick Actions
        st.markdown("#### ⚡ Quick Actions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📝 Generate Quiz", use_container_width=True):
                with st.spinner("Creating quiz..."):
                    prompt = f"Create 5 multiple choice questions about '{st.session_state.current_topic}'. Format:\nQ1: [question]\nA) [option]\nB) [option]\nC) [option]\nD) [option]\nAnswer: [letter]\n"
                    quiz = query_ai(prompt)
                    topic_info["quiz"] = quiz
                    st.rerun()
        
        with col2:
            if st.button("🎴 Generate Flashcards", use_container_width=True):
                with st.spinner("Creating flashcards..."):
                    prompt = f"Create 5 flashcards about '{st.session_state.current_topic}'. Format each as 'Q: [question] | A: [answer]'. Separate with '###'."
                    flashcards = query_ai(prompt)
                    topic_info["flashcards"] = flashcards
                    st.rerun()
        
        with col3:
            if st.button("📄 Generate Summary", use_container_width=True):
                with st.spinner("Creating summary..."):
                    prompt = f"Create a concise summary of '{st.session_state.current_topic}' with key points."
                    summary = query_ai(prompt)
                    topic_info["summary"] = summary
                    st.rerun()
        
        # Display Generated Content
        if topic_info["quiz"]:
            st.markdown("---")
            st.markdown("#### 📝 Quiz")
            st.markdown(f'<div class="content-box">{topic_info["quiz"]}</div>', unsafe_allow_html=True)
            st.download_button(
                "📥 Download Quiz",
                data=f"Quiz: {st.session_state.current_topic}\n\n{topic_info['quiz']}",
                file_name=f"{st.session_state.current_topic.replace(' ', '_')}_quiz.txt",
                key="download_quiz"
            )
        
        if topic_info["flashcards"]:
            st.markdown("---")
            st.markdown("#### 🎴 Flashcards")
            cards = topic_info["flashcards"].split('###')
            for i, card in enumerate(cards[:5], 1):
                if card.strip():
                    st.markdown(f'<div class="content-box"><strong>Card {i}:</strong><br>{card.strip()}</div>', unsafe_allow_html=True)
            st.download_button(
                "📥 Download Flashcards",
                data=f"Flashcards: {st.session_state.current_topic}\n\n{topic_info['flashcards']}",
                file_name=f"{st.session_state.current_topic.replace(' ', '_')}_flashcards.txt",
                key="download_flash"
            )
        
        if topic_info["summary"]:
            st.markdown("---")
            st.markdown("#### 📄 Summary")
            st.markdown(f'<div class="content-box">{topic_info["summary"]}</div>', unsafe_allow_html=True)
            st.download_button(
                "📥 Download Summary",
                data=f"Summary: {st.session_state.current_topic}\n\n{topic_info['summary']}",
                file_name=f"{st.session_state.current_topic.replace(' ', '_')}_summary.txt",
                key="download_sum"
            )
        
        # Download All
        if topic_info["quiz"] or topic_info["flashcards"] or topic_info["summary"]:
            st.markdown("---")
            all_content = f"""
COMPLETE STUDY MATERIAL
Topic: {st.session_state.current_topic}
Generated: {topic_info['time']}

{'='*50}
EXPLANATION
{'='*50}
{topic_info['explanation']}

{'='*50}
QUIZ
{'='*50}
{topic_info['quiz'] if topic_info['quiz'] else 'Not generated yet'}

{'='*50}
FLASHCARDS
{'='*50}
{topic_info['flashcards'] if topic_info['flashcards'] else 'Not generated yet'}

{'='*50}
SUMMARY
{'='*50}
{topic_info['summary'] if topic_info['summary'] else 'Not generated yet'}
"""
            st.download_button(
                "📦 Download Complete Study Material",
                data=all_content,
                file_name=f"{st.session_state.current_topic.replace(' ', '_')}_complete.txt",
                type="primary",
                use_container_width=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: white;'>Made with ❤️ for Students | Powered by Groq AI</p>", unsafe_allow_html=True)
