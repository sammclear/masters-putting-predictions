# 🏌️ Masters Tournament Putting Predictions

An interactive dashboard and analysis tool for predicting putting statistics at The Masters Tournament at Augusta National Golf Club.

## 📊 Overview

This project analyzes historical Masters putting data to predict the total number of putts for Day 1 of the tournament. It includes:

- **Interactive Dashboard**: Beautiful, responsive web interface with charts and statistics
- **Python Analysis Script**: Data processing and prediction calculations
- **JSON Data Export**: Structured prediction data for further analysis

## 🎯 Key Predictions

### Day 1 Statistics
- **Total Putts Predicted**: 2,655 putts
- **Field Size**: 90 players
- **Average Putts per Player**: 29.5 putts
- **Holes per Round**: 18

### Putt Distribution by Distance
- **0-5 feet**: 720 putts (27.1%)
- **5-10 feet**: 540 putts (20.3%)
- **10-20 feet**: 900 putts (33.9%)
- **20+ feet**: 495 putts (18.6%)

## 📁 Files

- `masters_dashboard.html` - Interactive web dashboard with charts and visualizations
- `fetch_masters_stats.py` - Python script for data analysis and predictions
- `masters_day1_putt_prediction.json` - Structured prediction data
- `masters_predictions_updated.py` - Enhanced prediction script with Day 2 analysis
- `README.md` - This file

## 🚀 Quick Start

### View the Dashboard

Simply open `masters_dashboard.html` in any modern web browser:

```bash
# Windows
start masters_dashboard.html

# macOS
open masters_dashboard.html

# Linux
xdg-open masters_dashboard.html
```

### Run the Analysis Script

```bash
python fetch_masters_stats.py
```

This will generate updated predictions and save them to `masters_day1_putt_prediction.json`.

## 📈 Dashboard Features

- **Real-time Statistics Cards**: Key metrics displayed prominently
- **Interactive Charts**: 
  - Bar chart showing putt distribution by distance
  - Doughnut chart showing percentage breakdown
- **Performance Ranges**: Expected putting performance categories
- **Key Factors**: Analysis of conditions affecting putting at Augusta
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Masters Theme**: Green gradient design with gold accents

## 🎨 Technologies Used

- **HTML5/CSS3**: Modern web standards
- **Chart.js**: Interactive data visualizations
- **Python 3**: Data analysis and predictions
- **JSON**: Data storage and exchange

## 📊 Methodology

The predictions are based on:

1. **Historical Masters Data**: Average putting statistics from previous tournaments
2. **Augusta National Characteristics**: Fast, undulating greens
3. **Field Size Analysis**: Typical Masters field composition
4. **Distance Distribution**: Statistical breakdown of putt lengths
5. **Performance Ranges**: Expected outcomes for different skill levels

## 🏆 Key Factors Affecting Putting

1. **Green Speed and Firmness**: Augusta's notoriously fast greens
2. **Pin Positions**: Typically moderate on Day 1
3. **Weather Conditions**: Wind and temperature effects
4. **Course Setup**: Rough height and green surrounds
5. **Player Field Strength**: Experience at Augusta National

## 📱 Screenshots

The dashboard features:
- Clean, professional Masters-themed design
- Interactive hover effects on all elements
- Smooth animations and transitions
- Mobile-responsive layout

## 🔮 Future Enhancements

- [ ] Day 2, 3, and 4 predictions
- [ ] Real-time data integration from Masters API
- [ ] Player-specific putting analysis
- [ ] Historical comparison charts
- [ ] Weather condition adjustments
- [ ] Cut line predictions

## 📝 Data Sources

Predictions are based on historical Masters Tournament statistics and typical Augusta National Golf Club putting averages.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## 📄 License

This project is open source and available for educational and analytical purposes.

## 👤 Author

Created for Masters Tournament analysis and prediction.

## 📧 Contact

For questions or collaboration opportunities, please reach out through GitHub.

---

**Note**: This is a predictive analysis tool based on historical data. Actual tournament results may vary based on current conditions, player performance, and other factors.

🏌️‍♂️ *"A tradition unlike any other"* - The Masters Tournament