# Critical Assumptions

## Instruction
Identify assumptions that could cause your final prototype to fail if they are wrong.

| Assumption ID | Category | Assumption | Related Requirement/User Story | Risk Level | Current Evidence | How to Test |
|---|---|---|---|---|---|---|
| A-01 | User Problem | Students frequently need quick access to campus information and would benefit from a chatbot instead of searching multiple university websites or documents.| FR-03 / US-01 | High | Interviews with students identified delays in finding campus information. | Conduct surveys and usability tests to compare chatbot use with current methods. |
| A-02 | Usability | Students can easily understand how to upload images and interact with the chatbot without additional training. | FR-08 / US-04 | Medium | UI designed using common chat application patterns. | Observe users completing image upload and question-answer tasks during prototype testing |
|A-03|Value proposition|Combining chatbot support with image recognition provides more value than a text-only chatbot for student services.|FR-05 / US-03|High|Based on project concept; no user validation yet.|Compare user satisfaction between text-only and image-enabled chatbot prototypes.|
|A-04|Technical feasibility|The image recognition model can accurately identify campus-related objects, buildings, notices, or student IDs under normal conditions.|FR-05 / US-03|High|Prototype uses a pre-trained vision model; no campus-specific testing completed.|Test the model with a dataset of real RSU campus images and measure recognition accuracy.|
## Categories
Use these categories:
- User problem
- Value proposition
- Usability
- Technical feasibility
- Business logic
- Data handling
