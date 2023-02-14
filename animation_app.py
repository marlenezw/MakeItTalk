
import os 
import gradio as gr
from PIL import Image as im
from scipy.io.wavfile import write

  
def generateVideo(input_img, input_audio): 
    
    print(f'this is the input image{input_img}')
    print(f'this is the input audio{input_audio}')

    data = im.fromarray(input_img)
      
    # saving the final output 
    # as a PNG file
    data.save('examples/in_image.jpg')

    write('examples/in_audio.wav', input_audio[0], input_audio[1])

    input_img = 'in_image.jpg'
    input_audio = 'in_audio.wav'

    os.system(f"python3 main_end2end.py --jpg {input_img}") #add image 

    video_name = 'examples/in_image_pred_fls_in_audio_audio_embed.mp4'

    return video_name


demo = gr.Interface(
    fn=generateVideo,
    inputs=[gr.Image(shape=(256, 256)), gr.Audio(), ],
    outputs= gr.Video().style(height=256, width=256),
    examples=[["examples/marlene_v2.jpg","examples/M6_04_16k.wav"]], 
        
)


demo.launch()