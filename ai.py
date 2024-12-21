from openai import OpenAI
from config import settings

client = OpenAI(

    api_key=settings.api_key
    
    )


def getRecipe(query: str, ingredients: list):
    # Create a zero-shot prompt asking the model to check if all required ingredients are available
    prompt = f"Given the recipe query: '{query}', and the following available ingredients: {ingredients},\n\n" \
             "Please check if all ingredients are available for this recipe.\n" \
             "If any ingredients are missing, respond with 'Sorry, we don't have all the ingredients for this recipe.'\n" \
             "Also, suggest the missing ingredients that need to be bought to complete the recipe.\n" \
             "If all ingredients are available, provide a recipe suggestion."

    completion = client.chat.completions.create(
        model="gpt-4",  # Replace with your specific model if needed
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    # Retrieve and return the response content
    response = completion.choices[0].message.content
    
    # Return the response
    return response


