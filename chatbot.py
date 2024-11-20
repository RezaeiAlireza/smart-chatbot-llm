from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import gradio as gr

# Load the model and tokenizer
model_name = "distilgpt2"  # Lightweight GPT-2 model
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define the chatbot function
def chatbot_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Create a Gradio interface
iface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(label="Enter your message"),
    outputs=gr.Textbox(label="Bot response"),
    title="Smart Chatbot"
)

# Run the interface
if __name__ == "__main__":
    iface.launch()
