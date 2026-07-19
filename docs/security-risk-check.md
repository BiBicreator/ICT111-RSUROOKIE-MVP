# Basic Security Risk Check

| Area | Risk Question | Current Status | Risk Level | Mitigation | Owner |
|---|---|---|---|---|---|
| Form input | Can incomplete or invalid data be submitted? | Required fields and basic validation are implemented, but additional validation can be improved. | Medium | Validate required fields, restrict invalid input, and display clear error messages. | Member 1 |
| Admin function | Can normal users access admin actions? | Admin features are separated from the student interface, but login protection should be strengthened. | High | Require administrator authentication before accessing admin functions. | Member 2 |
| Data display | Is private information visible to everyone? | Only public campus information is displayed. No personal student information is collected or shown. | Low | Continue displaying only public campus information and avoid collecting personal data. | Member 1 |
| Status update | Can records be edited without control? | Only administrators can updated building information and chatbot data. | Medium | Restrict editing privileges to authorized administrators and log updates where possible. | Member 3 |
| Public links | Does a public link expose data that should be private? | Public pages only displays campus information. Admin pages are not linked publicly. | Low | Keep administrator pages protected and avoid exposing management URLs. | Member 2 |
| File upload | If used, can unsafe or unrelated files be uploaded? | Users upload images for AI building recognition. File type restrictions should be enforced. | Medium | Accept only JPG, JPEG, and PNG image files, limit file size, and reject unsupported formats. | Member 1 |

## Security Decision

Continue with mitigation

The current prototype has basic security measures suitable for an educational MVP. Before the final prototype, the team will strengthen administrator authentication, improve input validation, restrict uploaded file types, and continue ensuring that no unnecessary personal information is collected or exposed.
