#!/usr/bin/env python3
"""Setup script for AI-BOT2"""

import os
import subprocess
import sys

def main():
    print("🚀 Setting up AI-BOT2...")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("📝 Creating .env file from template...")
        if os.path.exists('.env.example'):
            with open('.env.example', 'r') as src, open('.env', 'w') as dst:
                dst.write(src.read())
            print("✅ .env file created. Please add your GROQ_API_KEY.")
        else:
            with open('.env', 'w') as f:
                f.write('GROQ_API_KEY=your_groq_api_key_here\n')
            print("✅ .env file created. Please add your GROQ_API_KEY.")
    
    # Install requirements
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return
    
    print("\n🎉 Setup complete!")
    print("📋 Next steps:")
    print("1. Edit .env file and add your GROQ_API_KEY")
    print("2. Run: streamlit run app.py")
    print("3. Open http://localhost:8501 in your browser")

if __name__ == "__main__":
    main()