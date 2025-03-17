from flask import Flask, request, jsonify
import random

app = Flask(__name__)

protein_meals = [
    "닭가슴살 샐러드", "소고기 스테이크", "연어 스테이크", "닭가슴살 김밥", 
    "두부 스크램블", "참치 샌드위치", "계란말이 도시락", "삼계탕"
]

@app.route("/", methods=["GET"])
def home():
    return "카카오톡 오픈채팅봇 작동 중!"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("userRequest", {}).get("utterance", "").strip()
    
    if "점심" in user_message or "뭐 먹지" in user_message:
        random_menu = random.choice(protein_meals)
        response_text = f"오늘의 추천 단백질 메뉴는 {random_menu} 입니다!"
    else:
        response_text = "점심 메뉴가 궁금하면 '점심 뭐 먹지?' 라고 물어봐!"

    response = {
        "version": "2.0",
        "template": {
            "outputs": [{"simpleText": {"text": response_text}}]
        }
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 
