#for one input and one output
import gradio as gr

def greet(name):
    return "hello"+name+"!"

demo=gr.Interface(fn=greet, 
                  inputs=gr.Textbox(lines=2, placeholder="Name here..."), 
                  outputs="text")

demo.launch()