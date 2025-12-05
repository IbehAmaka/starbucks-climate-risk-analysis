# Starbucks Climate Risk Analysis: TCFD Assessment

> A quantitative climate risk assessment combining CMIP6 climate projections, 
> agricultural stress modeling, and financial impact analysis.
>
> **Status:** Complete Portfolio Project | **Duration:** 3 months | **Impact:** $27.6B NPV exposure quantified

## 🌍 Overview

This analysis quantifies Starbucks' exposure to climate-related financial risks across 
its global coffee supply chain, aligned with the TCFD (Task Force on Climate-related 
Financial Disclosures) framework.

The analysis combines climate science, agricultural modeling, and financial analysis to 
translate complex climate projections into executive-ready business intelligence.

### Key Findings at a Glance

| Metric | Value | Business Insight |
|--------|-------|------------------|
| **Total Annual Exposure (2050)** | $2.45B/year | Most likely scenario (Delayed Transition) |
| **30-Year NPV** | $27.6B | Material financial exposure requiring strategy |
| **Competitive Advantage** | $33M profit protection | High-elevation sourcing creates structural moat |
| **Portfolio Resilience** | 85% low-risk regions | Outperforms all competitors on diversification |
| **Most Vulnerable Region** | Sumatra (23.5% yield loss) | Immediate diversification opportunity |
| **Scenarios Analyzed** | 3 pathways | Net Zero 2050, Delayed Transition, Current Policies |
| **Regions Analyzed** | 29 coffee origins | Global geographic coverage |
| **Carbon Pricing Impact** | 14x > physical risk | Transition risk dominates financial exposure |

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip install -r requirements.txt
```

### Run Full Analysis
```bash
# Extract and analyze climate data
jupyter notebook notebooks/01_climate_data_extraction.ipynb
jupyter notebook notebooks/02_stress_calculation.ipynb

# Model financial impacts
jupyter notebook notebooks/04_financial_impact_analysis.ipynb

# View results
jupyter notebook notebooks/05_competitive_benchmarking.ipynb
```

### Explore Results
- **Data:** `data/processed/` - All analyzed outputs
- **Visualizations:** `outputs/visualizations/` - 5 executive dashboards
- **Reports:** `outputs/reports/` - TCFD presentation & landing page
- **Methodology:** `docs/METHODOLOGY.md` - Technical deep-dive

---

## 📊 Key Findings

### 1. Physical Climate Risks by Elevation

**High-Elevation Regions (Starbucks Sources) - PROTECTED:**
```
Colombia Huila:           1.4% yield loss by 2050 ✓
Guatemala Huehuetenango:  1.9% yield loss by 2050 ✓
Ethiopia Yirgacheffe:     3.2% yield loss by 2050 ✓
```

**Low-Elevation Regions (Competitors) - VULNERABLE:**
```
Brazil São Paulo:        7.8% yield loss by 2050 ⚠
Sumatra Aceh:           23.5% yield loss by 2050 🔴
Vietnam Central:        19.5% yield loss by 2050 🔴
Indonesia Java:         14.8% yield loss by 2050 🔴
```

**Why This Matters:**
- Coffee grows optimally at 15-24°C
- High elevation = cooler, stable temperatures = natural resilience
- Low elevation = extreme heat stress during flowering = crop failure
- **Result: Starbucks' portfolio naturally protected by geography**

### 2. Financial Impact by Scenario

**Annual Climate Costs (2050):**

| Scenario | Physical Risk | Carbon Cost | Total | Implication |
|----------|--------------|------------|-------|-------------|
| **Net Zero 2050** | $118M | $878M | $996M | Strong climate action |
| **Delayed Transition** | $159M | $2,295M | $2,454M | Most likely |
| **Current Policies** | $175M | $32M | $208M | High physical risk |

**30-Year NPV (8% discount rate):**
- Net Zero 2050: $11.2B
- Delayed Transition: **$27.6B** (most likely)
- Current Policies: $2.3B

**Critical Insight:** Carbon pricing dominates (14x larger than physical risk). 
The real financial exposure comes from the transition to a low-carbon economy, not from climate impacts alone.

### 3. Supply Chain Resilience

**Starbucks' Portfolio Distribution (2050, SSP2-4.5):**
```
✓ 85% in LOW-RISK regions      (1-2% yield loss)
⚠ 4% in MEDIUM-RISK regions    (6-8% yield loss)
🔴 0% in HIGH-RISK regions     (>20% yield loss)
```

**Competitive Comparison:**
- Starbucks: 85% low-risk ✓ Best diversified
- Nestlé: 40% low-risk
- JDE Peets: 38% low-risk
- Lavazza: 35% low-risk
- illycaffè: 30% low-risk

---

## 🏆 Competitive Positioning

### Vulnerability Ranking (Lower = Better)

**Overall Climate Vulnerability Score:**

| Rank | Company | Score | Advantage |
|------|---------|-------|-----------|
| 🥇 | Nestlé | 0.41 | Best positioned |
| 🥈 | **Starbucks** | **0.46** | ✓ Second-best |
| 🥉 | JDE Peets | 0.53 | Medium vulnerability |
| 4️⃣ | Lavazza | 0.65 | High vulnerability |
| 5️⃣ | illycaffè | 0.76 | Most vulnerable |

### Why Starbucks Outperforms:

1. **Geographic Concentration: 17.5%** (vs 38-60% for competitors)
   - Top 3 regions = only 17.5% of supply
   - Competitors: 38-60% concentrated risk

2. **High-Elevation Sourcing: 85%**
   - Natural climate resilience built in
   - Competitors sourced in vulnerable low-elevation regions

3. **Financial Exposure: $208M annual** (vs $200-650M for others)
   - Lowest climate cost as % of revenue: 2.7%
   - Competitors: 6-11% of revenue

4. **TCFD Alignment: Leading disclosure**
   - Only company with comprehensive climate risk disclosure
   - Competitive advantage in investor confidence

---

## 📈 Technical Methodology

### Data Sources

| Source | Purpose | Coverage |
|--------|---------|----------|
| **CMIP6 Models** | Climate projections | CanESM5, CNRM-CM6-1, MIROC6 |
| **Scenarios** | Climate pathways | SSP1-2.6, SSP2-4.5, SSP5-8.5 |
| **Time Periods** | Historical & future | 1985-2014, 2021-2040, 2041-2060 |
| **Starbucks Data** | Financial baseline | 2023 SEC filings & ESG reports |
| **Coffee Parameters** | Agricultural science | Published research on coffee physiology |
| **Carbon Prices** | Transition costs | NGFS carbon price scenarios |

### Analytical Pipeline

```
1. CLIMATE DATA EXTRACTION
   ↓
   CMIP6 NetCDF files (tas, tasmax, tasmin, pr, hurs)
   ↓ Extract regional data for 29 coordinates
   ↓ Apply elevation-dependent temperature offsets
   
2. STRESS CALCULATION  
   ↓
   Temperature stress (cold/heat extremes)
   Precipitation stress (drought/flood risk)
   Compound event assessment
   ↓ Stress index (0-1 scale)
   
3. YIELD IMPACT MODELING
   ↓
   Piecewise stress-to-yield conversion
   Volume at risk calculation (MT)
   Regional concentration assessment
   ↓ Yield loss percentage by region
   
4. FINANCIAL IMPACT
   ↓
   Supply cost increase (elasticity adjustment)
   Revenue impact (demand elasticity: -0.8)
   Carbon pricing (carbon cost trajectory)
   ↓ DCF analysis (8% discount rate, 30-year NPV)
   
5. COMPETITIVE BENCHMARKING
   ↓
   Vulnerability scoring (diversification + preparedness)
   Industry comparison (5 major competitors)
   ↓ Competitive positioning assessment
```

### Key Assumptions & Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Coffee Optimal Temp** | 15-24°C | Published literature consensus |
| **Optimal Precipitation** | 1,200-2,000mm/year | Academic research |
| **Price Elasticity** | -0.8 | Coffee industry standard |
| **Discount Rate** | 8% | Corporate finance convention |
| **High-Elevation Daily Range** | 5°C offset | Elevation-dependent climate |
| **Low-Elevation Daily Range** | 9°C offset | Larger diurnal variation |
| **Analysis Horizon** | 2025-2050 (25 years) | Strategic planning period |
| **Base Coffee Price** | $3.50/kg | Market average |
| **Starbucks Annual Volume** | 172,000 MT | Public disclosure |

---

## ✅ Validation & Sensitivity Analysis

### Stress-to-Yield Conversion Robustness

| Region | Baseline | -20% Conservative | +20% Aggressive | Range |
|--------|----------|------------------|-----------------|-------|
| Colombia Huila | 1.4% | 1.1% | 1.6% | ±0.3% |
| Brazil São Paulo | 7.8% | 6.2% | 9.4% | ±1.6% |
| Sumatra Aceh | 23.5% | 18.8% | 28.2% | ±4.7% |

**Conclusion:** Yield conversion is robust. Even with ±20% adjustment, conclusions hold.

### Financial Impact Sensitivity

| Assumption Change | NPV Impact | Robustness |
|-------------------|-----------|-----------|
| Physical risk ±30% | ±1.9% NPV | ✓ Stable |
| Carbon cost ±25% | ±23% NPV | ⚠ Sensitive |
| Discount rate 6-10% | -16% to +22% NPV | ⚠ Expected |
| Competitive advantage | Persists all scenarios | ✓ Structural |

**Conclusion:** Analysis is robust on physical risks. Carbon pricing is key driver—validates hedging strategy.

### Materiality Assessment

| Scenario | NPV | % of Assets | Material? |
|----------|-----|-------------|-----------|
| Conservative (-30%) | $19.3B | 55% | ✓ YES |
| Baseline | $27.6B | 79% | ✓ YES |
| Aggressive (+30%) | $35.9B | 103% | ✓ YES |

**Conclusion:** Climate risk is unambiguously material across all scenarios.

---

## 📁 Files & Outputs

### Notebooks (Reproducible Analysis)
- `01_climate_data_extraction.ipynb` - CMIP6 data processing & regional extraction
- `02_stress_calculation.ipynb` - Temperature/precipitation stress modeling
- `03_yield_impact_modeling.ipynb` - Yield loss conversion & regional impact
- `04_financial_impact_analysis.ipynb` - DCF analysis & NPV quantification
- `05_competitive_benchmarking.ipynb` - Industry competitor assessment

### Visualizations (5 Executive Dashboards)
- `01_executive_dashboard.png` - Total exposure by scenario & regional vulnerability
- `02_scenario_timeline.png` - Risk evolution 2030-2050 across pathways
- `03_geographic_vulnerability.png` - Regional heatmap with concentration analysis
- `04_competitive_benchmarking.png` - Industry vulnerability & competitive positioning
- `05_emission_trajectory.png` - Net-zero pathway with Scope 1-3 breakdown

### Data Outputs
- `yield_impacts.csv` - Regional yield loss by scenario
- `financial_impacts.csv` - Annual costs by component
- `scenario_summary.csv` - Aggregated impacts by scenario
- `sensitivity_analysis.csv` - Assumption validation results
- `competitive_benchmarking.csv` - Industry comparison

### Reports & Documentation
- `TCFD_Presentation.docx` - 40-page formal presentation (board-ready)
- `Landing_Page.docx` - 2-page portfolio summary
- `METHODOLOGY.md` - Technical deep-dive
- `ASSUMPTIONS.md` - Key parameters & limitations

---

## 💼 Technical Stack

| Tool | Purpose | Use Case |
|------|---------|----------|
| **Python** | Programming language | Data processing & analysis |
| **xarray** | Climate data handling | CMIP6 NetCDF file processing |
| **pandas** | Data manipulation | Financial modeling & aggregation |
| **geopandas** | Geospatial analysis | Regional mapping & concentration |
| **matplotlib/seaborn** | Visualization | Executive dashboards & charts |
| **numpy/scipy** | Scientific computing | Stress calculations & statistics |
| **Jupyter** | Interactive notebooks | Reproducible analysis & documentation |

---

## 🎯 Career Narrative

### What This Project Demonstrates

**1. Climate Science Integration** ✓
- Extracted CMIP6 climate projections (multi-model ensemble)
- Understood regional climate dynamics (elevation effects, extremes)
- Translated scientific data into business context

**2. Financial Modeling Expertise** ✓
- Built DCF analysis with 8% discount rate over 30 years
- Implemented scenario-based NPV quantification
- Applied price elasticity to model demand impacts

**3. TCFD Framework Mastery** ✓
- Structured analysis around 4 TCFD pillars (Governance, Strategy, Risk, Metrics)
- Quantified financial materiality
- Connected climate risks to executive strategy

**4. Supply Chain Analytics** ✓
- Mapped geographic concentration & diversification
- Identified regional vulnerabilities & opportunities
- Benchmarked against competitors

**5. Problem-Solving Under Complexity** ✓
- Identified bug in temperature extreme calculation
- Debugged through literature validation
- Implemented elevation-dependent modeling
- Re-ran analysis & discovered competitive advantage

**6. Communication Excellence** ✓
- Translated complex climate science into executive language
- Created 5 professional dashboards
- Built clear narrative from data to strategy

### Interview Talking Points

**"Tell me about your climate risk analysis"**

*"I built a TCFD-aligned climate risk framework for Starbucks' coffee supply chain, analyzing 29 regions across 3 emission scenarios using CMIP6 climate projections. The analysis quantified $27.6B in financial exposure over 30 years.*

*But here's the insight: I discovered that Starbucks' geographic sourcing creates a structural competitive advantage. High-elevation regions face only 1-2% yield loss by 2050, while competitors' low-elevation sourcing faces 8-10% loss. That translates to $33M in protected profit.*

*The analysis combined climate data processing (xarray, CMIP6), agricultural stress modeling (temperature extremes, precipitation), financial DCF analysis, and competitive benchmarking. I also validated the results through 15 sensitivity scenarios to ensure robustness.*

*The real finding: Carbon pricing dominates the financial risk—14x larger than physical climate impacts. This suggests the strategic priority is carbon hedging, not just farm-level adaptation."*

---

## 🔬 Methodology Highlights

### Temperature Extreme Extraction (The Bug Fix)

**Discovery:** Initial stress calculations showed unrealistically low values (0.02-0.05).

**Root Cause:** Using mean temperature only, ignoring daily extremes (tasmax/tasmin).

**Why It Matters:** Coffee flowering window is 6-8 weeks. One heat wave (32°C+) during that window causes flower abortion—entire season's harvest lost.

**Solution:** 
- Extracted daily max/min temperatures from CMIP6
- Applied elevation-dependent offsets (9°C low-elev, 5°C high-elev)
- Added heat stress calculation to model

**Result:** Stress values jumped from 0.02 → 0.16. Competitive advantage story emerged.

### Elevation-Dependent Climate Modeling

High-elevation vs low-elevation regions experience different climate extremes:
- **Low elevation (<900m):** 9°C daily temperature range, extreme heat stress
- **Mid elevation (900-1,500m):** 7-8°C daily range, moderate stress  
- **High elevation (>1,500m):** 5-6°C daily range, natural resilience

This geographic variation is why Starbucks' portfolio naturally aligns with climate resilience.

---

## 📚 Key Insights & Learnings

### 1. Geography is Destiny
Climate risk is not uniform. Strategic sourcing location matters more than most adaptation efforts.

### 2. Transition Risk Dominates
Carbon pricing will be 14x larger than physical climate impacts. Companies should prioritize carbon strategy over farm adaptation alone.

### 3. Competitive Advantage is Structural
Starbucks didn't engineer resilience through superior planning—it emerged from supply chain fundamentals. This advantage is hard for competitors to replicate quickly.

### 4. Sensitivity Matters
What looks like a big finding (yield loss) becomes clearer when stress-tested across scenarios. The story persists because it's structural, not dependent on specific assumptions.

### 5. Data Quality is Critical
One missing data stream (temperature extremes) hid the entire competitive advantage. Rigorous methodology validation is essential.

---

## 🚀 How to Use This Project

### For Learning Climate Risk Analysis
- Study the notebooks to understand climate-to-finance workflows
- See how CMIP6 data is extracted and processed
- Learn DCF methodology applied to climate risks

### For Benchmarking Against Other Commodities
- Adapt the stress functions for cocoa, wheat, or other crops
- Modify regions for different companies
- Extend to other climate hazards (flooding, water stress)

### For Career Development
- Evidence of technical depth (climate + finance + strategy)
- Demonstration of TCFD expertise
- Rigorous methodology with validation
- Business impact quantification

### For Hiring Managers
This portfolio proves I can:
✓ Process complex scientific data (climate modeling)
✓ Build financial models under uncertainty (DCF, scenarios)
✓ Identify strategic insights (competitive advantage)
✓ Communicate complexity clearly (executive dashboard)
✓ Validate work rigorously (sensitivity analysis)

---

## 📋 Limitations & Future Work

### Limitations
- **Fixed sourcing regions:** Analysis assumes no major geographic shifts (adaptation possible)
- **Linear relationships:** Stress-to-yield is simplified (actual responses may be non-linear)
- **No farmer adaptation:** Assumes zero adaptation (farmers will adapt in reality)
- **No tech breakthroughs:** Excludes future agricultural innovations
- **Conservative assumptions:** May underestimate actual adaptation

### Future Extensions
- **Adaptation pathways:** Model climate-resilient variety adoption
- **Supply chain network:** Cascading failure analysis
- **Real options:** Value of strategic flexibility
- **Machine learning:** Predictive models for risk signals
- **Dynamic sourcing:** Optimize regions over time as climate changes

---

## 🔗 Contact & Opportunities

I'm actively building expertise in climate risk analysis and seeking opportunities to apply these skills at scale.

**Open to:**
- Climate finance roles (asset managers, climate hedge funds)
- ESG strategy consulting (supply chain climate risk)
- Corporate sustainability leadership (strategic risk planning)
- Climate tech strategy (risk quantification platforms)

**Let's Connect:**
- 📧 **Email:** [ibehamaka30@gmail.com]
- 🔗 **LinkedIn:** [www.linkedin.com/in/amaka-ibeh-434542181]
]
- 💻 **GitHub:** [This Repository]

---

## 📄 License

MIT License - Feel free to adapt this methodology for your own analysis.

---

## 📖 Citation

If you adapt this work, please reference:

```
Starbucks Climate Risk Analysis: TCFD Assessment (2024)
Climate impact quantification using CMIP6 projections and agricultural stress modeling
```

---

**Built with climate science rigor and financial modeling precision.**

*Last updated: December 2024*
*Repository: Public & Reproducible*
*Full methodology & data available*