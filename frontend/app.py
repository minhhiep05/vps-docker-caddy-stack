from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return """
    <html>
      <head><title>DevOps Hiep</title></head>
      <body style="font-family: sans-serif; text-align:center; margin-top: 100px;">
        <h1>🚀 Xin chào chuyên gia!</h1>
        <p>Đây là app Flask chạy trên devopshiep.shop</p>
      </body>
    </html>
    """
 
@app.route("/health")
def health():
    return {"status": "ok"}
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 
