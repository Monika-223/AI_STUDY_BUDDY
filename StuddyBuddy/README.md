# 📚 AI Study Buddy - Your Personal AI Learning Companion

An intelligent, all-in-one study platform that helps students learn effectively through AI-powered explanations, quizzes, flashcards, and summaries. Built for modern learners who want to study smarter, not harder.

## ✨ Key Features

### 💬 Smart Chat Interface
- **One-Click Learning**: Enter a topic once and generate everything from one place
- **AI Teacher Explanations**: Get detailed, step-by-step explanations with examples
- **Educational Focus**: AI only responds to study-related questions
- **Topic History**: Quick access to recently studied topics

### 📝 Instant Quiz Generation
- Generate custom multiple-choice quizzes on any topic
- 5 questions per quiz with clear answer keys
- Perfect for self-assessment and exam preparation

### 🎴 Interactive Flashcards
- Create flashcards with one click
- 5 cards per topic for effective memorization
- Ideal for quick revision and active recall

### 📄 Smart Summaries
- Get concise summaries of complex topics
- Key points and important facts highlighted
- Perfect for last-minute revision

### 📥 Download Everything
- Download individual content (explanation, quiz, flashcards, summary)
- Download complete study material for a topic in one file
- All downloads in easy-to-read text format

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key from: [https://console.groq.com/keys](https://console.groq.com/keys)

### 3. Run the Application
```bash
streamlit run app.py
```

### 4. Access the App
Open your browser and go to `http://localhost:8501`

## 🎨 UI Features

- **Beautiful Homepage**: Professional landing page with feature overview
- **Gradient Design**: Eye-catching purple gradient background
- **Sidebar Navigation**: Easy navigation between sections
- **Progress Tracking**: Track topics studied and materials generated
- **Responsive Layout**: Works on all screen sizes
- **Download Buttons**: Green gradient buttons for easy downloads
- **Content Cards**: Organized display with color-coded sections

## 🔧 Technology Stack

- **Frontend**: Streamlit with custom CSS
- **AI Model**: Llama 3.1 8B Instant via Groq API
- **Backend**: Python
- **API**: Groq API (Fast & Reliable)
- **State Management**: Streamlit Session State

## 📝 How to Use

1. **Start Learning**: Click "Start Learning Now" on homepage
2. **Enter Topic**: Type any educational topic you want to learn
3. **Get Explanation**: AI provides detailed explanation instantly
4. **Generate Materials**: Click buttons to generate quiz, flashcards, or summary
5. **Download**: Download individual items or complete study material
6. **Track Progress**: View your studied topics in the sidebar

## 🎯 Perfect for Internship Projects

This project demonstrates:
- ✅ Modern UI/UX design with Streamlit
- ✅ API integration (Groq AI)
- ✅ State management and session handling
- ✅ File download functionality
- ✅ Responsive web design
- ✅ Real-world application development
- ✅ Educational technology implementation
- ✅ Clean code architecture

## 🌟 Project Highlights

- **Educational Focus**: AI restricted to educational content only
- **User-Friendly**: Intuitive interface requiring minimal clicks
- **Efficient**: Generate all study materials from one topic entry
- **Portable**: Download and study offline
- **Fast**: Powered by Groq's lightning-fast API
- **Free**: Uses free tier of Groq API

## 📦 Project Structure

```
StuddyBuddy/
├── app.py              # Main application file
├── .env                # API key configuration
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🔐 Environment Variables

```
GROQ_API_KEY=your_groq_api_key_here
```

## 📋 Requirements

```
streamlit==1.31.0
requests==2.31.0
python-dotenv==1.0.0
```

## 🚀 Deployment

This app can be deployed on:
- **Streamlit Cloud**: Free hosting for Streamlit apps
- **Heroku**: Cloud platform for Python apps
- **AWS/Azure**: Enterprise cloud platforms

## 🤝 Contributing

This is an internship project. Feel free to fork and enhance!

## 📄 License

Free to use for educational purposes.

## 👨‍💻 Developer

Built with ❤️ for Students

---

**Note**: This is an AI-powered educational tool. Always verify important information from authoritative sources.
