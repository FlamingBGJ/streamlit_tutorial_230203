#pythonfile.ipynb notebook
# 프로그램 작성시에는 pythonfile.py
# python3 pythonfile.py 로 실행
# streamlit run <streamlitapp>.py streamlit 파일은 이렇게 실행함
# ctrl+c 로 실행중인 터미널을 중지시킬 수 있다.

import streamlit as st
import pandas as pd

def main():
    st.title("First_App")

    df = pd.DataFrame({
        "first_col":[1,2,3,4],
        "second_col":[10,20,30,40]
    })

    st.write(df)

if __name__ == "__main__":
    main()

