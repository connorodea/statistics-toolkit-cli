#!/usr/bin/env python3
"""
Statistics Toolkit CLI
A comprehensive command-line statistics learning and analysis tool.

Usage: python stats_cli.py [command] [options]
"""

import sys
import os
import json
import csv
import argparse
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path

# =============================================================================
# Configuration and Data Classes
# =============================================================================

@dataclass
class StatResult:
    """Container for statistical test results."""
    test_name: str
    statistic: float
    p_value: float
    critical_value: Optional[float] = None
    confidence_interval: Optional[Tuple[float, float]] = None
    interpretation: str = ""
    steps: List[str] = None

class DataManager:
    """Handles data loading, saving, and management."""
    
    def __init__(self):
        self.data_dir = Path.home() / ".statstoolkit"
        self.data_dir.mkdir(exist_ok=True)
        self.current_data = {}
    
    def load_csv(self, filepath: str, column: str = None) -> np.ndarray:
        """Load data from CSV file."""
        try:
            df = pd.read_csv(filepath)
            if column:
                return df[column].dropna().values
            else:
                return df.select_dtypes(include=[np.number]).dropna().values
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None
    
    def save_data(self, name: str, data: np.ndarray):
        """Save data array to file."""
        filepath = self.data_dir / f"{name}.npy"
        np.save(filepath, data)
        print(f"Data saved as '{name}' in {filepath}")
    
    def load_data(self, name: str) -> Optional[np.ndarray]:
        """Load saved data array."""
        filepath = self.data_dir / f"{name}.npy"
        if filepath.exists():
            return np.load(filepath)
        return None
    
    def list_saved_data(self) -> List[str]:
        """List all saved data files."""
        return [f.stem for f in self.data_dir.glob("*.npy")]

# =============================================================================
# Descriptive Statistics Module
# =============================================================================

class DescriptiveStats:
    """Descriptive statistics calculations with step-by-step explanations."""
    
    @staticmethod
    def measures_of_center(data: np.ndarray, show_steps: bool = True) -> Dict:
        """Calculate and explain measures of center."""
        n = len(data)
        
        if show_steps:
            print("\n=== MEASURES OF CENTER ===")
            print(f"Sample size: n = {n}")
            print(f"Data: {data}")
        
        # Mean
        data_sum = np.sum(data)
        mean = np.mean(data)
        
        if show_steps:
            print(f"\nMEAN CALCULATION:")
            print(f"x̄ = Σx/n = {data_sum}/{n} = {mean:.4f}")
        
        # Median
        sorted_data = np.sort(data)
        median = np.median(data)
        
        if show_steps:
            print(f"\nMEDIAN CALCULATION:")
            print(f"Sorted data: {sorted_data}")
            if n % 2 == 0:
                mid1, mid2 = sorted_data[n//2-1], sorted_data[n//2]
                print(f"n is even: median = ({mid1} + {mid2})/2 = {median:.4f}")
            else:
                print(f"n is odd: median = {sorted_data[n//2]:.4f}")
        
        # Mode (for discrete data)
        values, counts = np.unique(data, return_counts=True)
        max_count = np.max(counts)
        modes = values[counts == max_count]
        
        if show_steps:
            print(f"\nMODE:")
            if len(modes) == 1:
                print(f"Mode = {modes[0]:.4f} (appears {max_count} times)")
            elif len(modes) == len(data):
                print("No mode (all values appear once)")
            else:
                print(f"Modes = {modes} (each appears {max_count} times)")
        
        return {
            'mean': mean,
            'median': median,
            'mode': modes,
            'n': n
        }
    
    @staticmethod
    def measures_of_spread(data: np.ndarray, show_steps: bool = True) -> Dict:
        """Calculate and explain measures of spread."""
        n = len(data)
        mean = np.mean(data)
        
        if show_steps:
            print("\n=== MEASURES OF SPREAD ===")
            print(f"Data: {data}")
            print(f"Mean: x̄ = {mean:.4f}")
        
        # Variance and Standard Deviation
        deviations = data - mean
        squared_deviations = deviations ** 2
        sum_squared_dev = np.sum(squared_deviations)
        
        # Sample variance and std dev
        variance = np.var(data, ddof=1)
        std_dev = np.std(data, ddof=1)
        
        if show_steps:
            print(f"\nVARIANCE CALCULATION:")
            print(f"Deviations from mean: {deviations}")
            print(f"Squared deviations: {squared_deviations}")
            print(f"Σ(x - x̄)² = {sum_squared_dev:.4f}")
            print(f"s² = Σ(x - x̄)²/(n-1) = {sum_squared_dev:.4f}/{n-1} = {variance:.4f}")
            print(f"\nSTANDARD DEVIATION:")
            print(f"s = √(s²) = √{variance:.4f} = {std_dev:.4f}")
        
        # Range
        data_range = np.max(data) - np.min(data)
        
        if show_steps:
            print(f"\nRANGE:")
            print(f"Range = max - min = {np.max(data):.4f} - {np.min(data):.4f} = {data_range:.4f}")
        
        return {
            'variance': variance,
            'std_dev': std_dev,
            'range': data_range,
            'min': np.min(data),
            'max': np.max(data)
        }
    
    @staticmethod
    def five_number_summary(data: np.ndarray, show_steps: bool = True) -> Dict:
        """Calculate five-number summary and check for outliers."""
        sorted_data = np.sort(data)
        
        q1 = np.percentile(data, 25)
        median = np.percentile(data, 50)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        
        if show_steps:
            print("\n=== FIVE-NUMBER SUMMARY ===")
            print(f"Sorted data: {sorted_data}")
            print(f"Min = {np.min(data):.4f}")
            print(f"Q1 = {q1:.4f}")
            print(f"Median = {median:.4f}")
            print(f"Q3 = {q3:.4f}")
            print(f"Max = {np.max(data):.4f}")
            print(f"\nIQR = Q3 - Q1 = {q3:.4f} - {q1:.4f} = {iqr:.4f}")
        
        # Outlier detection
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        outliers = data[(data < lower_fence) | (data > upper_fence)]
        
        if show_steps:
            print(f"\nOUTLIER DETECTION:")
            print(f"Lower fence = Q1 - 1.5×IQR = {q1:.4f} - 1.5×{iqr:.4f} = {lower_fence:.4f}")
            print(f"Upper fence = Q3 + 1.5×IQR = {q3:.4f} + 1.5×{iqr:.4f} = {upper_fence:.4f}")
            if len(outliers) > 0:
                print(f"Outliers: {outliers}")
            else:
                print("No outliers detected")
        
        return {
            'min': np.min(data),
            'q1': q1,
            'median': median,
            'q3': q3,
            'max': np.max(data),
            'iqr': iqr,
            'outliers': outliers,
            'lower_fence': lower_fence,
            'upper_fence': upper_fence
        }

# =============================================================================
# Hypothesis Testing Module
# =============================================================================

class HypothesisTests:
    """Comprehensive hypothesis testing with step-by-step explanations."""
    
    @staticmethod
    def one_sample_t_test(data: np.ndarray, mu0: float, alpha: float = 0.05,
                         alternative: str = 'two-sided', show_steps: bool = True) -> StatResult:
        """One-sample t-test with full explanation."""
        n = len(data)
        sample_mean = np.mean(data)
        sample_std = np.std(data, ddof=1)
        
        if show_steps:
            print(f"\n=== ONE-SAMPLE T-TEST ===")
            print(f"Sample size: n = {n}")
            print(f"Sample mean: x̄ = {sample_mean:.4f}")
            print(f"Sample std dev: s = {sample_std:.4f}")
            print(f"Hypothesized mean: μ₀ = {mu0}")
            print(f"Significance level: α = {alpha}")
        
        # Hypotheses
        if show_steps:
            print(f"\nSTEP 1: HYPOTHESES")
            print(f"H₀: μ = {mu0}")
            if alternative == 'two-sided':
                print(f"H₁: μ ≠ {mu0}")
            elif alternative == 'greater':
                print(f"H₁: μ > {mu0}")
            else:
                print(f"H₁: μ < {mu0}")
        
        # Test statistic
        t_stat = (sample_mean - mu0) / (sample_std / np.sqrt(n))
        df = n - 1
        
        if show_steps:
            print(f"\nSTEP 2: TEST STATISTIC")
            print(f"t = (x̄ - μ₀)/(s/√n)")
            print(f"t = ({sample_mean:.4f} - {mu0})/({sample_std:.4f}/√{n})")
            print(f"t = {t_stat:.4f} (df = {df})")
        
        # P-value
        if alternative == 'two-sided':
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        elif alternative == 'greater':
            p_value = 1 - stats.t.cdf(t_stat, df)
        else:
            p_value = stats.t.cdf(t_stat, df)
        
        # Critical value
        if alternative == 'two-sided':
            critical_value = stats.t.ppf(1 - alpha/2, df)
        else:
            critical_value = stats.t.ppf(1 - alpha, df)
        
        if show_steps:
            print(f"\nSTEP 3: P-VALUE")
            print(f"P-value = {p_value:.6f}")
            print(f"Critical value = ±{critical_value:.4f}" if alternative == 'two-sided' 
                  else f"Critical value = {critical_value:.4f}")
        
        # Decision
        reject_null = p_value < alpha
        
        if show_steps:
            print(f"\nSTEP 4: DECISION")
            print(f"α = {alpha}")
            if reject_null:
                print(f"P-value ({p_value:.6f}) < α ({alpha}): REJECT H₀")
                print("Evidence suggests the mean is significantly different from the hypothesized value")
            else:
                print(f"P-value ({p_value:.6f}) ≥ α ({alpha}): FAIL TO REJECT H₀")
                print("Insufficient evidence to conclude the mean differs from the hypothesized value")
        
        interpretation = f"{'Reject' if reject_null else 'Fail to reject'} H₀ at α = {alpha}"
        
        return StatResult(
            test_name="One-Sample t-test",
            statistic=t_stat,
            p_value=p_value,
            critical_value=critical_value,
            interpretation=interpretation
        )

# =============================================================================
# Command Line Interface
# =============================================================================

class StatsCLI:
    """Main command-line interface for the statistics toolkit."""
    
    def __init__(self):
        self.data_manager = DataManager()
        self.descriptive = DescriptiveStats()
        self.hypothesis = HypothesisTests()
    
    def main_menu(self):
        """Display main menu and handle user input."""
        while True:
            print("\n" + "="*60)
            print("        STATISTICS TOOLKIT - MAIN MENU")
            print("="*60)
            print("1.  Descriptive Statistics")
            print("2.  Hypothesis Testing")
            print("3.  Data Management")
            print("4.  Sample Data Demo")
            print("5.  Help")
            print("0.  Exit")
            print("="*60)
            
            try:
                choice = input("Enter your choice (0-5): ").strip()
                
                if choice == '0':
                    print("Thank you for using the Statistics Toolkit!")
                    break
                elif choice == '1':
                    self.descriptive_menu()
                elif choice == '2':
                    self.hypothesis_menu()
                elif choice == '3':
                    self.data_management_menu()
                elif choice == '4':
                    self.sample_data_demo()
                elif choice == '5':
                    self.help_menu()
                else:
                    print("Invalid choice. Please enter a number from 0-5.")
                    
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def descriptive_menu(self):
        """Descriptive statistics submenu."""
        print("\n=== DESCRIPTIVE STATISTICS ===")
        data = self.get_data_input()
        if data is None:
            return
        
        print("Choose analysis:")
        print("1. Measures of Center")
        print("2. Measures of Spread")
        print("3. Five-Number Summary")
        print("4. All Statistics")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            self.descriptive.measures_of_center(data)
        elif choice == '2':
            self.descriptive.measures_of_spread(data)
        elif choice == '3':
            self.descriptive.five_number_summary(data)
        elif choice == '4':
            self.descriptive.measures_of_center(data)
            self.descriptive.measures_of_spread(data)
            self.descriptive.five_number_summary(data)
    
    def hypothesis_menu(self):
        """Hypothesis testing submenu."""
        print("\n=== HYPOTHESIS TESTING ===")
        print("1. One-Sample t-test")
        
        choice = input("Enter choice (1): ").strip()
        
        if choice == '1':
            data = self.get_data_input()
            if data is None:
                return
            mu0 = float(input("Enter hypothesized mean (μ₀): "))
            alpha = float(input("Enter significance level (default 0.05): ") or "0.05")
            
            alt_choice = input("Alternative hypothesis (1=two-sided, 2=greater, 3=less): ").strip()
            alternative = {'1': 'two-sided', '2': 'greater', '3': 'less'}.get(alt_choice, 'two-sided')
            
            result = self.hypothesis.one_sample_t_test(data, mu0, alpha, alternative)
    
    def data_management_menu(self):
        """Data management submenu."""
        print("\n=== DATA MANAGEMENT ===")
        print("1. List saved data")
        print("2. Save current data")
        print("3. Load saved data")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            saved_data = self.data_manager.list_saved_data()
            if saved_data:
                print("Saved datasets:")
                for i, name in enumerate(saved_data, 1):
                    print(f"{i}. {name}")
            else:
                print("No saved data found.")
    
    def sample_data_demo(self):
        """Demonstrate with sample data."""
        print("\n=== SAMPLE DATA DEMONSTRATION ===")
        
        # Generate sample test scores
        np.random.seed(42)
        test_scores = np.array([85, 92, 78, 88, 95, 82, 79, 91, 87, 84])
        
        print("Using sample test scores:", test_scores)
        print("\nRunning complete analysis...")
        
        # Run all analyses
        self.descriptive.measures_of_center(test_scores)
        self.descriptive.measures_of_spread(test_scores)
        self.descriptive.five_number_summary(test_scores)
        
        # Hypothesis test
        print("\n" + "="*50)
        print("HYPOTHESIS TEST EXAMPLE")
        print("Testing if mean test score = 85")
        print("="*50)
        
        result = self.hypothesis.one_sample_t_test(test_scores, 85, 0.05, 'two-sided')
    
    def help_menu(self):
        """Display help information."""
        print("\n=== STATISTICS TOOLKIT HELP ===")
        print("This toolkit provides step-by-step statistical analysis.")
        print("\nFeatures:")
        print("• Descriptive Statistics - Mean, median, variance, etc.")
        print("• Hypothesis Testing - t-tests with full explanations")
        print("• Data Management - Save and load datasets")
        print("• Educational Focus - Shows all calculation steps")
        print("\nData Input:")
        print("• Manual entry: Enter numbers separated by spaces")
        print("• CSV files: Load data from spreadsheet files")
        print("• Saved data: Use previously saved datasets")
        print("\nFor more help, visit the documentation or examples folder.")
    
    def get_data_input(self) -> Optional[np.ndarray]:
        """Get data input from user."""
        print("\nData input options:")
        print("1. Enter values manually")
        print("2. Load from CSV file")
        print("3. Use saved data")
        
        choice = input("Choose option (1-3): ").strip()
        
        if choice == '1':
            data_str = input("Enter values separated by spaces or commas: ")
            try:
                # Handle both space and comma separators
                data_str = data_str.replace(',', ' ')
                data = np.array([float(x) for x in data_str.split()])
                return data
            except ValueError:
                print("Invalid data format. Please enter numeric values.")
                return None
                
        elif choice == '2':
            filepath = input("Enter CSV file path: ").strip()
            column = input("Enter column name (or press Enter for first numeric column): ").strip() or None
            return self.data_manager.load_csv(filepath, column)
            
        elif choice == '3':
            saved_data = self.data_manager.list_saved_data()
            if not saved_data:
                print("No saved data found.")
                return None
            
            print("Saved datasets:")
            for i, name in enumerate(saved_data, 1):
                print(f"{i}. {name}")
            
            try:
                idx = int(input("Choose dataset: ")) - 1
                if 0 <= idx < len(saved_data):
                    return self.data_manager.load_data(saved_data[idx])
            except ValueError:
                pass
            
            print("Invalid selection.")
            return None
        
        return None

def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(description="Statistics Toolkit CLI")
    parser.add_argument("--version", action="version", version="Statistics Toolkit 1.0")
    parser.add_argument("--interactive", "-i", action="store_true", 
                       help="Start interactive mode")
    parser.add_argument("--demo", action="store_true", 
                       help="Run sample data demonstration")
    
    args = parser.parse_args()
    
    cli = StatsCLI()
    
    if args.demo:
        cli.sample_data_demo()
    elif args.interactive or len(sys.argv) == 1:
        print("Welcome to the Statistics Toolkit!")
        print("A comprehensive tool for statistical analysis and learning.")
        cli.main_menu()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
