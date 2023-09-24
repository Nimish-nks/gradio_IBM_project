import gradio as gr

def greet(name, is_morning, is_evening, temperature):
    if is_morning:
        salutation = "Bonjour"
    elif is_evening:
        salutation = "Bonsoir"
    greeting = f"{salutation} {name}! It is {temperature} degrees today."
    num = (temperature - 32) * 5 / 9
    celsius = f"{num:.2f}°C"
    return greeting, celsius

with gr.Blocks() as demo:
    name = gr.Textbox(label="Your name")
    is_morning = gr.Checkbox(label="Is_morning")
    is_evening = gr.Checkbox(label="Is_evening")
    temperature = gr.Slider(0, 100, label="Temperature")
    greeting = gr.Textbox(label="Your greeting")
    celsius = gr.Textbox(label="Celsius")
    
    button = gr.Button(value="Greet")
    button.click(fn=greet, 
                 inputs=[name, is_morning, is_evening, temperature],
                 outputs=[greeting, celsius])

demo.launch()
