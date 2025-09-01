"""
Healthcare AI Demo - Corporate Standard Style
===========================================

Professional, stable interface using native Streamlit components only.
Designed for conservative healthcare organizations and regulatory environments.

Style Features:
- Native Streamlit components exclusively
- Corporate blue color scheme
- Bordered containers for clear sections
- Traditional sidebar navigation
- Maximum stability and reliability
"""

import streamlit as st
import sys
import os
from datetime import datetime

# Add src and shared directories to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shared'))

# Corporate Standard Style Configuration
st.set_page_config(
    page_title="Healthcare AI Demo - Corporate Standard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': """
        # Healthcare AI Demo - Corporate Standard Style
        
        This demonstration showcases how Snowflake's AI capabilities can transform 
        medical notes into actionable insights for improved patient care.
        
        **Corporate Standard Style Features:**
        - Professional, stable interface design
        - Native Streamlit components for maximum reliability
        - Clear visual hierarchy with bordered sections
        - Traditional navigation patterns
        
        **For demo purposes only - not for clinical use**
        """,
        'Get help': None,
        'Report a bug': None
    }
)

# Corporate Standard CSS - Minimal and stable
st.markdown("""
<style>
/* Corporate Standard Theme - Professional Blue */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Professional header styling */
.main-header {
    background: linear-gradient(90deg, #0066CC 0%, #004499 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 2rem;
    text-align: center;
}

/* Consistent button styling */
.stButton > button {
    background-color: #0066CC;
    color: white;
    border: none;
    border-radius: 0.25rem;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #004499;
    border: none;
}

/* Medical disclaimer styling */
.medical-disclaimer {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 0.5rem;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 4px solid #f39c12;
}

/* Style guide indicator */
.style-indicator {
    position: fixed;
    top: 10px;
    right: 10px;
    background-color: #0066CC;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    font-size: 0.8rem;
    font-weight: bold;
    z-index: 1000;
}
</style>
""", unsafe_allow_html=True)

# Style guide indicator
st.markdown("""
<div class="style-indicator">
    📊 Corporate Standard
</div>
""", unsafe_allow_html=True)

# Main application header
st.markdown("""
<div class="main-header">
    <h1>🏥 Healthcare AI Demonstration</h1>
    <h3>Corporate Standard Style</h3>
    <p>Professional Medical Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

# Import shared components
try:
    from data_processors import create_medical_disclaimer, format_medical_value
    from ai_helpers import show_ai_processing_status
    from connection_helper import get_demo_data_status
    
    # Show medical disclaimer - Corporate style uses bordered container
    with st.container(border=True):
        st.markdown("### ⚠️ Medical Disclaimer")
        st.markdown(create_medical_disclaimer())

except ImportError as e:
    st.error(f"Import error: {e}")
    st.info("Some shared components may not be available yet.")

# Main content area using Corporate Standard layout principles
col1, col2 = st.columns([2, 1])

with col1:
    with st.container(border=True):
        st.header("📋 Demo Overview")
        
        st.markdown("""
        **Corporate Standard Style Features:**
        
        ✅ **Maximum Stability**: Uses only native Streamlit components for guaranteed compatibility
        
        ✅ **Professional Appearance**: Clean, corporate-appropriate visual design
        
        ✅ **Clear Structure**: Bordered containers create obvious visual sections
        
        ✅ **Traditional Navigation**: Familiar sidebar-based navigation pattern
        
        ✅ **Regulatory Ready**: Conservative design suitable for healthcare compliance environments
        """)
        
        # Demo navigation buttons using standard Streamlit buttons
        st.subheader("🗺️ Application Navigation")
        
        nav_col1, nav_col2, nav_col3 = st.columns(3)
        
        with nav_col1:
            if st.button("🏥 Data Foundation", use_container_width=True):
                st.info("Navigate to Data Foundation page via sidebar →")
        
        with nav_col2:
            if st.button("🩺 Clinical Decision", use_container_width=True):
                st.info("Navigate to Clinical Decision Support page via sidebar →")
                
        with nav_col3:
            if st.button("🔬 AI Testing", use_container_width=True):
                st.info("Navigate to Prompt and Model Testing page via sidebar →")

with col2:
    with st.container(border=True):
        st.header("📊 System Status")
        
        try:
            # Get system status using shared functions
            status_data = get_demo_data_status()
            
            if status_data:
                st.metric(
                    label="Database Connection", 
                    value="✅ Connected"
                )
                st.metric(
                    label="Patient Records", 
                    value=format_medical_value(status_data.get('patient_count', 0), 'numeric')
                )
                st.metric(
                    label="AI Models Available", 
                    value="3 Models"
                )
            else:
                st.warning("System status check in progress...")
                
        except Exception as e:
            st.error(f"Status check error: {e}")
    
    # Corporate Standard info panel
    with st.container(border=True):
        st.header("💡 Style Guide Info")
        
        st.markdown("""
        **Target Users:**
        - Conservative healthcare organizations  
        - Regulatory compliance environments
        - Traditional enterprise IT departments
        - Clinical staff preferring familiar interfaces
        
        **Key Benefits:**
        - Zero third-party dependencies
        - Maximum update compatibility
        - Professional corporate appearance
        - Proven, stable design patterns
        """)

# Application comparison section
st.markdown("---")

with st.container(border=True):
    st.header("🎨 Style Comparison")
    
    comp_col1, comp_col2, comp_col3 = st.columns(3)
    
    with comp_col1:
        st.markdown("""
        **🔵 Corporate Standard** *(Current)*
        - Native Streamlit only
        - Professional blue theme  
        - Bordered containers
        - Maximum stability
        """)
        st.success("✅ Currently Viewing")
    
    with comp_col2:
        st.markdown("""
        **⚫ Modern Minimalist**
        - Contemporary design
        - Horizontal navigation
        - Spacious card layout
        - Premium feel
        """)
        if st.button("View Minimalist", key="view_minimalist"):
            st.info("🌐 Open http://localhost:8502 to view Modern Minimalist style")
    
    with comp_col3:
        st.markdown("""
        **🟡 Data-Dense Powerhouse**
        - Dark theme dashboard
        - Draggable components
        - High information density
        - Expert-focused interface
        """)
        if st.button("View Powerhouse", key="view_powerhouse"):
            st.info("🌐 Open http://localhost:8503 to view Data-Dense Powerhouse style")

# Footer with version and timestamp
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("**Style:** Corporate Standard")

with footer_col2:
    st.markdown(f"**Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

with footer_col3:
    st.markdown("**Version:** v1.0.0")

# Sidebar content - Corporate Standard uses full sidebar for navigation
with st.sidebar:
    st.markdown("### 🏥 Healthcare AI Demo")
    st.markdown("#### Corporate Standard Style")
    
    st.markdown("---")
    
    st.markdown("""
    **Navigation Instructions:**
    
    Use the pages in this sidebar to navigate through the application. Each page demonstrates the same functionality with Corporate Standard styling.
    
    **Pages Available:**
    - 🏥 Data Foundation
    - 🩺 Clinical Decision Support  
    - 🔬 Prompt and Model Testing
    - 📊 Population Health Analytics
    - 💰 Cost Analysis
    - 💊 Medication Safety
    - 📈 Quality Metrics
    - 🤖 AI Model Performance
    - 📋 Demo Guide
    """)
    
    st.markdown("---")
    
    # Style switching options
    st.markdown("### 🎨 Compare Styles")
    
    if st.button("🌐 Modern Minimalist", use_container_width=True):
        st.info("Open http://localhost:8502")
        
    if st.button("⚡ Data-Dense Powerhouse", use_container_width=True):
        st.info("Open http://localhost:8503")
    
    st.markdown("---")
    
    # Quick system info
    st.markdown("### ℹ️ System Info")
    st.markdown(f"**Port:** 8501")
    st.markdown(f"**Style:** Corporate")
    st.markdown(f"**Components:** Native Only")
    
    # Show shared backend status
    try:
        show_ai_processing_status("complete", "Backend systems ready")
    except:
        st.info("🔄 Backend initializing...")
