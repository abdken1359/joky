from quart import Blueprint, request, jsonify
import random
from .helpers import loadJokes
jokes=loadJokes()
api=Blueprint('api',__name__,url_prefix="/api")


@api.get('/jokes')
async def allJokes():
    category=request.args.get('category')
    limit=request.args.get("limit",type=int)
    if category:
        categories=list({c["category"] for c in jokes})
        if category in categories:
            from_category=[j for j in jokes if j["category"]==category]
            return jsonify({
                "status":"success",
                "category":category,
                "jokes":from_category,
            })
        else:
            return jsonify({
                "status":"error",
                "message":f"No jokes with category '{category}' found"
            })
    if limit:
        return jsonify({
            "status":"success",
            "limit":limit,
            "jokes":jokes[:limit],
        })
    return jsonify({
        "jokes":jokes
    })
    
@api.get("/jokes/random")
async def getRandomJoke():
    random_joke=random.choice(jokes)
    return jsonify({
        "status":"success",
        "joke":random_joke
    })

@api.get("/jokes/<int:id>")
async def getJokeById(id:int):
   for i,joke in enumerate(jokes):
       if i==id:
           return jsonify({
               "status":"success",
               "joke":joke
           })
   return jsonify({
       "status":"error",
       "message":f"No joke with id '{id}' found"
   })


               

@api.get("/jokes/categories")
async def allCategories():
    if len(jokes)>0:
        joke_categories=list({c["category"] for c in jokes})
        return jsonify({
            "categories":joke_categories
        })
@api.get("/jokes/search")
async def search():
    by_headline:str=request.args.get("headline")
    by_text:str=request.args.get("text")
    
    if by_headline:
        searched_jokes_by_headline=[j for j in jokes if by_headline.lower() in j["headline"].lower()]
        return jsonify({
            "status":"success",
            "search_term":by_headline,
            "jokes":searched_jokes_by_headline
        })
    if by_text:
        searched_jokes_by_text=[j for j in jokes if by_text.lower() in j["text"].lower()]
        return jsonify({
            "status":"success",
            "search_term":by_headline,
            "jokes":searched_jokes_by_text
        })
    return jsonify({
        "status":"error",
        "message":"No search term included in the query parameters. Add either headline or text as search terms.",
        
    }),400