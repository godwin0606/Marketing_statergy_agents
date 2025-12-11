# import TheMarketingCrew.streamlit as st
import streamlit as st
import json
from datetime import datetime
import time
from crew import TheMarketingCrew, Content
import os

# Page configuration
st.set_page_config(
    page_title="Marketing Crew AI",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    
    .input-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin-bottom: 2rem;
    }
    
    .output-section {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    
    .info-box {
        background-color: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #bee5eb;
        margin-bottom: 1rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .stProgress > div > div > div > div {
        background-color: #3498db;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🚀 Marketing Crew AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">AI-Powered Marketing Strategy & Content Creation</p>', unsafe_allow_html=True)
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["🏠 Dashboard", "📝 Input Form", "📊 Results", "⚙️ Settings"]
    )
    
    if page == "🏠 Dashboard":
        show_dashboard()
    elif page == "📝 Input Form":
        show_input_form()
    elif page == "📊 Results":
        show_results()
    elif page == "⚙️ Settings":
        show_settings()

def show_dashboard():
    st.markdown('<h2 class="sub-header">📊 Dashboard</h2>', unsafe_allow_html=True)
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>4</h3>
            <p>AI Agents</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>8</h3>
            <p>Tasks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>24/7</h3>
            <p>Availability</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>AI</h3>
            <p>Powered</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Information section
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **Welcome to Marketing Crew AI!** 
    
    This application uses AI agents to create comprehensive marketing strategies and content:
    
    - **Head of Marketing**: Leads strategy and research
    - **Content Creator**: Creates social media content and reels
    - **Content Writer**: Writes engaging blog posts
    - **SEO Specialist**: Optimizes content for search engines
    
    Navigate to the Input Form to get started!
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def show_input_form():
    st.markdown('<h2 class="sub-header">📝 Marketing Project Input</h2>', unsafe_allow_html=True)
    
    # Input form
    with st.container():
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        
        # Product Information
        st.subheader("🎯 Product Information")
        product_name = st.text_input(
            "Product/Service Name",
            placeholder="e.g., AI Powered Excel Automation Tool",
            help="Enter the name of your product or service"
        )
        
        product_description = st.text_area(
            "Product Description",
            placeholder="Describe your product/service in detail...",
            height=100,
            help="Provide a comprehensive description of your product or service"
        )
        
        # Target Audience
        st.subheader("Target Audience")
        target_audience = st.text_input(
            "Target Audience",
            placeholder="e.g., Small and Medium Enterprises (SMEs)",
            help="Describe your target audience"
        )
        
        # Budget
        st.subheader("💰 Budget")
        budget = st.text_input(
            "Marketing Budget",
            placeholder="e.g., Rs. 50,000",
            help="Enter your marketing budget"
        )
        
        # Additional Options
        st.subheader("⚙️ Additional Options")
        
        col1, col2 = st.columns(2)
        with col1:
            content_types = st.multiselect(
                "Content Types to Generate",
                ["Blog Posts", "Social Media Posts", "Instagram Reels", "Email Campaigns"],
                default=["Blog Posts", "Social Media Posts", "Instagram Reels"],
                help="Select the types of content you want to generate"
            )
        
        with col2:
            platforms = st.multiselect(
                "Target Platforms",
                ["LinkedIn", "Twitter", "Instagram", "Facebook", "Email"],
                default=["LinkedIn", "Twitter", "Instagram"],
                help="Select the platforms you want to target"
            )
        
        # Advanced Settings
        with st.expander("🔧 Advanced Settings"):
            temperature = st.slider(
                "AI Creativity Level",
                min_value=0.1,
                max_value=1.0,
                value=0.7,
                step=0.1,
                help="Higher values make the AI more creative, lower values make it more focused"
            )
            
            max_iterations = st.slider(
                "Maximum Iterations",
                min_value=1,
                max_value=50,
                value=30,
                help="Maximum number of iterations for content generation"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Generate Marketing Strategy & Content", type="primary", use_container_width=True):
                if validate_inputs(product_name, product_description, target_audience, budget):
                    run_marketing_crew(product_name, product_description, target_audience, budget, content_types, platforms, temperature, max_iterations)
                else:
                    st.error("Please fill in all required fields!")

def validate_inputs(product_name, product_description, target_audience, budget):
    return all([product_name.strip(), product_description.strip(), target_audience.strip(), budget.strip()])

def run_marketing_crew(product_name, product_description, target_audience, budget, content_types, platforms, temperature, max_iterations):
    # Create a session state to store results
    if 'results' not in st.session_state:
        st.session_state.results = {}
    
    # Progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Initialize the crew
        status_text.text("Initializing Marketing Crew...")
        progress_bar.progress(10)
        
        crew = TheMarketingCrew()
        
        # Prepare inputs
        inputs = {
            "product_name": product_name,
            "target_audience": target_audience,
            "product_description": product_description,
            "budget": budget,
            "current_date": datetime.now().strftime("%Y-%m-%d"),
            "content_types": content_types,
            "platforms": platforms,
            "temperature": temperature,
            "max_iterations": max_iterations
        }
        
        status_text.text("Running Market Research...")
        progress_bar.progress(20)
        time.sleep(1)
        
        status_text.text("Preparing Marketing Strategy...")
        progress_bar.progress(40)
        time.sleep(1)
        
        status_text.text("Creating Content Calendar...")
        progress_bar.progress(60)
        time.sleep(1)
        
        status_text.text("Generating Content...")
        progress_bar.progress(80)
        time.sleep(1)
        
        # Run the crew
        result = crew.marketingcrew().kickoff(inputs=inputs)
        
        status_text.text("Finalizing Results...")
        progress_bar.progress(90)
        time.sleep(1)
        
        # Store results
        st.session_state.results = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'inputs': inputs,
            'output': result
        }
        
        progress_bar.progress(100)
        status_text.text("✅ Marketing strategy and content generated successfully!")
        
        # Success message
        st.markdown('<div class="success-message">', unsafe_allow_html=True)
        st.success("Marketing strategy and content have been generated successfully!")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Show results immediately
        show_generated_results(result)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.exception(e)

def show_generated_results(result):
    st.markdown('<h2 class="sub-header">📊 Generated Results</h2>', unsafe_allow_html=True)
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Summary", "📝 Content", "📅 Calendar", "📈 Strategy"])
    
    with tab1:
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.subheader("📋 Executive Summary")
        
        if hasattr(result, 'raw') and result.raw:
            # Try to parse the result
            try:
                if isinstance(result.raw, str):
                    st.markdown(result.raw)
                else:
                    st.json(result.raw)
            except:
                st.text(str(result.raw))
        else:
            st.info("Results will be displayed here after generation.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.subheader("📝 Generated Content")
        
        # Content preview
        if hasattr(result, 'raw') and result.raw:
            st.text_area("Content Preview", str(result.raw), height=400)
        else:
            st.info("Content will be displayed here after generation.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.subheader("📅 Content Calendar")
        st.info("Content calendar will be displayed here after generation.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.subheader("Marketing Strategy")
        st.info("Marketing strategy will be displayed here after generation.")
        st.markdown('</div>', unsafe_allow_html=True)

def show_results():
    st.markdown('<h2 class="sub-header">�� Previous Results</h2>', unsafe_allow_html=True)
    
    if 'results' in st.session_state and st.session_state.results:
        results = st.session_state.results
        
        # Display timestamp
        st.info(f"Last generated: {results['timestamp']}")
        
        # Display inputs used
        with st.expander("📝 Inputs Used"):
            st.json(results['inputs'])
        
        # Display results
        with st.expander("📊 Generated Results"):
            if hasattr(results['output'], 'raw') and results['output'].raw:
                st.markdown(results['output'].raw)
            else:
                st.text(str(results['output']))
        
        # Download button
        if st.button("💾 Download Results as JSON"):
            results_json = json.dumps(results, default=str, indent=2)
            st.download_button(
                label="📥 Download",
                data=results_json,
                file_name=f"marketing_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
    else:
        st.info("No results available. Generate some content first!")

def show_settings():
    st.markdown('<h2 class="sub-header">⚙️ Settings</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="output-section">', unsafe_allow_html=True)
    
    st.subheader("🔧 Configuration")
    
    # Model settings
    st.selectbox(
        "Default AI Model",
        ["openrouter/mistralai/mistral-7b-instruct", "gemini/gemini-2.0-flash", "gpt-4"],
        index=0,
        help="Select the default AI model for content generation"
    )
    
    # Default temperature
    default_temp = st.slider(
        "Default Temperature",
        min_value=0.1,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Default creativity level for AI generation"
    )
    
    # Auto-save settings
    st.checkbox(
        "Auto-save results",
        value=True,
        help="Automatically save results to session"
    )
    
    # Clear results button
    if st.button("Clear All Results"):
        if 'results' in st.session_state:
            del st.session_state.results
        st.success("Results cleared successfully!")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()