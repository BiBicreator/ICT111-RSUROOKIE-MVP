# Legal and Ethical Checklist

## Project Title

RSU Campus Buddy – Smart Campus Chatbot for Student Services with Image Recognition

## Ethical Review

| Check Item | Yes/No | Evidence / Notes | Mitigation Action | Owner | GitHub Issue/Commit |
|---|---|---|---|---|---|
| Users are informed about the purpose of the prototype. | Yes | The homepage explains that the system helps students identify campus buildings and access campus information using AI image recognition. | Keep the project description visible on the homepage and provide a brief user guide. | Member 1 | Issue #3 |
| The prototype avoids misleading claims. | Yes | The system states that AI recognition results may not always be 100% accurate, especially for unclear images. | Display a disclaimer encouraging users to verify the information if recognition confidence is low. | Member 1 | Issue #3 |
| The prototype does not collect unnecessary sensitive data. | Yes | The prototype only accepts uploaded building images and does not collect personal information such as student ID, phone numbers, or email. | Continue limiting data collection to information required for the prototype. | Member 1 | Issue #2 |
| Users can understand what happens after submission. | Yes | After uploading an image, the system displays the recognition result, building details, facilities, opening hours, and chatbot response. | Maintain clear confirmation and feedback messages after each upload. | Member 1 | Issue #2 |
| Admin or manager actions are clearly separated from user actions. | Yes | Only administrators can add, edit, or update campus building information through the admin page. Students can only use the chatbot and search features. | Keep the admin interface separated and protect it with authentication. | Member 3 | Issue #5 |
| The prototype avoids unfair or harmful treatment of users. | Yes | The chatbot provides the same campus information to all users without discrimination. The AI model is trained using campus building images only. | Continue improving the AI models with diverse training images to reduce recognition errors. | Member 1 | Issue #3 |

## Summary Decision

- Safe to continue: Yes, with minor revisions.

### Required revision before implementation

- Improve the Google Teachable Machine AI model by training it with more campus building images.
- Add clearers guidance when uploaded images are blurry or cannot be recognized.
- Expand the chatbot knowledge base to answer more campus-related questions.
- Improve admin security by ensuring only authorized users can modify campus information.
