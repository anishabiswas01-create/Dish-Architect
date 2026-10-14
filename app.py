import streamlit as st

# ==========================================
# 📐 PHASE 1: APPLICATION SETUP & DESIGN
# ==========================================
st.set_page_config(
    page_title="Dish Architect",
    page_icon="🏗️",
    layout="wide"
)

# Custom Architectural CSS Overrides for a Tech-Forward Workspace
st.markdown("""
    <style>
    .stApp {
        background-color: #0f1115;
    }
    .blueprint-card {
        background-color: #161b22;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #30363d;
        border-left: 5px solid #2563eb;
        margin-bottom: 20px;
        color: #e0e6ed;
    }
    .metric-box {
        background-color: #0d1117;
        padding: 12px;
        border-radius: 6px;
        border: 1px solid #30363d;
        text-align: center;
        color: #e0e6ed;
    }
    .stButton>button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        width: 100%;
        border: none !important;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
    }
    </style>
""", unsafe_allowed_html=True)

# ==========================================
# 🛠️ PHASE 2: CORE FORMULATION ENGINE (MOCK)
# ==========================================
def execute_dish_synthesis(ingredients, matrix_mode, tightness_score):
    """
    Computes recipe structures from raw ingredients. 
    This calculates combinations dynamically based on ingredient constraints.
    """
    ingredients_lower = [i.lower().strip() for i in ingredients]
    
    # Structural rule mapping for Chicken + Bok Choy profiles
    if any("chicken" in i for i in ingredients_lower) and any("bok choy" in i for i in ingredients_lower):
        return {
            "title": "Deconstructed Coconut-Curry Chicken Broth",
            "justification": f"Calculated for structural crispness. Employs a low-heat extraction format to balance raw bitter greens against dense proteins using your adjusted {tightness_score}% filter matrix.",
            "allocations": {
                "Chicken Breast": "Primary Protein Strut",
                "Bok Choy Stems": "Structural Crunch Ribbons",
                "Ginger Core": "Aromatic Stabilization Core",
                "Coconut Milk": "Liquid Flavor Binder"
            },
            "blueprints": [
                "Extract lipids from chicken frames and simmer broth base with structural aromatics.",
                "Inject coconut milk reduction dynamically at 85°C to protect emulsification integrity.",
                "Flash-sear structural bok choy stem ribbons separately to lock in fiber elasticity.",
                "Layer the crisp green ribbons over the hot broth array immediately prior to deployment."
            ]
        }
    # Structural rule mapping for Paneer + Potato profiles
    elif any("paneer" in i for i in ingredients_lower) and any("potato" in i for i in ingredients_lower):
        return {
            "title": "Spiced Potato-Paneer Croquettes with Crisp Panko Shells",
            "justification": f"Optimized for low-moisture starch binding. Curation engine automatically redirected from a wet curry to a high-texture dry framework to protect structural cohesion.",
            "allocations": {
                "Paneer Block": "Rich Moisture Structural Binder",
                "Boiled Potatoes": "High-Density Base Anchor",
                "Green Chilies": "Sharp Acidic Contrast Nodes",
                "Breadcrumbs": "Exoskeletal Crisp Crust Layer"
            },
            "blueprints": [
                "Dehydrate and mash boiled potatoes to build a dense, structurally sound anchor.",
                "Grate fresh paneer and lace evenly with fine green chili structural nodes.",
                "Compress composite formulation into unified solid cylinders to maximize structural strength.",
                "Encase in a dry breadcrumb armor and flash-fry at 180°C until crisp shell forms."
            ]
        }
    # Dynamic fallback layout for random mixed pantry items
    else:
        joined_items = ", ".join(ingredients[:3])
        return {
            "title": f"Experimental Multi-Tiered {matrix_mode} Synthesis",
            "justification": f"Dynamic breakdown computed using raw elements: {joined_items}. Formulated to match a balanced structural matrix at a tight {tightness_score}% constraint threshold.",
            "allocations": {i: "Deconstructed Ingredient Component" for i in ingredients},
            "blueprints": [
                "Isolate raw materials and sort by density and moisture coefficients.",
                "Apply localized thermal conduction to robust structural components first.",
                "Incorporate delicate volatile aromatics at the final execution phase.",
                "Assemble the final layers sequentially to guarantee structural plate balance."
            ]
        }

# ==========================================
# 🗄️ PHASE 3: PERSISTENT MEMORY STORAGE
# ==========================================
if "pantry_inventory" not in st.session_state:
    # Pre-loading inventory with your default signature ingredients
    st.session_state.pantry_inventory = ["Chicken Breast", "Bok Choy", "Fresh Ginger", "Coconut Milk", "Curry Powder"]

# ==========================================
# 🏗️ PHASE 4: USER INTERFACE LAYOUT
# ==========================================
st.title("🏗️ Dish Architect")
st.caption("Raw materials in. Custom flavor blueprints engineered.")
st.write("---")

# Split screen workspace design
workshop_panel, blueprint_panel = st.columns(2, gap="large")

# --- LEFT COLUMN: THE WORKSHOP (INPUT) ---
with workshop_panel:
    st.header("📦 The Workshop")
    st.write("Register raw materials and adjust your formulation matrix.")
    
    # Input field to register a new raw block
    new_item = st.text_input("Import a raw ingredient:", placeholder="e.g., Paneer, Potatoes, Garlic...", key="input_field")
    if st.button("➕ Register Item to Workshop"):
        if new_item.strip() and new_item.strip() not in st.session_state.pantry_inventory:
            st.session_state.pantry_inventory.append(new_item.strip())
            st.rerun()

    st.write("### Current Active Blocks:")
    if not st.session_state.pantry_inventory:
        st.info("Workshop empty. Please register raw materials to start calculations.")
    else:
        # Loop to show active ingredients with individual delete options
        for idx, item in enumerate(st.session_state.pantry_inventory):
            row_col1, row_col2 = st.columns([4, 1])
            row_col1.markdown(f"⚙️ **{item}**")
            if row_col2.button("🗑️", key=f"del_{idx}"):
                st.session_state.pantry_inventory.pop(idx)
                st.rerun()

    st.write("---")
    st.subheader("Matrix Adjustments")
    
    flavor_profile_mode = st.selectbox(
        "Structural Engine Mode:",
        ["Cross-Cultural Fusion", "Textural Transformation", "Zero-Waste Pantry Extraction", "Structural Deconstruction"]
    )
    
    curation_tightness = st.slider(
        "Curation Filter Tightness:", 
        min_value=50, max_value=100, value=85, step=5
    )

    # Master Action Execution Button
    trigger_synthesis = st.button("⚡ Synthesize My Meal")

# --- RIGHT COLUMN: THE BLUEPRINT PANEL (OUTPUT) ---
with blueprint_panel:
    st.header("📐 Synthesized Architecture")
    
    if trigger_synthesis:
        if not st.session_state.pantry_inventory:
            st.error("Calculation failure: Cannot run formulations with an empty workshop.")
        else:
            with st.spinner("Architecting flavor profiles... Calculating structural integrity..."):
                # Run the current session ingredients through the logic calculations
                blueprint_outcome = execute_dish_synthesis(
                    st.session_state.pantry_inventory, 
                    flavor_profile_mode, 
                    curation_tightness
                )
                
                # Render the Primary Blueprint Outcome Card
                st.markdown(f"""
                    <div class="blueprint-card">
                        <h2 style='margin-top:0; color:#2563eb;'>✨ {blueprint_outcome['title']}</h2>
                        <p style='font-style: italic; margin-bottom:0;'>
                            <strong>Curation Justification:</strong> {blueprint_outcome['justification']}
                        </p>
                    </div>
                """, unsafe_allowed_html=True)
                
                # Render Component Material Allocations
                st.subheader("🏗️ Structural Matrix Allocations")
                alloc_cols = st.columns(len(blueprint_outcome["allocations"]))
                for col, (material, role) in zip(alloc_cols, blueprint_outcome["allocations"].items()):
                    with col:
                        st.markdown(f"""
                            <div class="metric-box">
                                <span style='font-size:11px; color:#9ca3af; text-transform:uppercase;'>{material}</span><br>
                                <strong style='font-size:12px; color:#10b981;'>{role}</strong>
                            </div>
                        """, unsafe_allowed_html=True)
                
                st.write(" ")
                
                # Render Step-by-Step Construction Guide
                st.subheader("📋 Execution Architecture Layout")
                for phase_num, instruction in enumerate(blueprint_outcome["blueprints"], 1):
                    st.markdown(f"**Phase {phase_num}.0:** {instruction}")
                    
                st.success("Synthesis complete. Structural integrity verified by Curation Engine Outcomes.")
    else:
