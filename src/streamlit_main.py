"""
Healthcare AI Demo - Main Streamlit Application
===============================================

Multi-page Streamlit application for demonstrating AI-powered medical notes analysis.
Designed for healthcare professionals including physicians, administrators, and researchers.
"""

import streamlit as st
import sys
import os
from datetime import datetime

# Add src to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Page configuration must be first Streamlit command
st.set_page_config(
    page_title="Healthcare AI Demo",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': """
        # Healthcare AI Demo
        
        This demonstration showcases how Snowflake's AI capabilities can transform 
        medical notes into actionable insights for improved patient care.
        
        **For demo purposes only - not for clinical use**
        """
    }
)

# Import connection helper
from connection_helper import get_connection_info, initialize_demo_environment

# Custom CSS for healthcare theme
st.markdown("""
<style>
/* Healthcare color palette */
:root {
    --primary-blue: #0066CC;
    --light-blue: #E6F2FF;
    --success-green: #28A745;
    --warning-amber: #FFC107;
    --danger-red: #DC3545;
    --text-dark: #212529;
    --text-muted: #6C757D;
}

/* Sidebar styling */
.css-1d391kg {
    background-color: var(--light-blue);
}

/* Main content area */
.main {
    padding-top: 2rem;
}

/* Custom card component */
.healthcare-card {
    background-color: white;
    padding: 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
    border-left: 4px solid var(--primary-blue);
}

/* Status indicators */
.status-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.875rem;
    font-weight: 500;
}

.status-connected {
    background-color: var(--success-green);
    color: white;
}

.status-error {
    background-color: var(--danger-red);
    color: white;
}

/* Medical disclaimer */
.medical-disclaimer {
    background-color: #FFF3CD;
    border: 1px solid #FFEEBA;
    color: #856404;
    padding: 1rem;
    border-radius: 0.25rem;
    margin: 1rem 0;
}

/* Demo scenario cards */
.scenario-card {
    background-color: #F8F9FA;
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 0.5rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.scenario-card:hover {
    background-color: #E9ECEF;
    transform: translateX(5px);
}

/* Metrics display */
.metric-container {
    background-color: white;
    padding: 1rem;
    border-radius: 0.5rem;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.metric-value {
    font-size: 2rem;
    font-weight: bold;
    color: var(--primary-blue);
}

.metric-label {
    color: var(--text-muted);
    font-size: 0.875rem;
}
</style>
""", unsafe_allow_html=True)

def display_header():
    """Display application header with branding"""
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        st.image("https://www.snowflake.com/wp-content/themes/snowflake/assets/img/brand-guidelines/logo-sno-blue.svg", 
                width=150)
    
    with col2:
        st.markdown("# 🏥 Healthcare AI Demo")
        st.markdown("**Transforming Medical Notes into Actionable Insights**")
    
    with col3:
        # Connection status
        conn_info = get_connection_info()
        if conn_info["status"] == "connected":
            st.markdown("""
            <div style='text-align: right; margin-top: 1rem;'>
                <span class='status-badge status-connected'>✓ Connected</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='text-align: right; margin-top: 1rem;'>
                <span class='status-badge status-error'>✗ Disconnected</span>
            </div>
            """, unsafe_allow_html=True)

def display_medical_disclaimer():
    """Display medical disclaimer for demo"""
    st.markdown("""
    <div class="medical-disclaimer">
        <strong>⚠️ Important Notice:</strong> This is a demonstration system only. 
        All medical insights shown are for illustration purposes and should not be used 
        for actual clinical decision-making. Always consult qualified healthcare professionals 
        for medical advice.
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application entry point"""
    # Display header
    display_header()
    
    # Initialize session state
    if 'demo_mode' not in st.session_state:
        st.session_state.demo_mode = True
    
    if 'selected_patient' not in st.session_state:
        st.session_state.selected_patient = None
    
    # Sidebar navigation (simplified)
    with st.sidebar:
        pass  # Sidebar will only contain the standard page navigation
    
    # Main content area
    st.markdown("---")
    
    # Welcome section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Welcome to the Healthcare AI Demonstration
        
        This demonstration showcases how Snowflake's integrated AI and data platform can 
        transform unstructured medical notes into valuable clinical insights. Using advanced 
        language models and the PMC patients dataset, we demonstrate practical applications 
        for:
        
        - 🩺 **Clinical Decision Support** - AI-powered differential diagnosis and treatment recommendations
        - 📊 **Population Health Analytics** - Identify patterns and optimize care across patient cohorts  
        - 🔬 **Medical Research** - Accelerate discovery with automated literature analysis
        - 🎓 **Medical Education** - Generate teaching cases and assessment materials
        
        ### Key Features
        
        - **Hybrid Architecture**: Pre-computed insights for speed + real-time AI for flexibility
        - **Multiple AI Models**: Optimized models for different medical tasks
        - **HIPAA-Ready Design**: All processing within Snowflake's secure environment
        - **Physician-Friendly Interface**: Designed with clinical workflows in mind
        """)
        
        # Display medical disclaimer
        display_medical_disclaimer()
    
    with col2:
        # Quick stats card
        st.markdown("""
        <div class="healthcare-card">
            <h4>Demo Dataset</h4>
            <div class="metric-container">
                <div class="metric-value">167K</div>
                <div class="metric-label">Patient Records</div>
            </div>
            <br>
            <div class="metric-container">
                <div class="metric-value">8</div>
                <div class="metric-label">AI Use Cases</div>
            </div>
            <br>
            <div class="metric-container">
                <div class="metric-value"><30s</div>
                <div class="metric-label">Analysis Time</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation instructions
    st.markdown("---")
    st.markdown("""
    ### 🚀 Getting Started
    
    Use the sidebar to navigate through the demonstration:
    
    1. **Data Foundation** - Explore the PMC patients dataset
    2. **Clinical Decision Support** - See AI-powered physician tools
    3. **Prompt and Model Testing** - Test prompts and models in real time
    4. **Population Health Analytics** - Analyze cohorts and trends
    
    For the best experience, start with the **Clinical Decision Support** page to see 
    immediate value for physicians.
    """)
    
    # Footer
    st.markdown("---")
    st.caption(f"Healthcare AI Demo v1.0 | Last updated: {datetime.now().strftime('%Y-%m-%d')} | For demonstration purposes only")

if __name__ == "__main__":
    main()