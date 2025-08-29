# SiS SPCS Healthcare Demo – Project Plan

This plan merges GPT’s perspective with the earlier plan and prioritizes by impact vs. effort. Work is organized into waves; each wave is shippable and improves demo quality.

## Legend
- Impact: 🔥 High / ⭐ Medium / ✴ Low
- Effort: S (small), M (medium), L (large)
- Type: UI, Viz, Data, AI, Ops

## Wave 0 – Foundations (Week 1)
1. Pin Streamlit 1.49+ and align local + SiS SPCS environments (🔥, S, Ops)
2. Document External Access Integration (EAI) for PyPI usage (🔥, S, Ops)
3. Adopt flex layout and sparklines in key metrics on landing page (🔥, S, UI)
4. Establish reusable card styles and color tokens (🔥, S, UI)

Deliverable: Updated landing visuals with sparklines, consistent cards, parity between dev and SiS SPCS.

## Wave 1 – Navigation & Tables (Weeks 2–3)
1. Add optional top navigation via `streamlit-option-menu` (🔥, S, UI)
2. Introduce `streamlit-aggrid` for patient lists and AI results (🔥, M, Viz)
3. Replace ad-hoc HTML with standardized card components (⭐, S, UI)

Deliverable: Professional nav + interactive, filterable tables.

## Wave 2 – Charts & Dashboards (Weeks 3–4)
1. Plotly risk gauges and clinical timelines (🔥, M, Viz)
2. ECharts dashboard for cohort KPIs (🔥, M, Viz)
3. Altair distributions and uncertainty bands (⭐, S, Viz)

Deliverable: Rich clinical and cohort dashboards with modern visuals.

## Wave 3 – Population Health & Maps (Weeks 4–5)
1. Geographic overlays with `streamlit-folium` (⭐, M, Viz)
2. Cohort builder UX and comparison views (🔥, M, UI)
3. Auto-refresh of population KPIs (⭐, S, UI)

Deliverable: Population health storytelling using cohorts and maps.

## Wave 4 – Clinical Decision Support Enhancements (Weeks 5–6)
1. Differential diagnosis tree visualization (🔥, M, Viz)
2. Medication interaction network graph (🔥, M, Viz)
3. Care pathway timeline with outcomes and alerts (🔥, M, Viz)

Deliverable: High-impact clinician-facing visuals that feel modern and insightful.

## Wave 5 – Prompt & Model Testing UX (Weeks 6–7)
1. Side-by-side prompt/model comparison with grades (🔥, M, AI)
2. Curated test sets and saved experiments (⭐, M, Data)
3. Cost/time estimates per run (⭐, S, AI)

Deliverable: Professional testing bench for prompts and models.

## Wave 6 – Advanced/Optional (Weeks 7–8+)
1. `streamlit-lottie` loading animations and toasts (✴, S, UI)
2. `streamlit-chat` AI consultation interface (⭐, M, AI)
3. Imaging workflows with `streamlit-drawable-canvas` (⭐, L, AI)
4. Telemedicine via `streamlit-webrtc` (✴, L, AI)

Deliverable: Showcase features for extended demos.

## Operational Tasks (Ongoing)
- Ensure SQL scripts remain stand‑alone and idempotent
- Keep a single DB/schema; validate USE statements and connections
- Version pinning in `pyproject.toml`/`requirements.txt`; match SiS SPCS
- Regular cleanup: remove/relocate unused files to `TRASH/`

## Risks & Mitigations
- Package availability via EAI: verify and stage rollouts per environment
- Performance in Snowsight: leverage caching (`st.cache_data`) and reduce query payloads
- Visual regressions: incremental rollout, page-by-page gating

## Success Criteria
- Visually polished landing and key pages
- Interactive tables and dashboards
- Stable performance and clean lints



