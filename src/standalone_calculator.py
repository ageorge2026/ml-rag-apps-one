#!/usr/bin/env python3
"""
Standalone Calculator Service
Acts as an infrastructural placeholder for your upcoming LangChain RAG logic.
Includes built-in pytest functions so the multi-stage Docker builder can validate it.
"""
import sys

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# =====================================================================
# SYSTEM ENTRYPOINT
# =====================================================================
if __name__ == "__main__":
    print("--- Simulating MLOps Application Runtime ---")
    print("Executing core system smoke checks...")
    
    # Run a quick internal verification loop
    assert add(10, 5) == 15
    assert subtract(10, 5) == 5
    assert multiply(10, 5) == 50
    assert divide(10, 5) == 2.0
    
    print("All internal software verifications: PASSED.")
    print("Application sitting in execution state. Exiting cleanly.")
    sys.exit(0)

# =====================================================================
# PYTEST UNIT TEST SUITE (Executed during Stage 1 Docker Build)
# =====================================================================
def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtraction():
    assert subtract(5, 3) == 2

def test_multiplication():
    assert multiply(3, 4) == 12

def test_division():
    assert divide(10, 2) == 5.0
