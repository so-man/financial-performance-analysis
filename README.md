Financial Performance Analysis

Comparative Study of 10 Major Technology Companies (2019–2023)

Overview
This project analyzes the financial performance of 10 publicly traded technology companies over a five-year period. The goal is to identify revenue leaders, margin efficiency, cash generation trends, and year-over-year growth patterns across the sector.
Companies covered: Apple, Microsoft, Amazon, Google, Meta, Tesla, Netflix, Nvidia, Adobe, Salesforce

What's Inside
├── financial_data.csv          # Cleaned dataset (50 rows, 15 columns)
├── analysis.py                 # Full analysis and chart generation script
├── Financial_Analysis_Report.pdf  # Portfolio-ready PDF report
├── charts/
│   ├── 01_revenue_by_company.png
│   ├── 02_revenue_trend.png
│   ├── 03_net_margin.png
│   ├── 04_free_cashflow.png
│   ├── 05_revenue_vs_income.png
│   ├── 06_margin_comparison.png
│   └── 07_correlation_heatmap.png
└── README.md

Key Metrics Analyzed

Total Revenue
Gross Profit and Gross Margin %
Operating Income and Operating Margin %
Net Income and Net Margin %
Free Cash Flow (FCF)
Capital Expenditure (CapEx)
Year-over-Year Revenue Growth %


Charts Generated
ChartDescriptionRevenue by CompanyBar chart comparing 2023 revenue across all 10 companiesRevenue TrendLine chart showing 5-year growth for top 5 companiesNet MarginBar chart with sector average benchmark lineFree Cash FlowFCF comparison across all companiesRevenue vs Net IncomeScatter plot with bubble size = net marginMargin ComparisonGrouped bar chart: Gross vs Operating vs Net marginCorrelation HeatmapPearson correlation across all financial metrics

Key Findings

Amazon leads in absolute revenue but operates on thin margins due to logistics costs
Microsoft records the highest net margin, reflecting its high-margin software and cloud model
Nvidia shows the fastest revenue growth rate driven by AI chip demand
Apple and Microsoft generate the most free cash flow, giving them significant financial flexibility
Software companies consistently outperform hardware and e-commerce peers on margin metrics
Revenue and gross profit show near-perfect correlation (>0.95), while margin metrics are independent of revenue scale


Tools Used
ToolPurposePython 3.xCore languagepandasData manipulation and aggregationNumPyNumerical operations and data generationmatplotlibBase charting libraryseabornStatistical visualizationReportLabPDF report generation

How to Run

Clone the repo

bashgit clone https://github.com/so-man/financial-performance-analysis
cd financial-performance-analysis

Install dependencies

bashpip install pandas numpy matplotlib seaborn reportlab

Run the analysis

bashpython analysis.py
Charts will be saved to the /charts folder automatically.

Dataset
The dataset is synthetically generated to mirror realistic financial reporting patterns for large-cap technology companies. Revenue figures are based on publicly available ballpark ranges with controlled growth rates and margin distributions applied per company. The data is intended for analytical and portfolio demonstration purposes.

About
Built by Soman Yadav as part of a data analytics portfolio.

Email: soman@pillrz.com
LinkedIn: linkedin.com/in/soman-yadav
X: @SomanDatGuy
