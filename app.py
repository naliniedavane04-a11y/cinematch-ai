<<<<<<< HEAD
import streamlit as st
import pandas as pd
import pickle
import difflib

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CineMatch AI | Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for visual polish
st.markdown("""
    <style>
    .main-header {
        font-size: 2.8rem;
        color: #E50914;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        text-align: center;
        color: #A0A0A0;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #1A1A1A;
        border-radius: 8px;
        padding: 12px;
        border-left: 4px solid #E50914;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# LOAD MODEL ARTIFACTS
# -----------------------------------------------------------------------------
@st.cache_resource
def load_data():
    """Loads and caches the pickled model artifacts."""
    with open('movies.pkl', 'rb') as f:
        movies_df = pickle.load(f)
    with open('similarity.pkl', 'rb') as f:
        similarity_mat = pickle.load(f)
    return movies_df, similarity_mat

try:
    movies, similarity = load_data()
except FileNotFoundError:
    st.error("⚠️ Model files (`movies.pkl`, `similarity.pkl`) not found! Please run the training notebook first to generate them.")
    st.stop()

# -----------------------------------------------------------------------------
# RECOMMENDATION ENGINE LOGIC
# -----------------------------------------------------------------------------
def get_recommendations(user_query: str, top_k: int = 10):
    """
    Finds nearest fuzzy title match and returns top_k similar movies.
    """
    clean_query = user_query.strip().lower()
    all_titles_lower = movies['title'].str.lower().tolist()
    
    # Fuzzy string match for typo tolerance
    matches = difflib.get_close_matches(clean_query, all_titles_lower, n=1, cutoff=0.3)
    
    if not matches:
        return None, None
        
    matched_title_lower = matches[0]
    matched_index = movies[movies['title'].str.lower() == matched_title_lower].index[0]
    actual_title = movies.loc[matched_index, 'title']
    
    # Retrieve similarity vector and sort
    sim_scores = list(enumerate(similarity[matched_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Filter out the target movie itself and slice top K
    sim_scores = [item for item in sim_scores if item[0] != matched_index][:top_k]
    
    rec_indices = [i[0] for i in sim_scores]
    scores = [i[1] for i in sim_scores]
    
    results = movies.iloc[rec_indices].copy()
    results['Similarity Score'] = scores
    
    return actual_title, results

# -----------------------------------------------------------------------------
# USER INTERFACE
# -----------------------------------------------------------------------------
st.markdown('<p class="main-header">🎬 CineMatch AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Content-Based Recommendation Engine powered by TF-IDF & Cosine Similarity</p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Settings")
num_recommendations = st.sidebar.slider(
    "Select Number of Recommendations:",
    min_value=3,
    max_value=15,
    value=10,
    step=1
)

st.sidebar.markdown("---")
st.sidebar.info("""
**How it works:**  
This system analyzes movie genre metadata, converts genres into numerical vectors using **TF-IDF**, and calculates pairwise **Cosine Similarity** scores.
""")

# Input selection
all_movie_titles = sorted(movies['title'].unique())
selected_movie = st.selectbox(
    "🔍 Search or select a movie:",
    options=all_movie_titles,
    index=0,
    help="Type to search for a movie in the database"
)

# Search Execution
if st.button("🚀 Get Recommendations", use_container_width=True):
    with st.spinner("Calculating similarity vectors..."):
        matched_title, recommendations = get_recommendations(selected_movie, top_k=num_recommendations)
        
        if recommendations is None:
            st.error(f"❌ Could not find any close match for '{selected_movie}'. Please try selecting another title.")
        else:
            st.success(f"Showing recommendations based on: **{matched_title}**")
            st.write("---")
            
            # Display results
            for idx, row in recommendations.reset_index(drop=True).iterrows():
                col_rank, col_info, col_score = st.columns([1, 5, 2])
                
                with col_rank:
                    st.markdown(f"### #{idx+1}")
                    
                with col_info:
                    st.markdown(f"**{row['title']}**")
                    st.caption(f"🎭 Genres: `{row['genres']}`")
                    
                with col_score:
                    score_pct = row['Similarity Score'] * 100
                    st.metric(
                        label="Match Confidence", 
                        value=f"{score_pct:.1f}%"
                    )
=======
import streamlit as st
import pandas as pd
import pickle
import difflib

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CineMatch AI | Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for visual polish
st.markdown("""
    <style>
    .main-header {
        font-size: 2.8rem;
        color: #E50914;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        text-align: center;
        color: #A0A0A0;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #1A1A1A;
        border-radius: 8px;
        padding: 12px;
        border-left: 4px solid #E50914;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# LOAD MODEL ARTIFACTS
# -----------------------------------------------------------------------------
@st.cache_resource
def load_data():
    """Loads and caches the pickled model artifacts."""
    with open('movies.pkl', 'rb') as f:
        movies_df = pickle.load(f)
    with open('similarity.pkl', 'rb') as f:
        similarity_mat = pickle.load(f)
    return movies_df, similarity_mat

try:
    movies, similarity = load_data()
except FileNotFoundError:
    st.error("⚠️ Model files (`movies.pkl`, `similarity.pkl`) not found! Please run the training notebook first to generate them.")
    st.stop()

# -----------------------------------------------------------------------------
# RECOMMENDATION ENGINE LOGIC
# -----------------------------------------------------------------------------
def get_recommendations(user_query: str, top_k: int = 10):
    """
    Finds nearest fuzzy title match and returns top_k similar movies.
    """
    clean_query = user_query.strip().lower()
    all_titles_lower = movies['title'].str.lower().tolist()
    
    # Fuzzy string match for typo tolerance
    matches = difflib.get_close_matches(clean_query, all_titles_lower, n=1, cutoff=0.3)
    
    if not matches:
        return None, None
        
    matched_title_lower = matches[0]
    matched_index = movies[movies['title'].str.lower() == matched_title_lower].index[0]
    actual_title = movies.loc[matched_index, 'title']
    
    # Retrieve similarity vector and sort
    sim_scores = list(enumerate(similarity[matched_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Filter out the target movie itself and slice top K
    sim_scores = [item for item in sim_scores if item[0] != matched_index][:top_k]
    
    rec_indices = [i[0] for i in sim_scores]
    scores = [i[1] for i in sim_scores]
    
    results = movies.iloc[rec_indices].copy()
    results['Similarity Score'] = scores
    
    return actual_title, results

# -----------------------------------------------------------------------------
# USER INTERFACE
# -----------------------------------------------------------------------------
st.markdown('<p class="main-header">🎬 CineMatch AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Content-Based Recommendation Engine powered by TF-IDF & Cosine Similarity</p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Settings")
num_recommendations = st.sidebar.slider(
    "Select Number of Recommendations:",
    min_value=3,
    max_value=15,
    value=10,
    step=1
)

st.sidebar.markdown("---")
st.sidebar.info("""
**How it works:**  
This system analyzes movie genre metadata, converts genres into numerical vectors using **TF-IDF**, and calculates pairwise **Cosine Similarity** scores.
""")

# Input selection
all_movie_titles = sorted(movies['title'].unique())
selected_movie = st.selectbox(
    "🔍 Search or select a movie:",
    options=all_movie_titles,
    index=0,
    help="Type to search for a movie in the database"
)

# Search Execution
if st.button("🚀 Get Recommendations", use_container_width=True):
    with st.spinner("Calculating similarity vectors..."):
        matched_title, recommendations = get_recommendations(selected_movie, top_k=num_recommendations)
        
        if recommendations is None:
            st.error(f"❌ Could not find any close match for '{selected_movie}'. Please try selecting another title.")
        else:
            st.success(f"Showing recommendations based on: **{matched_title}**")
            st.write("---")
            
            # Display results
            for idx, row in recommendations.reset_index(drop=True).iterrows():
                col_rank, col_info, col_score = st.columns([1, 5, 2])
                
                with col_rank:
                    st.markdown(f"### #{idx+1}")
                    
                with col_info:
                    st.markdown(f"**{row['title']}**")
                    st.caption(f"🎭 Genres: `{row['genres']}`")
                    
                with col_score:
                    score_pct = row['Similarity Score'] * 100
                    st.metric(
                        label="Match Confidence", 
                        value=f"{score_pct:.1f}%"
                    )
>>>>>>> d87cfb69e210d539b7f8625472accaf4ce88586c
                st.markdown("---")