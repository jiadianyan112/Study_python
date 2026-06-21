import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List,Dict

load_dotenv()

class HelloAgentLLM:
    def __init__(self,model:str = None,apiKey:str = None,baseURL:str=None,timeout:int=None):
        """
        初始化客户端。优先使用传入参数，如果未提供，则从环境变量加载。
        """
        self.model = model or os.getenv("LLM_MODEL_ID")
        apiKey =apiKey or os.getenv("LLM_API_KEY")
        baseURL=baseURL or os.getenv("LLM_BASE_URL")
        timeout = timeout or int(os.getenv("LLM_timeout",60))

        if not all([self.model,apiKey,baseURL]):
            raise ValueError("模型ID、API密钥和服务地址必须被提供或在.env文件中定义。")
        
        self.client = OpenAI(api_key=apiKey,base_url=baseURL,timeout=timeout)


    def think(self,messages:List[Dict[str,str]],temperature:float = 0) ->str:
        print(f'🧠正在调用{self.model}模型进行思考······')

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True
            )
            print("✅️大语言模型响应成功：")
            collected_content = []
            for chunk in response:
                if not chunk.choices:
                    continue
                content=chunk.choices[0].delta.content or ""
                print(content,end="",flush=True)
                collected_content.append(content)
            print()
            return "".join(collected_content)

        except Exception as e:
            print(f'调用{self.model} API时发生错误:{e}')
            return None
        
#-----------客户端使用----------
if __name__ == '__main__':
    try:
        llmClient = HelloAgentLLM()
        exampleMessages=[
            {"role":"system","content":"你是高级产品经理"},
            {"role":"user","content":"写一个音乐播放器的PRD"}
        ]
        print("调用大语言模型中······")
        responseText=llmClient.think(exampleMessages,0.6)
        if responseText:
            print("\n---模型响应---")
            print(responseText)
    except ValueError as e:
        print(e)
    