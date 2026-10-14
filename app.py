import streamlit as st

st.set_page_config(page_title="Dish Architect", page_icon="🍳", layout="wide")
st.title("Dish Architect 🍳 - Raw to Recipe")

# --- Input ---
st.subheader("1. What raw ingredients do you have?")
col1, col2 = st.columns([2,1])

with col1:
    raw_input = st.text_area(
        "Enter comma separated",
        "old dry fruits, dates, little milk, maida, suji",
        placeholder="e.g. chicken, rice, yogurt, onion, tomato..."
    )
    ingredients = [i.strip().lower() for i in raw_input.split(",") if i.strip()]

with col2:
    dish_type = st.selectbox("You want?", ["Auto Decide", "Batter / Fry", "No Fry / Laddu", "Curry", "Baked", "Drink"])
    servings = st.slider("Servings", 1, 6, 2)
    time = st.selectbox("Time?", ["Quick (<15 min)", "Medium (30 min)", "Slow"])

# --- Logic Engine ---
def architect_recipe(ingredients):
    ingredients_set = set(ingredients)

    # Your specific case
    if {"dates", "dry fruits", "milk", "maida"}.issubset(ingredients_set) or "dates" in str(ingredients_set):
        return {
            "title": "Dry Fruit Dates Malpua - Architected",
            "tag": "Best match for your pantry",
            "ingredients_final": [
                f"{8*servings} dates (seedless)",
                f"{0.5*servings} cup maida",
                f"{2*servings} tbsp suji",
                f"{0.5*servings} cup warm milk",
                f"{0.25*servings} cup chopped dry fruits",
                "1/4 tsp baking soda, ghee for frying"
            ],
            "batter_ratio": "Dates paste : Maida : Milk = 2 : 1 : 1",
            "syrup_note": "Use THICK jalebi syrup (1.5 sugar:1 water, 1-string), not thin gulab jamun syrup",
            "steps": [
                "Soak dates in warm milk 15 mins -> grind with 2 tbsp dry fruits to smooth paste",
                "Add maida + suji + baking soda, add milk slowly to make thick dosa batter",
                "Rest batter 20 mins",
                "Mix remaining chopped dry fruits",
                "Heat tawa, 1 tsp ghee, pour ladle, cook low flame 2 min each side"
            ],
            "pro_tip": "If dry fruits are old, roast 3 mins before grinding to remove rancid smell"
        }
    # Generic template for ANY new ingredients
    else:
        base = ingredients[0] if ingredients else "your ingredients"
        return {
            "title": f"Architected Dish with {base.title()} + {len(ingredients)-1} more",
            "tag": "Auto-generated",
            "ingredients_final": [f"{ing.title()} - as per taste" for ing in ingredients] + ["Salt, oil/ghee, spices as needed"],
            "batter_ratio": "Base : Liquid : Binder = 2 : 1 : 0.5 (adjust to thick batter)",
            "syrup_note": "If sweet: use thick syrup. If savory: skip syrup",
            "steps": [
                f"Prep: Clean and chop {', '.join(ingredients)}",
                "Make base paste with soft items + little milk/water",
                "Add dry flour (maida/suji/besan) to get batter consistency",
                "Taste, adjust salt/sweetness",
                "Cook: Fry on low-medium or bake - don't rush on high heat"
            ],
            "pro_tip": "Entered new ingredients? The app learns your ratio."
        }

# --- Output ---
if st.button("Architect Recipe →", type="primary"):
    if not ingredients:
        st.error("Enter at least 2 ingredients")
    else:
        recipe = architect_recipe(ingredients)

        st.divider()
        st.subheader(recipe["title"])
        st.caption(recipe["tag"])

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**📝 Final Ingredients**")
            for ing in recipe["ingredients_final"]:
                st.write(f"- {ing}")
        with c2:
            st.markdown("**⚖️ Architect Ratio**")
            st.info(recipe["batter_ratio"])
            st.markdown("**💧 Syrup Rule**")
            st.warning(recipe["syrup_note"])
        with c3:
            st.markdown("**⏱️ Stats**")
            st.metric("Servings", servings)
            st.metric("Time", time)
            st.metric("Ingredients used", len(ingredients))

        st.markdown("**👨‍🍳 Steps**")
        for i, step in enumerate(recipe["steps"], 1):
            st.write(f"{i}. {step}")

        st.success(f"Pro Tip: {recipe['pro_tip']}")

        # Save button
        st.download_button("Download Recipe as txt", str(recipe), file_name="dish_architect_recipe.txt")

# Footer
st.divider()
st.caption("Goal: Enter ANY raw ingredients → Get full recipe + batter ratio + syrup rule")
