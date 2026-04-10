# Dashboard Update Workflow

## Overview
This guide explains how to update the Masters Enhanced Dashboard with actual putting statistics data.

---

## 📋 Step-by-Step Workflow

### Step 1: Update Your Excel File
1. Open `putting stats real.xlsx`
2. Add/update the actual putting data for the round
3. Data format: Values represent **putts per hole** (e.g., 1.56 means 1.56 putts/hole)
4. Numbers in brackets (e.g., "1.50 (1)") represent three-putt counts - these are already included in the average
5. Save the file

### Step 2: Run the Analysis Script
```bash
python analyze_putting_final.py
```

**What this does:**
- Reads your Excel file
- Calculates actual statistics (total putts, averages, etc.)
- Compares actual vs predicted values
- Generates accuracy metrics
- Creates output files:
  - `final_comparison_results.json` - Detailed data
  - `comparison_summary.txt` - Text summary

**Expected Output:**
```
MASTERS DAY 1 PUTTING STATISTICS - ACTUAL VS PREDICTED
======================================================================
[SUCCESS] Excel file loaded
Total players: 91
...
OVERALL PREDICTION ACCURACY: 97.39%
[STAR] Prediction Rating: EXCELLENT
```

### Step 3: Review the Results
Check the generated files:
- **final_comparison_results.json** - Contains all the numbers you need
- **comparison_summary.txt** - Quick summary

Key values to note:
- `actual.total_putts` - Total putts for the round
- `actual.avg_putts_per_player` - Average putts per player
- `actual.min_putts` - Best performance
- `actual.max_putts` - Worst performance
- `comparison.overall_accuracy` - Prediction accuracy percentage

### Step 4: Update the Dashboard HTML

Open `masters_enhanced_dashboard.html` and update these sections:

#### A. Day 1 Stats Section (around line 356)
```html
<div class="stat-card">
    <div class="stat-label">Total Putts</div>
    <div class="stat-value">2,754</div>  <!-- UPDATE THIS -->
    <div style="font-size: 0.8em; color: #90EE90; margin-top: 5px;">
        Actual (Predicted: 2,685)
    </div>
</div>
```

Update these values:
- Total Putts stat-value
- Avg Putts/Player stat-value
- Best Performance stat-value
- Worst Performance stat-value

#### B. Comparison Section (around line 620)
```html
<div class="stat-value" style="font-size: 2em;">2,754</div>  <!-- UPDATE THIS -->
<div style="color: #90EE90; margin-top: 10px;">Predicted: 2,684</div>
<div style="color: #FFD700; font-size: 0.9em;">+70 putts (+2.62%)</div>  <!-- UPDATE THIS -->
```

Update these values in the comparison cards:
- Total Putts actual value and difference
- Avg Putts/Player actual value and difference
- Best Performance actual value
- Worst Performance actual value

#### C. Accuracy Display (around line 625)
```html
<div style="font-size: 3em; font-weight: bold; color: #ffd700; margin: 20px 0;">
    97.39% Accuracy  <!-- UPDATE THIS -->
</div>
```

#### D. Chart Data (around line 935)
```javascript
new Chart(document.getElementById('actualVsPredictedChart'), {
    type: 'bar',
    data: {
        labels: ['Total Putts', 'Avg Putts/Player', 'Best Performance', 'Worst Performance'],
        datasets: [{
            label: 'Predicted',
            data: [2684, 29.5, 25, 35],  // Keep these
        }, {
            label: 'Actual',
            data: [2754, 30.27, 22, 37],  // UPDATE THESE
        }]
    },
    ...
});
```

### Step 5: Test Locally
1. Open `masters_enhanced_dashboard.html` in your browser
2. Click on the "Comparison" tab
3. Verify all numbers are correct
4. Check that the chart displays properly

### Step 6: Commit and Push to GitHub
```bash
# Add the updated files
git add masters_enhanced_dashboard.html final_comparison_results.json comparison_summary.txt

# Commit with a descriptive message
git commit -m "Update dashboard with Day X actual results - XX.XX% accuracy"

# Push to GitHub
git push origin main
```

---

## 🔄 Quick Reference: Files to Update

| File | What to Update | How |
|------|---------------|-----|
| `putting stats real.xlsx` | Actual putting data | Manual entry |
| `analyze_putting_final.py` | Excel file path (if needed) | Edit line 205 |
| `masters_enhanced_dashboard.html` | Display values and charts | Manual edit (see Step 4) |

---

## 📊 Data Format Reference

### Excel Data Format
- **Values:** Putts per hole (e.g., 1.56 = 1.56 putts/hole)
- **Brackets:** Three-putt count (e.g., "1.50 (1)" = 1 three-putt)
- **Total Putts:** Value × 18 holes (e.g., 1.56 × 18 = 28.08 total putts)

### JSON Output Format
```json
{
  "actual": {
    "total_putts": 2754.36,
    "avg_putts_per_player": 30.27,
    "avg_putts_per_hole": 1.68,
    "field_size": 91,
    "min_putts": 21.96,
    "max_putts": 37.08
  },
  "comparison": {
    "overall_accuracy": 97.39,
    "rating": "EXCELLENT"
  }
}
```

---

## 🛠️ Troubleshooting

### Issue: Script can't find Excel file
**Solution:** Update the path in `analyze_putting_final.py` line 205:
```python
excel_path = r"C:\Users\SamMcLear\Desktop\putting stats real.xlsx"
```

### Issue: Numbers look wrong
**Check:**
1. Excel values are putts per hole (not total putts)
2. Script is reading the correct round column
3. No extra spaces or formatting in Excel cells

### Issue: Chart not displaying
**Check:**
1. All array values in JavaScript match (same number of items)
2. No syntax errors in the chart data
3. Browser console for JavaScript errors (F12)

---

## 💡 Tips

1. **Keep backups:** Save a copy of the dashboard before making changes
2. **Test locally first:** Always open the HTML file in a browser before pushing
3. **Consistent naming:** Use clear commit messages for tracking changes
4. **Document changes:** Note any unusual results or adjustments needed

---

## 📝 Example Workflow for Day 2

1. Update Excel with Day 2 data
2. Run: `python analyze_putting_final.py`
3. Note the results (e.g., 2,730 total putts, 30.0 avg)
4. Update dashboard Day 2 section with actual values
5. Update comparison section if needed
6. Test in browser
7. Commit: `git commit -m "Update dashboard with Day 2 actual results - 98.5% accuracy"`
8. Push: `git push origin main`

---

## 🎯 Future Enhancements

Consider automating:
- Excel → JSON conversion
- JSON → HTML value injection
- Automatic chart data updates

This could be done with a Python script that:
1. Reads the JSON results
2. Updates the HTML file programmatically
3. Commits and pushes automatically

---

**Last Updated:** April 10, 2026
**Version:** 1.0