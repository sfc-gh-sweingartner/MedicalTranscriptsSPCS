# Healthcare AI Demo - Complete Deployment Guide

A comprehensive Healthcare AI demonstration showcasing how Snowflake's AI capabilities can transform medical notes into actionable clinical insights. This solution demonstrates real-world applications of AI in healthcare including clinical decision support, population health analytics, cost analysis, and medical education.

## 🏥 Overview

This Healthcare AI Demo provides:

- **🩺 Clinical Decision Support** - AI-powered differential diagnosis and treatment recommendations
- **📊 Population Health Analytics** - Pattern analysis and care optimization across patient cohorts
- **🔬 Medical Research** - Automated literature analysis and research acceleration  
- **🎓 Medical Education** - Teaching case generation and assessment materials
- **💰 Cost Analysis** - Healthcare cost prediction and optimization
- **💊 Medication Safety** - Drug interaction and safety analysis
- **📈 Quality Metrics** - Care quality assessment and improvement
- **🤖 AI Model Performance** - Model testing and prompt optimization

**⚠️ Important:** This is a demonstration system for educational and showcase purposes only. Not for clinical use.

## 🏗️ Architecture

### Database Components
- **PMC_PATIENTS** - 167K+ medical case studies from PMC literature
- **HEALTHCARE_DEMO** - Analysis tables, AI processing procedures, and demo scenarios

### Application Components  
- **Streamlit Application** - Multi-page web interface for healthcare professionals
- **AI Processing Engine** - Batch and real-time analysis using Snowflake Cortex AI
- **Connection Helper** - Works in both local development and Snowflake environments

## 🚀 Quick Deployment

### Prerequisites

1. **Snowflake Account** with:
   - Cortex AI features enabled
   - ACCOUNTADMIN or sufficient privileges for database creation
   - Compute warehouse access

2. **Python Environment**:
   - Python 3.11+ (required for Snowflake stored procedures)
   - pip package manager

3. **Development Setup**:
   - Git repository access
   - Text editor or IDE

### Option 1: Automated Deployment (Recommended)

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd MedicalTranscripts
   ```

2. **Get the PMC Patient Data**:
   The PMC-Patients.csv file (584MB, 167K+ medical cases) is not included in this Git repository.
   
   Contact **stephen.weingartner@snowflake.com** to request the dataset. You can either:
   - Receive the CSV file to place at: `Data/PMC-Patients.csv`
   - Request a direct Snowflake data share (preferred)

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Snowflake Connection**:
   Create `~/.snowflake/config.toml`:
   ```toml
   default_connection_name = "healthcare_demo"

   [connections.healthcare_demo]
   account = "your-account-identifier"
   user = "your-username"
   password = "your-password"
   role = "ACCOUNTADMIN"  # or role with database creation privileges
   warehouse = "your-warehouse"
   ```

5. **Run Complete Deployment**:
   ```bash
   python scripts/deploy_healthcare_demo.py
   ```

   This automated script will:
   - ✅ Create PMC_PATIENTS database and load patient data
   - ✅ Create HEALTHCARE_DEMO database with all analysis tables
   - ✅ Install batch processing procedures with AI integration
   - ✅ Set up demo scenarios and reference data
   - ✅ Configure Cortex Search for fast patient retrieval
   - ✅ Validate the complete installation

5. **Launch the Application**:
   ```bash
   streamlit run src/streamlit_main.py
   ```

### Option 2: Manual Deployment

If you prefer to run the setup manually:

1. **Setup PMC_PATIENTS Database**:
   ```bash
   snowsql -f sql/00_setup_pmc_patients_database.sql
   # Then upload CSV: PUT file:///path/to/Data/PMC-Patients.csv @PMC_DATA_STAGE;
   # And load data using the COPY INTO commands in the SQL file
   ```

2. **Setup HEALTHCARE_DEMO Database**:
   ```bash
   snowsql -f sql/01_create_database_objects.sql
   snowsql -f sql/02_create_subset_and_new_tables.sql
   snowsql -f sql/03_create_batch_processing_procedure.sql
   ```

3. **Launch Streamlit**:
   ```bash
   streamlit run src/streamlit_main.py
   ```

## 📁 Project Structure

```
MedicalTranscripts/
├── README.md                                    # This deployment guide
├── requirements.txt                             # Python dependencies
├── Data/
│   └── PMC-Patients.csv                        # Medical case studies dataset (167K+ records)
├── sql/                                        # Database setup scripts
│   ├── 00_setup_pmc_patients_database.sql     # PMC patients database & table
│   ├── 01_create_database_objects.sql         # Core healthcare demo database  
│   ├── 02_create_subset_and_new_tables.sql    # Additional analysis tables
│   └── 03_create_batch_processing_procedure.sql # AI batch processing procedures
├── scripts/                                   # Deployment automation
│   ├── deploy_healthcare_demo.py              # Complete deployment script
│   └── setup_pmc_database.py                  # PMC database setup only
├── src/                                       # Streamlit application
│   ├── streamlit_main.py                      # Main app entry point
│   ├── connection_helper.py                   # Snowflake connection management
│   └── pages/                                 # Individual demo pages
│       ├── 1_🏥_Data_Foundation.py            # Dataset exploration
│       ├── 2_🩺_Clinical_Decision_Support.py  # AI-powered diagnosis
│       ├── 3_🔬_Prompt_and_Model_Testing.py   # Real-time AI testing
│       ├── 4_📊_Population_Health_Analytics.py # Cohort analysis
│       ├── 5_💰_Cost_Analysis.py              # Healthcare cost prediction
│       ├── 6_💊_Medication_Safety.py          # Drug interaction analysis
│       ├── 7_📈_Quality_Metrics.py            # Care quality assessment
│       ├── 8_🤖_AI_Model_Performance.py       # Model performance testing
│       └── 9_📋_Demo_Guide.py                 # Presentation guide
└── baseline_results/                          # AI model benchmarking data
    ├── baseline_pre_8k.csv
    └── baseline_post_8k.csv
```

## 🎯 Demo Scenarios

The application includes pre-configured demo scenarios:

1. **Complex Diagnostic Case** - 66-year-old with seizures and cardiac arrhythmia
2. **Pediatric Rare Disease** - 11-year-old with multicentric peripheral ossifying fibroma  
3. **High-Cost Patient Analysis** - Patient with multiple procedures and complications

Each scenario demonstrates different AI capabilities and is optimized for 5-minute presentations.

## 🔧 Configuration Options

### Snowflake Environment Variables
```bash
export SNOWFLAKE_ACCOUNT="your-account"
export SNOWFLAKE_USER="your-username"
export SNOWFLAKE_PASSWORD="your-password"
export SNOWFLAKE_ROLE="your-role"
export SNOWFLAKE_WAREHOUSE="your-warehouse"
```

### Streamlit Configuration
Create `.streamlit/config.toml`:
```toml
[server]
port = 8501
enableCORS = false

[theme]
primaryColor = "#0066CC"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

## 🧪 Testing & Validation

### Verify Installation
```bash
python scripts/validate_deployment.py
```

This will check:
- ✅ Database connectivity
- ✅ Required tables and data
- ✅ Cortex AI functionality  
- ✅ Stored procedures
- ✅ Demo scenarios

### Run Sample Analyses
```sql
-- Test AI analysis
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'llama3.1-8b', 
    'Analyze this patient case: ' || PATIENT_NOTES
) FROM PMC_PATIENTS.PMC_PATIENTS.PMC_PATIENTS LIMIT 1;

-- Test patient search
SELECT SNOWFLAKE.CORTEX.SEARCH(
    'patient_search_service',
    'chest pain shortness breath'
) LIMIT 5;
```

## 🌐 Deployment Environments

### Local Development
- Runs on localhost:8501
- Connects to Snowflake via config.toml
- Full development and testing capabilities

### Streamlit in Snowflake (SiS)
- Deploy directly to Snowflake environment
- Native integration with Cortex AI
- No external dependencies or configuration needed

#### Streamlit in Snowflake: required Packages
When deploying the Streamlit app inside Snowflake, add these packages in the app editor:

1. Open the Streamlit app in Snowflake and click the Packages dropdown in the editor.
2. Add the following packages:
   - snowflake.core
   - plotly
3. Save, then run/redeploy the app.

### Production Deployment
- Container deployment options available
- Environment variable configuration
- Load balancing and scaling considerations

## 🔒 Security & Compliance

### Data Privacy
- All patient data is de-identified case studies from published literature
- No real patient PHI or PII included
- Designed with HIPAA-ready architecture patterns

### Access Control
- Role-based access control (RBAC) 
- Database-level permissions
- Secure connection handling

### Audit & Monitoring
- All AI analyses logged in `REALTIME_ANALYSIS_LOG`
- Processing metrics tracked in `PROCESSING_STATUS`
- User activity monitoring capabilities

## 📊 Performance Optimization

### Pre-computed Insights
- Common analyses pre-processed for speed
- Hybrid approach: fast retrieval + real-time AI

### Caching Strategy
- Streamlit connection caching
- AI response caching for repeated queries
- Session state management

### Scaling Recommendations
- Warehouse sizing guidelines
- Concurrent user considerations
- Resource monitoring best practices

## 🐛 Troubleshooting

### Common Issues

1. **Connection Errors**
   ```
   ❌ Failed to connect to Snowflake
   ```
   - Verify config.toml credentials
   - Check network connectivity and firewall settings
   - Ensure warehouse is running

2. **Missing Data**
   ```
   ❌ PMC_PATIENTS table empty
   ```
   - Re-run CSV loading: `python scripts/setup_pmc_database.py`
   - Check file path to PMC-Patients.csv
   - Verify stage permissions

3. **AI/Cortex Errors**
   ```
   ❌ Cortex AI not available
   ```
   - Ensure Cortex features are enabled on your account
   - Check role permissions for AI functions
   - Verify warehouse has AI capabilities

4. **Streamlit Issues**
   ```
   ❌ Page not loading
   ```
   - Check Python version (3.11+ required)
   - Verify all dependencies installed: `pip install -r requirements.txt`
   - Review Streamlit logs for specific errors

### Getting Help

- **Error Logs**: Check Snowflake query history for detailed error messages
- **Validation Script**: Run `python scripts/validate_deployment.py` for diagnostics
- **Sample Data**: Use the included demo scenarios for testing
- **Documentation**: See inline code comments and docstrings

## 🔄 Updates & Maintenance

### Keeping Current
```bash
git pull origin main
pip install -r requirements.txt --upgrade
python scripts/deploy_healthcare_demo.py --update
```

### Database Maintenance
- Monitor warehouse usage and costs
- Review and archive analysis logs
- Update demo scenarios as needed

## 🤝 Contributing

This is a demonstration project designed for educational and showcase purposes. The codebase provides a foundation for building production healthcare AI applications on Snowflake.

### Development Setup
1. Fork the repository
2. Create feature branches
3. Follow existing code patterns and documentation standards
4. Test thoroughly before submitting changes

## 📄 License

This demonstration project is provided for educational and evaluation purposes. Please review your organization's policies regarding AI tools and patient data before deploying in any healthcare environment.

---

**🏥 Ready to transform healthcare with AI?** 

Start with the automated deployment script and explore the demo scenarios. Each page in the Streamlit application demonstrates different AI capabilities for healthcare professionals.

For questions or support, please refer to the troubleshooting section or contact the development team.

**⚠️ Remember: This is a demonstration system - not for clinical use!**
