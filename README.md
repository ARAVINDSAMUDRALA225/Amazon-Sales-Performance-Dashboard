# 📊 Amazon Sales Performance Dashboard

This project presents an end-to-end data analytics workflow on **Amazon India Sales Data** — from data cleaning and SQL validation to building a fully interactive **Power BI Dashboard** for business insights.

---

## 🎥 Dashboard Demo

<a href="https://drive.google.com/file/d/11O3RGUSfLOHLYBYr2oZPlro-SCM5LfZy/view?usp=sharing">▶ Click here to watch the demo video</a>

---

## 📌 Project Overview

This dashboard helps stakeholders analyze:

✔ Total sales & trends  
✔ Top product categories  
✔ High-revenue states & cities  
✔ Delivery success vs cancellations  
✔ Order growth by month  

---

## 🛠 Tech Stack Used

| Purpose | Tool |
|--------|------|
| Data Preprocessing | Python (Pandas, NumPy) |
| Database & Queries | MySQL |
| Business Intelligence | Power BI |
| Version Control | GitHub |

---

## 📂 Project Structure

Amazon-Sales-Performance-Dashboard/
│
├── data/
│ ├── Amazon_Sale_Report.csv # Raw dataset
│ └── Amazon_Sales_Cleaned.csv # Cleaned dataset
│
├── scripts/
│ └── amazon_sales_cleaning.py # Data cleaning script
│
├── sql/
│ └── amazon_sales_analysis_queries.sql # SQL analysis queries
│
├── reports/
│ └── Amazon_Sales_Performance_Dashboard.pbix # Power BI dashboard
│
└── README.md # Project documentation 

---

## 🧹 Data Cleaning (Python)

Tasks performed:

- Removed unnecessary / high-null fields  
- Converted **Date** to datetime format  
- Removed missing Amount / city / state values  
- Added **Month** column for time-based visuals  
- Exported cleaned file → `Amazon_Sales_Cleaned.csv`

📌 Script: `/scripts/amazon_sales_cleaning.py`

---

## 🗄 SQL Analysis

Validated and analyzed metrics like:

- Total orders  
- State-wise revenue  
- City-wise revenue  
- Delivered vs Cancelled orders  

📌 Queries: `/sql/amazon_sales_analysis_queries.sql`  
📸 Output screenshots included in repo  

---

## 📊 Power BI Dashboard Features

Dashboard Name: **Amazon Sales Performance Dashboard**

### 📌 KPIs

- Total Sales  
- Total Orders  
- Total Quantity Sold  
- Average Order Value (AOV)  
- Delivery Success Rate (%)  

### 📌 Visuals

| Visual Type | Purpose |
|------------|---------|
| Line Chart | Monthly Sales Trend |
| Pie Chart | Order Status Distribution |
| Donut Chart | Fulfillment Method Performance |
| Bar Chart | Top 10 States by Sales |
| Bar Chart | Category-wise Sales |
| Table | City-wise Sales Summary |
| Slicers | Month, Category, Status |

📌 File: `/reports/Amazon_Sales_Performance_Dashboard.pbix`

---

## 📈 Key Insights

- Mumbai, Bengaluru & Hyderabad are the top markets  
- T-shirts & Shirts drive most revenue  
- Majority orders are fulfilled by Amazon  
- **≈64%** Delivery success rate → needs improvement  
- Peak sales observed in **April**  

---

## 💼 Business Value

This dashboard helps teams:

- Analyze sales performance efficiently  
- Optimize delivery operations  
- Plan regional stock allocation  
- Identify revenue opportunities  
- Improve customer satisfaction KPIs  

---

## 🔮 Future Enhancements

- Add profit margin & cost metrics  
- Integrate real-time database refresh  
- Predictive analytics for demand forecasting  
- Role-based dashboards for deeper insights  

---

## 👤 Author

- **Name:** Aravind Samudrala  
- **Role:** Data Analyst Intern  
- **Email:** aravindsamudrala6601@gmail.com  
- **Tools:** Python | MySQL | Power BI  


