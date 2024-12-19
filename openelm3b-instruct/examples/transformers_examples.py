# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="apple/OpenELM-3B-Instruct", trust_remote_code=True)

# Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("apple/OpenELM-3B-Instruct", trust_remote_code=True)
