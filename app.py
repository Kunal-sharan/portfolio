import streamlit as st
import streamlit.components.v1 as components
import math
# Page configuration with sidebar expanded by default
st.set_page_config(
    page_title="Kunal Sharan | AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# js_code = """
# <script>
#   console.log(window.outerHeight);

# </script>
# """

# components.html(js_code, height=0) # height=0 hides the iframe if it's purely for script execution
# st.write("Streamlit app content after JavaScript execution.")
# Custom CSS for modern one-page UI
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        padding: 0 !important;
    }
    
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
    }
    
    body {
        background-color: #0d1117; 
        color: #c9d1d9; 
        font-family: 'Inter', sans-serif;
    }

    section {
        padding: 2rem 1rem;
        max-width: 1200px;
        margin: 0 auto;
        gap: 1 rem
    }
    
    .section-title {
        font-size: 2.5rem; 
        color: #58a6ff; 
        margin-bottom: 2rem; 
        text-align: center;
        font-weight: 600;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, #58a6ff, #00d4ff);
        border-radius: 2px;
    }
    
    .card {
        background: linear-gradient(145deg, #161b22, #0d1117);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid #30363d;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin: 2rem auto;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .card:hover {
        transform: translateY(-8px);
        border-color: #58a6ff;
        box-shadow: 0 16px 48px rgba(88, 166, 255, 0.2);
    }
    
   
    
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .project-card {
        background: linear-gradient(145deg, #161b22, #0d1117);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid #30363d;
        transition: all 0.3s ease;
        height: 100%;
        margin:1rem;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        border-color: #58a6ff;
        box-shadow: 0 12px 32px rgba(88, 166, 255, 0.15);
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #58a6ff;
        margin-bottom: 1rem;
    }
    
    .project-niche {
        color: #00d4ff;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .project-tech {
        color: #ffa657;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .project-desc {
        color: #c9d1d9;
        line-height: 1.6;
    }
    
    .skills-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .skill-item {
        margin-bottom: 1.5rem;
    }
    
    .skill-name {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    .skill-bar {
        height: 8px;
        background: #30363d;
        border-radius: 4px;
        overflow: hidden;
    }
    
    .skill-progress {
        height: 100%;
        background: linear-gradient(90deg, #58a6ff, #00d4ff);
        border-radius: 4px;
        transition: width 0.8s ease;
    }
    
    .contact-form {
        max-width: 600px;
        margin: 0 auto;
        background: linear-gradient(145deg, #161b22, #0d1117);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid #30363d;
    }
    
    .form-input {
        width: 100%;
        padding: 1rem;
        margin-bottom: 1.5rem;
        border: 1px solid #30363d;
        border-radius: 8px;
        background: #0d1117;
        color: #c9d1d9;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    
    .form-input:focus {
        outline: none;
        border-color: #58a6ff;
        box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.1);
    }
    
    .form-button {
        width: 100%;
        padding: 1rem 2rem;
        background: linear-gradient(90deg, #58a6ff, #00d4ff);
        border: none;
        border-radius: 8px;
        color: white;
        cursor: pointer;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .form-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(88, 166, 255, 0.3);
    }
    
    .footer {
        padding: 3rem 2rem;
        text-align: center;
        color: #8b949e;
        border-top: 1px solid #30363d;
        background: #0d1117;
    }
    
    
    a {
        text-decoration: none !important;
    }
    </style>
    """, 
    unsafe_allow_html=True
)


st.markdown('<section id="about">', unsafe_allow_html=True)
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.markdown('<h1>Kunal Sharan</h1>', unsafe_allow_html=True)
# with st.container(height=400):
c1,c2 = st.columns([1,1])
with c1:
    st.image("dp.jpg", 
                    caption="Kunal Sharan",width=300)
    st.markdown("""    <div style="text-align: center; margin-top: 2rem;">
            <p style="font-size: 1.1rem; color: #8b949e;">
                📧 <a href="mailto:ks904@snu.edu.in" style="color: #58a6ff;">ks904@snu.edu.in</a> | 
                💼 <a href="https://linkedin.com/in/kunalsharan" style="color: #58a6ff;">LinkedIn</a> | 
                🐙 <a href="https://github.com/Kunal-sharan" style="color: #58a6ff;">GitHub</a>
            </p>
        </div>
    """,unsafe_allow_html=True)
with c2:    
    st.markdown(
        """
        <div class="card">
            <p style="font-size: 1.1rem; line-height: 1.8; text-align: center;">
                🚀 Passionate AI Developer Intern with hands-on experience building RAG systems, no-code automations, 
                and innovative robotics solutions. Proficient in Python, LangChain, and real-time analytics with a 
                strong focus on open source contributions and scalable ML deployments. Currently pursuing ECE at 
                Shiv Nadar University while actively contributing to cutting-edge AI projects.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.markdown('</section>', unsafe_allow_html=True)

# Experience Section
st.markdown('<section id="experience">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <h3 style="color: #58a6ff; margin-bottom: 1rem;">🏢 AI Developer Intern</h3>
        <p style="color: #ffa657; font-weight: 500; margin-bottom: 1rem;">Beans n Brands • Remote • July 2024 – September 2024</p>
        <ul style="text-align: left; line-height: 1.8;">
            <li>🔧 Developed 5+ AI-driven no-code automations, reducing operational costs by <strong>15%</strong> using Make.com</li>
            <li>🤖 Engineered a Twilio-integrated RAG chatbot for restaurants using Flask, LangChain, and ChromaDB</li>
            <li>📈 Implemented real-time analytics dashboard improving customer engagement metrics</li>
            <li>⚡ Optimized workflow automation processes, increasing team productivity by 25%</li>
        </ul>
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown('</section>', unsafe_allow_html=True)
blog_data = ""
with open("blogs/first.md","r") as f:
    blog_data = f.read()

# blogs
blogs = [
    {
        'id': i,
        'title': f'Blog Post {i+1}',
        'summary': f'{blog_data[100:300]} ' + str(i+1),
        'content': f'{blog_data}'
    } for i in range(8)
]


# Function to display full blog
def show_full_blog(blog):
    with st.container(border=True):
        st.title(blog['title'])
        st.markdown(blog['content'], unsafe_allow_html=True)
        st.button("Back to Blogs", on_click=lambda: st.session_state.pop('selected_blog', None))

# Main view
if 'selected_blog' not in st.session_state:
    st.title("My Blog Collection")
    cols_per_row = 3
    rows = math.ceil(len(blogs) / cols_per_row)

    for row in range(rows):
        cols = st.columns(cols_per_row)
        for i in range(cols_per_row):
            idx = row * cols_per_row + i
            if idx < len(blogs):
                with cols[i]:
                    with st.container(border=True):
                        st.subheader(blogs[idx]['title'])
                        st.write(blogs[idx]['summary'])
                        if st.button("Read More", key=f'read_more_{idx}'):
                            st.session_state['selected_blog'] = blogs[idx]
                            st.rerun()

else:
    show_full_blog(st.session_state['selected_blog'])

# Projects Section
st.markdown('<section id="projects">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)
st.markdown('<div class="projects-grid">', unsafe_allow_html=True)

projects = [
    {
        "title": "🔄 AI-PDF Language Translator",
        "stack": "Python • PyTesseract • LangChain • Streamlit",
        "niche": "Document OCR & Multilingual Translation",
        "desc": "Achieved 85% translation accuracy for scanned PDFs with real-time processing. Served 50+ users via an intuitive Streamlit interface featuring live output preview and downloadable results.",
        "link": "https://www.linkedin.com/posts/kunal-sharan-4b018a260_pytesseract-langchain-python-activity-7197978042411999233-3_w5?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAEAZGkQBWWznqHroY5zmuGIe_mvaet0pWOM",
    },
    {
        "title": "📊 ListingLogic.ai",
        "stack": "BeautifulSoup • Selenium • Pandas • Matplotlib",
        "niche": "E-commerce Data Analytics",
        "desc": "Scraped 2000+ product listings for competitive market insights. Generated synthetic datasets for ML model training and built comprehensive dashboards for data visualization and content generation.",
        "link":"https://github.com/Kunal-sharan/Walmart_sparkathon"
    },
    {
        "title": "🤖 College finder",
        "stack": "python • bs4 • Langchain",
        "niche": "Scraping and NLP",
        "desc": "This application helps students find the best college based on their preferences. It collects rank and cutoff data through web scraping using BeautifulSoup from various websites and uses generative AI through Langchain to compare the data.",
        "link": "https://www.linkedin.com/posts/kunal-sharan-4b018a260_beautifulsoup-langchain-physicswallah-activity-7204472323725291520-T9T6?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEAZGkQBWWznqHroY5zmuGIe_mvaet0pWOM"
    },
    {
        "title": "🏠 Smart Security System",
        "stack": "NodeMCU • Raspberry Pi • Python • Twilio • Flask",
        "niche": "IoT & Security Solutions",
        "desc": "Developed motion-triggered facial recognition system with instant WhatsApp alerts. Integrated manual override controls and automated gate management for comprehensive home security.",
        "link" : "#"
    }
]

for project in projects:
    st.markdown(
        f"""
        
        <div class="project-card">
        <a  href="{project['link']}">
            <div class="project-title">{project['title']}</div>
            <div class="project-niche">🎯 {project['niche']}</div>
            <div class="project-tech">⚙️ {project['stack']}</div>
            <div class="project-desc">{project['desc']}</div>
        </a>
        </div>
        
        """, 
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)
st.markdown("<a href ='https://github.com/Kunal-sharan'>Show More</p>",unsafe_allow_html=True)


# Contact Section
st.markdown('<section id="contact">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Let\'s Connect</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="contact-form">
        <form action="https://formsubmit.co/ks904@snu.edu.in" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_next" value="https://thankyou-page-url.com">
            <input type="email" name="email" placeholder="📧 Your email address" class="form-input" required>
            <input type="text" name="subject" placeholder="📝 Subject" class="form-input" required>
            <textarea name="message" placeholder="💬 Your message here..." rows="5" class="form-input" required></textarea>
            <button type="submit" class="form-button">🚀 Send Message</button>
        </form>
    </div>
    
    <div style="text-align: center; margin-top: 2rem;">
        <p style="font-size: 1.1rem; color: #8b949e;">
            📧 <a href="mailto:ks904@snu.edu.in" style="color: #58a6ff;">ks904@snu.edu.in</a> | 
            💼 <a href="https://linkedin.com/in/kunalsharan" style="color: #58a6ff;">LinkedIn</a> | 
            🐙 <a href="https://github.com/Kunal-sharan" style="color: #58a6ff;">GitHub</a>
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown('</section>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>© 2025 Kunal Sharan • Built with ❤️ using Streamlit</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">
            🚀 Passionate about AI • 🎯 Open to opportunities • 🌟 Let's build the future together
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)