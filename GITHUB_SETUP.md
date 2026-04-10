# GitHub Repository Setup Instructions

## Quick Setup Guide

Your local Git repository is ready! Follow these steps to push it to GitHub:

### Step 1: Create the Repository on GitHub

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `masters-putting-predictions`
   - **Description**: `Interactive dashboard for Masters Tournament putting predictions with 4-day analysis, weather conditions, and player statistics`
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

### Step 2: Push Your Code

After creating the repository, run these commands in your terminal:

```bash
git remote add origin https://github.com/sammclear/masters-putting-predictions.git
git push -u origin main
```

### Step 3: Verify

Visit your repository at:
```
https://github.com/sammclear/masters-putting-predictions
```

## What's Included

Your repository contains:

- ✅ `README.md` - Complete documentation
- ✅ `masters_enhanced_dashboard.html` - Full 4-day interactive dashboard
- ✅ `masters_dashboard.html` - Original Day 1 dashboard
- ✅ `fetch_masters_stats.py` - Python analysis script
- ✅ `masters_day1_putt_prediction.json` - Prediction data
- ✅ `.gitignore` - Git ignore rules

## Sharing with IBM Colleague

Once pushed, share this link with your IBM colleague:
```
https://github.com/sammclear/masters-putting-predictions
```

They can:
- View the code online
- Clone the repository: `git clone https://github.com/sammclear/masters-putting-predictions.git`
- View the dashboard by opening the HTML files in a browser

## Optional: Enable GitHub Pages

To host the dashboard online:

1. Go to your repository settings
2. Navigate to **Pages** section
3. Under **Source**, select **main** branch
4. Click **Save**
5. Your dashboard will be available at:
   ```
   https://sammclear.github.io/masters-putting-predictions/masters_enhanced_dashboard.html
   ```

## Troubleshooting

If you get authentication errors:
- Use a Personal Access Token instead of password
- Or use GitHub CLI: `gh auth login`

## Need Help?

If you encounter any issues, let me know and I can help troubleshoot!