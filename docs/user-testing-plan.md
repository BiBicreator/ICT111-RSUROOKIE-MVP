# User Testing Results

## 1. Testing Summary

- **Date:** 28 July 2026
- **Number of testers:** 5
- **Prototype link:** `prototype/frontend.html`
- **Testing location/platform:** Desktop/Laptop using Google Chrome at Rangsit University

---

## 2. Task Completion Summary

| Task ID | Task | Completed? | Main Issue Found | Evidence / Comment |
| --- | --- | --- | --- | --- |
| T01 | Open the landing page and click **Try the Chatbot** | Yes | None | All testers easily located the CTA button. |
| T02 | Upload a building photo for AI recognition | Yes | Some building images were not recognized correctly | Similar-looking buildings reduced recognition accuracy. |
| T03 | Search for a building using the Directory | Yes | None | Search returned results quickly and accurately. |
| T04 | Open a building detail page | Yes | None | Testers successfully viewed building information and facilities. |
| T05 | Use the Interactive Campus Map | Partial | Some users were unsure which buildings were clickable | Suggested adding hover effects or tooltips. |
| T06 | Access the Admin Panel | Yes | Admin page needs clearer navigation | Functional but could be easier to locate. |
| T07 | View Dashboard Metrics | Yes | Metrics are currently simulated | Testers understood the dashboard but suggested real-time statistics in future versions. |

---

## 3. Common Usability Issues

| Issue ID | Issue Description | Severity | Related Requirement | Proposed Fix |
| --- | --- | --- | --- | --- |
| UI-01 | AI occasionally misidentifies similar-looking campus buildings. | Important | FR-03 | Retrain the Google Teachable Machine model with more building images. |
| UI-02 | Interactive campus map does not clearly indicate clickable buildings. | Useful | FR-07 | Add hover effects, labels, and visual highlights. |
| UI-03 | Admin Panel navigation could be more intuitive. | Useful | FR-09 | Add a clearer navigation menu and icons. |
| UI-04 | Dashboard metrics use simulated data only. | Future | FR-12 | Connect dashboard to real prototype usage data in a future version. |

---

## 4. User Feedback Summary

Most testers found the prototype easy to use and appreciated the AI building recognition feature. They liked having the building directory, campus map, and chatbot integrated into one platform. Testers suggested improving the accuracy of AI recognition by training the model with additional building images and making the interactive campus map easier to understand. Overall, users believed the prototype would be especially useful for new students and international students who are unfamiliar with the RSU campus.

---

## 5. Evidence-Based Decision

### ✅ Ready for Final Improvement

The core features of **RSU Campus Buddy (Smart Campus Chatbot with AI Image Recognition)** function as expected, including AI image recognition, the building directory, campus map, and admin panel. The remaining issues are related to usability improvements and AI model refinement rather than major functional problems. These enhancements will be completed before the final MVP release in Lab 14.
