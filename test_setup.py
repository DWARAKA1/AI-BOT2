#!/usr/bin/env python3
"""Test script to verify AI-BOT2 setup"""

import os
import sys
from dotenv import load_dotenv

def test_setup():
    print("🧪 Testing AI-BOT2 setup...")
    
    # Test 1: Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file found")
    else:
        print("❌ .env file not found")
        return False
    
    # Test 2: Load environment variables
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    
    if api_key and api_key != "your_groq_api_key_here":
        print("✅ GROQ_API_KEY configured")
    else:
        print("❌ GROQ_API_KEY not configured properly")
        return False
    
    # Test 3: Check required packages
    try:
        import streamlit
        import groq
        print("✅ Required packages installed")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        return False
    
    # Test 4: Test Groq connection
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        print("✅ Groq client initialized")
    except Exception as e:
        print(f"❌ Groq client error: {e}")
        return False
    
    print("\n🎉 All tests passed! Your setup is ready.")
    print("Run: streamlit run app.py")
    return True

if __name__ == "__main__":
    success = test_setup()
    sys.exit(0 if success else 1)