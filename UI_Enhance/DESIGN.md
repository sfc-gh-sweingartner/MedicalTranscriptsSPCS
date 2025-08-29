# SiS SPCS Healthcare Demo – Unified Design (GPT + Claude)

## Context
SiS SPCS removes the historic SiS package/version constraints by allowing PyPI packages via External Access Integration and supports modern Streamlit parity on release day. This unlocks a richer, more professional UI/UX, advanced visualization, and real-time interactivity while keeping all data and AI execution in Snowflake.

References:
- SiS vNext PrPr architecture (open-source parity, flex layout, sparklines, management APIs)
- Internal email (SPCS V2 requirements, package management, EAIs)
- Allowed Snowflake channel for Streamlit older environment: `https://repo.anaconda.com/pkgs/snowflake/`

## Objectives
- Elevate the demo from "functional" to "impressive": modern visuals, responsive layouts, polished interactions
- Preserve simplicity for demo flows while offering depth for power users
- Keep security: all data in a single Snowflake DB/schema, HIPAA-ready posture, no cross-script SQL dependencies
- Maintain Python 3.11; use only supported packages when running inside Snowflake runtime

## Design Principles
- Progressive enhancement: core pages remain; visuals and interactions upgrade incrementally
- Minimal cognitive load: strong information hierarchy with cards, sections, and summaries
- Reuse existing pages; prefer editing over creating redundant files. Decommission or move unused files to `TRASH/`
- No interdependent SQL scripts; each script remains runnable stand‑alone

## IA (Information Architecture)
- Landing (`streamlit_main.py`): brand header, quick stats with sparklines, scenario tiles
- Pages (existing):
  - Data Foundation (🏥)
  - Clinical Decision Support (🩺)
  - Prompt & Model Testing (🔬)
  - Population Health Analytics (📊)
  - Cost Analysis (💰)
  - Medication Safety (💊)
  - Quality Metrics (📈)
  - AI Model Performance (🤖)
  - Demo Guide (📋)

## UI/UX Upgrades
1) Navigation
- Add optional horizontal top nav (while keeping Streamlit native pages): `streamlit-option-menu` for polished tabs

2) Visual Hierarchy
- Replace ad-hoc HTML/CSS with reusable card components (e.g., `streamlit-card`) for patient and cohort summaries
- Use consistent palette and spacing; maintain medical disclaimer component

3) Metrics & Trends
- Use Streamlit 1.49+ sparklines in `st.metric` for trend context
- Micro trends per metric group (e.g., readmission rate, high-cost cohort count)

4) Data Grids
- Introduce `streamlit-aggrid` for patient lists and AI results tables with sorting, filtering, selection

5) Charts & Dashboards
- Plotly for clinical timelines, risk gauges, network graphs (medication interactions)
- ECharts for dense dashboards (performance, cohort comparisons)
- Altair for distribution and statistical views

6) Maps
- `streamlit-folium` for geographic health overlays where location data exists (synthetic if needed)

7) Loading/Feedback
- `streamlit-lottie` animations for longer computations
- Non-blocking UI with status toasts and progress indicators

8) Accessibility & Responsiveness
- Prefer built-ins (flex layout) and avoid brittle CSS class hooks

## AI/Analysis UX
- Clinical Decision Support: differential diagnosis tree, risk gauges, medication interaction network, care pathway timeline
- Prompt & Model Testing: side-by-side prompts/models, response grading rubric, cost/time estimates, curated test sets
- Population Analytics: cohort builder, KPI deck with sparklines, outlier detection surfacing rare presentations

## Packages (SiS SPCS)
Core (already present): `streamlit>=1.49`, `pandas`, `numpy`, `plotly`, `altair`, `matplotlib`, `seaborn`, `snowflake.core`

Additional (subject to EAI policy for PyPI):
- Navigation/UI: `streamlit-option-menu`, `streamlit-card`, `streamlit-elements`, `streamlit-toggle-switch`, `streamlit-pills`, `streamlit-autorefresh`, `streamlit-lottie`
- Tables/Charts: `streamlit-aggrid`, `streamlit-echarts`, `streamlit-folium`
- AI UX: `streamlit-chat`, `streamlit-ace`
- Imaging (optional): `pillow`, `opencv-python`, `streamlit-drawable-canvas`

Note: Verify each package against Snowflake EAI allowances and organizational policy before inclusion. For Streamlit-in-Snowflake legacy runtime, restrict to `repo.anaconda.com/pkgs/snowflake/`.

## Security & Ops
- Single DB/schema as per project rule; enforce via connection helper
- No SQL scripts referencing other scripts; keep idempotent, stand‑alone
- External Access Integration required for PyPI; document EAI name and outbound rules
- Version pinning in `pyproject.toml`/`requirements.txt`; align local dev and SiS SPCS

## Non‑Goals
- No clinical deployment features (only demo)
- No overhaul of data model; build atop existing tables and views

## Open Questions
- Which packages are approved for EAI in target account?
- Any branding requirements (logos/colors) beyond Snowflake defaults?

## Acceptance Criteria (Design)
- Visual polish: cards, metrics with trends, professional navigation
- Interactivity: sortable/filterable tables, responsive charts
- Stability: no linter errors; pages load within target thresholds



