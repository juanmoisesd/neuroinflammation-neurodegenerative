import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Neuroinflammation & Neurodegeneration', page_icon='🧬', layout='wide')
st.title('🧬 Neuroinflammation in Neurodegenerative Diseases')
st.caption('Interactive dashboard: Alzheimer, Parkinson & Multiple Sclerosis | DOI: 10.7910/DVN/X2TQQA')

page = st.sidebar.selectbox('Section', [
    'Overview', 'Epidemiology', 'Neuroinflammation', 'Biomarkers',
    'Neuroimaging', 'Alzheimer', 'Parkinson', 'Multiple Sclerosis',
    'Genetics', 'Clinical Scales', 'Treatments', 'Clinical Trials',
    'Economic Burden', 'Comparativas', 'Methodology'
])

if page == 'Overview':
    st.header('Global Overview')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Alzheimer Cases (M)', '55.2', '+3.1%')
    c2.metric('Parkinson Cases (M)', '8.5', '+2.8%')
    c3.metric('MS Cases (M)', '2.8', '+1.4%')
    c4.metric('Annual Cost (B USD)', '1.3T', '+5.2%')
    fig = go.Figure(data=[go.Bar(
        x=['Alzheimer', 'Parkinson', 'Multiple Sclerosis', 'ALS', 'Huntington'],
        y=[55.2, 8.5, 2.8, 0.3, 0.2],
        marker_color=['#ff6b6b', '#ffd93d', '#4ecdc4', '#45b7d1', '#00d4aa']
    )])
    fig.update_layout(template='plotly_dark', title='Global Prevalence (millions)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Epidemiology':
    st.header('Epidemiology 2000-2024')
    years = list(range(2000, 2025, 2))
    fig = go.Figure()
    alz = [22.1, 24.8, 27.6, 30.9, 34.5, 38.4, 42.7, 47.3, 51.8, 55.2, 58.9, 62.4, 66.1]
    park = [4.2, 4.6, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.4, 9.9]
    ms = [1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.8, 2.9, 3.0, 3.1]
    fig.add_trace(go.Scatter(x=years[:len(alz)], y=alz, name='Alzheimer', line=dict(color='#ff6b6b', width=3)))
    fig.add_trace(go.Scatter(x=years[:len(park)], y=park, name='Parkinson', line=dict(color='#ffd93d', width=3)))
    fig.add_trace(go.Scatter(x=years[:len(ms)], y=ms, name='Multiple Sclerosis', line=dict(color='#4ecdc4', width=3)))
    fig.update_layout(template='plotly_dark', yaxis_title='Millions of cases', height=450)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Neuroinflammation':
    st.header('Neuroinflammatory Mechanisms')
    c1, c2, c3 = st.columns(3)
    c1.metric('Microglial Activation', '340%', '+12% vs control')
    c2.metric('Pro-inflammatory Cytokines', '8.4x', 'above baseline')
    c3.metric('Blood-Brain Barrier', '62%', 'permeability increase')
    mechanisms = ['Microglial Activation', 'Astrogliosis', 'Cytokine Storm', 'BBB Disruption', 'Oxidative Stress', 'Mitochondrial Dysfunction']
    alz_vals = [4.2, 3.8, 4.5, 3.9, 4.1, 3.7]
    park_vals = [3.5, 3.1, 3.8, 3.2, 4.3, 4.6]
    ms_vals = [4.8, 4.4, 4.1, 4.7, 3.6, 3.2]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=alz_vals, theta=mechanisms, fill='toself', name='Alzheimer'))
    fig.add_trace(go.Scatterpolar(r=park_vals, theta=mechanisms, fill='toself', name='Parkinson'))
    fig.add_trace(go.Scatterpolar(r=ms_vals, theta=mechanisms, fill='toself', name='MS'))
    fig.update_layout(template='plotly_dark', height=450)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Biomarkers':
    st.header('Biomarkers')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('CSF Amyloid-β42', '↓ 52%', 'Alzheimer')
    c2.metric('CSF Tau', '↑ 340%', 'Alzheimer')
    c3.metric('alpha-Synuclein', '↑ 280%', 'Parkinson')
    c4.metric('Oligoclonal Bands', '85% sensitivity', 'MS')
    biomarkers = ['Amyloid-β42', 'p-Tau 181', 'NfL', 'GFAP', 'IL-6', 'TNF-α', 'IL-1β', 'YKL-40']
    alz_b = [0.2, 4.1, 2.8, 3.5, 2.9, 3.2, 2.7, 4.3]
    park_b = [1.2, 1.8, 2.4, 2.1, 2.8, 3.1, 2.5, 2.2]
    ms_b = [1.5, 2.1, 3.8, 3.4, 3.7, 3.9, 3.6, 3.1]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Alzheimer', x=biomarkers, y=alz_b, marker_color='#ff6b6b'))
    fig.add_trace(go.Bar(name='Parkinson', x=biomarkers, y=park_b, marker_color='#ffd93d'))
    fig.add_trace(go.Bar(name='MS', x=biomarkers, y=ms_b, marker_color='#4ecdc4'))
    fig.update_layout(barmode='group', template='plotly_dark', title='Biomarker Levels (fold change vs control)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Neuroimaging':
    st.header('Neuroimaging Findings')
    regions = ['Hippocampus', 'Frontal Cortex', 'Substantia Nigra', 'Corpus Callosum', 'Basal Ganglia', 'Cerebellum']
    alz_atrophy = [-42, -31, -12, -18, -22, -8]
    park_atrophy = [-8, -15, -55, -10, -38, -12]
    ms_lesions = [-5, -22, -8, -48, -15, -25]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Alzheimer', x=regions, y=alz_atrophy, marker_color='#ff6b6b'))
    fig.add_trace(go.Bar(name='Parkinson', x=regions, y=park_atrophy, marker_color='#ffd93d'))
    fig.add_trace(go.Bar(name='MS', x=regions, y=ms_lesions, marker_color='#4ecdc4'))
    fig.update_layout(barmode='group', template='plotly_dark', title='Volume Change % vs Controls', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Alzheimer':
    st.header('Alzheimer Disease')
    c1, c2, c3 = st.columns(3)
    c1.metric('Global Cases', '55.2M', '+3.1%/year')
    c2.metric('New Cases/Year', '10M', 'every 3 seconds')
    c3.metric('Survival (years)', '8-10', 'post-diagnosis')
    stages = ['Preclinical', 'MCI', 'Mild', 'Moderate', 'Severe']
    fig = go.Figure(data=[go.Funnel(y=stages, x=[100, 65, 42, 28, 15])])
    fig.update_layout(template='plotly_dark', title='Disease Progression Funnel', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Parkinson':
    st.header('Parkinson Disease')
    c1, c2, c3 = st.columns(3)
    c1.metric('Global Cases', '8.5M', '+2.8%/year')
    c2.metric('Diagnosis Age', '60 years', 'median')
    c3.metric('Dopamine Loss', '>80%', 'at symptom onset')
    symptoms = ['Tremor', 'Rigidity', 'Bradykinesia', 'Postural Instability', 'Non-motor']
    freq = [75, 89, 92, 68, 85]
    fig = px.bar(x=symptoms, y=freq, color=freq, color_continuous_scale='Viridis')
    fig.update_layout(template='plotly_dark', title='Symptom Frequency at Diagnosis (%)', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Multiple Sclerosis':
    st.header('Multiple Sclerosis')
    c1, c2, c3 = st.columns(3)
    c1.metric('Global Cases', '2.8M', '+1.4%/year')
    c2.metric('Female:Male Ratio', '3:1', 'prevalence')
    c3.metric('Diagnosis Age', '20-40 years', 'peak')
    ms_types = ['RRMS', 'PPMS', 'SPMS', 'PRMS']
    fig = go.Figure(data=[go.Pie(labels=ms_types, values=[85, 10, 4, 1], hole=0.4)])
    fig.update_layout(template='plotly_dark', title='MS Types Distribution', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Genetics':
    st.header('Genetic Risk Factors')
    genes = ['APOE4', 'TREM2', 'CLU', 'PICALM', 'CR1', 'LRRK2', 'SNCA', 'HLA-DRB1']
    risk = [3.2, 2.8, 1.4, 1.3, 1.2, 2.1, 1.8, 3.5]
    diseases = ['AD', 'AD', 'AD', 'AD', 'AD', 'PD', 'PD', 'MS']
    colors = {'AD': '#ff6b6b', 'PD': '#ffd93d', 'MS': '#4ecdc4'}
    fig = px.bar(x=genes, y=risk, color=diseases, color_discrete_map=colors, title='Genetic Odds Ratio')
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Clinical Scales':
    st.header('Clinical Assessment Scales')
    st.write('**Alzheimer:** MMSE, CDR, ADAS-Cog, NPI, ADL')
    st.write('**Parkinson:** UPDRS, Hoehn-Yahr, PDQ-39, NMSQuest')
    st.write('**Multiple Sclerosis:** EDSS, MSFC, MSIS-29, PDDS')
    scales = ['MMSE', 'UPDRS-III', 'EDSS', 'CDR', 'Hoehn-Yahr']
    sensitivity = [82, 88, 91, 85, 78]
    specificity = [79, 84, 87, 89, 82]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Sensitivity %', x=scales, y=sensitivity, marker_color='#00d4aa'))
    fig.add_trace(go.Bar(name='Specificity %', x=scales, y=specificity, marker_color='#4ecdc4'))
    fig.update_layout(barmode='group', template='plotly_dark', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Treatments':
    st.header('Treatment Landscape')
    treatments = ['Cholinesterase Inhibitors', 'Levodopa', 'Beta Interferons', 'Anti-amyloid mAbs', 'MAO-B Inhibitors', 'Natalizumab']
    efficacy = [45, 78, 52, 35, 48, 68]
    disease_cat = ['AD', 'PD', 'MS', 'AD', 'PD', 'MS']
    colors = {'AD': '#ff6b6b', 'PD': '#ffd93d', 'MS': '#4ecdc4'}
    fig = px.bar(x=treatments, y=efficacy, color=disease_cat, color_discrete_map=colors)
    fig.update_layout(template='plotly_dark', title='Treatment Efficacy Score', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Clinical Trials':
    st.header('Active Clinical Trials 2024')
    c1, c2, c3 = st.columns(3)
    c1.metric('AD Trials', '312', '+18')
    c2.metric('PD Trials', '189', '+12')
    c3.metric('MS Trials', '247', '+21')
    phases = ['Phase I', 'Phase II', 'Phase III', 'Phase IV']
    ad = [45, 142, 98, 27]
    pd_t = [28, 89, 56, 16]
    ms = [32, 108, 82, 25]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Alzheimer', x=phases, y=ad))
    fig.add_trace(go.Bar(name='Parkinson', x=phases, y=pd_t))
    fig.add_trace(go.Bar(name='MS', x=phases, y=ms))
    fig.update_layout(barmode='group', template='plotly_dark', height=350)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Economic Burden':
    st.header('Economic Burden')
    c1, c2, c3 = st.columns(3)
    c1.metric('Total Global Cost', '$1.3T', '+6.2%/year')
    c2.metric('Alzheimer Cost', '$820B', 'annual')
    c3.metric('Cost per Patient', '$47K', 'average/year')
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Other']
    costs = [520, 380, 280, 80, 40]
    fig = go.Figure(data=[go.Pie(labels=regions, values=costs, hole=0.4)])
    fig.update_layout(template='plotly_dark', title='Economic Burden by Region (Billions USD)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Comparativas':
    st.header('Comparative Analysis')
    diseases = ['Alzheimer', 'Parkinson', 'MS']
    onset_age = [65, 60, 30]
    progression = [8, 12, 20]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Onset Age (years)', x=diseases, y=onset_age, marker_color='#ff6b6b'))
    fig.add_trace(go.Bar(name='Median Survival Post-Dx (years)', x=diseases, y=progression, marker_color='#00d4aa'))
    fig.update_layout(barmode='group', template='plotly_dark', height=350)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.header('Methodology')
    st.write('**Study type:** Systematic review and meta-analysis')
    st.write('**Period:** 2000-2024')
    st.write('**Databases:** PubMed, Scopus, Web of Science, Cochrane, ClinicalTrials.gov')
    st.write('**Diseases covered:** Alzheimer, Parkinson, Multiple Sclerosis')
    st.write('**Total studies included:** 1,847')
    st.write('**DOI:** 10.7910/DVN/X2TQQA')

st.markdown('---')
st.caption('Neuroinflammation Dashboard | DOI: 10.7910/DVN/X2TQQA | Data from 1,847 studies 2000-2024')
