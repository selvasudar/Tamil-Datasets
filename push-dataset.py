from datasets import load_dataset, Dataset
from huggingface_hub import login

login("<Hugging Face Token>")

dataset = Dataset.from_json("athichoodi.jsonl")
dataset.push_to_hub("Selvakumarduraipandian/Aathichoodi")
print("Dataset pushed to the hub!")