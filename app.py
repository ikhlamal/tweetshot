import subprocess
import streamlit as st

# Mengambil screenshot dari tweet
tweet_url = "https://twitter.com/jack/status/20"
try:
    subprocess.run(["tweetcapture", tweet_url], check=True)
    print("Screenshot tweet berhasil diambil!")
except subprocess.CalledProcessError as e:
    print("Error:", e)
