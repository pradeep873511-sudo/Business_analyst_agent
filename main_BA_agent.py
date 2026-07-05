from profiler_BA_agent import profile_data
from analyst_BA_agent import analyze_data
from insight_BA_agent import generate_insights
from report_BA_agent import generate_report

def run_pipeline(file_path):
    profile = profile_data(file_path)
    analysis = analyze_data(file_path)
    insights = generate_insights(profile, analysis)
    report = generate_report(insights)
    return report, analysis