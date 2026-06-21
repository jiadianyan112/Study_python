

PLANNER_PROMPT_TEMPLATE = """
你是一个顶级AI规划专家，你的任务是将用户提出的复杂问题拆解成一个由多个简单步骤组成的行动计划。
请确保计划中的每一步都是一个独立、可执行的子任务。并且严格按照逻辑顺序排列。
你的输出必须是一个python列表，列表中每个元素都是一个描述子任务的字符串。

问题：{question}
请严格按照以下格式进行输出，前后缀"```pyhton和```"是必要的：
```python
{"步骤一","步骤二","步骤三"}

```
"""

from llm_client import HelloAgentLLM
import ast


class Planner:
    def __init__(self,llm_client):
        self.llm_client=llm_client

    def plan(self,question:str) ->str:
        """
        根据用户的问题生成一个行动计划。
        """
        prompt = PLANNER_PROMPT_TEMPLATE.format(question=question)

        messages= [{"role":"user","content":prompt}]

        print('---正在生成计划---')
        response_text = self.llm_client.think(messages=messages) or ""

        print(f"---计划已生成：\n{response_text}")

        #解析LLM输出的列表字符串
        try:
            # 找到```python和```之间的内容
            plan_str = response_text.split("```python")[1].split("```")[0].strip()
            # 使用ast.literal_eval来安全地执行字符串，将其转换为Python列表
            plan = ast.literal_eval(plan_str)
            return plan if isinstance(plan,list) else []


        except(ValueError,SyntaxError,IndexError) as e:
            print(f"❌️解析计划时出错：{e}")
            print(f"原始响应：{response_text}")
            return []
        except Exception as e:
            print(f"❌️解析计划时发生未知错误：{e}")
            return []
