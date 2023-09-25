from transformers import pipeline
import gradio as gr


model=pipeline('text-generation')

def predict(prompt):
    prediction=model(prompt)[0]["generated_text"]
    return prediction

demo=gr.Interface(fn=predict,
                  inputs="text",
                  outputs="text")

demo.launch(server_name="0.0.0.0")