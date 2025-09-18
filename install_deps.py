#!/usr/bin/env python3
"""
Installation script for xsukax EN-AR Offline Translator
This script installs all required dependencies and downloads translation models
"""

import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install {package}: {e}")
        return False

def download_models():
    """Download the translation models"""
    try:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        
        print("\n📥 Downloading English to Arabic model...")
        # English to Arabic model
        en_ar_model_name = "Helsinki-NLP/opus-mt-en-ar"
        en_ar_tokenizer = AutoTokenizer.from_pretrained(en_ar_model_name)
        en_ar_model = AutoModelForSeq2SeqLM.from_pretrained(en_ar_model_name)
        
        # Save models locally
        os.makedirs("models", exist_ok=True)
        en_ar_tokenizer.save_pretrained("models/en-ar-tokenizer")
        en_ar_model.save_pretrained("models/en-ar-model")
        print("✓ English to Arabic model downloaded and saved")
        
        print("\n📥 Downloading Arabic to English model...")
        # Arabic to English model
        ar_en_model_name = "Helsinki-NLP/opus-mt-ar-en"
        ar_en_tokenizer = AutoTokenizer.from_pretrained(ar_en_model_name)
        ar_en_model = AutoModelForSeq2SeqLM.from_pretrained(ar_en_model_name)
        
        ar_en_tokenizer.save_pretrained("models/ar-en-tokenizer")
        ar_en_model.save_pretrained("models/ar-en-model")
        print("✓ Arabic to English model downloaded and saved")
        
        return True
    except Exception as e:
        print(f"✗ Failed to download models: {e}")
        return False

def main():
    print("🚀 Starting installation of xsukax EN-AR Offline Translator dependencies...\n")
    
    # List of required packages
    packages = [
        "flask",
        "flask-cors", 
        "transformers",
        "torch",
        "sentencepiece",
        "sacremoses",
        "nltk"
    ]
    
    print("📦 Installing Python packages...")
    failed_packages = []
    
    for package in packages:
        if not install_package(package):
            failed_packages.append(package)
    
    if failed_packages:
        print(f"\n⚠️  Failed to install: {', '.join(failed_packages)}")
        print("Please install them manually using: pip install <package_name>")
        return False
    
    print("\n✓ All packages installed successfully!")
    
    # Download NLTK data for sentence splitting
    try:
        import nltk
        print("\n📚 Downloading NLTK data...")
        nltk.download('punkt', quiet=True)
        print("✓ NLTK punkt tokenizer downloaded")
    except Exception as e:
        print(f"⚠️  Failed to download NLTK data: {e}")
    
    # Download translation models
    print("\n🤖 Downloading AI translation models...")
    if not download_models():
        print("\n⚠️  Failed to download models. Please check your internet connection.")
        return False
    
    print("\n🎉 Installation completed successfully!")
    print("\nNext steps:")
    print("1. Run: python translator_api.py")
    print("2. Open translator.html in your browser")
    print("3. Start translating offline with xsukax!")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n💥 Unexpected error: {e}")
        sys.exit(1)