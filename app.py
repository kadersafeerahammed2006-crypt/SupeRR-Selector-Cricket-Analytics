"""
SupeRR Selector Season 2 - PressurePlay Cricket Analytics Intelligence Platform
High-End Dark Blue Sports Analytics Design
"""

import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Configure Page
st.set_page_config(
    page_title="PressurePlay Analytics | SupeRR Selector S2",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Bespoke Dark Blue Theme CSS
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hide Default Streamlit Clutter */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Background Canvas */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0A1938 0%, #040916 65%, #02050D 100%) !important;
        color: #E2E8F0;
    }
    
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1400px !important;
    }

    /* Custom Header Bar */
    .header-box {
        background: linear-gradient(135deg, rgba(14, 30, 68, 0.85) 0%, rgba(8, 17, 40, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 16px;
        padding: 24px 32px;
        margin-bottom: 24px;
        box-shadow: 0 20px 40px -15px rgba(2, 6, 23, 0.9), 0 0 20px rgba(56, 189, 248, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        backdrop-filter: blur(12px);
    }
    
    .brand-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        background: linear-gradient(90deg, #FFFFFF 0%, #BAE6FD 50%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .brand-subtitle {
        color: #94A3B8;
        font-size: 0.95rem;
        margin-top: 4px;
        font-weight: 400;
    }
    
    .pill-badge {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-blue {
        background: rgba(14, 165, 233, 0.15);
        color: #38BDF8;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }
    
    .badge-gold {
        background: rgba(245, 158, 11, 0.15);
        color: #FBBF24;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }
    
    .badge-emerald {
        background: rgba(16, 185, 129, 0.15);
        color: #34D399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    .badge-crimson {
        background: rgba(239, 68, 68, 0.15);
        color: #F87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }

    /* KPI Hero Cards */
    .kpi-container {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 16px;
        margin-bottom: 24px;
    }
    
    .kpi-card {
        background: linear-gradient(145deg, rgba(15, 31, 71, 0.75) 0%, rgba(9, 19, 44, 0.9) 100%);
        border: 1px solid rgba(56, 189, 248, 0.18);
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 8px 25px rgba(2, 6, 23, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transition: transform 0.2s ease, border-color 0.2s ease;
        position: relative;
        overflow: hidden;
    }
    
    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.4);
    }
    
    .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #0284C7, #38BDF8);
    }
    
    .kpi-card.gold::after {
        background: linear-gradient(90deg, #D97706, #FBBF24);
    }
    
    .kpi-card.crimson::after {
        background: linear-gradient(90deg, #DC2626, #F87171);
    }
    
    .kpi-card.emerald::after {
        background: linear-gradient(90deg, #059669, #34D399);
    }
    
    .kpi-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
    }
    
    .kpi-value {
        font-size: 1.85rem;
        font-weight: 700;
        color: #F8FAFC;
        font-family: 'JetBrains Mono', monospace;
        line-height: 1.2;
    }
    
    .kpi-delta {
        font-size: 0.8rem;
        margin-top: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Card Panels */
    .panel-box {
        background: linear-gradient(145deg, rgba(14, 30, 68, 0.75) 0%, rgba(7, 16, 38, 0.9) 100%);
        border: 1px solid rgba(56, 189, 248, 0.16);
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(2, 6, 23, 0.6);
    }
    
    .panel-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
        letter-spacing: -0.3px;
    }

    /* Leaderboard Card List */
    .leader-row {
        background: rgba(10, 23, 54, 0.6);
        border: 1px solid rgba(56, 189, 248, 0.12);
        border-radius: 10px;
        padding: 12px 18px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: all 0.2s ease;
    }
    
    .leader-row:hover {
        background: rgba(14, 33, 76, 0.85);
        border-color: rgba(56, 189, 248, 0.35);
        transform: translateX(4px);
    }
    
    .rank-circle {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.9rem;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .rank-1 {
        background: linear-gradient(135deg, #F59E0B, #D97706);
        color: #000;
        box-shadow: 0 0 12px rgba(245, 158, 11, 0.4);
    }
    
    .rank-2 {
        background: linear-gradient(135deg, #94A3B8, #64748B);
        color: #000;
    }
    
    .rank-3 {
        background: linear-gradient(135deg, #B45309, #78350F);
        color: #FFF;
    }
    
    .rank-other {
        background: rgba(15, 31, 71, 0.9);
        color: #94A3B8;
        border: 1px solid rgba(56, 189, 248, 0.2);
    }

    /* Modern Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(10, 22, 51, 0.85);
        padding: 8px;
        border-radius: 14px;
        border: 1px solid rgba(56, 189, 248, 0.18);
        margin-bottom: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 10px;
        color: #94A3B8;
        padding: 10px 22px;
        font-weight: 600;
        font-size: 0.92rem;
        border: none;
        transition: all 0.2s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #F8FAFC;
        background: rgba(56, 189, 248, 0.08);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
    }
    
    /* Comparison Fighter Card */
    .vs-card {
        background: linear-gradient(145deg, rgba(14, 30, 68, 0.8) 0%, rgba(8, 18, 42, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 12px 35px rgba(2, 6, 23, 0.7);
    }
    
    .vs-player-name {
        font-size: 1.5rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-top: 10px;
    }
    
    .vs-rating-badge {
        font-size: 2.2rem;
        font-weight: 800;
        font-family: 'JetBrains Mono', monospace;
        color: #38BDF8;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Data Loader
DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "powerbi")

@st.cache_data
def load_all_data():
    bat_rank = pd.read_csv(os.path.join(DATA_DIR, "powerbi_batter_rankings.csv"))
    bowl_rank = pd.read_csv(os.path.join(DATA_DIR, "powerbi_bowler_rankings.csv"))
    bat_perf = pd.read_csv(os.path.join(DATA_DIR, "powerbi_batter_performance.csv"))
    bowl_perf = pd.read_csv(os.path.join(DATA_DIR, "powerbi_bowler_performance.csv"))
    comp_sum = pd.read_csv(os.path.join(DATA_DIR, "powerbi_competition_summary.csv"))
    seas_sum = pd.read_csv(os.path.join(DATA_DIR, "powerbi_season_summary.csv"))
    press_sum = pd.read_csv(os.path.join(DATA_DIR, "powerbi_pressure_summary.csv"))
    rel = pd.read_csv(os.path.join(DATA_DIR, "powerbi_ranking_reliability.csv"))

    batters = pd.merge(bat_rank, bat_perf, on=["player_id", "player_name"]).sort_values("rank")
    bowlers = pd.merge(bowl_rank, bowl_perf, on=["player_id", "player_name"]).sort_values("rank")

    return bat_rank, bowl_rank, bat_perf, bowl_perf, comp_sum, seas_sum, press_sum, rel, batters, bowlers

(
    bat_rank,
    bowl_rank,
    bat_perf,
    bowl_perf,
    comp_sum,
    seas_sum,
    press_sum,
    rel,
    batters,
    bowlers,
) = load_all_data()

# Plotly Theme Helper
def apply_dark_theme(fig, height=360):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=height,
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#94A3B8", size=11),
        margin=dict(t=35, b=25, l=30, r=20),
        xaxis=dict(
            gridcolor="rgba(56, 189, 248, 0.08)",
            linecolor="rgba(56, 189, 248, 0.2)",
            tickfont=dict(color="#94A3B8")
        ),
        yaxis=dict(
            gridcolor="rgba(56, 189, 248, 0.08)",
            linecolor="rgba(56, 189, 248, 0.2)",
            tickfont=dict(color="#94A3B8")
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.28,
            xanchor="center",
            x=0.5,
            font=dict(color="#CBD5E1")
        )
    )
    return fig

# Header Banner
st.markdown("""
<div class="header-box">
    <div>
        <div class="brand-title">
            <span>⚡</span> SupeRR Selector <span style="font-weight: 300; opacity: 0.85;">Season 2</span>
        </div>
        <div class="brand-subtitle">
            PressurePlay Intelligence Engine • Empirical Bayes Multi-Criteria Rating Model
        </div>
    </div>
    <div style="display: flex; gap: 8px;">
        <span class="pill-badge badge-blue">867 Matches</span>
        <span class="pill-badge badge-gold">200,999 Deliveries</span>
        <span class="pill-badge badge-emerald">Empirical Bayes Shrinkage</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Tournament Macro Overview",
    "🏏 Top 10 Batters Leaderboard",
    "🎯 Top 10 Bowlers Leaderboard",
    "⚡ Match Pressure Analytics",
    "⚔️ Head-to-Head Player Comparison"
])

# ==========================================
# TAB 1: TOURNAMENT OVERVIEW
# ==========================================
with tab1:
    tot_deliveries = comp_sum['total_deliveries'].sum()
    tot_matches = comp_sum['total_matches'].sum()
    tot_pressure_deliveries = comp_sum['pressure_deliveries'].sum()
    pressure_pct = (tot_pressure_deliveries / tot_deliveries) * 100
    crit_balls = press_sum[press_sum['category_name'] == 'Critical']['total_deliveries'].values[0]

    # KPI Row
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card">
            <div class="kpi-label">Total Matches</div>
            <div class="kpi-value">{tot_matches}</div>
            <div class="kpi-delta"><span class="pill-badge badge-blue">IPL & T20I</span></div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Total Deliveries</div>
            <div class="kpi-value">{tot_deliveries:,}</div>
            <div class="kpi-delta"><span class="pill-badge badge-blue">100% Granular</span></div>
        </div>
        <div class="kpi-card gold">
            <div class="kpi-label">Pressure Deliveries</div>
            <div class="kpi-value">{tot_pressure_deliveries:,}</div>
            <div class="kpi-delta"><span class="pill-badge badge-gold">Index ≥ 0.40</span></div>
        </div>
        <div class="kpi-card gold">
            <div class="kpi-label">Pressure Share</div>
            <div class="kpi-value">{pressure_pct:.2f}%</div>
            <div class="kpi-delta"><span class="pill-badge badge-gold">High Stakes Load</span></div>
        </div>
        <div class="kpi-card crimson">
            <div class="kpi-label">Critical Deliveries</div>
            <div class="kpi-value">{crit_balls:,}</div>
            <div class="kpi-delta"><span class="pill-badge badge-crimson">7.40% High Hazard</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.3])
    with c1:
        st.markdown('<div class="panel-box"><div class="panel-title">🥧 Pressure Tier Delivery Share</div>', unsafe_allow_html=True)
        press_levels = press_sum[press_sum['dimension_type'] == 'Pressure Level'].copy()
        fig_donut = px.pie(
            press_levels,
            values="total_deliveries",
            names="category_name",
            hole=0.6,
            color="category_name",
            color_discrete_map={
                "Low": "#10B981",
                "Medium": "#38BDF8",
                "High": "#F59E0B",
                "Critical": "#EF4444"
            }
        )
        fig_donut.update_traces(
            textinfo="percent+label",
            textposition="outside",
            marker=dict(line=dict(color="#071126", width=2))
        )
        apply_dark_theme(fig_donut, height=330)
        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="panel-box"><div class="panel-title">📉 Strike Rate Compression: Normal vs Pressure</div>', unsafe_allow_html=True)
        fig_comp = go.Figure()
        fig_comp.add_trace(go.Bar(
            x=comp_sum['competition_group'],
            y=comp_sum['normal_sr'],
            name='Normal Baseline SR',
            marker=dict(color='#3B82F6', line=dict(color='rgba(255,255,255,0.1)', width=1))
        ))
        fig_comp.add_trace(go.Bar(
            x=comp_sum['competition_group'],
            y=comp_sum['pressure_sr'],
            name='Pressure Strike Rate',
            marker=dict(color='#F59E0B', line=dict(color='rgba(255,255,255,0.1)', width=1))
        ))
        apply_dark_theme(fig_comp, height=330)
        fig_comp.update_layout(barmode='group', yaxis_title="Strike Rate")
        st.plotly_chart(fig_comp, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel-box"><div class="panel-title">📈 Historical Evolution Across Seasons (2022–2026)</div>', unsafe_allow_html=True)
    fig_line = px.line(
        seas_sum,
        x="season",
        y="pressure_sr",
        color="competition_group",
        markers=True,
        color_discrete_map={"IPL": "#38BDF8", "T20I": "#818CF8", "Other T20": "#34D399"}
    )
    apply_dark_theme(fig_line, height=300)
    fig_line.update_traces(line=dict(width=3), marker=dict(size=8))
    fig_line.update_layout(yaxis_title="Pressure Strike Rate")
    st.plotly_chart(fig_line, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 2: TOP 10 BATTERS
# ==========================================
with tab2:
    top10_b = batters[batters['is_top_10'] == 1].copy()
    w_sr = (top10_b['pressure_runs'].sum() / top10_b['pressure_balls'].sum()) * 100

    # Batters Hero KPI Row
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card gold">
            <div class="kpi-label">#1 Ranked Batter</div>
            <div class="kpi-value">Brian Bennett</div>
            <div class="kpi-delta"><span class="pill-badge badge-gold">Rating 74.32 (Raw 85.38)</span></div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Top 10 Avg Rating</div>
            <div class="kpi-value">{top10_b['adjusted_rating'].mean():.2f}</div>
            <div class="kpi-delta"><span class="pill-badge badge-blue">Empirical Bayes Shrinkage</span></div>
        </div>
        <div class="kpi-card emerald">
            <div class="kpi-label">Weighted Pressure SR</div>
            <div class="kpi-value">{w_sr:.2f}</div>
            <div class="kpi-delta"><span class="pill-badge badge-emerald">+18.72 pts vs Baseline</span></div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Peak Pressure SR</div>
            <div class="kpi-value">173.17</div>
            <div class="kpi-delta"><span class="pill-badge badge-blue">Cooper Connolly</span></div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Max Clutch Lift</div>
            <div class="kpi-value">+33.91</div>
            <div class="kpi-delta"><span class="pill-badge badge-emerald">Atharwa Taide (+33.91 SR)</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Custom Top 10 Batter Cards
    st.markdown('<div class="panel-box"><div class="panel-title">🏆 Top 10 Batters Under Pressure: Official Rankings</div>', unsafe_allow_html=True)
    
    for idx, r in top10_b.iterrows():
        rk = int(r['rank'])
        rk_class = f"rank-{rk}" if rk <= 3 else "rank-other"
        rk_icon = "🥇" if rk == 1 else ("🥈" if rk == 2 else ("🥉" if rk == 3 else f"#{rk}"))
        diff_badge = f'<span class="pill-badge badge-emerald">{r["strike_rate_diff"]:+.2f} SR</span>' if r['strike_rate_diff'] > 0 else f'<span class="pill-badge badge-crimson">{r["strike_rate_diff"]:+.2f} SR</span>'
        
        st.markdown(f"""
        <div class="leader-row">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div class="rank-circle {rk_class}">{rk_icon}</div>
                <div>
                    <div style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC;">{r['player_name']}</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">{r['competitions']} • {int(r['pressure_balls'])} Pressure Balls • {int(r['pressure_runs'])} Runs</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="text-align: right;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Pressure SR</div>
                    <div style="font-size: 1.1rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; color: #38BDF8;">{r['pressure_strike_rate']:.2f}</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Clutch Surge</div>
                    <div>{diff_badge}</div>
                </div>
                <div style="text-align: right; min-width: 100px;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Adjusted Rating</div>
                    <div style="font-size: 1.35rem; font-weight: 800; font-family: 'JetBrains Mono', monospace; color: #FBBF24;">{r['adjusted_rating']:.2f}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="panel-box"><div class="panel-title">⚡ Pressure SR vs Normal Baseline (Top 10)</div>', unsafe_allow_html=True)
        fig_scatter_bat = px.scatter(
            top10_b,
            x="normal_strike_rate",
            y="pressure_strike_rate",
            size="pressure_runs",
            color="player_name",
            text="player_name",
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig_scatter_bat.add_shape(
            type="line", line=dict(dash="dash", color="rgba(255,255,255,0.4)", width=1.5),
            x0=110, y0=110, x1=180, y1=180
        )
        fig_scatter_bat.update_traces(textposition='top center')
        apply_dark_theme(fig_scatter_bat, height=340)
        fig_scatter_bat.update_layout(showlegend=False, xaxis_title="Normal Strike Rate", yaxis_title="Pressure Strike Rate")
        st.plotly_chart(fig_scatter_bat, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel-box"><div class="panel-title">🎯 Boundary % vs Dot Ball % Under Pressure</div>', unsafe_allow_html=True)
        fig_bar_bat = go.Figure()
        fig_bar_bat.add_trace(go.Bar(
            y=top10_b['player_name'],
            x=top10_b['pressure_boundary_pct'],
            name='Boundary %',
            orientation='h',
            marker_color='#10B981'
        ))
        fig_bar_bat.add_trace(go.Bar(
            y=top10_b['player_name'],
            x=top10_b['pressure_dot_ball_pct'],
            name='Dot Ball %',
            orientation='h',
            marker_color='#EF4444'
        ))
        apply_dark_theme(fig_bar_bat, height=340)
        fig_bar_bat.update_layout(barmode='group', xaxis_title="Percentage (%)")
        st.plotly_chart(fig_bar_bat, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 3: TOP 10 BOWLERS
# ==========================================
with tab3:
    top10_bw = bowlers[bowlers['is_top_10'] == 1].copy()
    w_econ = (top10_bw['pressure_runs_conceded'].sum() * 6) / top10_bw['pressure_legal_balls'].sum()

    # Bowlers Hero KPI Row
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card gold">
            <div class="kpi-label">#1 Ranked Bowler</div>
            <div class="kpi-value">Brad Evans</div>
            <div class="kpi-delta"><span class="pill-badge badge-gold">Rating 71.58 (Raw 89.26)</span></div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Top 10 Avg Rating</div>
            <div class="kpi-value">{top10_bw['adjusted_rating'].mean():.2f}</div>
            <div class="kpi-delta"><span class="pill-badge badge-blue">Empirical Bayes Shrinkage</span></div>
        </div>
        <div class="kpi-card emerald">
            <div class="kpi-label">Weighted Pressure Econ</div>
            <div class="kpi-value">{w_econ:.2f} RPO</div>
            <div class="kpi-delta"><span class="pill-badge badge-emerald">vs 7.82 Tourn Econ</span></div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Elite Run Suppression</div>
            <div class="kpi-value">4.64 RPO</div>
            <div class="kpi-delta"><span class="pill-badge badge-blue">Corbin Bosch</span></div>
        </div>
        <div class="kpi-card crimson">
            <div class="kpi-label">Strike Weapon</div>
            <div class="kpi-value">16 Wkts</div>
            <div class="kpi-delta"><span class="pill-badge badge-crimson">Nuwan Thushara (10.67%)</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Custom Top 10 Bowler Cards
    st.markdown('<div class="panel-box"><div class="panel-title">🏆 Top 10 Bowlers Under Pressure: Official Rankings</div>', unsafe_allow_html=True)
    
    for idx, r in top10_bw.iterrows():
        rk = int(r['rank'])
        rk_class = f"rank-{rk}" if rk <= 3 else "rank-other"
        rk_icon = "🥇" if rk == 1 else ("🥈" if rk == 2 else ("🥉" if rk == 3 else f"#{rk}"))
        diff_badge = f'<span class="pill-badge badge-emerald">{r["economy_diff"]:+.2f} RPO</span>' if r['economy_diff'] > 0 else f'<span class="pill-badge badge-crimson">{r["economy_diff"]:+.2f} RPO</span>'
        
        st.markdown(f"""
        <div class="leader-row">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div class="rank-circle {rk_class}">{rk_icon}</div>
                <div>
                    <div style="font-size: 1.05rem; font-weight: 700; color: #F8FAFC;">{r['player_name']}</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">{r['competitions']} • {int(r['pressure_legal_balls'])} Legal Balls • {int(r['pressure_wickets'])} Wickets</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="text-align: right;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Pressure Economy</div>
                    <div style="font-size: 1.1rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; color: #38BDF8;">{r['pressure_economy']:.2f} RPO</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Run Suppression</div>
                    <div>{diff_badge}</div>
                </div>
                <div style="text-align: right; min-width: 100px;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Adjusted Rating</div>
                    <div style="font-size: 1.35rem; font-weight: 800; font-family: 'JetBrains Mono', monospace; color: #FBBF24;">{r['adjusted_rating']:.2f}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="panel-box"><div class="panel-title">🛡️ Pressure Economy vs Normal Baseline (Top 10)</div>', unsafe_allow_html=True)
        fig_scatter_bowl = px.scatter(
            top10_bw,
            x="normal_economy",
            y="pressure_economy",
            size="pressure_wickets",
            color="player_name",
            text="player_name",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_scatter_bowl.add_shape(
            type="line", line=dict(dash="dash", color="rgba(255,255,255,0.4)", width=1.5),
            x0=4, y0=4, x1=11, y1=11
        )
        fig_scatter_bowl.update_traces(textposition='top center')
        apply_dark_theme(fig_scatter_bowl, height=340)
        fig_scatter_bowl.update_layout(showlegend=False, xaxis_title="Normal Economy Rate (RPO)", yaxis_title="Pressure Economy Rate (RPO)")
        st.plotly_chart(fig_scatter_bowl, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel-box"><div class="panel-title">🔒 Dot Ball % vs Boundary Conceded %</div>', unsafe_allow_html=True)
        fig_bar_bw = go.Figure()
        fig_bar_bw.add_trace(go.Bar(
            y=top10_bw['player_name'],
            x=top10_bw['pressure_dot_ball_pct'],
            name='Dot Ball %',
            orientation='h',
            marker_color='#38BDF8'
        ))
        fig_bar_bw.add_trace(go.Bar(
            y=top10_bw['player_name'],
            x=top10_bw['pressure_boundary_conceded_pct'],
            name='Boundary Conceded %',
            orientation='h',
            marker_color='#EF4444'
        ))
        apply_dark_theme(fig_bar_bw, height=340)
        fig_bar_bw.update_layout(barmode='group', xaxis_title="Percentage (%)")
        st.plotly_chart(fig_bar_bw, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 4: PRESSURE ANALYSIS
# ==========================================
with tab4:
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card crimson">
            <div class="kpi-label">Critical Pressure Load</div>
            <div class="kpi-value">{crit_balls:,} Balls</div>
            <div class="kpi-delta"><span class="pill-badge badge-crimson">7.40% High Hazard</span></div>
        </div>
        <div class="kpi-card crimson">
            <div class="kpi-label">Death Overs Hazard</div>
            <div class="kpi-value">7.80% Wkts</div>
            <div class="kpi-delta"><span class="pill-badge badge-crimson">Peak Phase Hazard</span></div>
        </div>
        <div class="kpi-card gold">
            <div class="kpi-label">Critical Dot Surge</div>
            <div class="kpi-value">45.67%</div>
            <div class="kpi-delta"><span class="pill-badge badge-gold">+11.06% vs Low Pressure</span></div>
        </div>
        <div class="kpi-card emerald">
            <div class="kpi-label">Chasing Economy</div>
            <div class="kpi-value">8.32 RPO</div>
            <div class="kpi-delta"><span class="pill-badge badge-emerald">Innings 2 Pressure</span></div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Tournament Compression</div>
            <div class="kpi-value">-1.35 RPO</div>
            <div class="kpi-delta"><span class="pill-badge badge-blue">Low vs Critical</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="panel-box"><div class="panel-title">📊 Delivery Outcome Rates by Innings Stage</div>', unsafe_allow_html=True)
        stage_df = press_sum[press_sum['dimension_type'] == 'Innings Stage']
        fig_stage = px.bar(
            stage_df,
            x="category_name",
            y=["dot_ball_pct", "boundary_pct", "wicket_pct"],
            barmode="group",
            color_discrete_map={
                "dot_ball_pct": "#38BDF8",
                "boundary_pct": "#F59E0B",
                "wicket_pct": "#EF4444"
            }
        )
        apply_dark_theme(fig_stage, height=330)
        fig_stage.update_layout(xaxis_title="Innings Stage", yaxis_title="Percentage (%)")
        st.plotly_chart(fig_stage, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel-box"><div class="panel-title">⚡ Delivery Outcome Rates by Pressure Tier</div>', unsafe_allow_html=True)
        level_df = press_sum[press_sum['dimension_type'] == 'Pressure Level']
        fig_level = px.bar(
            level_df,
            x="category_name",
            y=["dot_ball_pct", "boundary_pct", "wicket_pct"],
            barmode="group",
            color_discrete_map={
                "dot_ball_pct": "#38BDF8",
                "boundary_pct": "#F59E0B",
                "wicket_pct": "#EF4444"
            }
        )
        apply_dark_theme(fig_level, height=330)
        fig_level.update_layout(xaxis_title="Pressure Tier", yaxis_title="Percentage (%)")
        st.plotly_chart(fig_level, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 5: HEAD-TO-HEAD COMPARISON
# ==========================================
with tab5:
    disc = st.radio("Select Discipline to Compare:", ["Batting", "Bowling"], horizontal=True)

    if disc == "Batting":
        p_list = batters['player_name'].tolist()
        c1, c2 = st.columns(2)
        with c1:
            p_a_name = st.selectbox("Select Player A:", p_list, index=0)
        with c2:
            p_b_name = st.selectbox("Select Player B:", p_list, index=1 if len(p_list) > 1 else 0)

        p_a = batters[batters['player_name'] == p_a_name].iloc[0]
        p_b = batters[batters['player_name'] == p_b_name].iloc[0]

        # Side-by-Side Fighter Cards
        c_left, c_mid, c_right = st.columns([1.2, 0.6, 1.2])
        with c_left:
            st.markdown(f"""
            <div class="vs-card">
                <span class="pill-badge badge-blue">Rank #{int(p_a['rank'])} • {p_a['competitions']}</span>
                <div class="vs-player-name">{p_a_name}</div>
                <div class="vs-rating-badge">{p_a['adjusted_rating']:.2f}</div>
                <div style="color: #94A3B8; font-size: 0.85rem;">Raw Rating: {p_a['raw_rating']:.2f} | Reliability: {p_a['reliability_tier']}</div>
            </div>
            """, unsafe_allow_html=True)
        with c_mid:
            delta_rat = p_a['adjusted_rating'] - p_b['adjusted_rating']
            delta_color = "#34D399" if delta_rat > 0 else "#F87171"
            st.markdown(f"""
            <div style="text-align: center; padding-top: 35px;">
                <div style="font-size: 2.2rem; font-weight: 900; color: #94A3B8;">VS</div>
                <div style="font-size: 1.1rem; font-weight: 700; color: {delta_color}; margin-top: 8px;">
                    Δ {delta_rat:+.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)
        with c_right:
            st.markdown(f"""
            <div class="vs-card">
                <span class="pill-badge badge-gold">Rank #{int(p_b['rank'])} • {p_b['competitions']}</span>
                <div class="vs-player-name">{p_b_name}</div>
                <div class="vs-rating-badge" style="color: #FBBF24;">{p_b['adjusted_rating']:.2f}</div>
                <div style="color: #94A3B8; font-size: 0.85rem;">Raw Rating: {p_b['raw_rating']:.2f} | Reliability: {p_b['reliability_tier']}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # 5-Pillar Score Comparison
        pillars = [
            "score_pressure_vs_baseline",
            "score_pressure_strike_rate",
            "score_pressure_batting_average",
            "score_dot_and_boundary",
            "score_match_consistency"
        ]
        pillar_labels = ["Clutch Lift", "Pressure SR", "Pressure Avg", "Boundary/Dot", "Consistency"]

        st.markdown('<div class="panel-box"><div class="panel-title">⚔️ 5-Pillar Rating Comparison: Head-to-Head Breakdown</div>', unsafe_allow_html=True)
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Bar(
            x=pillar_labels,
            y=[p_a[p] for p in pillars],
            name=p_a_name,
            marker_color="#38BDF8"
        ))
        fig_radar.add_trace(go.Bar(
            x=pillar_labels,
            y=[p_b[p] for p in pillars],
            name=p_b_name,
            marker_color="#F59E0B"
        ))
        apply_dark_theme(fig_radar, height=320)
        fig_radar.update_layout(barmode='group', yaxis=dict(range=[0, 100], title="Pillar Score (0–100)"))
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        p_list = bowlers['player_name'].tolist()
        c1, c2 = st.columns(2)
        with c1:
            p_a_name = st.selectbox("Select Bowler A:", p_list, index=0)
        with c2:
            p_b_name = st.selectbox("Select Bowler B:", p_list, index=1 if len(p_list) > 1 else 0)

        p_a = bowlers[bowlers['player_name'] == p_a_name].iloc[0]
        p_b = bowlers[bowlers['player_name'] == p_b_name].iloc[0]

        c_left, c_mid, c_right = st.columns([1.2, 0.6, 1.2])
        with c_left:
            st.markdown(f"""
            <div class="vs-card">
                <span class="pill-badge badge-blue">Rank #{int(p_a['rank'])} • {p_a['competitions']}</span>
                <div class="vs-player-name">{p_a_name}</div>
                <div class="vs-rating-badge">{p_a['adjusted_rating']:.2f}</div>
                <div style="color: #94A3B8; font-size: 0.85rem;">Raw Rating: {p_a['raw_rating']:.2f} | Reliability: {p_a['reliability_tier']}</div>
            </div>
            """, unsafe_allow_html=True)
        with c_mid:
            delta_rat = p_a['adjusted_rating'] - p_b['adjusted_rating']
            delta_color = "#34D399" if delta_rat > 0 else "#F87171"
            st.markdown(f"""
            <div style="text-align: center; padding-top: 35px;">
                <div style="font-size: 2.2rem; font-weight: 900; color: #94A3B8;">VS</div>
                <div style="font-size: 1.1rem; font-weight: 700; color: {delta_color}; margin-top: 8px;">
                    Δ {delta_rat:+.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)
        with c_right:
            st.markdown(f"""
            <div class="vs-card">
                <span class="pill-badge badge-gold">Rank #{int(p_b['rank'])} • {p_b['competitions']}</span>
                <div class="vs-player-name">{p_b_name}</div>
                <div class="vs-rating-badge" style="color: #FBBF24;">{p_b['adjusted_rating']:.2f}</div>
                <div style="color: #94A3B8; font-size: 0.85rem;">Raw Rating: {p_b['raw_rating']:.2f} | Reliability: {p_b['reliability_tier']}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        pillars = [
            "score_pressure_vs_baseline",
            "score_pressure_economy",
            "score_pressure_wicket_rate",
            "score_dot_and_boundary",
            "score_match_consistency"
        ]
        pillar_labels = ["Run Suppression", "Pressure Econ", "Wicket Strike", "Dot/Boundary", "Consistency"]

        st.markdown('<div class="panel-box"><div class="panel-title">⚔️ 5-Pillar Rating Comparison: Head-to-Head Breakdown</div>', unsafe_allow_html=True)
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Bar(
            x=pillar_labels,
            y=[p_a[p] for p in pillars],
            name=p_a_name,
            marker_color="#38BDF8"
        ))
        fig_radar.add_trace(go.Bar(
            x=pillar_labels,
            y=[p_b[p] for p in pillars],
            name=p_b_name,
            marker_color="#F59E0B"
        ))
        apply_dark_theme(fig_radar, height=320)
        fig_radar.update_layout(barmode='group', yaxis=dict(range=[0, 100], title="Pillar Score (0–100)"))
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; color: #475569; font-size: 0.8rem; padding: 24px 0 10px 0;">
    SupeRR Selector Season 2 • PressurePlay Cricket Intelligence Engine • Powered by Streamlit & Plotly
</div>
""", unsafe_allow_html=True)
