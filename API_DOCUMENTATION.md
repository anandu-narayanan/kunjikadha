# 📡 API Documentation

## Base URL
```
http://localhost:8000
```

## Authentication
Currently, no authentication required for public endpoints.
Admin panel requires superuser credentials.

---

## Endpoints

### 1. Home Page
**GET** `/`

Returns the home page with story creation form.

**Response:** HTML page

**Example:**
```
GET http://localhost:8000/
```

---

### 2. Create Story (Form Submission)
**POST** `/`

**Request:**
```html
Content-Type: application/x-www-form-urlencoded

character=കാക്ക&place=വനം&theme=friendship
```

**Response:**
Redirects to story detail page if successful.

**Error Response:**
```html
Status: 200
Response: Home page with error message
```

---

### 3. View Story
**GET** `/story/<session_id>/`

Display current story with choices.

**Parameters:**
- `session_id` (UUID): Unique story session identifier

**Response:** HTML page with story content

**Example:**
```
GET http://localhost:8000/story/f47ac10b-58cc-4372-a567-0e02b2c3d479/
```

---

### 4. Continue Story (AJAX)
**POST** `/api/story/<session_id>/continue/`

Generate next part of the story based on user's choice.

**Parameters:**
- `session_id` (UUID): Unique story session identifier

**Request Headers:**
```
Content-Type: application/json
X-CSRFToken: csrf_token_value
```

**Request Body:**
```json
{
  "choice": "The selected choice text"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "story": "Next part of the story...",
  "moral": "Moral lesson...",
  "choice1": "First choice with emoji",
  "choice2": "Second choice with emoji"
}
```

**Error Response (400):**
```json
{
  "error": "No choice selected"
}
```

**Error Response (500):**
```json
{
  "error": "Error generating story: Details of error"
}
```

**Example:**
```javascript
fetch('/api/story/f47ac10b-58cc-4372-a567-0e02b2c3d479/continue/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCookie('csrftoken')
  },
  body: JSON.stringify({
    choice: "കാക്ക വനത്തിലേ പറന്ന് പോയി"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

### 5. New Story
**GET** `/new/`

Redirect to home page to start a new story.

**Response:** Redirect to `/`

---

### 6. View All Stories
**GET** `/all-stories/`

Display list of all created stories.

**Response:** HTML page with stories grid

**Example:**
```
GET http://localhost:8000/all-stories/
```

---

### 7. Admin Panel
**GET** `/admin/`

Access Django admin interface.

**Requires:** Superuser login

**Features:**
- View all story sessions
- Edit story content
- Delete stories
- Manage users

---

## Response Formats

### Story Object
```json
{
  "story": "Five to six lines of Malayalam story...",
  "moral": "Simple moral lesson in Malayalam...",
  "choice1": "🔴 First choice option",
  "choice2": "🔵 Second choice option"
}
```

### Error Object
```json
{
  "error": "Descriptive error message",
  "code": "ERROR_CODE (optional)"
}
```

---

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Server Error |

---

## Rate Limiting

No rate limiting currently implemented.
For production, consider adding:
- Django Ratelimit
- API Throttling middleware

---

## CORS

Currently configured for localhost only.
For production, update `CORS_ALLOWED_ORIGINS` in settings.py

---

## AI API Integration

### Gemini API
- **Endpoint**: https://generativelanguage.googleapis.com/v1/models/gemini-pro
- **Model**: gemini-pro
- **Max Tokens**: 500
- **Temperature**: 0.7

### OpenAI API
- **Endpoint**: https://api.openai.com/v1/chat/completions
- **Model**: gpt-3.5-turbo
- **Max Tokens**: 500
- **Temperature**: 0.7

---

## Prompt Structure

### Initial Story Prompt
```
Generate a short interactive Malayalam children's story.

Requirements:
- Age: 3-6 years old
- Language: Simple Malayalam
- Character: {character}
- Place: {place}
- Theme: {theme}

Format your response with markers:
STORY: [story content]
MORAL: [moral lesson]
CHOICE1: [first choice]
CHOICE2: [second choice]
```

### Continuation Prompt
```
Continue a Malayalam children's story.

Previous story:
{previous_story}

User selected: {user_choice}

Format your response with markers:
STORY: [next story part]
MORAL: [moral lesson]
CHOICE1: [first choice]
CHOICE2: [second choice]
```

---

## Database Models

### StorySession
```python
{
  "id": 1,
  "session_id": "UUID",
  "character": "String (100 chars)",
  "place": "String (100 chars)",
  "theme": "String (100 chars)",
  "story_text": "Text (current story)",
  "story_history": "JSON array of story parts",
  "created_at": "DateTime",
  "updated_at": "DateTime"
}
```

---

## Examples

### Example 1: Create Story
```bash
curl -X POST http://localhost:8000/ \
  -d "character=കാക്ക&place=വനം&theme=friendship" \
  -L
```

### Example 2: Continue Story
```bash
curl -X POST http://localhost:8000/api/story/f47ac10b-58cc-4372-a567-0e02b2c3d479/continue/ \
  -H "Content-Type: application/json" \
  -d '{"choice":"കാക്ക സ്നേഹിതരെ കാണാനായി പോയി"}'
```

### Example 3: Get All Stories
```bash
curl http://localhost:8000/all-stories/
```

---

## Troubleshooting

### 403 CSRF Token Missing
**Issue**: CSRF token required for POST requests
**Solution**: Include X-CSRFToken header or use Django template form

### 404 Session Not Found
**Issue**: Invalid session_id
**Solution**: Verify session_id is correct UUID format

### 500 API Error
**Issue**: AI API call failed
**Solution**: Check API key, rate limits, and internet connection

---

## Future Endpoints (Roadmap)

- `GET /api/stories/` - List all stories (JSON)
- `GET /api/story/<id>/` - Get single story (JSON)
- `DELETE /api/story/<id>/` - Delete story
- `PUT /api/story/<id>/` - Update story
- `POST /api/auth/login/` - User authentication
- `GET /api/statistics/` - Usage statistics

---

## Performance Notes

- Story generation: 5-15 seconds (depends on AI API)
- Database queries optimized with select_related
- Static files cached by browser
- AJAX prevents full page reloads

---

## Security Considerations

✅ **Implemented:**
- CSRF protection
- XSS prevention (Django templates)
- SQL injection prevention (ORM)
- Session handling
- Input validation

⚠️ **For Production:**
- Enable HTTPS
- Add rate limiting
- Implement authentication
- Add logging
- Use environment variables for secrets
- Regular security audits

---

**API Version**: 1.0  
**Last Updated**: 2024  
**Built with**: Django 4.2 + Python 3.9+
