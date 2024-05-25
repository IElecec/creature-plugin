from flask import Flask
from flask import request
from flask import send_file
app = Flask(__name__)

def make_json_response(data, status_code=200):
    response = make_response(json.dumps(data), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/select_story", methods=['POST'])
async def select_story():
    story_type = request.get_json()['story_type']
    selected = hgt.selectStory(story_type)
    title = selected['题目']
    tangmian = selected['汤面']
    prompt = f"输出海龟汤故事信息，格式为题目：《{title}》和汤面：{tangmian}, 告诉用户一个只能用是或不是回答的问题示例，然后请用户提问题。"
    anwser = [title, tangmian]
    return make_json_response({"story_firstshow": anwser, "prompt": prompt})
@app.route("/anwser_question", methods=['POST'])
async def anwser_question():
    question = request.get_json()['question']
    tangdi = hgt.cur_story['汤底']
    prompt = f"你正在玩海龟汤，游戏状态是{hgt.status}， 根据汤底：{tangdi}, 用“是”、“不是”、或“不重要”回答问题：{question}，" \
              "回答必须只能从“是”、“不是”、或“不重要”这三个里选择。不允许添加内容。"
    return make_json_response({"message": "我的回答是：", "prompt": prompt})
@app.route("/add_story", methods=['POST'])
async def add_story():
    story = request.get_json()
    response = hgt.addStory(story)
    prompt = "不允许添加内容。"
    return make_json_response({"message": response, "prompt": prompt})
@app.route("/make_prediction", methods=['POST'])
async def make_prediction():
    prediction = request.get_json()['prediction']
    tangdi = hgt.cur_story['汤底']
    prompt = f"你正在玩海龟汤, 用户推断完整的故事是：{prediction}，请你根据汤底：{tangdi}，判断用户推断出的故事和汤底是否一直，并只能用“是”或“不是”回答" \
            "回答必须只能从“是”或“不是”这两个里选择。不允许添加内容。"
    return make_json_response({"message": "你的判断是：是还是不是。", "prompt": prompt})
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
    app.run(debug=True, host='139.224.200.123', port=8088)
