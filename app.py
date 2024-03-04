import subprocess
import streamlit as st

# URL tweet yang ingin diambil screenshotnya
tweet_url = "https://twitter.com/hideo_kojima_en/status/1002107372091817984"

# Menjalankan tweetshot menggunakan subprocess
try:
    subprocess.run(["tweetshot", tweet_url], check=True)
    st.write("Screenshot berhasil diambil!")
except subprocess.CalledProcessError as e:
    print("Error:", e)
