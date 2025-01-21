from transformers import T5Tokenizer, T5ForConditionalGeneration

# モデルとトークナイザのロード
model_name = "t5-large"  # 他のモデルサイズも使用可能（例：t5-base, t5-large）
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# 曲のタイトルのリスト
titles = [
    "Beatles - Yesterday",
    "Beatles - Let It Be",
    "Beatles - Hey Jude",
    "Beatles - Come Together",
    "Beatles - Help!",
]

# キャプションを生成する関数
def generate_caption(title):
    input_text = f"caption the following English title of songs by the date it composed: {title}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=500, num_beams=50, early_stopping=True)
    caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return caption

# 各タイトルに対してキャプションを生成
for title in titles:
    caption = generate_caption(title)
    print(f"Title: {title}\nCaption: {caption}\n")