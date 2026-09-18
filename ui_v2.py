from __future__ import annotations

import html
import streamlit as st


def apply_theme():
    st.markdown("""<style>
:root{--navy:#0B2341;--blue:#2563EB;--bg:#F4F7FB;--line:#E2E8F0;--text:#0F172A;--muted:#64748B}
html,body,[class*="css"]{font-family:Pretendard,"Noto Sans KR","Apple SD Gothic Neo",sans-serif}
.stApp{background:var(--bg);color:var(--text)}
.block-container{max-width:1480px;padding:1.25rem 2rem 3rem}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,var(--navy),#091D35);border:0}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label{border-radius:10px;padding:.62rem .72rem;color:#D7E3F2}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p{color:#D7E3F2!important;font-weight:600}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover{background:rgba(255,255,255,.07)}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked){background:var(--blue);box-shadow:0 6px 16px rgba(37,99,235,.28)}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) p{color:#fff!important}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p{color:#9FB1C8!important}
h1,h2,h3,h4{color:var(--text);letter-spacing:-.035em}
[data-testid="stMetric"]{background:#fff;border:1px solid var(--line);border-radius:14px;padding:15px 17px;box-shadow:0 5px 18px rgba(15,23,42,.035)}
[data-testid="stMetricLabel"]{color:var(--muted);font-size:13px}
[data-testid="stMetricValue"]{color:var(--text);font-weight:800}
[data-testid="stVerticalBlockBorderWrapper"]{border-color:var(--line)!important;border-radius:14px!important;background:#fff;box-shadow:0 5px 18px rgba(15,23,42,.035)}
.stButton>button,.stFormSubmitButton>button{border-radius:9px;min-height:2.55rem;font-weight:700}
.stButton>button[kind="primary"],.stFormSubmitButton>button[kind="primary"]{background:var(--blue);border-color:var(--blue)}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]>div{border-radius:9px!important}
.planx-brand{display:flex;align-items:center;gap:10px;margin:3px 2px 24px}
.planx-brand-mark{width:38px;height:38px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:linear-gradient(145deg,#3B82F6,#60A5FA);color:#fff;font-size:20px;font-weight:800}
.planx-brand-title{font-size:19px;line-height:1.1;font-weight:800;color:#fff;letter-spacing:-.03em}
.planx-brand-sub{font-size:10px;color:#9FB1C8;margin-top:3px}
.planx-hero{background:linear-gradient(135deg,#fff 0%,#fff 62%,#EEF5FF 100%);border:1px solid var(--line);border-radius:18px;padding:24px 27px;margin-bottom:16px;box-shadow:0 8px 25px rgba(15,23,42,.04)}
.planx-eyebrow{color:var(--blue);font-size:11px;font-weight:800;letter-spacing:.1em;margin-bottom:7px}
.planx-hero h1{margin:0;font-size:31px;line-height:1.18}
.planx-hero p{margin:8px 0 0;color:var(--muted);font-size:14px}
.planx-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:17px 18px;min-height:108px;box-shadow:0 5px 18px rgba(15,23,42,.035)}
.planx-card-title{font-size:12px;color:var(--muted);margin-bottom:7px;font-weight:700}
.planx-card-value{font-size:22px;color:var(--text);font-weight:800;letter-spacing:-.03em}
.planx-card-note{margin-top:6px;font-size:11px;color:#94A3B8}
.planx-empty{background:#fff;border:1px dashed #CBD5E1;border-radius:14px;padding:20px;color:var(--muted)}
.planx-source{display:inline-flex;align-items:center;gap:5px;color:var(--muted);background:#F8FAFC;border:1px solid var(--line);padding:4px 8px;border-radius:999px;font-size:10px}
.planx-status-ok{color:#047857;background:#ECFDF5;border-color:#A7F3D0}
.planx-status-wait{color:#92400E;background:#FFFBEB;border-color:#FDE68A}
.planx-status-bad{color:#B91C1C;background:#FEF2F2;border-color:#FECACA}
</style>""",unsafe_allow_html=True)


def brand():
    st.markdown("""<div class="planx-brand"><div class="planx-brand-mark">↗</div><div><div class="planx-brand-title">StockDash</div><div class="planx-brand-sub">STOCK DASHBOARD</div></div></div>""",unsafe_allow_html=True)


def hero(title:str,subtitle:str,eyebrow:str="STOCK DASHBOARD"):
    st.markdown(f"""<div class="planx-hero"><div class="planx-eyebrow">{html.escape(eyebrow)}</div><h1>{html.escape(title)}</h1><p>{html.escape(subtitle)}</p></div>""",unsafe_allow_html=True)


def card(title:str,value:str,note:str="",status:str=""):
    extra=f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(f"""<div class="planx-card"><div class="planx-card-title">{html.escape(title)}</div><div class="planx-card-value">{html.escape(value)}</div><div class="planx-card-note">{html.escape(note)}</div>{extra}</div>""",unsafe_allow_html=True)


def empty_state(title:str,message:str):
    st.markdown(f"""<div class="planx-empty"><strong style="color:#334155">{html.escape(title)}</strong><br><span>{html.escape(message)}</span></div>""",unsafe_allow_html=True)


def source_badge(label:str,state:str="wait"):
    cls={"ok":"planx-status-ok","bad":"planx-status-bad"}.get(state,"planx-status-wait")
    st.markdown(f'<span class="planx-source {cls}">{html.escape(label)}</span>',unsafe_allow_html=True)
