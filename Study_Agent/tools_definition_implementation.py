from typing import Dict,Any
from serpapi import GoogleSearch
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

def search(query:str) -> str:
    """
    基于SerpApi的智能体网络引擎工具。
    智能解析搜索结果，优先返回直接答案或知识图谱信息。
    """

    print(f'正在搜索：{query}')

    try:
        api_key=os.getenv("SERPAPI_API_KEY")
        params = {
            "engine":"google",
            "q":query,
            "api_key":api_key,
            "gl":"cn", #Geo Location（地理位置/国家地区）
            "hl":"zh-cn" #Host Language（主机语言/界面语言）
        }
        client= GoogleSearch(params)
        results = client.get_dict()
        if "answer_box_list" in results:
            return "\n".join(results["answer_box_list"])
        if "answer_box" in results and "answer"in results["answer_box"]:
            return results["answer_box"]["answer"]
        if "knowledge_graph" in results and "description" in results["knowledge_graph"]:
            return results["knowledge_graph"]["description"]
        if "organic_results" in results and results["organic_results"]:
            snippets = [
                f"[{i+1}] {res.get('title','')}\n{res.get('snippet','')}" 
                for i,res in enumerate(results["organic_results"][:3])
            ]
            return "\n\n".join(snippets)
        return f"对不起，没有找到关于'{query}'的信息"

    except Exception as e:
        return f"搜索时发生错误{e}"

class ToolExecutor:
    """
    工具执行器,负责管理和执行工具。
    """
    def __init__(self):
        self.tools:Dict[str,Dict[str,Any]]={}

    def registerTool(self,name:str,description:str,func:callable):
        """
        向工具管理器注册一个新工具
        """
        if name in self.tools:
            print(f"工具'{name}'已存在,将被覆盖。")

        self.tools[name]={"description":description,"func":func}    
        print(f"工具{name}已注册。")
    

    def getTool(self,name:str) ->callable:
        """
        根据名称获取一个工具的执行函数
        """
        return self.tools.get(name,{}).get("func")
    
    def getAvailableTools(self)->str:
        """
        获取所有可用工具的格式化字符串
        """
        return "\n".join([f"-{name}:{info['description']}"
                          for name,info in self.tools.items()])


#-----工具初始化和使用示例-----------

if __name__ =='__main__':
    #1、初始化工具执行器
    toolexecutor=ToolExecutor()
    
    #注册搜索工具
    search_description =  "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    toolexecutor.registerTool('search',search_description,search)

    #打印可用工具
    print("\n------可用的工具-------")
    print(toolexecutor.getAvailableTools())

    #智能体调用工具
    tool_name="search"
    tool_input=str(input("请输入要询问的问题："))
    tool_function=toolexecutor.getTool(tool_name)
    if tool_function:
        observation = tool_function(tool_input)
        print("-----观察------")
        print(observation)
    else:
        print(f"未找到名为{tool_name}的工具")