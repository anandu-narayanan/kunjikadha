"""
Utility functions for AI story generation.
Supports both OpenAI and Google Gemini APIs.
"""
import importlib
import re
import sys
from pathlib import Path
from django.conf import settings


def _local_site_packages_paths():
    """
    Return likely site-packages locations for the project's local virtualenv.
    """
    project_root = Path(__file__).resolve().parent.parent
    venv_dir = project_root / 'venv'

    candidates = [
        venv_dir / 'Lib' / 'site-packages',
        venv_dir / 'lib' / 'site-packages',
    ]

    lib_dir = venv_dir / 'lib'
    if lib_dir.exists():
        candidates.extend(path / 'site-packages' for path in lib_dir.glob('python*'))

    unique_candidates = []
    seen = set()
    for candidate in candidates:
        candidate_str = str(candidate)
        if candidate.exists() and candidate_str not in seen:
            unique_candidates.append(candidate)
            seen.add(candidate_str)

    return unique_candidates


def _ensure_local_site_packages_on_path():
    """
    Make packages from the project's venv visible when Django is launched
    with a different Python interpreter.
    """
    for candidate in reversed(_local_site_packages_paths()):
        candidate_str = str(candidate)
        if candidate_str not in sys.path:
            sys.path.insert(0, candidate_str)


def _import_optional_module(module_name):
    """
    Try importing a dependency, then retry after exposing the local venv.
    """
    try:
        return importlib.import_module(module_name)
    except ImportError:
        _ensure_local_site_packages_on_path()
        try:
            return importlib.import_module(module_name)
        except ImportError:
            return None


def _missing_dependency_message(package_name, pip_command):
    """
    Build a clearer dependency error for whichever interpreter launched Django.
    """
    message = (
        f"{package_name} library not installed in the current Python interpreter "
        f"({sys.executable}). Install with: {pip_command}"
    )

    if _local_site_packages_paths():
        message += " or start Django using the project's virtualenv Python."

    return message


openai = _import_optional_module('openai')
OPENAI_AVAILABLE = openai is not None

legacy_genai = _import_optional_module('google.generativeai')
modern_genai = _import_optional_module('google.genai')
GEMINI_AVAILABLE = legacy_genai is not None or modern_genai is not None


def generate_initial_story(character, place, theme):
    """
    Generate the initial story based on character, place, and theme.
    
    Args:
        character (str): Character name in Malayalam
        place (str): Place name in Malayalam
        theme (str): Story theme
        
    Returns:
        dict: Contains 'story', 'choice1', 'choice2', 'moral'
    """
    prompt = f"""Generate a short interactive Malayalam children's story.

Requirements:
- Age: 3-6 years old
- Language: Simple Malayalam (use common, easy words)
- Character: {character}
- Place: {place}
- Theme: {theme}

Format your response EXACTLY as follows (use these exact markers):
STORY: [5-6 lines of simple Malayalam story]
MORAL: [Simple moral lesson in Malayalam]
CHOICE1: [First choice for continuing the story in Malayalam, start with an emoji]
CHOICE2: [Second choice for continuing the story in Malayalam, start with an emoji]

Make sure:
1. Use simple, friendly Malayalam
2. Include emojis to make it engaging
3. Keep sentences short
4. Make choices interesting but age-appropriate
5. Include a clear moral lesson"""
    
    response_text = call_ai_api(prompt)
    
    # Parse the response
    story_data = parse_story_response(response_text)
    return story_data


def continue_story(character, place, theme, previous_story, user_choice):
    """
    Continue the story based on previous context and user choice.
    
    Args:
        character (str): Character name
        place (str): Place name
        theme (str): Story theme
        previous_story (list): List of previous story parts
        user_choice (str): The choice selected by user
        
    Returns:
        dict: Contains 'story', 'choice1', 'choice2', 'moral'
    """
    # Build context from previous story
    context = "\n".join([
        f"Previous story:\n{part['story']}" 
        for part in previous_story
    ])
    
    prompt = f"""Continue a Malayalam children's story.

Original Story Setup:
- Character: {character}
- Place: {place}
- Theme: {theme}

{context}

User selected: {user_choice}

Now generate the NEXT part of the story (5-6 lines continuing from where it left off).

Format your response EXACTLY as follows:
STORY: [5-6 lines continuing the story, building on what happened before]
MORAL: [Updated moral lesson if needed]
CHOICE1: [First choice for the next step, start with an emoji]
CHOICE2: [Second choice for the next step, start with an emoji]

Requirements:
1. Maintain story continuity
2. Use simple Malayalam
3. Include emojis
4. Keep it age-appropriate (3-6 years)
5. Make it engaging and fun"""
    
    response_text = call_ai_api(prompt)
    
    # Parse the response
    story_data = parse_story_response(response_text)
    return story_data


def call_ai_api(prompt):
    """
    Call the configured AI API (OpenAI or Gemini).
    
    Args:
        prompt (str): The prompt to send to the AI
        
    Returns:
        str: The response text from the AI
    """
    provider = settings.AI_API_PROVIDER.lower()
    
    if provider == 'openai':
        return call_openai_api(prompt)
    elif provider == 'gemini':
        return call_gemini_api(prompt)
    else:
        raise ValueError(f"Unknown AI provider: {provider}")


def call_openai_api(prompt):
    """
    Call OpenAI API to generate story.
    """
    if not OPENAI_AVAILABLE:
        raise ImportError(_missing_dependency_message('OpenAI', 'pip install openai'))
    
    if not settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not configured in environment")
    
    # Set the API key
    openai.api_key = settings.OPENAI_API_KEY
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative Malayalam children's story writer. Generate simple, engaging stories for kids aged 3-6."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error calling OpenAI API: {str(e)}")


def call_gemini_api(prompt):
    """
    Call Google Gemini API to generate story.
    """
    if not GEMINI_AVAILABLE:
        raise ImportError(
            _missing_dependency_message(
                'Google Generative AI',
                'pip install google-generativeai'
            )
        )
    
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not configured in environment")
    
    try:
        if modern_genai is not None:
            response = modern_genai.Client(
                api_key=settings.GEMINI_API_KEY
            ).models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            if getattr(response, 'text', None):
                return response.text.strip()

        if legacy_genai is not None:
            # Configure the API key
            legacy_genai.configure(api_key=settings.GEMINI_API_KEY)

            # Find a supported model for generate_content
            model_name = None
            if hasattr(legacy_genai, 'list_models'):
                try:
                    models = list(legacy_genai.list_models())
                    for model in models:
                        supported = getattr(model, 'supported_generation_methods', [])
                        if supported and 'generateContent' in supported:
                            model_name = getattr(model, 'name', None)
                            break
                except Exception:
                    model_name = None

            # Fallback default model
            if not model_name:
                model_name = 'models/gemini-2.5-flash'

            if hasattr(legacy_genai, 'GenerativeModel'):
                model = legacy_genai.GenerativeModel(model_name)
                if not hasattr(model, 'generate_content'):
                    raise Exception('Gemini GenerativeModel missing generate_content method')

                response = model.generate_content(prompt)

                # Parse response object
                if hasattr(response, 'result') and response.result:
                    candidates = getattr(response.result, 'candidates', None)
                    if candidates:
                        first = candidates[0]
                        content = None
                        if hasattr(first, 'content') and first.content:
                            if hasattr(first.content, 'parts'):
                                content = ''.join(getattr(part, 'text', '') for part in first.content.parts)
                            elif isinstance(first.content, str):
                                content = first.content
                        elif isinstance(first, dict) and first.get('content'):
                            data = first['content']
                            if isinstance(data, dict) and data.get('parts'):
                                content = ''.join(p.get('text', '') for p in data['parts'])
                            elif isinstance(data, str):
                                content = data
                        if content:
                            return content.strip()

                if hasattr(response, 'content') and response.content:
                    return str(response.content).strip()
                if hasattr(response, 'text') and response.text:
                    return str(response.text).strip()

            if hasattr(legacy_genai, 'generate'):
                response = legacy_genai.generate(model=model_name, prompt=prompt)
                if isinstance(response, dict):
                    candidates = response.get('candidates', [])
                    if candidates:
                        first = candidates[0]
                        content = first.get('content', {}).get('parts', [])
                        if content:
                            return ''.join(p.get('text', '') for p in content).strip()

        # Fallback to OpenAI if configured
        if OPENAI_AVAILABLE and settings.OPENAI_API_KEY:
            return call_openai_api(prompt)

        raise Exception('Gemini response did not include text or model method unavailable.')
    except Exception as e:
        raise Exception(f"Error calling Gemini API: {str(e)}")


def parse_story_response(response_text):
    """
    Parse the AI response to extract story, choices, and moral.
    
    Args:
        response_text (str): The raw response from AI API
        
    Returns:
        dict: Parsed story data with 'story', 'choice1', 'choice2', 'moral'
    """
    data = {
        'story': '',
        'choice1': '',
        'choice2': '',
        'moral': ''
    }
    
    # Extract STORY
    story_match = re.search(r'STORY:\s*(.+?)(?=MORAL:|CHOICE1:|$)', response_text, re.DOTALL)
    if story_match:
        data['story'] = story_match.group(1).strip()
    
    # Extract MORAL
    moral_match = re.search(r'MORAL:\s*(.+?)(?=CHOICE1:|CHOICE2:|$)', response_text, re.DOTALL)
    if moral_match:
        data['moral'] = moral_match.group(1).strip()
    
    # Extract CHOICE1
    choice1_match = re.search(r'CHOICE1:\s*(.+?)(?=CHOICE2:|$)', response_text, re.DOTALL)
    if choice1_match:
        data['choice1'] = choice1_match.group(1).strip()
    
    # Extract CHOICE2
    choice2_match = re.search(r'CHOICE2:\s*(.+?)$', response_text, re.DOTALL)
    if choice2_match:
        data['choice2'] = choice2_match.group(1).strip()
    
    return data
