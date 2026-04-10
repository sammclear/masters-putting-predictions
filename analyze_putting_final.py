import pandas as pd
import json
from datetime import datetime
import re

def clean_numeric_value(value):
    """Extract numeric value from strings like '1.56 (1)' or '1.56'"""
    if pd.isna(value):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        # Extract first number from string
        match = re.search(r'(\d+\.?\d*)', value)
        if match:
            return float(match.group(1))
    return None

def analyze_actual_putting_data(excel_path):
    """Analyze actual putting data - values are putts per hole"""
    
    print("=" * 70)
    print("MASTERS DAY 1 PUTTING STATISTICS - ACTUAL VS PREDICTED")
    print("=" * 70)
    
    # Predicted values
    predicted = {
        'total_putts': 2684,
        'field_size': 91,
        'avg_putts_per_player': 29.5
    }
    
    try:
        # Read Excel file
        df = pd.read_excel(excel_path)
        
        print(f"\n[SUCCESS] Excel file loaded")
        print(f"Total players: {len(df)}")
        
        # Clean Round 1 data
        round1_raw = df['Round 1'].dropna()
        round1_clean = []
        
        for value in round1_raw:
            cleaned = clean_numeric_value(value)
            if cleaned is not None:
                round1_clean.append(cleaned)
        
        print(f"Players with Round 1 data: {len(round1_clean)}")
        
        print("\n" + "=" * 70)
        print("UNDERSTANDING THE DATA")
        print("=" * 70)
        print("\nThe values in your Excel represent: PUTTS PER HOLE")
        print("Example: 1.22 putts/hole × 18 holes = 21.96 total putts")
        
        # Calculate actual statistics
        print("\n" + "=" * 70)
        print("ACTUAL DAY 1 STATISTICS")
        print("=" * 70)
        
        # Average putts per hole
        avg_putts_per_hole = sum(round1_clean) / len(round1_clean)
        
        # Average putts per player (18 holes)
        avg_putts_per_player = avg_putts_per_hole * 18
        
        # Total putts for all players
        total_putts = sum(round1_clean) * 18
        
        # Min and max with player names
        min_putts_per_hole = min(round1_clean)
        max_putts_per_hole = max(round1_clean)
        min_putts_total = min_putts_per_hole * 18
        max_putts_total = max_putts_per_hole * 18
        
        # Find player names for best and worst
        min_idx = round1_clean.index(min_putts_per_hole)
        max_idx = round1_clean.index(max_putts_per_hole)
        
        # Get player names (clean up URLs)
        best_player = df['Player'].iloc[min_idx].split(' (')[0] if '(' in str(df['Player'].iloc[min_idx]) else df['Player'].iloc[min_idx]
        worst_player = df['Player'].iloc[max_idx].split(' (')[0] if '(' in str(df['Player'].iloc[max_idx]) else df['Player'].iloc[max_idx]
        
        print(f"\nAverage putts per hole: {avg_putts_per_hole:.4f}")
        print(f"Average putts per player (18 holes): {avg_putts_per_player:.2f}")
        print(f"Total putts (all {len(round1_clean)} players): {total_putts:,.0f}")
        print(f"\nBest performance: {best_player} - {min_putts_per_hole:.2f} putts/hole = {min_putts_total:.0f} total putts")
        print(f"Worst performance: {worst_player} - {max_putts_per_hole:.2f} putts/hole = {max_putts_total:.0f} total putts")
        
        # Comparison with predictions
        print("\n" + "=" * 70)
        print("PREDICTED VS ACTUAL COMPARISON")
        print("=" * 70)
        
        diff_total = total_putts - predicted['total_putts']
        diff_avg = avg_putts_per_player - predicted['avg_putts_per_player']
        
        accuracy_total = 100 - abs(diff_total / predicted['total_putts'] * 100)
        accuracy_avg = 100 - abs(diff_avg / predicted['avg_putts_per_player'] * 100)
        overall_accuracy = (accuracy_total + accuracy_avg) / 2
        
        print(f"\n{'Metric':<30} {'Predicted':<15} {'Actual':<15} {'Difference':<15} {'Accuracy'}")
        print("-" * 85)
        print(f"{'Total Putts':<30} {predicted['total_putts']:<15,} {total_putts:<15,.0f} {diff_total:<+15,.0f} {accuracy_total:.2f}%")
        print(f"{'Avg Putts per Player':<30} {predicted['avg_putts_per_player']:<15.2f} {avg_putts_per_player:<15.2f} {diff_avg:<+15.2f} {accuracy_avg:.2f}%")
        print(f"{'Field Size':<30} {predicted['field_size']:<15} {len(round1_clean):<15} {len(round1_clean) - predicted['field_size']:<+15} 100.00%")
        
        print(f"\n{'='*85}")
        print(f"OVERALL PREDICTION ACCURACY: {overall_accuracy:.2f}%")
        print(f"{'='*85}")
        
        # Rating
        if overall_accuracy >= 98:
            rating = "EXCEPTIONAL"
            emoji = "[TROPHY]"
            comment = "Prediction was extremely accurate!"
        elif overall_accuracy >= 95:
            rating = "EXCELLENT"
            emoji = "[STAR]"
            comment = "Prediction was highly accurate!"
        elif overall_accuracy >= 90:
            rating = "VERY GOOD"
            emoji = "[CHECK]"
            comment = "Prediction was quite accurate!"
        elif overall_accuracy >= 85:
            rating = "GOOD"
            emoji = "[CIRCLE]"
            comment = "Prediction was reasonably accurate."
        else:
            rating = "FAIR"
            emoji = "[TRIANGLE]"
            comment = "Prediction could be improved."
        
        print(f"\n{emoji} Prediction Rating: {rating}")
        print(f"{comment}")
        
        # Detailed breakdown
        print("\n" + "=" * 70)
        print("DETAILED BREAKDOWN")
        print("=" * 70)
        
        print(f"\nTotal Putts:")
        print(f"  Predicted: {predicted['total_putts']:,} putts")
        print(f"  Actual:    {total_putts:,.0f} putts")
        print(f"  Difference: {diff_total:+,.0f} putts ({diff_total/predicted['total_putts']*100:+.2f}%)")
        
        if abs(diff_total) < 50:
            print(f"  Analysis: Within 50 putts - EXCELLENT prediction!")
        elif abs(diff_total) < 100:
            print(f"  Analysis: Within 100 putts - VERY GOOD prediction!")
        elif abs(diff_total) < 150:
            print(f"  Analysis: Within 150 putts - GOOD prediction!")
        
        print(f"\nAverage Putts per Player:")
        print(f"  Predicted: {predicted['avg_putts_per_player']:.2f} putts")
        print(f"  Actual:    {avg_putts_per_player:.2f} putts")
        print(f"  Difference: {diff_avg:+.2f} putts ({diff_avg/predicted['avg_putts_per_player']*100:+.2f}%)")
        
        if abs(diff_avg) < 0.5:
            print(f"  Analysis: Within 0.5 putts - EXCEPTIONAL accuracy!")
        elif abs(diff_avg) < 1.0:
            print(f"  Analysis: Within 1 putt - EXCELLENT accuracy!")
        elif abs(diff_avg) < 1.5:
            print(f"  Analysis: Within 1.5 putts - VERY GOOD accuracy!")
        
        # Save results
        results = {
            'timestamp': datetime.now().isoformat(),
            'predicted': predicted,
            'actual': {
                'total_putts': float(total_putts),
                'avg_putts_per_player': float(avg_putts_per_player),
                'avg_putts_per_hole': float(avg_putts_per_hole),
                'field_size': int(len(round1_clean)),
                'min_putts': float(min_putts_total),
                'max_putts': float(max_putts_total),
                'best_player': best_player,
                'worst_player': worst_player
            },
            'comparison': {
                'total_putts_diff': float(diff_total),
                'total_putts_diff_percent': float(diff_total/predicted['total_putts']*100),
                'avg_putts_diff': float(diff_avg),
                'avg_putts_diff_percent': float(diff_avg/predicted['avg_putts_per_player']*100),
                'accuracy_total': float(accuracy_total),
                'accuracy_avg': float(accuracy_avg),
                'overall_accuracy': float(overall_accuracy),
                'rating': rating
            }
        }
        
        with open('final_comparison_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n[SUCCESS] Results saved to 'final_comparison_results.json'")
        
        # Create summary for sharing
        summary = f"""
MASTERS DAY 1 PUTTING STATISTICS COMPARISON
{'='*70}

PREDICTED:
  Total Putts: {predicted['total_putts']:,}
  Avg Putts/Player: {predicted['avg_putts_per_player']:.2f}
  Field Size: {predicted['field_size']}

ACTUAL:
  Total Putts: {total_putts:,.0f}
  Avg Putts/Player: {avg_putts_per_player:.2f}
  Field Size: {len(round1_clean)}

COMPARISON:
  Total Putts Difference: {diff_total:+,.0f} ({diff_total/predicted['total_putts']*100:+.2f}%)
  Avg Putts Difference: {diff_avg:+.2f} ({diff_avg/predicted['avg_putts_per_player']*100:+.2f}%)
  
ACCURACY: {overall_accuracy:.2f}% - {rating}
"""
        
        with open('comparison_summary.txt', 'w') as f:
            f.write(summary)
        
        print(f"[SUCCESS] Summary saved to 'comparison_summary.txt'")
        
        return results
        
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    excel_path = r"C:\Users\SamMcLear\Desktop\putting stats real.xlsx"
    
    print("MASTERS PUTTING STATISTICS COMPARISON TOOL")
    print("Comparing predicted vs actual Day 1 putting statistics")
    print("=" * 70)
    
    results = analyze_actual_putting_data(excel_path)
    
    if results:
        print("\n" + "=" * 70)
        print("ANALYSIS COMPLETE!")
        print("=" * 70)
        print("\nFiles created:")
        print("  - final_comparison_results.json (detailed data)")
        print("  - comparison_summary.txt (shareable summary)")
        
        print("\n" + "=" * 70)
        print(f"FINAL ANSWER:")
        print(f"Prediction Accuracy: {results['comparison']['overall_accuracy']:.2f}%")
        print(f"Rating: {results['comparison']['rating']}")
        print("=" * 70)

# Made with Bob
