#!/usr/bin/env python3
"""
Quick test to verify everything is working.
"""

import numpy as np
from stats_cli import DescriptiveStats, HypothesisTests

def test_basic_functionality():
    print("Testing Statistics Toolkit...")
    
    # Test data
    data = np.array([85, 92, 78, 88, 95, 82, 79, 91, 87, 84])
    
    print("\n1. Testing Descriptive Statistics:")
    result = DescriptiveStats.measures_of_center(data, show_steps=False)
    print(f"   Mean: {result['mean']:.2f}")
    print(f"   Median: {result['median']:.2f}")
    
    print("\n2. Testing Hypothesis Test:")
    test_result = HypothesisTests.one_sample_t_test(data, 85, show_steps=False)
    print(f"   t-statistic: {test_result.statistic:.4f}")
    print(f"   p-value: {test_result.p_value:.6f}")
    
    print("\n✅ All basic functionality working!")
    print("\nReady to use! Try:")
    print("  python stats_cli.py")

if __name__ == "__main__":
    test_basic_functionality()
