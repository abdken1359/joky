from quart import Blueprint,render_template
a=Blueprint("app",__name__)
@a.get("/")
async def home():
    return await render_template('index.html')