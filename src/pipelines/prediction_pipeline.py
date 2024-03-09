import os,sys  
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.logger import logging
from src.exception import CustomException
from transformers import Pipeline,AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,text):
        try:
            tokenizer = AutoTokenizer.from_pretrained("C:\text_summarization_project\artifacts\pegasus-samsum-tokenizer")
            gen_kwargs = {"length_penality" :0.8, "num_beams":8, "max_length":128}
            model_j = AutoModelForSeq2SeqLM.from_pretrained("C:\text_summarization_project\artifacts\pegasus-samsum-model")
            pipe = Pipeline("summarization",model = model_j,tokenizer = tokenizer)
            print("dialogue")
            print(text)
            output = pipe(text,**gen_kwargs)[0]["summary_text"]
            print("summary")
            print(output)
            return output

            

            
        except Exception as e:
            logging.info("exception occured at predictpipeline file")
            raise CustomException(e,sys)

        