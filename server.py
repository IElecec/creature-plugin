from flask import Flask
from flask import request
from flask import send_file
from flask import make_response
import json 
import random

app = Flask(__name__)
attributes = ["水:水属性和水的掌控有关，包括液体的气化","火:火属性和火的掌控有关。包括温度和燃烧","木:木属性和木的掌控有关，与植物的生命现象相伴而生","光:光属性可以掌控光的发射，治疗等。也可以在视觉上引起致盲",
"暗:光属性的对立属性，可以与光属性相互湮灭","金:金属性和常见的金属","土:土属性和大地相关，包括岩石的生成，甚至可以引起陨石","无:无属性异兽大多拥有虚化与吞噬功能，除阴影之地难以见到，疑似大量存在于虚空，实力玄妙莫测"]
characters = ["种族","爱吃的食物","天敌","习性","性格","体型","性格","年龄","性别"]
habitats = [
    "永恒乐园：一片广袤的灰白土地上，矗立着数不清的游乐园，其中的异兽大多呈现类似于游乐器材的形式，也有各种玩偶进行了活化，其中的异兽大多诡异，带有一定的恐怖色彩。其中的异兽大多是暗属性和光属性",
    "炼狱山脉：四处充斥着岩浆的山脉，极高的温度无法让正常的异兽生存，可以在这片极热之地存活的，是大部分火属性异兽，他们大多身躯庞大，皮糙肉厚。",
    "潮海金字塔：位于深海底部的倒金字塔建筑，由远古的神话异兽建筑，其中最下层的居住着这里的皇族异兽，越往浅层则异兽越简单。这里大多生活着水属性异兽",

    "飓风之都：高天之上，透过层层云雾可以看见一座无比巨大被飓风裹挟的城市，其中生活着众多属性的异兽，它们都拥有者较强的飞行能力，能够吞食云雾来成长。",

    "阴影之地：这个星球最南部被完全的黑暗所笼罩，不可观测。栖息在这里的异兽都是暗属性异兽。",

    "北极晨光：这个星球最北部被完全的光明所笼罩，与潮海金字塔、阴影之地接壤，水路环绕富有优良港湾，商业繁荣，是世界商贸中心，汇聚着世界上最会经商的异兽，大多是金属性与光属性",

    "巨木：这片大地的中心有一棵苍天大树，是远古的木属性神话异兽。在这棵树上主要栖息着其它木属性异兽。在巨木的底部存在着许多水、土、暗属性异兽。",

    "迷雾沼泽：南大陆的一处隐秘之地，在外界看来一团巨大的雾霭笼罩了这片地区，进入之后无法分辨方向。这里大多数生存着木属性、水属性、土属性的异兽",

    "虚空：在阴影之地中间一片虚无到极致的实体地点，这里看上去什么都没有，但是曾经进入这里的探险家无一生还，曾有异兽具有虚无吞噬的能力且强得可怕从其中走出。",

]

def make_json_response(data, status_code=200):
    response = make_response(json.dumps(data), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

# @app.route("/select_story", methods=['POST'])
# async def select_story():
#     story_type = request.get_json()['story_type']
#     selected = hgt.selectStory(story_type)
#     title = selected['题目']
#     tangmian = selected['汤面']
#     prompt = f"输出海龟汤故事信息，格式为题目：《{title}》和汤面：{tangmian}, 告诉用户一个只能用是或不是回答的问题示例，然后请用户提问题。"
#     anwser = [title, tangmian]
#     return make_json_response({"story_firstshow": anwser, "prompt": prompt})
# @app.route("/anwser_question", methods=['POST'])
# async def anwser_question():
#     question = request.get_json()['question']
#     tangdi = hgt.cur_story['汤底']
#     prompt = f"你正在玩海龟汤，游戏状态是{hgt.status}， 根据汤底：{tangdi}, 用“是”、“不是”、或“不重要”回答问题：{question}，" \
#           "回答必须只能从“是”、“不是”、或“不重要”这三个里选择。不允许添加内容。"
#     return make_json_response({"message": "我的回答是：", "prompt": prompt})
# @app.route("/add_story", methods=['POST'])
# async def add_story():
#     story = request.get_json()
#     response = hgt.addStory(story)
#     prompt = "不允许添加内容。"
#     return make_json_response({"message": response, "prompt": prompt})
# @app.route("/make_prediction", methods=['POST'])
# async def make_prediction():
#     prediction = request.get_json()['prediction']
#     tangdi = hgt.cur_story['汤底']
#     prompt = f"你正在玩海龟汤, 用户推断完整的故事是：{prediction}，请你根据汤底：{tangdi}，判断用户推断出的故事和汤底是否一直，并只能用“是”或“不是”回答" \
#             "回答必须只能从“是”或“不是”这两个里选择。不允许添加内容。"
#     return make_json_response({"message": "你的判断是：是还是不是。", "prompt": prompt})

@app.route("/generate_pet",methods=['POST'])
async def generate_pet():
    attribute = random.choice(attributes)
    habitat = random.choice(habitats)
    message = "请生成一个全新的物种,并生成一个它的个体"
    prompt = f"描述一下用户与它相遇的场景，但不要告知用户它除了外貌之外的信息。该物种具有该背景:{habitat}，且该生物且具有以下属性{attribute},且具有以下信息:"+"、".join(characters)
    return make_json_response({"message":message,"prompt":prompt})

@app.route("/get_information",methods=['GET'])
async def get_information():
    # pet = request.get_json()['pet']
    prompt = f"将该个人的各种信息'[信息种类]：具体内容'的格式表格的形式分行列举出来,信息包括："+",".join(characters)
    return make_json_response({"pet":"之前生成的异兽","prompt":prompt})

@app.route("/logo.png")
async def plugin_logo():
    return send_file('logo.png', mimetype='image/png')

@app.route("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.host_url
    with open(".well-known/ai-plugin.json", encoding="utf-8") as f:
        text = f.read().replace("PLUGIN_HOST", host)
        return text, 200, {"Content-Type": "application/json"}

@app.route("/.well-known/openapi.yaml")
async def openapi_spec():
    with open(".well-known/openapi.yaml", encoding="utf-8") as f:
        text = f.read()
        return text, 200, {"Content-Type": "text/yaml"}

@app.route("/.well-known/example.yaml")
async def example_spec():
    with open(".well-known/example.yaml", encoding="utf-8") as f:
        text = f.read()
        return text, 200, {"Content-Type": "text/yaml"}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8088)
