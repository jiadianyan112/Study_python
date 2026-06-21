from serpapi import SerpApiClient
import os
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
            "q":"query",
            "api_key":api_key,
            "gl":"cn", #Geo Location（地理位置/国家地区）
            "hl":"zh-cn" #Host Language（主机语言/界面语言）
        }
        client= SerpApiClient(params)
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
