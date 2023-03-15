import streamlit as st
import time

st.title("streamlit 超入門")

st.write("progress bar")
"start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("お問い合わせ内容を書く")
# text = st.text_input(
#     "あなたの趣味は"
# )

# condition = st.slider(
#     "あなたの調子は",
#     0,100,50
# )

# "あなたの今の調子は", condition

#     "あなたが好きな数字を教えてください",
#     list(range(1,11))
# )   
# "あなたの好きな数字は", option, "です"
# if st.checkbox("show image"):
#     img = Image.open("cat.jpg")
#     st.image(img, caption ="cat", use_column_width = True)
