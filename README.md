# Generate Prompts and Images with Given Input

A user interface that creates example prompts based on input and image based on selected prompt. Created using Azure OpenAI API.

## Environment
1. Install all dependency
```
pip install -r requirements.txt
```

2. Set up secrets.toml to store openai api key
   - create a secrets.toml file in directory.
   - create a Azure openai account and set up a key and endpoint, instuction can be found [here]([https://platform.openai.com/api-keys](https://learn.microsoft.com/en-us/azure/ai-services/openai/))
   - copy the following code, replace {} with your own information in secrets.toml
```
endpoint = "https://{resource name}.openai.azure.com/"
key = "{your key}"
completionendpoint = "https://{resource name}.openai.azure.com/openai/deployments/{model}/chat/completions?api-version={version}"
adminpassword = "{custom password for login}"
```

## Run the App
Run the streamlit command
```
streamlit run app.py 
```
The web will be on http://localhost:8501/ if run on own computer or server.

Enter password to enter (password retrieved from adminpassword in secrets.toml)
![image](https://github.com/user-attachments/assets/22e9e425-ea8f-4305-b424-673f99e7cf35)

Enter a description and generate sample prompts.
![image2](https://github.com/user-attachments/assets/5f92b4cb-79ee-4ec0-a0bb-f6a8342b38d2)

Enter a sample prompt or type in your own to generate image.
![image3](https://github.com/user-attachments/assets/bdca880c-28f7-49dc-b04f-c468e91f0430)

## HuggingFace Space
Application is on [huggingface space](https://huggingface.co/spaces/Jaspertw177/ImageGenerator)

Password required.

