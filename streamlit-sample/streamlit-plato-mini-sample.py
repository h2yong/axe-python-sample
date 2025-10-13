import streamlit as st
from streamlit_chat import message
from utils import select_response
# 加载模型
from paddlenlp.transformers import UnifiedTransformerTokenizer
from paddlenlp.transformers import UnifiedTransformerLMHeadModel

model_name = 'plato-mini'
model = UnifiedTransformerLMHeadModel.from_pretrained(model_name)
tokenizer = UnifiedTransformerTokenizer.from_pretrained(model_name)

st.set_page_config(
    page_title="PLATO-MINI Chat - Demo",
    page_icon=":robot:"
)

st.header("PLATO-MINI Chat - Demo")
st.markdown("[Github](https://github.com/ai-yash/st-chat)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(history):
    inputs = tokenizer.dialogue_encode(
        history, add_start_token_as_response=True, return_tensors=True, is_split_into_words=False
    )
    inputs["input_ids"] = inputs["input_ids"].astype("int64")
    ids, scores = model.generate(
        input_ids=inputs["input_ids"],
        token_type_ids=inputs["token_type_ids"],
        position_ids=inputs["position_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=64,
        min_length=1,
        decode_strategy="sampling",
        temperature=1.0,
        top_k=5,
        top_p=1.0,
        num_beams=0,
        length_penalty=1.0,
        early_stopping=False,
        num_return_sequences=20,
    )
    max_dec_len = 64
    num_return_sequences = 20
    bot_response = select_response(
        ids, scores, tokenizer, max_dec_len, num_return_sequences, keep_space=False
    )[0]
    return bot_response

def get_text():
    input_text = st.text_input("用户: ","你好！", key="input")
    return input_text

history = []
user_input = get_text()
history.append(user_input)
if user_input:
    output = query(history)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    history.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
